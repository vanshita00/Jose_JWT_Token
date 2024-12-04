from fastapi import FastAPI
# from jose import jwt 
from function import create_access_token,decode_token

app=FastAPI()

# ALGORITHM='HS256'
# SECRET="I AM SECRET KEY"

# def create_access_token(subject:str):
#     token=jwt.encode({'data':subject},SECRET)
#     return {"access_token":token}

# def decode_token(token:str):
#     data=jwt.decode(token,SECRET)
#     return data


@app.get("/")
async def root():
    return{"message":"Hello World"}


@app.get("/create-token")
async def create_token_api(name:str):
    token=create_access_token(subject=name)
    return token


@app.post("/decode-token")
async def decode_token_api(token:str):
    data=decode_token(token=token)
    return data
   