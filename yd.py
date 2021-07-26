import requests
from pprint import pprint
import os

token = " "


class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.token = token


    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self):
        url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        headers = self.get_headers()
        name = os.path.basename(self.file_path)
        params = {"path": name, "overwrite": True}
        res = requests.get(url=url, params=params, headers=headers)
        pprint(res.json())
        href = res.json()['href']
        responce = requests.put(url=href, data=open(self.file_path, 'rb'))
        responce.raise_for_status()
        if responce.status_code == 201:
            return print("Успешно")


if __name__ == '__main__':
    uploader = YaUploader('D:/test.txt')
    result = uploader.upload()
