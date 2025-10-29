import serial
import time
import csv
import numpy as np
from datetime import datetime

# --- Configuration ---
SERIAL_PORT = 'COM22'      # Change as needed
BAUD_RATE = 115200
TIMEOUT = 1
POINTS_PER_SWEEP = 401

# --- Helper functions ---

def connect_to_device(port, baud, timeout):
    try:
        ser = serial.Serial(port, baud, timeout=timeout)
        time.sleep(2)
        print(f"Connected to {port} at {baud} bps")
        return ser
    except serial.SerialException as e:
        print(f"Serial connection error: {e}")
        return None

def send_command(ser, command, delay=0.1):
    """Send a command and wait briefly."""
    cmd = command.strip() + "\r\n"
    ser.write(cmd.encode('utf-8'))
    time.sleep(delay)
    print(f"Sent: {command}")

def read_one_sweep(ser, points):
    """Read one full sweep of numeric amplitude data."""
    amplitudes = []
    start_time = time.time()
    while len(amplitudes) < points:
        line = ser.readline().decode(errors='ignore').strip()
        if not line:
            # timeout guard in case of stall
            if time.time() - start_time > 5:
                print("Timed out waiting for sweep data.")
                break
            continue
        try:
            amplitudes.append(float(line))
        except ValueError:
            # Ignore status or echoes
            continue
    return np.array(amplitudes)

def save_sweep_to_csv(frequencies, amplitudes):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"sweep_{timestamp}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Frequency (Hz)', 'Amplitude (dBm)'])
        writer.writerows(zip(frequencies, amplitudes))
    print(f"[{timestamp}] Saved sweep to {filename}")

# --- User configuration ---

def get_user_config():
    print("=== TinySA Ultra Data Logger ===\n")
    mode = input("Select mode:\n1. Center frequency + span\n2. Start and stop frequency\nEnter choice (1 or 2): ").strip()

    if mode == "1":
        center = float(input("Enter center frequency in MHz (e.g., 433): ")) * 1e6
        span = float(input("Enter span in MHz (e.g., 10): ")) * 1e6
        start_freq = center - span / 2
        stop_freq = center + span / 2
    elif mode == "2":
        start_freq = float(input("Enter start frequency in MHz: ")) * 1e6
        stop_freq = float(input("Enter stop frequency in MHz: ")) * 1e6
    else:
        print("Invalid selection. Defaulting to 100–150 MHz.")
        start_freq, stop_freq = 100e6, 150e6

    log_interval = float(input("Enter logging interval in seconds: "))
    print(f"\nConfigured Range: {start_freq/1e6:.3f}–{stop_freq/1e6:.3f} MHz")
    print(f"Logging every {log_interval:.1f} seconds.\n")
    return start_freq, stop_freq, log_interval

# --- Main loop ---

def main():
    start_freq, stop_freq, log_interval = get_user_config()
    ser = connect_to_device(SERIAL_PORT, BAUD_RATE, TIMEOUT)
    if not ser:
        return

    freqs = np.linspace(start_freq, stop_freq, POINTS_PER_SWEEP)

    print("Starting logging... (Ctrl+C to stop)\n")

    try:
        while True:
            # Trigger a sweep each time
            send_command(ser, f"scan {int(start_freq)} {int(stop_freq)}")
            send_command(ser, "data 2")

            amps = read_one_sweep(ser, POINTS_PER_SWEEP)

            if amps.size > 0:
                save_sweep_to_csv(freqs, amps)
            else:
                print("Warning: No data received for this sweep.")

            time.sleep(log_interval)

    except KeyboardInterrupt:
        print("\nStopped by user.")
    finally:
        if ser and ser.is_open:
            ser.close()
            print("Serial connection closed.")

if __name__ == "__main__":
    main()

