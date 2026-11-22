# 🐍 Python practice

A collection of Python learning exercises, utilities, and sample projects.

## 🚀 Overview

This repository contains Python sample code, exercises, unit tests, and small utilities created as part of learning and practicing Python development.

It follows a clean project structure with:

src/ for application code

tests/ for unit tests

requirements.txt for dependencies

.gitignore to keep the repo clean

## 📂 Project Structure
learning/python/
│
├── src/
│   ├── main.py
│   └── sorting/          # 10 sorting algorithms (see src/sorting/README.md)
│
├── tests/
│   ├── test_main.py
│   └── test_sorting.py
│
├── requirements.txt
├── .gitignore
└── README.md
## 🔢 Sorting Techniques
Bubble, selection, insertion, shell, merge, quick, heap, counting, radix and bucket sort, written from scratch with complexity notes, a demo/benchmark and tests.
Details: [src/sorting/README.md](src/sorting/README.md)

```bash
python -m src.sorting              # demo
python -m src.sorting --bench 2000 # benchmark
```

## 🛠 Setup Instructions
### 1️⃣ Clone the repository
git clone https://github.com/balaji014/learning.git
cd learning/python
### 2️⃣ Create a virtual environment
python -m venv .venv
### 3️⃣ Activate the environment
#### Windows
.venv\Scripts\activate
#### Mac/Linux
source .venv/bin/activate
### 4️⃣ Install dependencies
pip install -r requirements.txt
## 🧪 Running Tests
#### pytest is used for unit testing.
python -m pytest
#### Expected output:
221 passed in 0.10s
## 📦 Dependencies
All dependencies are listed in requirements.txt.

To add new packages:
pip install <package>
pip freeze > requirements.txt
## 🧰 Tools & Technologies
**Python 3.10+** <br/>
**VS Code** <br/>
**pytest for testing** <br/>
**Git/GitHub for version control**

## 📈 Future Enhancements
. Add more Python examples and utilities<br/>
. Add CI/CD pipeline (GitHub Actions)<br/>
. Add Pylint/Ruff/Black for code quality<br/>
. Add sample APIs (FastAPI/Flask)<br/>
. Add beginner-to-advanced Python practice tasks<br/>

# 👨‍💻 Balaji Gurram
**Integration Architect | Python Learner** <br/>
**GitHub: https://github.com/balaji014**

## 📜 License
This project is open-source under the MIT License.

