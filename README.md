# How To Build and Deploy a Flask Application Using Docker 
## `Using VS Code and the Docker extension.`

Build a simple “Hello World” Flask application and deploy it using the Docker extension.  
#### runserver-sample.py
```
"""
python runserver-sample.py
"""
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """Return a friendly HTTP greeting."""
    message = "Hello World"
    return message

if __name__ == "__main__":
    app.run(host="0.0.0.0")

```
#### requirements.txt
```
Flask==1.1.2
gunicorn
```
To create a Dockerfile and everything else you need just run `Docker: Add Docker Files to Workspace` in the command palette (`ctlr+shift+p` in windows).  

Select the `Python: Flask` option for the first question and then, the extension will ask you if you would like to include the optional Docker compose files.  
Choose `yes`; this way you will be able to debug the application running inside the container later.  
Finally, choose the python file holding the Flask application (the code provided above) and the port you would like to expose (`5000` is the default). You are ready!

Now, to build the image, right-click on the generated Dockerfile and choose `Build Image....` A terminal will open and your image will be ready in a matter of seconds.  

To run the application, select the Docker icon from the left panel, locate your image in the `Images` section, right-click it and choose run. That simple.  

In the `Containers` section locate the running container, right-click it and choose `View Logs`. This command will display the logs of your container in the terminal.  
Get the endpoint that it is listening to (should be `http://0.0.0.0:5000`). To get the results of your Python service run `curl http://0.0.0.0:5000`.

That’s it! The Docker extension for VS Code simplifies the process and you get back the time to concentrate on your code.