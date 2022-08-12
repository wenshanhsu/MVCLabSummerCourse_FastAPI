# Homework - FastAPI

## Description
### This is a collection of the top 50 of kkbox's annual cumulative list
Calculation range:2022-01-01 ~ 2022-08-11

## Setup
### How to run
* **Step 1: Install Python Packages**
    * > pip install -r requirements.txt
* **Step 2: Run by uvicorn (Localhost)**
    * > uvicorn main:app --reload
    * Default host = 127.0.0.1, port = 8000
* **Step 3: Test API using Swagger UI**
    * http://127.0.0.1:8000/docs

## Json Structure
* Rank(int) = Song's rank in Top 50 of kkbox's annual cumulative list
* Song(str) = Song name
* Singer(str)  = Who sing the song
* Date(str) = Song release date


## GET methods
* > /get-song
    * Assign ranking to song data.
* > /get-top10
    * Get Top 10 of kkbox's annual cumulative list.
* > /show-song
    * List all the song.

## POST methods
* > /add-song
    * Add a song to json file.
* > /upload-file
    * Upload file to server.

