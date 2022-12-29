# API Deployment with FastAPI

**Introduction**

In this lesson, we will give an overview of Python-type hints. With these in hand, we will delve into FastAPI which leverages type hints to build a robust and self-documenting REST API. We will first build out our API locally, test it, and then deploy it to Heroku and again test it once live.

- Review of Python Type Hints
- Fundamentals of FastAPI
- Local API Testing
- Heroku Revisited
- Live API Testing

## Python Type Hints Overview

Python is a dynamically typed language, which means the variable's type is checked at run-time as opposed to statically typed where the variable type is declared in the code, e.g. `int a`.

Python's type hinting system nudges Python towards static typing, but as the name states, these are merely type **hints** and not type **declarations**. This means that Python itself does not enforce type checking. Instead, the type hints enable additional functionality in the Python ecosystem such as static type checking in an IDE or modules that depend on type hints.

An example of a Python type hint:
```
from typing import Union

def foo(a: Union[list,str], b: int = 5) -> str:
    pass
```
This declares a function that takes in two arguments: one that is required and one that is optional. The first one expects either a list or a string, the second expects an int. Finally, the function is expected to return a string. As shown, you can import various types of primitives from the typing module.

**Further Reading**

[PEP 483](https://www.python.org/dev/peps/pep-0483/) on The Theory of Type Hints

The [docs](https://docs.python.org/3/library/typing.html) for the Python `typing` module.

## Introduction to FastAPI


**FastAPI** is a modern API framework that relies heavily on type hints for its capabilities.

As the name suggests, FastAPI is designed to be fast in execution and also in development. It is built for maximum flexibility in that it is solely an API. You are not tied into particular backends, frontends, etc. thus enabling composability with your favorite packages and/or existing infrastructure.

Getting started is as simple as writing a main.py containing:
```
from fastapi import FastAPI

# Instantiate the app.
app = FastAPI()

# Define a GET on the specified endpoint.
@app.get("/")
async def say_hello():
    return {"greeting": "Hello World!"}
```

To run our app, we will use uvicorn in our shell: `uvicorn main:app --reload`.

- The `--reload` allows you to make changes to your code and have them instantly deployed without restarting uvicorn.

By default, our app will be available locally at http://127.0.0.1:8000. The output of the above snippet will return a JSON response as `{"greeting": "Hello World!"}` on the browser (URL `http://127.0.0.1:8000`).
Further Reading

The FastAPI [docs](https://fastapi.tiangolo.com/) are excellently written, check them out!

## Core Features of FastAPI

FastAPI's type checking uses a mix of standard Python type hints in function definitions as well as the package Pydantic to define data models which define the types that are expected in a request body, like the following example:

```
# Import Union since our Item object will have tags that can be strings or a list.
from typing import Union 

from fastapi import FastAPI
# BaseModel from Pydantic is used to define data objects.
from pydantic import BaseModel

# Declare the data object with its components and their type.
class TaggedItem(BaseModel):
    name: str
    tags: Union[str, list] 
    item_id: int

app = FastAPI()

# This allows sending of data (our TaggedItem) via POST to the API.
@app.post("/items/")
async def create_item(item: TaggedItem):
    return item
```

This little bit of code unlocks many features such as converting the body to JSON, converting and validating types as necessary, and generating automatic documentation (which we can visit by going to 127.0.0.1:8000/docs or the equivalent URL when live).
```
 ## Core Features of Fast API Continued

 In the previous page we learned how to use Pydantic to create a data model which we passed in as a request body. Now we will build on that and with path and query parameters:

# A GET that in this case just returns the item_id we pass, 
# but a future iteration may link the item_id here to the one we defined in our TaggedItem.
@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int = 1):
    return {"fetch": f"Fetched {count} of {item_id}"}

# Note, parameters not declared in the path are automatically query parameters.
```

Path and query parameters are naturally strings since they are part of the endpoint URL. However, the type hints automatically convert the variables to their specified type. FastAPI automatically understands the distinction between path and query parameters by parsing the declaration. Note, to create optional query parameters use Optional from the `typing` module.

If we wanted to query the above API running on our local machine it would be via `http://127.0.0.1:8000/items/42/?count=1`.

[demo script](./1_fast_api_demo/)

**Code Explanation**

The first file, `main.py`, contains the definition of the API. There are two methods, a `post` and a `get`.

The post takes a JSON object with the format defined by the `pydantic` model `TaggedItem`. In this case, this item is some object with a `name`, one or more `tags` in the form of strings, and an integeter `item_id`.

The get method is used to retrieve `count` instances of `item_id`. This example is just a stub, but one can imagine the post method populating a database with various items and then the get method would be used to retrieve items from the database.

To run this we use the command `uvicorn main:app --reload`. This launches a local server which we use to interact with our API.

In `sample_request.py` we see part of that functionality at work. A post request is made to the local host where our API is running. This post reqest contains a JSON object which is a Hitchhking Kit that has the tags of book and towel, and, surprising to fans of Douglas Adams, it has an item_id of 23. To send this post request to our running server use python sample_request.py while the server is running.

## Local API Testing 

As we saw previous running FastAPI locally is straight forward: uvicorn main:app --reload.

However, this is clunky, and likely impossible if we want to run our tests automatically in our Continuous Integration framework. To get around this FastAPI includes a built-in testing framework:

```
from fastapi.testclient import TestClient

# Import our app from main.py.
from main import app

# Instantiate the testing client with our app.
client = TestClient(app)

# Write tests using the same syntax as with the requests module.
def test_api_locally_get_root():
    r = client.get("/")
    assert r.status_code == 200
```

We will see more details on the requests module on a later page.

**Further Reading**

FastAPI's [tutorial](https://fastapi.tiangolo.com/tutorial/testing/) on local testing.

## Heroku Fundamentals Expanded

In the previous lesson we covered a few fundamentals of Heroku such as **dynos**, **slugs**, and the `Procfile`. Now we will put those fundamentals to work in deploying a web app to Heroku.

Heroku operates on a handful of key principles, a few of which we discuss here. We already touched on dynos which are virtualized containers used for running discrete processes. This connects directly to **statelessness**. Heroku does not store or cache any of your data. If you want to save anything then you must connect your app some form of external storage. Likewise, processes are seen as **disposable**. They can be started or stopped at any time. This is what allows rapid iteration, fault tolerance, and scalability with Heroku.

Heroku's last principle which is the undercurrent throughout everything we have discussed is that of "**build, release, run**". Heroku breaks the app life-cycle into three discrete stages. Whenever we interact with Heroku we are interacting with one of these discrete stages.

And finally, the `Procfile` previously shown was missing a few crucial pieces to get it to function on Heroku. The full file is:

```
web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}
```

Previously when we locally deployed our app it automatically used 127.0.0.1 which is the localhost. Here we use 0.0.0.0 which is the IP used to tell a server to listen on every open network interface. Heroku dynamically assigns the port to the `PORT` variable. In `Unix ${VARIABLE:-default}` is used to assign a default if `VARIABLE` is not set, so here we set the port CLI option to `PORT` and failing that set it to 5000.

**Further Reading**

Heroku's [article](https://devcenter.heroku.com/articles/runtime-principles) on their Runtime Principles.

An excellent StackExchange [post](https://superuser.com/a/949522) on 127.0.0.1 vs. 0.0.0.0.

## Exploring Heroku's CLI

Steps

- Install the Heroku CLI. I used the Ubunutu installation instructions: `curl https://cli-assets.heroku.com/install.sh | sh`
- Type 'heroku' to see the full list of commands.
- To create an app with a specific name and to specify it as Python app use: `heroku create name-of-the-app --buildpack heroku/python`
    - Note that manually specifying it as a Python app is not necessary. Heroku will automatically try and detect the language of your app. In the case of Python it searches for either a requirements.txt or setup.py.

- We can view our apps buildpacks using `heroku buildpacks --app name-of-the-app`.
- Now we'll initiate our folder as a git repository and commit it so we can connect it to our new Heroku app.
    - `git init`
    - `git add *`
    - `git commit -m "Initial commit."`
  
- Connect the repo to our new app: `heroku git:remote --app name-of-the-app`.
    - The app will launch after a few moments.

- Enter into the Heroku VM using: `heroku run bash --app name-of-the-app`.
    - There is not much to see here. Explore the various Unix commands such as `pwd`, and `ls`. Doing `ls ..` reveals many of the standard folders one would expect in a Unix environment. Note this is very lightweight, not even `vi` is included!

## Live Testing with the requests Module

We will test our API one final time now that it is fully deployed. To do this we will use the `requests` module. This module makes it painless to POST, GET, DELETE, etc. with any API.

Using a few lines of code we can POST to an endpoint and retrieve both the status code and the resulting JSON in the response object:
```
import requests

response = requests.post('/url/to/query/')

print(response.status_code)
print(response.json())
```

The requests module is expansive, but a few helpful additions to the bare HTTP methods include authentication and passing in data as JSON objects using the `auth` and `data` parameters, respectively. E.g.:

r = requests.post('/url/to/query/', auth=('usr', 'pass'), data=json.dumps(data))

**Trying out Live APIs**

A fun way to get experience with the `requests` module is to query a live API! There is an extensive list of free and public APIs [here](https://github.com/public-apis/public-apis). Many of these do not even require an authorization key, though getting access to one that needs a key is also good practice!

Note that not all APIs are created equally and some have way significantly more documentation than others. For instance the Art Institute of Chicago's API has extensive [documentation](https://api.artic.edu/docs/#website-2). Some APIs even have their documentation using Swagger like you saw with FastAPI!

Further Reading

The [docs](https://docs.python-requests.org/) for the `requests` module.

FastAPI includes HTTPException.

For more information on FastAPI's error handling see [here](https://fastapi.tiangolo.com/tutorial/handling-errors/) and for metadata see [here](https://fastapi.tiangolo.com/tutorial/metadata/).
