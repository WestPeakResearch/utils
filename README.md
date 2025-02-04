# WestPeak Research Assocaition Utilities

### Alumni LinkedIn Scraper

To scrape for alumni placements, enter list of required alumni in `input.csv`. Here is an example below:

```csv
name,linkedin
John Doe,https://www.linkedin.com/in/jdoe/
Karen Doe,https://www.linkedin.com/in/kdoe/
```

Obtain an API key from RapidAPI for the follwing API: https://rapidapi.com/iscraper/api/linkedin-profiles-and-company-data.
Then, run `python alumni.py <your_api_key_here>`. The scraped user data will be saved in `output.csv`. Note that if there
 are many entries in the input (100+), the free API limit may be reached; you may have to switch to the paid API plan.

### Donut Dates Pairings

Put all names into `names.csv`, run the `donutdates.py` script, and you will get the pairings. Note that the algorithm will 
fail if there are odd number of names.

### Strikes Visualizations Generator

Put analysts separated by role into `roster.json`, including number of strikes as the value. Run `strikes.py` to generate a 
chart that displays the strike counts.