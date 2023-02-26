from duckduckgo_search import ddg_images
from fastcore.all import *
from fastai.vision.all import *
from fastdownload import download_url
import ssl
from time import sleep
import certifi
ssl._create_default_https_context = ssl._create_unverified_context
ssl_context = ssl.create_default_context(cafile=certifi.where())

def search_images(term, max_images=30):
    print(f"Searching for '{term}'")
    return L(ddg_images(term, max_results=max_images)).itemgot('image')

searches = 'dog','park'
path = Path('dog_or_park')

# DOWLOAD ONE BIRD PIC
# urls = search_images('dog photos', max_images=1)
# urls[0]

# dest = 'dog.jpg'
# download_url(urls[0], dest, show_progress=False)

# from fastai.vision.all import *
# im = Image.open(dest)
# im.to_thumb(256,256)

for o in searches:
    dest = (path/o)
    dest.mkdir(exist_ok=True, parents=True)
    download_images(dest, urls=search_images(f'{o} photo'))
    sleep(10)  # Pause between searches to avoid over-loading server
    download_images(dest, urls=search_images(f'{o} sunny photo'))
    sleep(10)
    download_images(dest, urls=search_images(f'{o} cloudy photo'))
    sleep(10)
    resize_images(path/o, max_size=400, dest=path/o)

failed = verify_images(get_image_files(path))
failed.map(Path.unlink)
len(failed)
