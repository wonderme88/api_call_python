import requests
import logging
import constants.api_end_points
import constants.http_std_codes
import constants.constants_strings

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='cust_api.log',  # Specify the filename
    filemode='w'  # 'w' mode overwrites the file, 'a' mode appends
)

def get_customer_names():
    url= constants.api_end_points.Isro_baseUrl+constants.api_end_points.Customer_Satellites
    logging.info(f"The url is {url}")
    response = requests.get(url)

    if response.status_code == constants.http_std_codes.HTTP_SUCCESS:
        response_json = response.json()
        list_size = len(response_json[constants.constants_strings.CUSTOMER_SATELLITES])
        logging.info(f"The list_size is {list_size}")
        logging.info(f"Data from response is {response_json[constants.constants_strings.CUSTOMER_SATELLITES][0][constants.constants_strings.ID]}")
        customer_list = []
        launch_date_list = []
        cust_id_name_list=[]
        for x in range(0, list_size):
            customer_list.append((response_json[constants.constants_strings.CUSTOMER_SATELLITES][x][constants.constants_strings.ID])+ ("  ")+ (response_json[constants.constants_strings.CUSTOMER_SATELLITES][x][constants.constants_strings.COUNTRY])+ " "+(response_json[constants.constants_strings.CUSTOMER_SATELLITES][x][constants.constants_strings.LAUNCH_DATE]))
            # launch_date_list.append(response_json[constants.constants_strings.CUSTOMER_SATELLITES][x][constants.constants_strings.LAUNCH_DATE])
            print(customer_list)
        return customer_list
    else:  
        logging.info(f"Failed to fetch data. Status code: {response.status_code}")
        return []

def generate_html_file(customer_names, html_file_name):
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
   
    list_items = "\n".join([f"<li>{name}</li>" for name in customer_names])
    logging.info(list_items)
    with open(html_file_name, "w") as html_file:
        html_content = html_template.format(list_items)
        html_file.write(html_content)
        print(f"HTML file '{html_file_name}' created with user names.")

if __name__ == "__main__":
    customer_names = get_customer_names()
    html_file_name = "customer_names.html"

    generate_html_file(customer_names, html_file_name)
    
