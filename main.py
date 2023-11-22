from Spiders.audible import EbaySpider


spider = EbaySpider(
    headless=True  #headless = scraping without the browser
)

spider.exec(
    ## Linking to 25 pages
    # Link: "https://www.audible.com/search"
    ## Only linking 5 pages (for testing purposes)
    link="https://www.audible.com/adblbestsellers?ref_pageloadid=not_applicable&ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=6fb0ac98-e9fb-4acd-8278-aa237978ed3e&pf_rd_r=0GXSQJZZKZDBA6ZEYWRB&pageLoadId=FRGmBqy6L6mMCbQR&ref_plink=not_applicable&creativeId=1642b4d1-12f3-4375-98fa-4938afc1cedc&overrideBaseCountry=true&ipRedirectOverride=true&ref_pageloadid=not_applicable&pf_rd_p=f50add7f-c842-4751-adde-62bf930d9265&pf_rd_r=WW84CAC5RKSMTNRYBPHE&pageLoadId=L6Z8M8SiumYZCJ2I&ref_plink=not_applicable&creativeId=b50d3acf-bf15-400e-8f43-f1ebd0e505ca",
    output_csv = "Reports/audible_data.csv",
    # output_json = "Reports/audible_data.json"
)
