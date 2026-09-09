from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()



@app.get("/", response_class=HTMLResponse)
def read_root():
	return """
<!DOCTYPE html>
    <html>
        <head>
            <title>FastAPI HTML</title>
        </head>
        <body>
            <h1>Hello World !</h1>
        </main>
    </html>"""
