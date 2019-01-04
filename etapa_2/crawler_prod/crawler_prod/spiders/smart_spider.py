import scrapy


class SmartSpider(scrapy.Spider):
    name = "smartphone"
    start_urls = [
        'https://www.buscape.com.br/celular-e-smartphone',
    ]

    def parse(self, response):
        for smartphone in response.css('div.card--product__name.u-truncate-multiple-line'):
            yield {'titulo'     : smartphone.css('::text').extract_first(),
                   'categoria'  : 'smartphone'}
        
        css_selec = 'li.pagination__item.pagination__icon.button-tab-links a::attr(href)'
        try:
            # extrai o segundo link (link para próxima página da segunda em diante)
            next_page = response.css(css_selec)[1].extract()
        except Exception as e:
            # extrai o primeiro link (link para a próxima página quando se está na primeira)
            next_page = response.css(css_selec).extract_first()
        
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)