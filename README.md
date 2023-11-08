# News Article Scraping and Text Classification

This repository contains a Python script for scraping news articles from The New York Times and performing text classification using a Random Forest classifier. The code is divided into two parts: Code 1 for scraping articles and Code 2 for text classification.

## Prerequisites

Before running the code, ensure you have the following prerequisites installed:

- Python 3.x
- Required Python packages (you can install them using `pip`):
  - requests
  - BeautifulSoup4
  - scikit-learn

## Instructions

1. Clone this repository to your local machine using the following command:

git clone https://github.com/your-username/your-repo-name.git

3. **Code 1: Scraping NYT Articles**

- Open the `code1_scrape_nyt.py` file in a text editor.
- If you'd like to scrape articles from a different website, replace the `url` variable with the URL of that website.
- Run the script to scrape articles and save them to a CSV file using the following command:

  ```
  python code1_scrape_nyt.py
  ```

- The scraped articles will be saved to a file named `nyt_articles.csv`.

4. **Code 2: Text Classification with Random Forest**

- Open the `code2_text_classification.py` file in a text editor.
- Replace the `texts` and `labels` variables with your own text data and labels.
- Run the script to perform text classification using the following command:

  ```
  python code2_text_classification.py
  ```

- The script will load the data, perform text classification using a Random Forest classifier, and display the accuracy, classification report, and confusion matrix.

Please customize the data in Code 2 to match your specific text classification task.


## Acknowledgments

- Thanks to [The New York Times](https://www.nytimes.com/) for providing news articles for scraping.

Feel free to modify the code and instructions as needed for your specific use case.
