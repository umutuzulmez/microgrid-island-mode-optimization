# Microgrid Optimization in Island Mode (GAMS – MILP)

This project presents a 24-hour operational planning model for an islanded microgrid formulated as a **Mixed-Integer Linear Programming (MILP)** problem. The optimization framework is implemented in GAMS using the CPLEX solver, and all scenario outputs and visualization scripts are included in the repository.

The model jointly evaluates photovoltaic (PV) generation, wind turbine (WT) generation, a diesel generator (DG), and a battery energy storage system (BESS). Critical, semi-critical, and flexible load groups are represented through separate demand profiles, all enforced through full-service constraints.

---

## 1. System Description

The microgrid model consists of the following components:
* **Photovoltaic (PV) generation**
* **Wind turbine (WT) generation**
* **Diesel generator (DG)** with a binary on/off status and minimum load requirement
* **Battery Energy Storage System (BESS)**
* **Critical, semi-critical, and flexible loads**

All resources and loads are evaluated on an hourly basis.

---

## 2. Repository Structure

```
├── gams/              
│   ├── scenario1.gms
│   └── scenario2.gms
│
├── data/              
│   └── README_DATA.md
│
├── results/           
│   ├── scenario1_results.csv
│   ├── scenario2_results.csv
│   └── plots/
│       ├── s1_plot_*.png  
│       └── s2_plot_*.png  
│
├── scripts/
│   └── generate_plots.py
│
├── requirements.txt   
└── README_EN.md
└── README_TR.md
```

---

## 3. Scenarios

### **Scenario 1 – Deterministic case**

PV and WT generation limits are defined using fixed capacity profiles.

### **Scenario 2 – Real meteorological data**

PV and WT capacity limits are derived from real solar irradiance and wind speed measurements.

Both scenarios share the same structure, decision variables, constraints, and objective function. Although the data sources differ, the scenarios remain directly comparable in terms of operational behavior and constraint effects.

---

## 4. Optimization Model

### **Objective Function**

The objective is to minimize total operating cost, which includes:

* PV generation cost
* WT generation cost
* BESS charging and discharging cost
* Diesel generator fuel cost

Since all load groups are fully served by definition, the model does not include load-shedding penalties.

### **Main Constraints**

* Hourly energy balance
* PV and WT capacity limits
* DG maximum and minimum power constraints
* Binary DG operating status
* BESS charge and discharge limits
* SOC bounds (20% – 90%)
* Full service of critical, semi-critical, and flexible loads

---

## 5. Outputs

The CSV files generated for each scenario contain the following hourly variables:

* **scenario1_results.csv**
* **scenario2_results.csv**

Each file contains the following hourly variables:

* PV generation
* WT generation
* DG output and operating state
* BESS charging and discharging
* SOC profile
* Served critical, semi-critical, and flexible loads
* Total supply distribution
* DG-based carbon emissions

These CSV files are directly connected to the generated plots.

---

## 6. Visualizations

Each scenario includes seven plots, resulting in a total of fourteen figures:

1. Battery power flow
2. Carbon emissions
3. Energy flow and source contribution
4. Renewable generation profile
5. Load distribution
6. SOC profile
7. Total operating cost

---

## 7. Running the Model

### **Requirements**

* GAMS + CPLEX
* Python

### **Steps**

1. Run either `scenario1.gms` or `scenario2.gms` in GAMS.
2. The outputs will be stored automatically in the `results/` directory.
3. To generate the plots:
```
pip install -r requirements.txt
python scripts/generate_plots.py
```
---

## 8. License

This project is distributed under the **MIT License**.

---

## 9. Contact

For technical discussion, collaboration, or project inquiries, feel free to get in touch.
