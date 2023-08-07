title = []
author = []
price = []
desc = []
num_pages = []
date_issue = []
publisher = []

for i in range(1,3):
    url="https://www.gramedia.com/categories/buku?page={}".format(i)
    driver.get(url)
    time.sleep(0.2)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for tag in soup.find_all( 'div',{"_ngcontent-web-gramedia-c26":"","class":"ng-star-inserted"} ):
        
        try:
            links.append("https://www.gramedia.com"+tag.find('a',{"_ngcontent-web-gramedia-c26":""})['href'])
        except:
            pass

    for link in links:
        driver.get(link)
        time.sleep(0.3)
        html_ind = driver.page_source
        soup_ind = BeautifulSoup(html_ind, "html.parser")

        try:
            title.append( soup_ind.find( 'div', {"class":"book-title"} ).get_text() )
        except:
            title.append("NaN")
        try:
            author.append( soup_ind.find('span',{"class":"title-author"}).get_text() )
        except:
            author.append("NaN")
        try:
            price.append( soup_ind.find('div',{'class':'price'}).find('p').get_text() )
        except:
            price.append("NaN")
        try:
            desc.append( soup_ind.find('div',{'class':'product-desc'}).get_text() )
        except:
            desc.append("NaN")
        try:
            num_pages.append( soup_ind.find('div',{'class':'detail-section'}).find_all('p')[0].get_text() )
        except:
            num_pages.append("NaN")
        try:
            date_issue.append( soup_ind.find('div',{'class':'detail-section'}).find_all('p')[2].get_text() )
        except:
            date_issue.append("NaN")
        try:
            publisher.append( soup_ind.find('div',{'class':'detail-section'}).find_all('p')[1].get_text() )
        except:
            publisher.append("NaN")

pages = pd.DataFrame()
pages['Title'] = title
pages['Author'] = author
pages['Price'] = price
pages['Desc'] = desc
pages['Num Pages'] = num_pages
pages['Date Issue'] = date_issue
pages['Publisher'] = publisher

pages
