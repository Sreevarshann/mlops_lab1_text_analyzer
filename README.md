# MLOps Lab 1 – Temperature Converter & Text Analyzer Projects

This project is part of the **IE-7374 MLOps Lab** at Northeastern University.  
It demonstrates how to use **GitHub, virtual environments, testing frameworks, and GitHub Actions** for automation.

---

## 📂 Project Structure

```
mlops_lab1/
├── src/                # Source code files
│   ├── converter.py    # Temperature converter functions + CLI
│   └── text_analyzer.py # Text analyzer functions
├── test/               # Test cases
│   ├── test_converter_pytest.py
│   ├── test_converter_unittest.py
│   ├── test_text_pytest.py
│   └── test_text_unittest.py
├── data/               # Placeholder for datasets (not used in this lab)
├── .github/workflows/  # GitHub Actions CI/CD workflows
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Features

### 🔹 Temperature Converter
- Celsius → Fahrenheit  
- Fahrenheit → Celsius  
- Celsius → Kelvin  
- Kelvin → Celsius  
- Run directly in the terminal for conversions  

### 🔹 Text Analyzer
- Count words  
- Count characters  
- Count vowels  
- Count consonants  
- Check if text is palindrome  
- Find most common word  
- Reverse text  
- Summary dictionary (all stats together)

---

## ▶️ How to Run

### Temperature Converter

1. **Activate the virtual environment:**
   ```bash
   source lab_01/bin/activate
   ```

2. **Run the converter in terminal:**
   ```bash
   python3 src/converter.py
   ```

3. **Example usage:**
   ```
   Enter temperature in Celsius: 30
   30.0°C in Fahrenheit = 86.00°F
   30.0°C in Kelvin = 303.15K
   ```

### Text Analyzer

Run directly in Python:

```python
from src.text_analyzer import *

print(count_words("hello world"))         # 2
print(count_chars("hello"))               # 5
print(count_vowels("apple"))              # 2
print(count_consonants("apple"))          # 3
print(is_palindrome("madam"))             # True
print(most_common_word("hi hi hello"))    # hi
print(reverse_text("python"))             # nohtyp
print(summary("madam is coding"))
```

---

## 🧪 Running Tests

### Pytest
```bash
pytest -q
```

### Unittest
```bash
python3 -m unittest
```

---

## 🤖 GitHub Actions

- `pytest_action.yml` → Runs pytest tests on every push
- `unittest_action.yml` → Runs unittest tests on every push

---

## 📌 Author

**Sreevarshan Sathiyamurthy**  
Master's in Data Analytics Engineering  
Northeastern University
