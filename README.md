## About the Project
This code is written to get a better understanding Chain of Responsibility Design Pattern.

## Getting Started

### Installation
```
git clone https://github.com/henk-vd-brink/python-dp-chain_of_responsibility.git
cd python-dp-chain_of_responsibility
```

### Run
```
python app
```


## Structure
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
    │   ├── base_build_chain.py
    │   ├── departments
    │   │   ├── __init__.py
    │   │   ├── base_department.py
    │   │   ├── heavy_department.py
    │   │   ├── mail_department.py
    │   │   └── regular_department.py
    │   ├── parcel.py
    │   └── parsers
    │       ├── base_parser.py
    │       └── xml_parser.py
    └── tests
        └── test.py
```
