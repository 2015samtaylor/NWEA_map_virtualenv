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

2. **Install Required Packages**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Configuration**
    - Ensure `modules/login.py` contains the `logIn()` function.
    - Ensure `config.py` contains the `username` and `password` variables.

## Usage

1. **Run the Script**
    ```bash
    python script_name.py
    ```

## Script Overview

The script performs the following steps:

1. **Setup Logging**
    - Logs are saved to `NWEA_Map.log` with a timestamp.

2. **Prepare Download Directory**
    - Deletes the existing `downloads` directory.
    - Creates a new `downloads` directory.

3. **Configure Chrome Options**
    - Sets the default download directory.
    - Enables automatic downloads.

4. **Initialize WebDriver**
    - Uses ChromeDriverManager to install and initialize Chrome WebDriver with specified options.

5. **Perform Automated Tasks**
    - Logs into the NWEA Map system using provided credentials.
    - Navigates to the data export section.
    - Unzips downloaded files in the same directory.

6. **Cleanup and Exit**
    - Ensures the browser is closed.
    - Logs script exit and any errors encountered.

## Logging

Logs are created in `NWEA_Map.log` and include timestamps and messages indicating the progress and any issues encountered during the script execution.

## Notes

- Ensure ChromeDriver is compatible with your installed version of Chrome.
- Update `config.py` with correct `username` and `password` for the NWEA Map system.
- Potential pop up at the home screen login could cause future issues

---

