from fastapi import FastAPI, UploadFile, File
from fastapi.requests import Request
app = FastAPI()

db = []
mb = []
@app.post("/DeviceSnaps")
async def upload_file(request:Request,file: UploadFile = File(...)):
    rqst_info = await request.json()
    contents = await file.read()
    db.append(file)
    # Process the contents of the file
    return {"filename": file.filename}

@app.get("/images")
async def show_image():  
    for i in db:
        mb.append(i)
    return mb