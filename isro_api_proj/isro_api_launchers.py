import requests
import constants.api_end_points
import constants.constants_strings
import logging
import constants.http_std_codes

# Configure the logging settings
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


# Configure the logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='app.log',  # Specify the filename
    filemode='w'  # 'w' mode overwrites the file, 'a' mode appends
)

def get_launchers_names():
    url =  constants.api_end_points.Isro_baseUrl + constants.api_end_points.Launchers 
    logging.info(f"The url is {url}")
    response = requests.get(url)

    if response.status_code == constants.http_std_codes.HTTP_SUCCESS:
        response_json = response.json()
        list_size = len(response_json[constants.constants_strings.LAUNCHERS])
        logging.info(f"The list_size is {list_size}")
        logging.info(f"Data from response is {response_json[constants.constants_strings.LAUNCHERS][0][constants.constants_strings.ID]}")
        launchers_id_list = []
        launchers_country_list = []
        for x in range(0, list_size):
            launchers_id_list.append(response_json[constants.constants_strings.LAUNCHERS][x][constants.constants_strings.ID])
        return launchers_id_list
    else:  
        logging.info(f"Failed to fetch data. Status code: {response.status_code}")
        return []

def generate_html_file(launchers_names, html_file_name):
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Launchers Names</title>
    </head>
    <body>
        <h1>Launchers Names</h1>
        <ul>
            {} 
        </ul>
    </body>
    </html>
    """
    list_items = "\n".join([f"<li>{name} </li>" for name in launchers_names])
    list_items2 = "\n".join([f"<li>{name} </li>" for name in ])
    logging.info(list_items)
    with open(html_file_name, "w") as html_file:
        html_content = html_template.format(list_items)
        html_file.write(html_content)
        print(f"HTML file '{html_file_name}' created with ids.")

if __name__ == "__main__":
    launchers_ids = get_launchers_names()
    html_file_name = "launchers_names.html"

    generate_html_file(launchers_ids, html_file_name)
