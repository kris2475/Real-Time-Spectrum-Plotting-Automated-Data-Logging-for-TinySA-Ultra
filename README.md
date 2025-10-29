# Tiny Spectrum Analyser Tools 🇬🇧📡  
**Real-Time Spectrum Plotting & Automated Data Logging for TinySA Ultra**

---

## 🧭 Executive Summary

The **Tiny Spectrum Analyser Tools** provide an efficient, Python-based interface for the **TinySA Ultra** — a compact and affordable spectrum analyser.  
These scripts transform the TinySA Ultra into a **powerful RF monitoring and data collection platform**, enabling **live visualisation**, **automated logging**, and **CSV data export** for post-analysis.

With these tools, you can:
- Visualise live RF spectra directly from the TinySA Ultra  
- Automatically log periodic sweeps to timestamped CSV files  
- Configure custom frequency ranges and logging intervals  
- Integrate seamlessly into laboratory workflows or automated testing setups  

These scripts bridge the gap between simple on-device measurements and full PC-based spectrum analysis.

---

## 💡 Introduction

The **TinySA Ultra** is a versatile handheld spectrum analyser, but its limited display restricts long-term monitoring and in-depth analysis.  
This project extends its capabilities using **Python**, **Serial communication**, and **Matplotlib**, allowing you to view, record, and analyse spectrum data conveniently on your computer.

This repository contains two complementary scripts:

| Script | Function | Key Features |
|--------|-----------|---------------|
| `Tiny_Spectrum_Analyser_plot.py` | Live plotting | Real-time graph of amplitude vs. frequency, automatic scaling, and per-sweep CSV export |
| `Tiny_SA_Logger.py` | Background logging | Logs spectrum sweeps to timestamped CSV files at fixed intervals (user-defined frequency range and interval) |

---

## ⚙️ Features at a Glance

- 🔌 Simple serial connection (configurable COM port)
- 🧠 Intelligent frequency configuration — choose centre/span or start/stop range
- 💾 Automatic saving of every sweep with timestamped filenames
- 📊 Real-time Matplotlib visualisation (plot script)
- 🕒 Adjustable logging interval (seconds or minutes)
- 📈 CSV export for post-processing (NumPy, Pandas, Excel, etc.)
- 🧩 Compatible with Windows, macOS, and Linux

---

## 🧰 Requirements

- Python 3.8 or later  
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
Visualises the live RF spectrum in real time from the TinySA Ultra.

#### Run:
```bash
python Tiny_Spectrum_Analyser_plot.py
```

#### Behaviour:
- Prompts for serial port (default `COM22`)
- Streams spectrum data continuously
- Displays amplitude vs. frequency in an updating Matplotlib plot
- Saves each sweep automatically as:
  ```
  spectrum_sweep_YYYYMMDD_HHMMSS.csv
  ```

---

### 2️⃣ Periodic Data Logger  
**File:** `Tiny_SA_Logger.py`

#### Purpose:
Continuously logs TinySA Ultra data to CSV files at regular intervals.

#### Run:
```bash
python Tiny_SA_Logger.py
```

#### Configuration Prompts:
```
=== TinySA Ultra Data Logger ===

Select mode:
1. Centre frequency + span
2. Start and stop frequency
Enter choice (1 or 2): 1
Enter centre frequency in MHz (e.g., 433): 433
Enter span in MHz (e.g., 20): 10
Enter logging interval in seconds (e.g., 60): 10
```

#### Behaviour:
- Configures TinySA sweep range dynamically
- Reads a complete sweep of amplitude data via serial
- Saves timestamped CSV files every *N* seconds, for example:
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

- Combine live plotting and logging into a single GUI application  
- Add MQTT / InfluxDB support for networked data streaming  
- Web dashboard for remote spectrum viewing  
- Real-time anomaly detection (signal spikes or interference alerts)

---

## 🪪 Licence

This project is licensed under the **MIT Licence** — see the [LICENCE](LICENCE) file for details.

---

## 👤 Author

**Kris Seunarine**  

