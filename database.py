import sqlite3
import pandas as pd

def store_to_db(df, db_name="data/youtube.db"):
    conn = sqlite3.connect(db_name)
    df.to_sql("trending", conn, if_exists="replace", index=False)
    conn.close()

if __name__ == "__main__":
    df = pd.read_csv("data/raw_data/trending_videos.csv")
    store_to_db(df)
