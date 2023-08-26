import requests
import constants.api_end_points
import logging

# Configure the logging settings
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Configure the logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',  # Specify the filename
    filemode='w'  # 'w' mode overwrites the file, 'a' mode appends
)

def get_spacecft_names():
    url =  constants.api_end_points.Isro_baseUrl + constants.api_end_points.Spacecrafts  #"https://isro.vercel.app/api/spacecrafts" #"https://isro.vercel.app/api/launchers"
    logging.info(f"The url is {url}")
    response = requests.get(url)

    if response.status_code == 200:
        response_json = response.json()
        #print(f"response json: {response_json}")
        #return [user["name"] for user in users]
        #print(response_json)
        # #print(response_json['spacecrafts'])
        # print(response_json['spacecrafts'][0]['name'])
        # print(response_json['spacecrafts'][1]['name'])
        list_size = len(response_json['spacecrafts'])
        spacecft_ids_list = []
        spacecft_names_list = []
        for x in range(0, list_size):
            spacecft_ids_list.append(response_json['spacecrafts'][x]['id'])
            spacecft_names_list.append(response_json['spacecrafts'][x]['name'])
        return spacecft_names_list
    else:  
        logging.info(f"Failed to fetch data. Status code: {response.status_code}")
        return []

def generate_html_file(spacecft_names, html_file_name):
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Spacecraft Names</title>
    </head>
    <body>
        <h1>Spacecraft Names</h1>
        <ul>
            {} 
        </ul>
    </body>
    </html>
    """
    #print(spacecft_names)
    list_items = "\n".join([f"<li>{name}</li>" for name in spacecft_names])
    logging.info(list_items)
    with open(html_file_name, "w") as html_file:
        html_content = html_template.format(list_items)
        html_file.write(html_content)
        print(f"HTML file '{html_file_name}' created with user names.")

if __name__ == "__main__":
    spacecft_names = get_spacecft_names()
    html_file_name = "spacecft_names.html"

    generate_html_file(spacecft_names, html_file_name)
