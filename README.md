# SuperSearch

SuperSearch is a powerful and versatile Python package designed to facilitate advanced search and data extraction capabilities. By leveraging the GPT-4 AI model and integrating with Google search and web scraping techniques, SuperSearch offers an efficient and convenient way to obtain information on various topics.


## Features

- Query GPT-4 AI model for intelligent and relevant answers
- Google search integration for real-time information retrieval
- Web scraping capabilities for data extraction and analysis
- Summarization of lengthy content
- JSON-based communication for easy integration with other applications
- Easy-to-use interface for quick and accurate responses to complex queries

## Installation

To install SuperSearch, simply run:

```
pip install super_search_gpt
```
## Example Usage 1

Here's a quick example of how to use SuperSearch:

```
from super_search import SuperSearch
api_key = "your_openai_api_key"
query = "What is the capital of France?"
sup = SuperSearch(api_key)
final_answer, messages = sup.get_answer(query, max_iterations=10, debug=True)
print(f"Final Answer: {final_answer}")
```

For more information and advanced usage, please refer to the [documentation](https://github.com/gershonavi/your-package/wiki).

# Example Usage 2
```
query =''' what is the news summary in california '''
sup = SuperSearch(gpt_api_key=api_key1,google_search_key=google_search_key1,cse_id=cse_id1,
                  max_iterations_per_answer=15, use_google_search_api=True,)

final_answer, messages = sup.get_answer(query, debug=True)
print(f"Final Answer: {final_answer}")
```

```
Raw answer: {"Answer": "None", "Google": "news summary in california", "Scrap": "None", "Location": 0}
Answer: {'Answer': None, 'Google': 'news summary in california', 'Scrap': None, 'Location': 0}
[{"url": "https://www.latimes.com/", "title": "Los Angeles Times: News from California, the nation and world", "description": "The L.A. Times is a leading source of breaking news, entertainment, sports, politics, and more for Southern California and the world."}, {"url": "https://www.energy.ca.gov/news/2021-03/california-releases-report-charting........
.
.
.
{'role': 'user', 'content': '{"q": " what is the news summary in california ", "Google_Reply": "None", "Scrap_Reply": "None", "Location_Reply": 0, "Error": ""}'}
Final Answer: Here are some news summaries from California sources:
1. Los Angeles Times: Provides breaking news, entertainment, sports, politics, and more for Southern California and the world (https://www.latimes.com/).
2. California Releases Report Charting Path to 100 Percent Clean Electricity: An initial analysis called for in Senate Bill 100 regarding clean energy (https://www.energy.ca.gov/news/2021-03/california-releases-report-charting-path-100-percent-clean-electricity).
3. California News from US News Best States: Provides an interactive platform for ranking the 50 U.S. states, alongside news analysis and daily reporting (https://www.usnews.com/news/california).
4. CNN: Offers the latest news and breaking news for the U.S., world, weather, entertainment, politics, and health (https://www.cnn.com/).
5. Budget News from California Community Colleges Chancellor's Office: Shares summary information related to California Community College budgets (https://www.cccco.edu/About-Us/Chancellors-Office/Divisions/College-Finance-and-Facilities-Planning/Budget-News).
6. UC Davis News, Magazine, Experts and Media Resources: Features news, research, and COVID-19 resources (https://www.ucdavis.edu/news).
7. Tax News from FTB.ca.gov: Informs tax professionals, taxpayers, and business owners about state income tax laws (https://www.ftb.ca.gov/about-ftb/newsroom/tax-news/index.html).
8. California Governor Newsroom: Shares recent news about California's governor (https://www.gov.ca.gov/newsroom/).
9. California Consumer Privacy Laws – CCPA & CPRA: Offers analysis of California's consumer privacy laws (https://pro.bloomberglaw.com/brief/california-consumer-privacy-laws-ccpa-cpra/).


```



## License

SuperSearch is released under the [MIT License](https://opensource.org/licenses/MIT).


## Contributing

We welcome contributions to SuperSearch! If you're interested in contributing, feel free to submit a pull request or open an issue.
