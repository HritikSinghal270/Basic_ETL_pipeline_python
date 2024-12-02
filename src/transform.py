import pandas as pd
import logging

def clean_data(raw_data):
    """
    Transform the raw JSON data into a clean DataFrame.
    """
    try:
        df = pd.DataFrame.from_dict(raw_data, orient="index")
        df = df.reset_index().rename(columns={
            "index": "date",
            "1. open": "open",
            "2. high": "high",
            "3. low": "low",
            "4. close": "close",
            "5. volume": "volume"
        })
        df["date"] = pd.to_datetime(df["date"])
        df[["open", "high", "low", "close", "volume"]] = df[["open", "high", "low", "close", "volume"]].astype(float)
        return df
    except Exception as e:
        logging.error(f"Error during data transformation: {e}")
        raise
