# NWEA Map Automation Script

This script automates the process of logging into the NWEA Map system, navigating to the data export section, and unzipping the downloaded files. The script is designed to run with minimal intervention and logs its progress for easier troubleshooting.

## Prerequisites

- Python 3.x
- Selenium
- Chrome WebDriver
- WebDriver Manager
- Necessary modules for login and configuration

## Installation

1. **Clone the Repository**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Set Up the Environment**

    **Create a Virtual Environment with pipenv**: 
    ```bash
    pipenv install
    ```

    This will create a virtual environment and install the dependencies listed in the `Pipfile`.

3. **Set Up Configuration**
    - Ensure `modules/login.py` contains the `logIn()` function.
    - Ensure `config.py` contains the `username` and `password` variables.

## Usage

1. **Create a Batch File for Running the Script**

    **Create a Batch File**: Save the following content as a batch file in the same directory as `Pipfile` and `Pipfile.lock`.

    ```batch
    @echo off
    REM Navigate to the directory containing Pipfile and main.py

    REM Install dependencies using pipenv
    pipenv install

    REM Run the Python script
    pipenv run python ..\main.py

    REM Pause the window to view any output or errors
    pause
    ```

    **Run the Batch File**: Double-click `NWEA_Map.bat` or execute it from Command Prompt to run the script in the virtual environment.

## Script Overview

The script performs the following steps:

1. **Setup Logging**
    - Logs are saved to `NWEA_Map.log` in the `virtual_env` directory with a timestamp. This log file records the progress of the script and any issues encountered.

2. **Prepare Download Directory**
    - Deletes the existing `downloads` directory if it exists.
    - Creates a new `downloads` directory in the `virtual_env` directory. This is where downloaded files are saved.

3. **Configure Chrome Options**
    - Sets the default download directory to the `downloads` directory within the `virtual_env` folder.
    - Enables automatic downloads.

4. **Initialize WebDriver**
    - Uses ChromeDriverManager to install and initialize Chrome WebDriver with specified options.

5. **Perform Automated Tasks**
    - Logs into the NWEA Map system using provided credentials.
    - Navigates to the data export section.
    - Unzips downloaded files in the `virtual_env` directory.

6. **Cleanup and Exit**
    - Ensures the browser is closed.
    - Logs script exit and any errors encountered directly to SQL table if success or failure, runtime, etc..
    

## Logging

Logs are created in `NWEA_Map.log` located in the `virtual_env` directory. The log file includes timestamps and messages indicating the progress and any issues encountered during the script execution.

## Notes

- Ensure ChromeDriver is compatible with your installed version of Chrome.
- Update `config.py` with correct `username` and `password` for the NWEA Map system.
- Potential pop-ups at the home screen login could cause future issues.

---