# Data Directory

This directory is reserved for external input datasets used in the microgrid optimization framework.

At the current stage of the project, all numerical parameters, load profiles, and generation constraints are defined directly inside the GAMS model files (scenario1.gms and scenario2.gms). Therefore, no external CSV files are included here yet.

The directory is kept in the repository to enable future extensions where:
- PV and WT generation profiles
- Critical / semi-critical / flexible load profiles
- BESS technical parameters
- Diesel generator data
- Economic and emission factors

may be provided as external datasets.

