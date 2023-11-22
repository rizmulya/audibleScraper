from Driver import By


class Locator:
    CONTAINER = (By.CLASS_NAME, "adbl-impression-container ")
    PRODUCTS = (By.XPATH, ".//li[contains(@class, 'productListItem')]")
    PAGINATION = (By.XPATH, "//ul[contains(@class, 'pagingElements')]")
    PAGES = (By.TAG_NAME, "li")
    NEXT_BTN = (By.XPATH, "//span[contains(@class, 'nextButton')]")
    