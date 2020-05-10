from google_images_search import GoogleImagesSearch
from configparser import ConfigParser
import os

# download_images expects a query string that is passed to google's image search API.
# 1,000 JPG images are downloaded into subdirectories for each query string.
def download_images(query, gis, base_download_dir):
    # Google specific search parameters
    search_params = {
        'q': query,
        'num': 1000,
        'safe': 'high',
        'fileType': 'jpg',
        'imgType': 'photo'
    }

    try:
        gis.search(search_params=search_params, path_to_dir=base_download_dir + str(query))
    except:
        print("Cannot download images from query: " + str(query))

# main function
def main():

    parser = ConfigParser()
    parser.read(os.path.join(os.path.dirname(__file__), '../../../config', 'image.cfg'))
    search_strings = parser.get('image_download_config', 'search_strings')
    base_download_dir = parser.get('image_download_config', 'base_download_dir')
    google_api_key = parser.get('image_download_config', 'google_api_key')
    google_project_cx = parser.get('image_download_config', 'google_project_cx')

    # Specify Google API keys for google image search
    gis = GoogleImagesSearch(google_api_key, google_project_cx)

    for query in search_strings:
        download_images(query,gis,base_download_dir)

if __name__ == "__main__":
    main()