import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(file_path="data/raw_data/trending_videos.csv"):
    df = pd.read_csv(file_path)
    df["title_length"] = df["title"].apply(len)
    plt.hist(df["title_length"], bins=20, edgecolor='black')
    plt.title("Distribution of Video Title Lengths")
    plt.xlabel("Title Length")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_data()
