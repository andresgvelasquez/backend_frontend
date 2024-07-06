from fastapi import FastAPI

app = FastAPI()

@app.get('/') #Ruta base o raiz de mi app web
def root():
    return 'Hi, my name is FastAPI'