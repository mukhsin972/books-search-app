import scrapy
import json

class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        books = response.css('article.product_pod')
        for book in books:
            yield {
                'title': book.css('h3 a::attr(title)').get(),
                'price': book.css('.price_color::text').get(),
                'availability': book.css('.availability::text').re_first('\S+'),
                'rating': book.css('p::attr(class)').re_first('star-rating (\w+)')
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
