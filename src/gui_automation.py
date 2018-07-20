from os.path import join
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from concurrent.futures import ThreadPoolExecutor
###############################################################################
#####                            setup                                    #####
###############################################################################
base_url = 'http://www.futanet.hu/versenyeredmeny.php?versenyeredmeny[method]=keres'
opts = Options()
opts.set_headless()

out_path = 'data/interim/tables'


###############################################################################
#####              selenium functions getting our data                    #####
###############################################################################
def init_browser():
    """Initialize browser and sets dropdown menu items"""
    browser = Chrome(options=opts)
    browser.get(base_url)
    select_no_results = Select(browser.find_element_by_id('versenyeredmeny[oldal]'))
    competitions = Select(browser.find_element_by_id('versenyeredmeny[verseny]'))
    return browser, select_no_results, competitions


def get_table_from_site(idx):
    """Downloads the site at idx"""
    try:
        browser, select_no_results, competitions = init_browser()
        select_no_results.select_by_index(5)
        competitions.select_by_index(idx)
        browser.find_element_by_class_name('formbtn').click()
        t = browser.page_source.encode('utf-8')
        fname = competition_names[idx] + '.html'
        with open(join(out_path, fname), 'wb') as f:
            f.write(t)
        browser.quit()
    except Exception as e:
        print(e)

###############################################################################
#####        initialize selenium, get the list of competitions            #####
###############################################################################
browser, select_no_results, competitions = init_browser()
competition_elements = browser.find_elements_by_id('versenyeredmeny[verseny]')
competition_names = [e.text for e in competition_elements][0]
competition_names = competition_names.split('\n')
competition_names = [e.strip() for e in competition_names]

select_no_results.select_by_index(5)

###############################################################################
#####                       download tables                               #####
###############################################################################
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(get_table_from_site, list(range(1, len(competition_names)+1)))
