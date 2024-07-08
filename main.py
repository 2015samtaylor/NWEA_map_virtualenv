from modules.login import *
from config import username, password
import shutil

logging.basicConfig(filename='NWEA_Map.log', level=logging.INFO,
                   format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',force=True)
logging.info('\n\n-------------NWEA_Map new instance log')

shutil.rmtree(os.getcwd() + '\\downloads')
create_directory('downloads')

chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : os.getcwd() + '\\downloads',
         'profile.default_content_setting_values.automatic_downloads': 1,
         'profile.content_settings.exceptions.automatic_downloads.*.setting': 1}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)

logIn(username, password, driver)
get_to_data_export(driver)
unzip_files_in_same_dir()
driver.close()