# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

#!/usr/bin/env python
import scraperwiki
import lxml.html
import urlparse

# La Vanguardia
html = scraperwiki.scrape("http://www.lavanguardia.com/")

root = lxml.html.fromstring(html)
articles = root.cssselect("span.story-author-name")

for article in articles:
    record = {}
    record['Author'] = article.text
    record['Media'] = "La Vanguardia"

    print record, '------------'

    scraperwiki.sqlite.save(["Author"], record)

# La Vanguardia titulars
html = scraperwiki.scrape("http://www.lavanguardia.com/")

root = lxml.html.fromstring(html)
articles = root.cssselect("a.story-header-title-link")

for article in articles:
    record = {}
    record['Author'] = article.text
    record['Media'] = "La Vanguardia"

    print record, '------------'

    scraperwiki.sqlite.save(["Author"], record)


# Ara.cat
html = scraperwiki.scrape("https://www.ara.cat/")

root = lxml.html.fromstring(html)
articles = root.cssselect("span.byline")

for article in articles:
    record = {}
    record['Author'] = article.text
    record['Media'] = "Ara.cat"

    print record, '------------'

    scraperwiki.sqlite.save(["Author"], record)

# Catalunya Plural
html = scraperwiki.scrape("http://catalunyaplural.cat/ca")

root = lxml.html.fromstring(html)
articles = root.cssselect('a[href]')

for article in articles:
    record = {}
    record['Author'] = article.text
    record['Media'] = "Catalunya Plural"

    print record, '------------'

    scraperwiki.sqlite.save(["Author"], record)

# Directa
html = scraperwiki.scrape("https://directa.cat/")

root = lxml.html.fromstring(html)
articles = root.cssselect('a.autor')

for article in articles:
    record = {}
    record['Author'] = article.text
    record['Media'] = "Directa"

    print record, '------------'

    scraperwiki.sqlite.save(["Author"], record)

# El Mon

with open(r'D:/TOT/M%C3%A0ster%20BCU/S2%20-%20Specialist%20journalism,%20investigations%20and%20coding/Scraping/Diaris/El%20M%C3%B3n%20-%20El%20diari%20lliure,%20obert%20i%20per%20compartir%207M.html', "r") as f:
    page = f.read()
root = html.fromstring(page)

# root = lxml.html.fromstring(html)
articles = root.cssselect('span.author')

for article in articles:
    record = {}
    record['Author'] = article.text
    record['Media'] = "El Mon"

    print record, '------------'

    scraperwiki.sqlite.save(["Author"], record)

# # Vilaweb - scraping links - FORBIDDEN
# html = scraperwiki.scrape("https://www.vilaweb.cat/")

# root = lxml.html.fromstring(html)
# articles = root.cssselect("a[starts-with(@class, 'link-noticia')]")

# for article in articles:
#     record = {}
#     record['Author'] = article.attrib['href']
#     record['Media'] = "Vilaweb"

#     print record, '------------'

#     scraperwiki.sqlite.save(["Author"], record)

# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
