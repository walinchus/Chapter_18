# Data stored on individual pages not accessible from one single page
# typical URL is https://paulbradshaw.github.io/scraping-for-everyone/scottishschools/iSchoolid_5237521.html
# Need to cycle through a list of those codes
#If you want to understand this scraper - start at the bottom where it says 'base_url' (line 40 or so)
import scraperwiki
import lxml.html

#Create a function called 'scrape_table' which is called in the function 'scrape_page' below
#The 'scrape_page' function also passed the contents of the page to this function as 'root'
def scrape_table(root):
    #Use cssselect to find the contents of a particular HTML tag, and put it in a new object 'rows'
    #there's more than one table, so we need to specify the class="destinations", represented by the full stop
    rows = root.cssselect("table.destinations tr")
    for row in rows:
        #Create a new empty record
        record = {}
        #Assign the contents of <td to a new object called 'table_cells'
        table_cells = row.cssselect("td")
        #If there's anything
        if table_cells: 
            #Put the contents of the first <td into a record in the column 'FSM'
            record['FSM'] = table_cells[0].text
            #this takes the ID number, which has been named item in the for loop below
            record['ID'] = item
            print record, '------------'
            #Save in the SQLite database, with the ID code to be used as the unique reference
            scraperwiki.sqlite.save(["ID"], record)

#this creates a new function and (re)names whatever parameter is passed to it - i.e. 'next_link' below - as 'url'
def scrape_page(url):
    #now 'url' is scraped with the scraperwiki library imported above, and the contents put into a new object, 'html'
    html = scraperwiki.scrape(url)
    print html
    #now we use the lxml.html function imported above to convert 'html' into a new object, 'root'
    root = lxml.html.fromstring(html)
    #now we call another function on root, which we write - above
    scrape_table(root)

#START HERE: This is the part of the URL which all our pages share
base_url = 'https://paulbradshaw.github.io/scraping-for-everyone/scottishschools/iSchoolid_'
#And these are the numbers which we need to complete that URL to make each individual URL
#This list has been compiled using the =JOIN formula in Google Docs on a column of school codes
schoolIDs =['5237521','5244439','5237629','5237823','5234026']
#go through the schoolIDs list above, and for each ID...
for item in schoolIDs:
    #show it in the console
    print item
    #create a URL called 'next_link' which adds that ID to the end of the base_url variable
    next_link = base_url+item+'.html'
    #pass that new concatenated URL to a function, 'scrape_page', which is scripted above
    print next_link
scrape_page(next_link)
