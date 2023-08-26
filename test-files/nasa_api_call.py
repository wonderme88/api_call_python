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
    
def save_image_from_url(url,file_name):
    response = requests.get(url)

    if response.status_code == 200:
        with open(file_name, "wb") as file:
            file.write(response.content)
        print(f"Image saved as {file_name}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")



if __name__ == "__main__":
    sample_data = get_sample_data()

    if sample_data:
        print("Nasa Data:")
        print("Date:", sample_data["date"])
        print("Copyright:", sample_data["copyright"])
        print("Title:", sample_data["title"])
        print("Image Url:", sample_data["url"])
        image_url =   sample_data["url"] # Replace with the image URL
        image_file_name = "downloaded_image.jpg"    # Choose a filename for the downloaded image

    save_image_from_url(image_url, image_file_name)


    
