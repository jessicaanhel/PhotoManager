import requests
import json

json_holder_with_photos = 'https://jsonplaceholder.typicode.com/photos'


def getImportedPhotosApi(url: str):
    if not type(url) is str:
        raise TypeError("Only string is allowed")
    response = requests.get(url)
    return response.text


converted_api_response_to_json = json.loads(
    getImportedPhotosApi(json_holder_with_photos))

fixtures = []
for photo_dictionary in converted_api_response_to_json:
    initialed_django_serialization_format = {"model": "viewer.photo",
                                             "pk": photo_dictionary["id"],
                                             "fields": photo_dictionary}
    fixtures.append(initialed_django_serialization_format)

json_object = json.dumps(fixtures, indent=4)

f = open("fixtures.json", "w")
f.write(json_object)
f.close()
