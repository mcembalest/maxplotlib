from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import StreamingResponse
from maxplotlib.plot import plot

app = FastAPI(debug=False)

def stream_module_result(module_result, media_type="text/plain"):
    try:
        return StreamingResponse(module_result, media_type=media_type)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/plot/")
async def calculate_api(chat: str = Form(...)):
    return stream_module_result(plot(chat))