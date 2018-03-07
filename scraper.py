# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html

# Read in a page
html = scraperwiki.scrape("http://www.lavanguardia.com/")

# Find something on the page using css selectors
root = lxml.html.fromstring(html)
bylines = root.cssselect("span.story-author-name")

# for byline in bylines:
#     print lxml.html.tostring(byline) 
#     print byline.text.encode('utf-8')
    
for byline in bylines:
  record = { "byline" : byline.text.encode('utf-8') } # column name and value
  scraperwiki.sqlite.save(["byline"], record) # save the records one by one

for byline in bylines:
  record = { "byline" : byline.text_content().encode('utf-8') } # column name and value
  scraperwiki.sqlite.save(["byline"], record) # save the records one by one
    
# titles = root.cssselect("a.story-header-title-link")



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
