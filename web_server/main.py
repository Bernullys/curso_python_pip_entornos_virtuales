import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3, 4, 5]

@app.get('/contact')
def get_list():
    return {"name": "bernardo"}

@app.get('/try', response_class=HTMLResponse)
def get_list():
    return """
        <h1>I'm a html from python </h1>
    
    """

def run():
    store.get_categories()


if __name__=="__main__":
    run()