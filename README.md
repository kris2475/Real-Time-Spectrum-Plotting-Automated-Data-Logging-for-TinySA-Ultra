# Tiny Spectrum Analyser Tools 📡  
**Real-Time Spectrum Plotting & Automated Data Logging for TinySA Ultra**

---

## 🧭 Executive Summary

The **Tiny Spectrum Analyser Tools** provide an efficient Python-based interface for the **TinySA Ultra** — a compact and affordable spectrum analyzer.  
These scripts transform your TinySA Ultra into a **powerful RF monitoring and data collection platform**, enabling **live visualization**, **automated logging**, and **CSV data export** for post-analysis.

With these tools, you can:
- Visualize live RF spectra directly from the TinySA Ultra
- Automatically log periodic sweeps to timestamped CSV files
- Configure custom frequency ranges and logging intervals
- Integrate easily into your RF lab workflow or automated testing setup

These scripts bridge the gap between simple on-device measurements and full PC-based spectrum analysis.

---

## 💡 Introduction

The **TinySA Ultra** is a versatile handheld spectrum analyzer, but its small screen limits long-term monitoring and in-depth data analysis.  
This project extends its capabilities using **Python**, **Serial communication**, and **Matplotlib** — allowing you to view, record, and analyze spectrum data with ease.

The repository includes two companion scripts:

| Script | Function | Key Features |
|--------|-----------|---------------|
| `Tiny_Spectrum_Analyser_plot.py` | Live plotting | Real-time graph of amplitude vs. frequency, dynamic autoscaling, and per-sweep CSV export |
| `Tiny_SA_Logger.py` | Background logging | Logs spectrum sweeps to timestamped CSV files at fixed intervals (user-defined frequency range and interval) |

---

## ⚙️ Features at a Glance

- 🔌 Simple serial connection (auto-configurable COM port)
- 🧠 Intelligent frequency control — choose center/span or start/stop range
- 💾 Automated saving of every sweep with timestamps
- 📊 Real-time Matplotlib visualization (plot script)
- 🕒 Configurable logging interval (seconds or minutes)
- 📈 CSV export for post-processing (NumPy, Pandas, Excel, etc.)
- 🧩 Compatible with Windows, macOS, and Linux

---

## 🧰 Requirements

- Python 3.8+
- TinySA Ultra connected via USB
- Python packages:
  ```bash
  pip install pyserial numpy matplotlib
  ```

---

## 🚀 Usage Overview

### 1️⃣ Real-Time Plotting  
**File:** `Tiny_Spectrum_Analyser_plot.py`

#### Purpose:
Visualize the live RF spectrum in real-time from your TinySA Ultra.

#### Run:
```bash
python Tiny_Spectrum_Analyser_plot.py
```

#### Behavior:
- Prompts you for serial port (default `COM22`)
- Streams spectrum data continuously
- Displays amplitude vs. frequency in a live updating Matplotlib plot
- Saves each sweep automatically as:
  ```
  spectrum_sweep_YYYYMMDD_HHMMSS.csv
  ```

---

### 2️⃣ Periodic Data Logger  
**File:** `Tiny_SA_Logger.py`

#### Purpose:
Continuously log TinySA Ultra data to CSV files at set intervals.

#### Run:
```bash
python Tiny_SA_Logger.py
```

#### Configuration Prompts:
```
=== TinySA Ultra Data Logger ===

Select mode:
1. Center frequency + span
2. Start and stop frequency
Enter choice (1 or 2): 1
Enter center frequency in MHz (e.g., 433): 433
Enter span in MHz (e.g., 20): 10
Enter logging interval in seconds (e.g., 60): 10
```

#### Behavior:
- Configures TinySA sweep range dynamically
- Reads a full sweep of amplitude data via serial
- Saves timestamped CSV every N seconds, e.g.:
  ```
  sweep_20251029_194522.csv
  ```

---

## 📂 Example Output (CSV)

| Frequency (Hz) | Amplitude (dBm) |
|----------------|-----------------|
| 4.30E+08       | -92.5           |
| 4.31E+08       | -91.8           |
| 4.32E+08       | -93.2           |
| ...            | ...             |

---

## 🧠 Applications

- Continuous RF environment monitoring  
- Signal stability or drift analysis  
- Frequency occupancy and interference studies  
- Logging test results during automated RF experiments  
- Long-term data collection for IoT or EMC testing

---

## 🧩 Future Enhancements

- Combine live plotting + logging into one GUI tool  
- Add MQTT / InfluxDB support for networked data streaming  
- Web dashboard for remote spectrum viewing  
- Real-time anomaly detection (spike or signal alerting)

---

## 🪪 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Kris Seunarine**  

> “From handheld scans to full-spectrum insights — power up your TinySA Ultra.”
