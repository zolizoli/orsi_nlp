from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

base_url = 'http://www.futanet.hu/versenyeredmeny.php?versenyeredmeny[method]=keres'
opts = Options()
opts.set_headless()
browser = Chrome(options=opts)
browser.get(base_url)


select_no_results = Select(browser.find_element_by_id('versenyeredmeny[oldal]'))
select_no_results.select_by_index(5)

competitions = browser.find_element_by_id('versenyeredmeny[verseny]')
for competition in competitions.find_elements_by_name('option'):
    competition.click()
    hits = browser.find_elements_by_class_name('inp')
    browser.find_element_by_class_name('formbtn').click()
    print(browser.page_source.encode('utf-8'))
    break
t = browser.page_source
with open('data/')