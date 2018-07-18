from os.path import join
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

base_url = 'http://www.futanet.hu/versenyeredmeny.php?versenyeredmeny[method]=keres'
opts = Options()
opts.set_headless()

out_path = 'data/iterim/tables'


def init_browser():
    browser = Chrome(options=opts)
    browser.get(base_url)
    select_no_results = Select(browser.find_element_by_id('versenyeredmeny[oldal]'))
    competitions = Select(browser.find_element_by_id('versenyeredmeny[verseny]'))
    return browser, select_no_results, competitions

browser, select_no_results, competitions = init_browser()
select_no_results.select_by_index(5)

i = 0
for i in range(0, 10):
    try:
        #TODO: get name and date of event, use it in fname
        browser, select_no_results, competitions = init_browser()
        select_no_results.select_by_index(5)
        competitions.select_by_index(i)
        browser.find_element_by_class_name('formbtn').click()
        t = browser.page_source.encode('utf-8')
        fname = str(i).zfill(4) + '.html'
        with open(join(out_path, fname), 'wb') as f:
            f.write(t)
        i += 1
    except Exception as e:
        continue
