import requests


def spacecraft_ids ():
    url="https://isro.vercel.app/api/launchers"
    response = requests.get(url)
    
    if response.status_code==200:
        response_json = response.json()
        # print(response_json)
        list_size= len(response_json['launchers'])
        print(list_size)
        

    else:
        print(f"failed to fetch data, status code: {response.status_code}")
        return []
    





spacecraft_ids()