
# MLOps Lab 1 – Temperature Converter Project

This project is part of the **IE-7374 MLOps Lab** at Northeastern University.  
It demonstrates how to use **GitHub, virtual environments, testing frameworks, and GitHub Actions** for automation.

## 📂 Project Structure
```

mlops\_lab1\_text\_converter/
│── src/                # Source code files
│   └── converter.py    # Temperature converter functions + CLI
│── test/               # Test cases
│   ├── test\_converter\_pytest.py
│   └── test\_converter\_unittest.py
│── data/               # Placeholder for datasets (not used in this lab)
│── .github/workflows/  # GitHub Actions CI/CD workflows
│── .gitignore
│── requirements.txt
│── README.md

````

## ⚙️ Features
- Celsius → Fahrenheit  
- Fahrenheit → Celsius  
- Celsius → Kelvin  
- Kelvin → Celsius  
- Run directly in the terminal for conversions

## ▶️ How to Run
1. Activate the virtual environment:
   ```bash
   source lab_01/bin/activate
````

2. Run the converter in terminal:

   ```bash
   python3 src/converter.py
   ```
3. Example usage:

   ```
   Enter temperature in Celsius: 30
   30.0°C in Fahrenheit = 86.00°F
   30.0°C in Kelvin = 303.15K
   ```

## 🧪 Running Tests

### Pytest

```bash
pytest -q
```

### Unittest

```bash
python3 -m unittest test/test_converter_unittest.py
```

## 🤖 GitHub Actions

* `pytest_action.yml` → Runs pytest tests on every push
* `unittest_action.yml` → Runs unittest tests on every push

## 📌 Author

**Sreevarshan Sathiyamurthy**
Master’s in Data Analytics Engineering
Northeastern University
