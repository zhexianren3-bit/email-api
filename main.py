from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "邮件API"}
@app.post("/send")
def send(to: str, subject: str = "test", body: str = ""):
    return {"success": True, "msg": "邮件发送成功"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
