import fastapi
app = fastapi.FastAPI()
@app.get("/")
async def root():
    return {"message":"Hello world"}
@app.get("/item_id/{item_id}")
async def read_item(item_id):
    return {"message":item_id}