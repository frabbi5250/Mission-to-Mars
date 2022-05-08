
    # Import Splinter and BeautifulSoup\n",
    from splinter import Browser\n",
    from bs4 import BeautifulSoup as soup\n",
    from webdriver_manager.chrome import ChromeDriverManager"
  
   def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}\n",
    browser = Browser('chrome', **executable_path, headless=False)

   #Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)
    
    #Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)"
 
    # Use the base URL to create an absolute URL\n",
     img_url = f'https://spaceimages-mars.com/{img_url_rel}
     img_url
  
    import pandas as pd
    df = pd.read_html('https://galaxyfacts-mars.com')
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
  
    # Import Splinter, BeautifulSoup, and Pandas
    from splinter import Browser
    from bs4 import BeautifulSoup as soup
    import pandas as pd
    from webdriver_manager.chrome import ChromeDriverManager

    # Set the executable path and initialize Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
 
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com/
    browser.visit(url)
    
    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)
    
    # Use the parent element to find the first a tag and save it as `news_title`
    news_title = slide_elem.find('div', class_='content_title').get_text()
    news_title
   
    # Use the parent element to find the paragraph text\n",
    news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    news_p
  
    ### JPL Space Images Featured Image"
   
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)
   
  
    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')
    img_soup
   
    # find the relative image url
    img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    img_url_rel
  
    # Use the base url to create an absolute url\n",
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    img_url
 
    # Use `pd.read_html` to pull the data from the Mars-Earth Comparison section
    df = pd.read_html('https://galaxyfacts-mars.com')
    df.head()

    # Create a DataFrame\n",
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
    # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles"
   
    ### Hemispheres
   
    # 1. Use browser to visit the URL
    url = 'https://marshemispheres.com/
    browser.visit(url)"
  
    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []
    
    # 3. Write code to retrieve the image urls and titles for each hemisphere.\n",
    links = browser.find_by_css('a.product-item img')
    # Next, loop through those links, click the link, find the sample anchor, return the href\n",
    for i in range(len(links)):
        hemisphere = {}
    
    # find the elements on each loop 
     browser.find_by_css('a.product-item img')[i].click()
    #  find the Sample image anchor tag and extract the href
    sample_elem = browser.links.find_by_text('Sample').first
    hemisphere['img_url'] = sample_elem['href']

    #  Hemisphere title
    hemisphere['title'] = browser.find_by_css('h2.title').text
    
    # Append hemisphere object to list
    hemisphere_image_urls.append(hemisphere)
    #navigate backwards
    browser.back()
   
