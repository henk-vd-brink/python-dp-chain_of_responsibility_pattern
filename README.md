# Design Patterns: Chain of Responsibility

This code is written to get a better understanding Chain of Responsibility Design Pattern.

# Structure
```bash
.
├── README.md
└── app
    ├── __main__.py
    ├── app.py
    ├── data
    │   └── parcels.xml
    ├── src
    │   ├── __init__.py
    │   ├── abc_build_chain.py
    │   ├── departments
    │   │   ├── __init__.py
    │   │   ├── abc_department.py
    │   │   ├── heavy_department.py
    │   │   ├── mail_department.py
    │   │   └── regular_department.py
    │   ├── parcel.py
    │   └── parsers
    │       ├── abc_parser.py
    │       └── xml_parser.py
    └── tests
        └── test.py
```

# Usage 

Command: 
```bash
python app
```

