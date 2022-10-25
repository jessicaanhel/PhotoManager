import requests

json_holder_with_photos = 'https://jsonplaceholder.typicode.com/photos'


def getImportedPhotosApi(url: str):
    if not type(url) is str:
        raise TypeError("Only string is allowed")
    response = requests.get(url)
    f = open("fixture.json", "w")
    f.write(response.text)
    f.close()


getImportedPhotosApi(json_holder_with_photos)
