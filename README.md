# Edu-Blog

## Blog Web App System

Welcome aboard to our web application system, version 1.0! We provide documentation and resources to help you navigate the entire system.

From signing up on the platform to signing in, reading, and updating your blogs or content, we've made it easy for you to interact with our user-friendly interface.

Our platform is built on **Django**.

Since it is still in testing mode, we will provide instructions on how to check it out.

---

## Cloning the Repository

### via HTTPS:
```sh
https://github.com/devharnold/Edu-Blog.git
```

### via SSH:
```sh
git@github.com:devharnold/Edu-Blog.git
```

### via GitHub CLI:
```sh
gh repo clone devharnold/Edu-Blog
```

---

## Downloading Dependencies in Your Project Directory

### Initializing a Python Virtual Environment

#### **On Windows (CMD or PowerShell):**
1. Navigate to your project directory:
   ```sh
   cd path\to\your\project
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
3. Activate the virtual environment:
   - **Command Prompt (CMD):**
     ```sh
     venv\Scripts\activate
     ```
   - **PowerShell:**
     ```sh
     venv\Scripts\Activate.ps1
     ```
     *If you get an execution policy error, run:*
     ```sh
     Set-ExecutionPolicy Unrestricted -Scope Process
     ```
     *before activating.*

#### **On Linux (Terminal):**
1. Navigate to your project directory:
   ```sh
   cd /path/to/your/project
   ```
2. Create a virtual environment (*Ensure you have `python3` installed*):
   ```sh
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   ```sh
   source venv/bin/activate
   ```

To deactivate the virtual environment on both operating systems, run:
```sh
deactivate
```

---

## Installing Django
```sh
pip install Django
```

---

## Running the Server
```sh
python3 manage.py runserver
```

