
from modules.login import *
from modules.logging_metadata import *
from config import username, password
import shutil
import pandas as pd

logger = JobLogger('NWEA_Map', 'python')
logging.basicConfig(filename='NWEA_Map.log', level=logging.INFO,
                   format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',force=True)
logging.info('\n\n-------------NWEA_Map new instance log')

try:
    shutil.rmtree(os.getcwd() + '\\downloads')
    logging.info('Removing downloads folder')
except FileNotFoundError:
    logging.info('Unable to remove downloads folder, it does not exist')

create_directory('downloads')

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : os.getcwd() + '\\downloads',
         'profile.default_content_setting_values.automatic_downloads': 1,
         'profile.content_settings.exceptions.automatic_downloads.*.setting': 1}
chrome_options.add_experimental_option('prefs', prefs)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options = chrome_options)


def main():
    try:
        logIn(username, password, driver)
        get_to_data_export(driver)
        unzip_files_in_same_dir()

        try:
            driver.quit()
            logging.info('Browser closed.')
        except Exception as e:
            logging.error(f'Error closing browser: {e}')

        # Confirm script exit
        logging.info('Script exiting.')

        logger.log_job('Success')
        logger.send_frame_to_SQL()
    except:
        logging.info('Process failed')
        logger.log_job('Failure')
        logger.send_frame_to_SQL()

main()