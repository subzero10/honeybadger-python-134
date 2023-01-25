from fastapi import FastAPI
from honeybadger import honeybadger, contrib

honeybadger.configure(api_key="YOUR_API_KEY")
app = FastAPI()
app.add_middleware(contrib.ASGIHoneybadger)


@app.get("/")
async def root():
    raise Exception("This will get reported!")
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
