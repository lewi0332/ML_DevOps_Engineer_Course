**Summary**

Start by reading relevant modules:

```
from flask import Flask, request
import pandas as pd
```

Then, instantiate your app with the Flask() command:
```
app = Flask(__name__)
```
Create a function that will read and return files. We can call this function an auxiliary function, or in other words, a helper function:
```
def readpandas(filename):
    thedata=pd.read_csv(filename)
    return thedata
```
Specify our first endpoint, with a default route:
```
@app.route('/')
def index():
    user = request.args.get('user')
    return str(user=='Bradford') + '\n'   
```
Now, the most important part: specify another endpoint, with a different route, that accomplishes another, more complex task:
```
@app.route('/medians')
def summary():
    filename = request.args.get('filename')  
    thedata=readpandas(filename)
    return str(thedata.median(axis=0))
```
Notice that every endpoint has its own, unique function with its own, unique return statement.

Finally, run the app, specifying a hostname and a port:
```
app.run(host='0.0.0.0', port=8000)
```

Performance_Testing_and_Preparing_a_Model_for_Production
