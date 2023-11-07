import requests

url = 'http://127.0.0.1:5000/compare_images'

data = {
    'image_1': 'path_to_image_1',
    'image_2': 'path_to_image_2'
}

response = requests.post(url, json=data)
result = response.json()['result']
print(result)  # This will print the result (True or False)
