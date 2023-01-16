import scrapy


class LawsSpider(scrapy.Spider):
    name = 'laws'
    allowed_domains = ['laws.bahamas.gov.bs']
    start_urls = ['http://laws.bahamas.gov.bs/cms/en/legislation/acts.html']

    def parse(self, response):
        table = response.css('table')[0]
        

        for tr in table.css('tr')[2:]:

            item_id = tr.css('td.hasTip::text').get().strip()

            if item_id == '':
                item_id = tr.css('td.noTip::text').get().strip()
            
            short_title = tr.css('td.hasTip a::text').get().strip()
            title_url = 'http://laws.bahamas.gov.bs' + tr.css('td.hasTip a::attr(href)').get().strip()

            category = tr.css('td.category ::text').get().strip()

            commencement = tr.css('td.commencement ::text').get().strip()

            yield {
                'item_id' : item_id,
                'title' : short_title,
                'url' : title_url,
                'category' : category,
                'commencement' : commencement,
            }

        


        
