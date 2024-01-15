import fastapi
import test
app = fastapi.FastAPI()
@app.get("/")
async def root():
    return {"message":"Hello world"}
@app.get("/item_id/{item_id}")
async def read_item(item_id : int):
    item_id = test.sumpi(item_id)
    return {"message":item_id}
@app.get("/name/{name}")
async def givename(name : str):
    name = "Dear my respect:" + name
    return{"title":name}