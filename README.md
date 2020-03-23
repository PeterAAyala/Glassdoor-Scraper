## Disclaimer

This scraper is provided as a public service because Glassdoor does not offer an official API for reviews. Glassdoor Terms of use (available [here](https://www.glassdoor.com/about/terms.htm)) lists automated tools, including scraping, as against the terms of use. I cannot guarantee that your Glassdoor account will not be banned by using this. Lastly, I will remove this repository if I am contacted to do so by Glassdoor.

## Introduction 

This script will scape all employee reviews for a company on Glassdoor and output into a csv file. This was my first script built using Scrapy, so feel free to let me know about any potential improvements. 

## Installation and Usage 

1. Download or clone the repository with `git clone https://github.com/PeterAAyala/Glassdoor-Scraper.git`

2. Run `pip install scrapy` if you have do not have it installed.

3. Open `mainScaper.py`, which is found in `Glassdoor-Scraper/GlassdoorScraper/spiders/`. Here you will see `start_urls` on line 9, which defines the first page of the company you are intested in. Right now it is set to Google. Search the company you are interested in and replace this with the link you're interested in.

4. Open `settings.py`, and you will see `DEPTH_LIMIT = 2` on line 17. This defines how many pages you want to scrape before exiting. You should comment this line out to gather all the reviews for a company, but I suggest keeping it in and completeing step 5 to make sure the script works properly before . 

5. Run the script and define your desired csv file name by doing 

   ```
   cd Glassdoor-Scraper
   scrapy crawl mainScraper -o "yourFileName.csv"
   ```

   ​