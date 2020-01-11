Maximal cut SDP relaxation
==============================

This project contains my implementation of SDP relaxation of Max Cut problem, the Goemans-Williamson algorithm, brute force solution, tests for it and the [pdf-report](https://github.com/rvg77/max-cut/blob/master/reports/Max_cut_relaxation.pdf) about all the work done.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   ├── models         <- Contains maxcut implementations
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── cut_visual.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------
