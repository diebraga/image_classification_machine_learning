from duckduckgo_search import ddg_images
from fastcore.all import *
from fastai.vision.all import *
from fastdownload import download_url
import ssl
from time import sleep
import certifi

ssl._create_default_https_context = ssl._create_unverified_context
ssl_context = ssl.create_default_context(cafile=certifi.where())

def search_images(term, max_images=80):
    print(f"Searching for '{term}'")
    return L(ddg_images(term, max_results=max_images)).itemgot('image')

searches = ['dog', 'cat', 'other']
path = Path('classification')

for o in searches:
    dest = (path/o)
    dest.mkdir(exist_ok=True, parents=True)
    if o == 'other':
        download_images(dest, urls=search_images(f'{o} photos'))
    else:
        download_images(dest, urls=search_images(f'{o} photos'))
        sleep(10)  # Pause between searches to avoid over-loading server
        download_images(dest, urls=search_images(f'{o} park photos'))
        sleep(10)
        download_images(dest, urls=search_images(f'{o} walk photos'))
        sleep(10)
    resize_images(path/o, max_size=400, dest=path/o)

failed = verify_images(get_image_files(path))
failed.map(Path.unlink)
len(failed)
