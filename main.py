#import packet
from fastapi import FastAPI, Request, Header, HTTPException
import pandas as pd

#buat dataframe baru
df = pd.DataFrame()

df['UserName'] = ['Undertaker', 'Rey', 'edge']
df['Location'] = ['texas','maxico','colombia']

#pswd api_key
API_KEY = "testingapitokenkey1234"

#BUAT OBJEK
app = FastAPI()


# membuat function * url (endpoint)

# endpoint untuk retridve all data
# http://www.domain.com
@app.get("/")
def handlerdata(request: Request):
    # get request headers
    headers = request.headers

    return {
        "masssege": "this is fastapi data",
        "headers": headers
    }

# endpoint secret
@app.get("/secret")
def handerSecret(api_key: str = Header(None)):
    #cek api_key
    if api_key != API_KEY:
        return {
            "error":"anda tidak lolos"
        }
    
# endpoint get all data from dataframe
@app.get("/data")
def handlerDf():
    return df.to_dict(orient="record")

