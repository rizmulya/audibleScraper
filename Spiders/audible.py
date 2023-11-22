from Driver import By, WebDriverWait, EC, pd
from Driver.WebDriver import WebDriver
from Spiders.Locator import Locator


class EbaySpider:
    def __init__(self, headless):
        self.driver = WebDriver(headless).driver

    def navigate_to_website(self, link):
        print("Navigating to the website...")
        self.driver.get(link)
        self.driver.maximize_window()

    def scrape_data(self):
        print("Scraping data...")
        container = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(Locator.CONTAINER)
        )
        products = WebDriverWait(container, 5).until(
            EC.presence_of_all_elements_located(Locator.PRODUCTS)
        )
        book_title = []
        book_author = []
        book_length = []
        for product in products:
            print("Scraping ...")
            book_title.append(product.find_element(By.XPATH, ".//h3[contains(@class, 'bc-heading')]").text)
            book_author.append(product.find_element(By.XPATH, ".//li[contains(@class, 'authorLabel')]").text)
            book_length.append(product.find_element(By.XPATH, ".//li[contains(@class, 'runtimeLabel')]").text)
        return book_title, book_author, book_length

    def pagination(self):
        pagination = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(Locator.PAGINATION)
        )
        pages = WebDriverWait(pagination, 5).until(
            EC.presence_of_all_elements_located(Locator.PAGES)
        )
        last_pages = int(pages[-2].text) # 25
        book_title = []
        book_author = []
        book_length = []
        for i in range(1, last_pages+1): # 24+1
            title, author, length = self.scrape_data()
            book_title.extend(title)
            book_author.extend(author)
            book_length.extend(length)
            # 
            try:
                print(f"going to page {i+1} ...") if i<last_pages else None
                next_page = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(Locator.NEXT_BTN)
                )
                next_page.click()
            except:
                pass
        return {"book_title": book_title, "book_author": book_author, "book_length": book_length}

    def close_driver(self):
        self.driver.close()

    def exec(self, link, output_csv=False, output_json=False):
        self.navigate_to_website(link)
        data = self.pagination()
        self.close_driver()

        df = pd.DataFrame(data)
        if output_csv:
            df.to_csv(output_csv, index=False)
        if output_json:
            df.to_json(output_json, orient="records", indent=4)
        print(df)
        print("Scraping successful!")
