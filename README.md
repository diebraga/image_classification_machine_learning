# Is it a dog
FastApi api that predicts if it's rather a dog or not using fastAI image classification.
and a react frontend that consumes the endpoint.

## How to use

### Requirements

- Python3
- NodeJs
- Npm or Yarn

#### Backend

- Create a virtual enviroment running in yuor terminal: 

<code>python3 -m venv env</code>

- Actinvate your virtual enviroment running: 

On mac: <code>source env/bin/activate</code>

On windows: <code>.\env\Scripts\activate</code>

- Install dependecies: 

<code>pip install -r requirements.txt</code>

- Create image classification running in your terminal:

<code>python3 download_img.py</code>

It will create a folder classification with pictures of dogs and 
non dogs in your root.

- Train your model running in your terminal:

<code>python3 train.py</code>

It will create a file called dog_or_park.pkl in your root.

- Run your server:

<code>uvicorn app:app --reload</code>

Your server will be running at http://127.0.0.1:8000


#### Frontend

- In you terminal:

Open another terminal and go to the frontend folder

<code>cd frontend</code>

- Install dependencies:

<code>npm install</code>

or

<code>yarn</code>

Your frontend will be running at http://127.0.0.1:5173

![ezgif com-video-to-gif](https://user-images.githubusercontent.com/52054459/221587640-71d1a669-7c86-44f9-95c4-1924f61c87cc.gif)

![ezgif com-video-to-gif (1)](https://user-images.githubusercontent.com/52054459/221587528-382d140e-bd8e-43fb-8d36-76e4109a1515.gif)
