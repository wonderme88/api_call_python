import requests

def get_sample_data():
    url = "https://jsonplaceholder.typicode.com/posts/100"  # API endpoint
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
        print("Sample Data:")
        #print("Title:", sample_data["title"])
        #print("Body:", sample_data["body"])
        print("Id:", sample_data["id"])
