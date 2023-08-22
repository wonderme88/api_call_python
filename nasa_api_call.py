import requests

def get_sample_data():
    url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"  # API endpoint
    response = requests.get(url)

    print(response)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    sample_data = get_sample_data()

    if sample_data:
        print("Nasa Data:")
        print("Date:", sample_data["date"])
        print("Copyright:", sample_data["copyright"])
        print("Title:", sample_data["title"])
        print("Image Url:", sample_data["url"])
