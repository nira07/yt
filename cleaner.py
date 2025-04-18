import pandas as pd

def clean_data(file_path="data/raw_data/trending_videos.csv"):
    df = pd.read_csv(file_path)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df["title"] = df["title"].str.strip()
    return df

if __name__ == "__main__":
    df = clean_data()
    print(df.head())
