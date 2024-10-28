import requests
import os
import shutil


def download_picture(folder, filename, link):
    file_path = os.path.join(folder, filename)
    response_link = requests.get(link)
    with open(file_path, "wb") as file:
        file.write(response_link.content)


def main():
    url = "https://random.dog/woof.json"
    folder = "dogs"

    if not os.path.isdir(folder):
        os.mkdir(folder)
        for num in range(1, 51):
            params = {"filter": "mp4,webm"}
            response = requests.get(url, params=params)
            json = response.json()
            picture_link = json["url"]
            link, picture_extension = os.path.splitext(picture_link)
            filename = f"dog_{num}{picture_extension}"
            download_picture(folder, filename, link)
    else:
        shutil.rmtree(folder)


if __name__ == "__main__":
    main()
