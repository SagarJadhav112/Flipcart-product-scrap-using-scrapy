import scrapy


class FlipcartSpider(scrapy.Spider):
    name = 'flipcart'
    # allowed_domains = ['flipcart.com']
    # start_urls = ['https://www.flipkart.com/search?q=phone&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_5_0_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_5_0_na_na_na&as-pos=5&as-type=HISTORY&suggestionId=phone&requestId=af0cd99c-0918-48a3-8f22-36450837689b']

    def start_requests(self):
        yield scrapy.Request (
            url="https://www.flipkart.com/search?q=phone&page=",
            callback=self.parse)



    def parse(self, response):
        products = response.xpath('//div[@class="_2kHMtA"]')
        for product in products:


            try:
                product_name = product.xpath(".//div[@class='MIXNux']/following ::div[@class='_4rR01T']/text()").get()
            except:
                product_name = " Not available"


            try:
                product_price = product.xpath(".//div[@class='_25b18c']/child ::div[@class='_30jeq3 _1_WHN1']/text()").get().replace("₹", "")
            except:
                product_price = "Not available"


            try :
                product_ram = product.xpath(".//ul[@class='_1xgFaf']/child ::li[@class='rgWa7D'][1]/text()").get()
            except :
                product_ram = "Not available"


            try :
                product_display = product.xpath(".//ul[@class='_1xgFaf']/child ::li[@class='rgWa7D'][2]/text()").get()
            except:
                product_display = "Not available"


            try:
                product_camera = product.xpath(".//ul[@class='_1xgFaf']/child ::li[@class='rgWa7D'][3]/text()").get()
            except:
                product_camera = "Not available"

            bettary =product.xpath(".//ul[@class='_1xgFaf']/child ::li[@class='rgWa7D'][4]/text()").get()


            try :
                processor = product.xpath(".//ul[@class='_1xgFaf']/child ::li[@class='rgWa7D'][5]/text()").get()
            except :
                processor = "Not available"


            try:
                product_warranty = product.xpath(".//ul[@class='_1xgFaf']/child ::li[@class='rgWa7D'][6]/text()").get()
            except:
                product_warranty = "Not available"
   
            yield{
                "product_name": product_name,
                "product_price": product_price,
                "product_ram" : product_ram,
                "product_display": product_display,
                "product_camera": product_camera ,
                "product_warranty":product_warranty,
                "bettary":bettary,
                "processor" : processor}

        next_page = response.xpath("//span[text()='Next']/parent::a/@href").get()
        if next_page:
            abs_url = f"https://www.flipkart.com{next_page}"
            
            yield scrapy.Request(
                abs_url,
                callback=self.parse)
            


    
        # if next_page is not None :
        #     next_page_url = "https://www.flipkart.com" + next_page
        #     yield scrapy.Request(next_page_url, callback=self.parse)


        # next_page = response.css('a._1LKTO3 ::attr(href)'[1]).extract()  
        # if next_page is not None:
        #     next_page_url = "https://www.flipkart.com"+ next_page
        #     yield response.follow(next_page_url,callback=self.parse)
        # 
        #  
        # # if next_page:
        #     abs_url = f"https://www.amazon.in{next_page}"
        #     yield scrapy.Request(
        #         url = abs_url,
        #         callback = self.parse 






        
