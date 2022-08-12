# FastAPI Tutorial with Basic PyQuery Project
import os
import json
import random
import shutil
from fastapi import FastAPI, HTTPException, UploadFile, Request
from fastapi.responses import JSONResponse
from typing import  Union
from pyquery import PyQuery
from pydantic import BaseModel
from uuid import uuid4 # Universally Unique Identifier

# PyDantic BaseModel Class
class Song(BaseModel) :
    Rank: int
    Song : str
    Singer : str
    Date : str

# Exception Class
class MyException(Exception) :
    def __init__(self, name: str) :
        self.name = name

class SongNotFound(Exception) :
    def __init__(self, name: str) :
        self.name = name


app = FastAPI() # FastAPI Module

# Local data initialize
song = []
my_file = 'song.json'
upload_file_names = []


# Load local json file if exist
if os.path.exists(my_file) :
    with open(my_file, "r") as f :
        song = json.load(f)

# GET Method Exercise(Basic)
@app.get('/')
def root() :
    return { "message": "Hello Welcome to  2022-01-01 ~ 2022-08-11 Top50 KKbox Song" }

@app.exception_handler(SongNotFound)
def not_exist(request: Request, exc : SongNotFound) :
    return JSONResponse(
        status_code = 404,
        content = {
            'message' : f'Oops! Rank:{exc.name} is not in Top50 KKbox list'
    },
)

@app.get('/get-song')
def get_song(song_rank: int = 1) :
    if not song_rank :
        raise HTTPException(404, f"Oops!Out Of Range. Tips:1~50")
    else :
        for i in song :
            if i['Rank'] == song_rank :
                return { f"Rank":f"{song_rank} is {i['Song']},Singer is {i['Singer']}" }
        raise SongNotFound(name = song_rank)

@app.get('/get-top10')
def get_top10() :
    top10 = []
    for i in song :
        if (i['Rank'] > 0)&(i['Rank'] < 11) :
            top10.append(i)
    return { 'Top10 is:': top10 }


# GET Method Exercise
@app.get('/show-song')
def show_song() :
    return { 'This is Top50 KKbox Song' : song }

# Exception Handler
@app.exception_handler(MyException)
def call_exception_handler(request:Request, exc : MyException) :
    return JSONResponse(
        status_code = 420,
        content = {
            'Message' : f'Oops ! {exc.name} did something....'
        }
    )

# POST Method Exercise
@app.post('/add-song', response_model = Song)
def create_song(songg: Song) :
    song_dict = songg.dict()
    song_dict.update()
    song.append(song_dict)
    # Save a new item into local database(JSON file)
    with open(my_file, "w") as f :
        json.dump(song, f, indent = 4)
    return song_dict


# POST Method Exercise(Upload File & Save to local)
@app.post('/upload')
def Upload_file(file: Union[UploadFile, None] = None) :
    if not file : 
        return { "message" : "No file upload" }
    try :
        file_location = './' + file.filename
        with open(file_location, "wb") as f :
            shutil.copyfileobj(file.file, f)
            file.close()
        upload_file_names.append(file.filename)
        return { "Result" : "OK" }
    except:
        raise MyException(name = f'Upload File {file.filename}')

'''
Notion :
    If you want to run this command below
        > python main.py
    You have to uncomment the main function below !
'''
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app = 'main:app', reload = True) # Default host = 127.0.0.1, port = 8000