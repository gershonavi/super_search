from setuptools import setup, find_packages

setup(
    name="super_search_gpt",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "googlesearch-python",
        "beautifulsoup4",
        "openai",
        "pandas",
        "requests-html",
        "requests",
    ],
    author="Avi Gershon",
    author_email="gershonavi@gmail.com",
    description="SuperSearch is a powerful Python package for advanced search and data extraction. It leverages the GPT-4 AI model, Google search, and web scraping to efficiently obtain information on various topics. Ideal for developers needing quick, accurate responses to complex queries and data extraction, analysis, and summarization from multiple web sources. Easy to integrate, SuperSearch enhances functionality and user experience, saving time on manual research and enabling smarter, more effective solutions.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gershonavi/super_search",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)