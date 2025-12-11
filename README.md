# Microgrid Island Mode Optimization (GAMS – MILP)

This repository contains an individually developed optimization model for an islanded microgrid using **GAMS/CPLEX**.  
The project includes the full MILP formulation, data inputs, scenario-based results, and Python visualizations.

The microgrid model includes:

- Photovoltaic (PV) generation  
- Wind turbine (WT) generation  
- Diesel generator (DG)  
- Battery Energy Storage System (BESS)  
- Critical, semi-critical, and flexible loads  
- 24-hour island-mode operation  

---

## Project Structure
```
gams/ → GAMS optimization models (scenario 1 & 2)
data/ → Input datasets
results/ → Simulation outputs (CSV)
results/plots → Python-generated charts
docs/ → Additional documents (optional)
```

---

## Optimization Model (MILP)

The model minimizes total microgrid operating cost while satisfying:

- Energy balance  
- PV/WT generation limits  
- DG on/off constraints  
- BESS charge/discharge model  
- SOC constraints (20–90%)  
- Load priority equations  

---

## Python Visualizations

Visualizations include:

- Battery SOC  
- Energy flow  
- DG usage  
- Renewable contribution  
- Cost and emission comparison  

Charts are located in: 
```
results/plots/
```

---

## Running the Model

1. Install **GAMS + CPLEX**  
2. Open `scenario1.gms` or `scenario2.gms`  
3. Press **F9**  
4. CSV results appear in `/results/`  

---

## License

MIT License.



