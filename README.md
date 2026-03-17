# Personal Data Toolkit CLI

A command-line tool for inspecting and analyzing CSV datasets.

This tool allows you to explore, filter, sort, and summarize data directly from the terminal. It is designed as a lightweight alternative to quick data inspection tasks without requiring heavy libraries like pandas.

---

## Features

- Load and inspect CSV datasets
- View row count and column names
- Preview first N rows
- Get unique values for a column
- Filter rows using conditions
- Sort data by any column (ascending/descending)
- Retrieve top N records based on a column
- Generate dataset summaries
- Built-in logging system
- Modular and extensible design

---

## Project Structure
```brew
personal-data-toolkit-cli/
│
├── cli.py # Command-line interface
├── toolkit.py # Core dataset operations (OOP)
├── utils.py # Helper functions (CSV loading, utilities)
│
├── sample_data/ # Example datasets
│ ├── users.csv
│ ├── sales.csv
│ └── products.csv
│
├── logs/
│ └── app.log # Application logs
│
├── README.md
├── requirements.txt
└── .gitignore
```


---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/personal-data-toolkit-cli.git
cd personal-data-toolkit-cli
```
No external dependencies required (uses Python standard library).

## Usage

All commands follow this pattern:
```brew
python cli.py --file <filename> [options]
```

## Commands
### 1. Row Count
```brew
python cli.py --file users.csv --rows
```

### 2. Column Names
```brew
python cli.py --file users.csv --columns
```
### 3. Preview First N Rows
```brew
python cli.py --file users.csv --head 5
```

### 4. Unique Values
```brew
python cli.py --file users.csv --unique country
```

### 5. Filter Rows
```brew
python cli.py --file users.csv --filter country=USA
```

### 6. Sort Data
```brew
python cli.py --file users.csv --sort-by age
```

#### Descending:
```brew
python cli.py --file users.csv --sort-by age --desc
```

### 7. Top N Records
```brew
python cli.py --file sales.csv --sort-by amount --top 3
```

### 8. Dataset Summary
```brew
python cli.py --file users.csv --summary
```

## Example Output
```brew
Rows where country=USA:
{'id': '1', 'name': 'Alice', 'age': '25', 'country': 'USA'}
{'id': '4', 'name': 'David', 'age': '35', 'country': 'USA'}
```

## Logging

Logs are stored in:

logs/app.log

Example log entries:
```brew
2026-03-17 00:12:01 - INFO - Program started
2026-03-17 00:12:05 - ERROR - Column not found
```

## Concepts Demonstrated

This project integrates multiple core Python concepts:

1. Data structures (lists, dictionaries, sets)

2. Functions and modular design

3. File handling (CSV)

4. List and dictionary comprehensions

5. Sorting and lambda functions

6. Generators (optional streaming)

7. Object-Oriented Programming (OOP)

8. Error handling (try/except)

9. Logging

10. Command-line interfaces (argparse)


## Example Datasets

Sample datasets are provided in the sample_data/ folder:
```brew
users.csv

sales.csv

products.csv
```

## Future Improvements

1. Export filtered results to CSV

2. Multi-condition filtering

3. Pretty table output

4. Numeric statistics (mean, min, max)

5. Search across all columns

6. Installable CLI command


## Author

**Sumit Barua**

MS Computer Science

Western Michigan University
