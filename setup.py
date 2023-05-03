from setuptools import setup, find_packages

setup(
    name="super_search",
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
    description="SuperSearch is a powerful and versatile Python package designed to facilitate advanced search and data extraction capabilities. By leveraging the GPT-4 AI model and integrating with Google search and web scraping techniques, SuperSearch offers an efficient and convenient way to obtain information on various topics. It is particularly useful for developers who require swift and accurate responses to complex queries, as well as for those who need to extract, analyze, and summarize data from multiple web sources. The package is easy to use and can be seamlessly integrated into a wide range of applications to enhance their functionality and user experience. With SuperSearch, you can quickly find the answers you need, save time on manual research, and focus on building smarter and more effective solutions.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your-package",
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