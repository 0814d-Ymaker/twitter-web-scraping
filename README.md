# Twitter/X Web Scraping Project

This repository contains my implementation of a Twitter/X web scraping task based on the open-source `twitter_download` project.

Original project: https://github.com/caolvchong-top/twitter_download

The project was used as a practical exercise in undergraduate research. The main task was to collect 10,000 tweets containing the word `Trump` within a specified search period and to validate the final dataset.

## Project Result

The search period was configured as:

`since:2026-09-10 until:2026-10-01`

The final dataset is stored in:

`Trump_10000_tweets.csv`

Final validation results:

1. Total tweets: 10,000
2. Unique Tweet URLs: 10,000
3. Tweets with `Trump` in Tweet Content: 10,000
4. Tweets outside the configured date range: 0

Although the search range was configured from September 10 to September 30, 2026, the collected results were concentrated on September 30 because of the large number of available search results.

## Main Modifications

Several changes were made to the original project during the task.

### 1. Transaction ID Generation

The original transaction ID generation process did not work correctly with the current Twitter/X webpage response.

`transaction_generate.py` was modified to create an authenticated `requests.Session()`, add the required headers and Cookie, and use this session when retrieving the X webpage required for transaction ID generation.

### 2. HTTP 429 Handling

During large-scale scraping, Twitter/X returned HTTP 429 after the request limit was reached.

The request logic in `tag_down.py` was modified to check the HTTP status code before JSON parsing. When HTTP 429 is returned, the current scraping round stops normally instead of attempting to parse the response as JSON.

### 3. Cursor-Based Resumable Scraping

Since approximately 1,000 tweets could normally be collected before the request limit was reached, cursor persistence was added to support scraping across multiple runs.

The latest cursor is saved locally during execution and can be loaded when the program is started again. This allows scraping to continue from the previous search position instead of restarting from the beginning.

### 4. Data Merging and Validation

`merge_csv.py` was added for final data processing.

It performs the following operations:

1. Reads the collected CSV data.
2. Keeps only records whose Tweet Content contains `Trump`.
3. Removes duplicate tweets based on Tweet URL.
4. Generates the final dataset containing exactly 10,000 valid records.

## Main Files

`main.py`  
Original entry point for the basic downloading functionality.

`tag_down.py`  
Keyword-based tweet scraping, including HTTP 429 handling and cursor-based continuation.

`transaction_generate.py`  
Transaction ID generation with authenticated session handling.

`merge_csv.py`  
Final keyword filtering, Tweet URL deduplication, and dataset generation.

`Trump_10000_tweets.csv`  
Final validated dataset containing 10,000 tweets.

`settings.json`  
Configuration file for local execution.

`requirements.txt`  
Python dependency information.

## Configuration

Twitter/X authentication information is required for local execution.

Authentication credentials are intentionally not included in this repository. Users must provide their own valid Cookie information locally before running the scraper.

Do not upload personal authentication credentials to a public repository.

## Dependencies

The project uses Python and the dependencies listed in `requirements.txt`.

The main listed dependencies are:

`httpx==0.28.1`

`XClientTransaction==1.0.3`

## Notes

Twitter/X may apply request rate limits during scraping. This project does not attempt to bypass these limits. When HTTP 429 is returned, the current scraping round is stopped and scraping can be resumed later using the saved cursor.

The project is intended for programming learning and academic research. Users should comply with applicable laws, platform rules, and relevant data and copyright requirements.

## Acknowledgement

This project is based on the open-source `twitter_download` repository created by its original author:

https://github.com/caolvchong-top/twitter_download

The original project and its license are retained in this repository. The modifications described above were made as part of this web scraping exercise.


