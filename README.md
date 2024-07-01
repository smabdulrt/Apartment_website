
# Apartments Scraper

This project scrapes rental information from apartments.com for listings in Los Angeles, CA. It extracts various details like the property name, address, rental price, and more, and saves them to a CSV file.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Setup

### Prerequisites

- Python 3.7+
- Google Chrome browser

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/apartments-scraper.git
    cd apartments-scraper
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your ZenRows API key:

    Replace the placeholder `""` with your actual ZenRows API key in the script.

## Usage

1. Place the `apartments.csv` file containing the input URLs in the project directory. The CSV should have a header row with at least one column named `link`.

2. Run the script:

    ```bash
    python scrape_apartments.py
    ```

3. The scraped data will be appended to `data_1.csv`.

## Project Structure

```
apartments-scraper/
├── README.md
├── requirements.txt
├── apartments.csv
└── scrape_apartments.py
```

- `README.md`: This file.
- `requirements.txt`: Lists the dependencies required for the project.
- `apartments.csv`: Input file containing URLs to scrape.
- `scrape_apartments.py`: Main script to perform the web scraping.

## Dependencies

- `undetected-chromedriver`: For using Chrome in headless mode with undetected scraping.
- `requests`: For making HTTP requests.
- `scrapy`: For extracting data from the web pages.
- `webdriver_manager`: To manage ChromeDriver.
- `zenrows`: API client for ZenRows.

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This `README.md` file provides an overview of the project, setup instructions, usage, dependencies, and contribution guidelines. Adjust the instructions according to your project's specific details and structure.
