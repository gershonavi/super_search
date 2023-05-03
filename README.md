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

\`\`\`
pip install super_search
\`\`\`

## Usage

Here's a quick example of how to use SuperSearch:

\`\`\`python
from super_search import SuperSearch

api_key = "your_openai_api_key"
query = "What is the capital of France?"

sup = SuperSearch(api_key)
final_answer, messages = sup.get_answer(query, max_iterations=10, debug=True)

print(f"Final Answer: {final_answer}")
\`\`\`

For more information and advanced usage, please refer to the [documentation](https://github.com/gershonavi/your-package/wiki).

## License

SuperSearch is released under the [MIT License](https://opensource.org/licenses/MIT).


## Contributing

We welcome contributions to SuperSearch! If you're interested in contributing, feel free to submit a pull request or open an issue.
