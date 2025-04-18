import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_youtube_trending(url="https://www.youtube.com/feed/trending"):
    headers = {
        "User-Agent": "Mozilla/5.0",
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # NOTE: Real scraping of video metadata requires Selenium or YouTube API.
    titles = [tag.text.strip() for tag in soup.select("a#video-title")]
    
    df = pd.DataFrame({"title": titles})
    df.to_csv("data/raw_data/trending_videos.csv", index=False)
    return df

if __name__ == "__main__":
    fetch_youtube_trending()
