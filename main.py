import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_link(self, disk_file_path: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        url_to_load = data.get('href')
        return url_to_load
    def upload(self, disk_file_path, filename):
        url_to_load = self._get_link(disk_file_path=disk_file_path)
        response = requests.put(url_to_load, data=open(filename, 'rb'))
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    path_to_file = 'netology/1.txt'
    token = ''
    uploader = YaUploader(token=token)
    uploader.upload(path_to_file, 'test.txt')