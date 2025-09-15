from fastapi import FastAPI

app = FastAPI(title="Payment API Validator", version="0.1.0")

@app.get("/")
def read_root():
    return {"message": "Payment API Validator is running"}

@app.get("/health")
def health_check():
    return {"status": "OK"}

