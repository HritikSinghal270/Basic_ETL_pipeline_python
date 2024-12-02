This project demonstrates a simple ETL (Extract, Transform, Load) pipeline built using Python. 
The pipeline fetches data from an external API (Alpha Vantage), processes the raw data to clean and transform it into a usable format, 
and stores the processed data into a PostgreSQL database.

Features
Extract: Retrieves stock market data from the Alpha Vantage API.
Transform: Cleans and processes the raw data to ensure consistency and usability.
Load: Inserts the transformed data into a PostgreSQL database for further analysis.

Prerequisites
Python 3.8+
PostgreSQL
API key from Alpha Vantage

How to Use
Clone the repository.
Set up the .env file with your API key and database credentials.

Run the pipeline using:
python src/main.py
