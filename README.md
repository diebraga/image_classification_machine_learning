# Is it a cat or a dog

FastApi api that predicts if it's a cat or a dog using fastAI image classification.

![demo1](https://user-images.githubusercontent.com/52054459/224771687-2ed97135-8669-4775-a81b-e1097fd26500.gif)

- Deployed site: <a href="https://leafy-elf-2f1dcb.netlify.app">CLICK HERE</a> as 
  I'm using a free tie to deploy this site you may ecounter limitations or the app
  could not be working follow the instructions bellow to run locally.

### Requirements

- Python3

#### Backend

- Create a virtual enviroment running in yuor terminal:

<code>python3 -m venv env</code>

- Actinvate your virtual enviroment running:

On mac: <code>source env/bin/activate</code>

On windows: <code>.\env\Scripts\activate</code>

- Install dependecies:

<code>pip install -r requirements.txt</code>

- Create image classification running in your terminal:

<code>python3 download.py</code>

It will create a folder classification with pictures of dogs and cats in your root.
attention: `You should verify if each folder contains really cats and dogs also this pretrained model tends to be biased toward cats consired add more dogs data`

- Train your model running in your terminal:

<code>python3 train.py</code>

It will create a file called dog_or_park.pkl in your root.

- Run your server:

<code>uvicorn app:app --reload</code>

Your server will be running at http://127.0.0.1:8000

#### Frontend

- Link to frontend repo: <a href="https://github.com/diebraga/is_dog_machine_learning_frontend">CLICK HERE</a>


