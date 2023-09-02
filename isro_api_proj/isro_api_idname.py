import requests


def get_spacecraft_id ():
    url="https://isro.vercel.app/api/launchers"
    response = requests.get(url)
    
    if response.status_code==200:
        response_json = response.json()
        # print(response_json)
        list_size= len(response_json['launchers'])
        print(list_size)
        spacecraft_id_list =[]
        # spacecraft_name_list=[]
        for i in range (0,list_size):
             spacecraft_id_list.append(response_json['launchers'][i]['id'])
        return spacecraft_id_list

    else:
        print(f"failed to fetch data, status code: {response.status_code}")
        return []
    
get_spacecraft_id()




