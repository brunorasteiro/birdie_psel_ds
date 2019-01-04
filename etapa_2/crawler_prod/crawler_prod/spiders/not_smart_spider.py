import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider

class SmartSpider(CrawlSpider):
    name = "nao_smartphone"
    start_urls = [
        'https://www.buscape.com.br/sitemap',
        'https://www.buscape.com.br/sitemap?pagina=2'
    ]

    def parse(self, response):
        prod_links = LinkExtractor(restrict_css='div.card--container', deny='.*/celular-e-smartphone')
        pages = prod_links.extract_links(response)
        
        for page in pages:
            #print(page.url)
            yield scrapy.Request(page.url, callback=self.parse_prod)


    def parse_prod(self, response):
        for n_smart in response.css('div.card--product__name.u-truncate-multiple-line'):
            yield {'titulo'     : n_smart.css('::text').extract_first(),
                   'categoria'  : 'nao-smartphone'}
        
        if 'celular-e-smartphone' in response.request.url:
            css = 'li.pagination__item.pagination__icon.button-tab-links a::attr(href)'
            page = 1

            try:
                # extrai o segundo link (link para próxima página da segunda em diante)
                next_page = response.css(css)[1].extract()
                page = int(response.request.url.split('=')[1])
            except Exception as e:
                # extrai o primeiro link (link para a próxima página quando se está na primeira)
                next_page = response.css(css).extract_first()

            #if (next_page is not None) and (page < 50):
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse_prod)