import serial
import time
import matplotlib.pyplot as plt
import numpy as np
import csv
from datetime import datetime

# --- Configuration ---
SERIAL_PORT = 'COM22'   # Change to your TinySA port (e.g., '/dev/ttyACM0' or 'COM5')
BAUD_RATE = 115200
TIMEOUT = 1
POINTS_PER_SWEEP = 401  # Default TinySA sweep resolution (adjust if needed)

# --- Helper Functions ---

def save_sweep_to_csv(frequencies, amplitudes):
    """Save one sweep to a timestamped CSV file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
    filename = f"spectrum_sweep_{timestamp}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Frequency (Hz)', 'Amplitude (dBm)'])
        writer.writerows(zip(frequencies, amplitudes))
    print(f"Saved sweep to: {filename}")

def connect_to_device(port, baud, timeout):
    """Connect to TinySA Ultra via serial."""
    try:
        ser = serial.Serial(port, baud, timeout=timeout)
        time.sleep(2)
        print(f"Connected to {port} at {baud} bps")
        return ser
    except serial.SerialException as e:
        print(f"Serial error: {e}")
        return None

def send_command(ser, command):
    """Send command to TinySA."""
    cmd = command.strip() + "\r\n"
    ser.write(cmd.encode('utf-8'))
    print(f"Sent: {command}")
    time.sleep(0.1)

def prompt_user_for_range():
    """Prompt user for frequency input method and values."""
    print("\nSelect frequency input method:")
    print("1 → Center frequency and Span")
    print("2 → Start and Stop frequencies")
    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "1":
        center_mhz = float(input("Enter center frequency (MHz): "))
        span_mhz = float(input("Enter span (MHz): "))
        center = center_mhz * 1e6
        span = span_mhz * 1e6
        start = center - span / 2
        stop = center + span / 2
    elif choice == "2":
        start_mhz = float(input("Enter start frequency (MHz): "))
        stop_mhz = float(input("Enter stop frequency (MHz): "))
        start = start_mhz * 1e6
        stop = stop_mhz * 1e6
    else:
        print("Invalid choice, using default 100–150 MHz range.")
        start, stop = 100e6, 150e6

    print(f"\nSweep Range: {start/1e6:.3f}–{stop/1e6:.3f} MHz")
    return start, stop

def read_one_sweep(ser, points):
    """Read one full sweep of amplitude data (one value per line)."""
    amps = []
    while len(amps) < points:
        line = ser.readline().decode(errors='ignore').strip()
        if not line:
            continue
        try:
            amps.append(float(line))
        except ValueError:
            # Ignore command echoes or other responses
            print("Non-numeric:", line)
            continue
    return np.array(amps)

def plot_spectrum(freqs, amps, ax, fig):
    """Plot the live spectrum."""
    ax.clear()
    ax.plot(freqs / 1e6, amps, color='#1e88e5', linewidth=1.5)
    ax.set_title("TinySA Ultra Live Spectrum")
    ax.set_xlabel("Frequency (MHz)")
    ax.set_ylabel("Amplitude (dBm)")
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_ylim(np.min(amps) - 5, np.max(amps) + 5)
    fig.canvas.draw_idle()
    plt.pause(0.05)

# --- Main Loop ---

def main():
    ser = connect_to_device(SERIAL_PORT, BAUD_RATE, TIMEOUT)
    if ser is None:
        return

    start_freq, stop_freq = prompt_user_for_range()

    # Send sweep setup commands
    send_command(ser, f"scan {int(start_freq)} {int(stop_freq)}")
    send_command(ser, "data 2")   # enable amplitude output

    plt.ion()
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.show()

    print("\nCollecting sweeps... (Ctrl+C to stop)\n")

    try:
        while plt.fignum_exists(fig.number):
            amps = read_one_sweep(ser, POINTS_PER_SWEEP)
            freqs = np.linspace(start_freq, stop_freq, POINTS_PER_SWEEP)
            plot_spectrum(freqs, amps, ax, fig)
            save_sweep_to_csv(freqs, amps)
    except KeyboardInterrupt:
        print("\nStopped by user.")
    finally:
        if ser and ser.is_open:
            ser.close()
            print("Serial connection closed.")
        plt.ioff()
        plt.close(fig)

if __name__ == "__main__":
    main()




