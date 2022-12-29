import requests

url = 'https://api.artic.edu/api/v1/artworks/129884'
# url = 'https://api.artic.edu/api/v1/artworks/27992?fields=id,title,image_id'

response = requests.get(url)

response.status_code
data = response.json()



image_url= data['config']['iiif_url']+'/' + data['data']['image_id'] + '/full/843,/0/default.jpg'

response = requests.get(image_url)

response.status_code

with open('image.jpg', 'wb') as f:
    f.write(response.content)

from IPython.display import Image
Image(filename='image.jpg')