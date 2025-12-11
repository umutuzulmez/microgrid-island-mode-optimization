# Microgrid Island Mode Optimization (GAMS – MILP)

This repository presents a fully developed Mixed-Integer Linear Programming (MILP) optimization model for an island-mode microgrid. The model is implemented in **GAMS** using the **CPLEX** solver and includes complete datasets, scenario-based results, and visualization outputs.

The project aims to provide a transparent, reproducible, and engineering‑oriented framework for microgrid operations, covering renewable generation, diesel dispatch, and BESS energy management.

---

## 1. Microgrid Architecture

The modeled microgrid operates entirely in island mode over a 24‑hour horizon and includes the following components:

* **Photovoltaic (PV) generation**
* **Wind turbine (WT) generation**
* **Diesel generator (DG)** with on/off decision variables
* **Battery Energy Storage System (BESS)**
* **Critical, semi-critical, and flexible loads**

Load prioritization ensures uninterrupted supply to critical and semi-critical loads under all operational conditions.

---

## 2. Project Structure

```
├── gams/              # GAMS optimization models
│   ├── scenario1.gms
│   └── scenario2.gms
│
├── data/              # Input datasets
│   └── README_DATA.md
│
├── results/           # Model outputs
│   ├── scenario1_results.csv
│   ├── scenario2_results.csv
│   └── plots/
│       ├── s1_plot_*.png  # 7 plots (Scenario 1)
│       └── s2_plot_*.png  # 7 plots (Scenario 2)
│
├── requirements.txt   # Python dependencies for visualizations
└── README_EN.md
└── README_TR.md
```

---

## 3. Scenarios

### **Scenario 1 – Deterministic Baseline**

A reference scenario using fixed generation and load profiles.

### **Scenario 2 – Real Meteorological Data**

Uses actual solar and wind datasets to reflect realistic renewable variability.

Both scenarios maintain identical model structure and constraints, enabling direct comparison.

---

## 4. MILP Optimization Model

The optimization problem minimizes the total operating cost of the microgrid subject to operational and physical constraints.

### **Objective Function**

Minimize:

* Diesel generator fuel cost
* Start/stop cost
* Unserved flexible load penalties (if applicable)

### **Key Constraints**

* **Energy balance:** supply = demand for each hour
* **Renewable limits:** PV/WT generation upper bounds
* **DG operation:** binary on/off status, output bounds, startup constraints
* **BESS model:** charge/discharge power limits, charge efficiency, discharge efficiency
* **SOC boundaries:** 20% ≤ SOC ≤ 90%
* **Load priority:** critical and semi-critical loads must be fully satisfied

---

## 5. Results

The main outputs for each scenario are provided as:

* **scenario1_results.csv**
* **scenario2_results.csv**

Each file contains the following hourly variables:

* PV generation
* WT generation
* DG power output
* BESS charging/discharging
* SOC (State of Charge)
* Served load (critical, semi-critical, flexible)
* Total supply and unmet load

These CSV files are directly connected to the generated plots.

---

## 6. Visualizations (14 Plots)

The **plots/** directory contains 14 charts:

* **7 for Scenario 1**
* **7 for Scenario 2**

Plot names follow the same structure for both scenarios, enabling one-to-one comparison.

### Included charts (for each scenario):

1. Battery Power Flow
2. Carbon Emissions
3. System Energy Flow and Source Contribution
4. Renewable Energy Utilization
5. Residential Load Contribution
6. Battery State of Charge (SOC)
7. Total Operating Cost

---

## 7. Running the Model

### **Requirements**

* GAMS + CPLEX Solver
* Python (for visualizations)

### **Steps**

1. Open GAMS.
2. Load `scenario1.gms` or `scenario2.gms`.
3. Run with **F9**.
4. CSV outputs will be generated automatically in the **results/** directory.
5. To regenerate plots:

```
pip install -r requirements.txt
```

---

## 8. License

This project is distributed under the **MIT License**.

---

## 9. Contact

For questions or collaboration:

* Email or LinkedIn contact can be added here.

This repository is designed for academic, research, and engineering portfolio use, providing a comprehensive example of microgrid optimization implemented with GAMS and MILP.
