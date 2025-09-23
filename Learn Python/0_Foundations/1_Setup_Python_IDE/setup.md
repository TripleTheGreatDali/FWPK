# Setting Up Python and IDEs

Welcome! Before diving into Python programming, you need to set up your environment. This guide will show you how to install Python and choose the right IDE on **Windows, Linux, Mac, and Raspberry Pi**.

---

## Why Setting Up Properly Matters

A proper setup allows you to:

* Write, run, and debug code efficiently
* Organize projects systematically
* Avoid errors caused by missing dependencies
* Scale your learning from small scripts to real-world projects

---

## 1. Installing Python

Python comes pre-installed on some systems but it’s important to ensure you have the **latest stable version (Python 3.x)**.

### Windows

1. Go to [Python.org](https://www.python.org/downloads/windows/)
2. Download the **Windows installer (64-bit recommended)**
3. Run the installer and check **“Add Python to PATH”**
4. Click **Install Now**
5. Verify installation in Command Prompt:

```bash
python --version
```

### Mac (macOS)

1. macOS comes with Python 2.x pre-installed; you need Python 3.x
2. Install **Homebrew** if not installed:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

3. Install Python 3:

```bash
brew install python
```

4. Verify installation:

```bash
python3 --version
```

### Linux (Ubuntu/Debian)

1. Update package list:

```bash
sudo apt update
```

2. Install Python 3 and pip:

```bash
sudo apt install python3 python3-pip
```

3. Verify installation:

```bash
python3 --version
pip3 --version
```

### Raspberry Pi (Raspbian / Raspberry Pi OS)

1. Python 3 is pre-installed on most Raspberry Pi distributions
2. To update and ensure the latest version:

```bash
sudo apt update
sudo apt upgrade
sudo apt install python3 python3-pip
```

3. Verify installation:

```bash
python3 --version
pip3 --version
```

---

## 2. Choosing an IDE (Integrated Development Environment)

An IDE helps you write, debug, and organize code efficiently. Recommended options:

### VS Code (All Platforms)

* Lightweight, fast, highly customizable
* Install from [VS Code website](https://code.visualstudio.com/)
* Install Python extension inside VS Code
* Features: syntax highlighting, debugging, Git integration, virtual environment support

### PyCharm (Windows, Mac, Linux)

* Full-featured IDE for Python
* Community edition is free
* Download from [JetBrains PyCharm](https://www.jetbrains.com/pycharm/download/)
* Features: intelligent code completion, project management, testing tools

### Thonny (Linux, Mac, Windows, Raspberry Pi)

* Beginner-friendly, pre-installed on Raspberry Pi
* Lightweight, simple interface
* Download: [Thonny.org](https://thonny.org/)
* Ideal for learning Python basics

### Other Options

* **Jupyter Notebook:** Interactive coding, ideal for data science
* **Atom:** Lightweight editor, customizable with packages

---

## 3. Setting Up Virtual Environments

Virtual environments help isolate project dependencies.

1. Create a folder for your projects
2. Open terminal or command prompt in that folder
3. Create a virtual environment:

```bash
python3 -m venv env
```

4. Activate the environment:

* **Windows:**

```bash
.\env\Scripts\activate
```

* **Linux / Mac / Raspberry Pi:**

```bash
source env/bin/activate
```

5. Install packages inside the virtual environment using pip:

```bash
pip install package_name
```

---

## 4. Test Your Setup

Create a simple Python file `hello.py`:

```python
print("Hello, Python!")
```

Run it using:

```bash
python hello.py      # Windows
python3 hello.py     # Linux, Mac, Raspberry Pi
```

Expected output:

```
Hello, Python!
```

---

Your Python environment is now ready. You can start coding, experimenting, and learning efficiently!
