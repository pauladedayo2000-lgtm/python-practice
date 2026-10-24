# Python Practice

A collection of 8 beginner Python exercises, one per core concept, with
automated tests for two of them.

## Requirements
- Python 3.10 or higher (includes IDLE)
- Git (optional, only needed to clone the repository)

## Setup
1. Clone or download this repository.
2. Open IDLE. No packages need to be installed.

## How to run an exercise
In IDLE, click File, then Open, choose the .py file, and press F5.

| Concept | Folder | File to run | What it does |
|---|---|---|---|
| Variables and data types | 01_variables_and_data_types | bmi_calculator.py | Calculates BMI from user input |
| Conditionals | 02_conditionals | grade_classifier.py | Converts a score to a letter grade |
| Loops | 03_loops | multiplication_table.py | Prints times tables until you type q |
| Functions | 04_functions | palindrome_checker.py | Checks if text is a palindrome |
| Modules | 05_modules | convert_demo.py | Uses unit_converter.py and datetime |
| Error handling | 06_error_handling | safe_divide.py | Divides two numbers without crashing |
| File handling | 07_file_handling | word_counter.py | Counts words in sample.txt, writes output.txt |
| Script organisation | 08_script_organisation | expense_tracker.py | Command-line expense tracker |

## How to run the tests
Tests use Python's built-in unittest module.
- 02_conditionals/test_grade_classifier.py
- 06_error_handling/test_safe_divide.py

Open a test file in IDLE and press F5. A passing run prints OK.

## Debugging note
See DEBUGGING_NOTE.md.