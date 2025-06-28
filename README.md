# IoT-Based Microgrid Hardware Testbed
Main features: 
    1. IoT-based: A Microgrid Testbed based on Internet-of-things protocal (MQTT), which is good for distributed system.
    2. Authenticity: All the components are real hardware.
    3. Transparency：No simulator is involved and everything is visible.
    4. Cost-efficiency: the entire system costs around 1/40 of HIL system.
    5. Safety: Operating at 12V eliminates major concerns regarding electrical isolation.
    6. Easy Observation and control: The developed UI and SCADA system make the system-wide oberservation and control easier.
---

## System structure
![System structure](Slide9.JPG)

--- 

## Software Version

| Software | Version |
|-----------|----------|
| **Matlab** | 2020b |
| **CCS** | V12.7.1.00001 (TI compiler v22.6.1.LTS) |
| **Ubuntu**| 22.04 LTS |
 **python**| 3.11 |
 **PyQt6, PySide6**| 6.7.2 |
  **Paho-mqtt**| 2.1.0|
  **pyserial**| 3.5|
  **mosquitto**| 2.0.20|
  

---

## Required Hardware

- **Raspberry Pi:** 4*Raspberry Pi 5 (4G)
- **DSP controller:** 4*LAUNCHXL-F28379D  
- **Rounter** 
- **Others:**  
  - A Windos or Linux PC for SCADA 
  - Inductors, Capacitos for LC filters, feeders and loads
  - Relay blocks, circuit breakers for load changes
  - Banana cables, meters, oscilloscope ...
---

## System Parameters
| Source   | Inverter | DC Bus | LC Filter    |
| -------- | -------- | ------ | ------------ |
| DG 1 | 100VA    | 45V    | 0.56mH; 22μF |
| DG 2 | 100VA    | 45V    | 0.56mH; 22μF |
| DG 3 | 100VA    | 45V    | 0.56mH; 22μF |
| DG 4 | 100VA    | 45V    | 0.56mH; 22μF |

| Load          | Total Resistance | Inductance | Inductor DCR |
| ------------- | ---------------- | ---------- | ------------ |
| Load 1 (Z1)   | 10.08Ω (R + DCR) | 6.25mH ±1% | 2.08Ω        |
| Load 2 (Z2)   | 28.34Ω (R + DCR) | 8.0mH ±1%  | 3.34Ω        |
| Load 3 (Z3)   | 25.56Ω (R + DCR) | 1.8mH ±1%  | 0.85Ω        |
| Load 4 (Z4.1) | 10.08Ω (R + DCR) | 6.25mH ±1% | 2.08Ω        |
| Load 4 (Z4.2) | Adjustable: 10Ω  | -          | -            |

| Feeder       | Total Resistance   | Inductance | Inductor DCR |
| ------------ | ------------------ | ---------- | ------------ |
| Feeder (Z12) | 0.13Ω (0.1Ω + DCR) | 3.3μH ±15% | 0.03Ω        |
| Feeder (Z23) | 0.13Ω (0.1Ω + DCR) | 3.3μH ±15% | 0.03Ω        |
| Feeder (Z34) | 0.13Ω (0.1Ω + DCR) | 3.3μH ±15% | 0.03Ω        |
---


## Grid Level
![Grid Level1](Slide10.JPG)
![SystemPic](Slide11.JPG)
---

## Control Level
![Control Level](Slide12.JPG)
---

## SCADA
![SCADA](Slide13.JPG)
---

## Communication
![Communication](Slide14.JPG)
---

##  Operation Recoerd
![Record](Slide15.JPG)
---    

##  Implemented Algorithm
Droop control:
[1] N. Pogaku, M. Prodanovic, and T. C. Green, "Modeling, Analysis and Testing of Autonomous Operation of an Inverter-Based Microgrid," *IEEE Transactions on Power Electronics*, vol. 22, no. 2, pp. 613–625, Mar. 2007.  
Secondary control: 
[2] V. Nasirian, Q. Shafiee, J. M. Guerrero, F. L. Lewis, and A. Davoudi, “Droop-free distributed control for AC microgrids,” IEEE Trans. Power Electron., vol. 31, no. 2, pp. 1600–1617, Feb. 2016
---  
    
