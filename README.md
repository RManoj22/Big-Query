# Project Setup Instructions

## Prerequisites

Ensure you have the following installed on your machine:

- Python 3.8 or higher
- pip (Python package manager)
- Streamlit library (will be installed via requirements.txt)

---

## Setup Guide

Follow these steps to set up the project and run the application:

### Step 1: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 2: Activate the Virtual Environment

- **On Windows**:
  ```bash
  .\venv\Scripts\activate
  ```
- **On macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Required Dependencies

Install the dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

Start the application using Streamlit:

```bash
streamlit run main.py
```

---

## Additional Information

- To deactivate the virtual environment after use, simply run:

  ```bash
  deactivate
  ```

- If you encounter any issues, ensure all dependencies are properly installed and Python is added to your system PATH.

Enjoy using the application!

