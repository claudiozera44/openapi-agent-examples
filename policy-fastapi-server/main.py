from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(servers=[{"url": "http://localhost:7000"}])

# Policies data
policies = {
    2021: [
        {"stampReference": "B21R9990008X", "client": "Meridian Risk Partners Ltd"},
        {"stampReference": "L21M9990008B", "client": "Blackfriars Insurance Services"},
        {"stampReference": "L21M9990011K", "client": "Thames Valley Broking House"},
    ],
    2022: [
        {"stampReference": "L22R0398498M", "client": "Sterling & Associates Risk Management"},
        {"stampReference": "U22R0417438P", "client": "Albion Syndicate 1847"},
        {"stampReference": "T22R0568368L", "client": "Crown Underwriting Agency"},
    ],
    2023: [
        {"stampReference": "L23R0304486T", "client": "Chancery Lane Insurance Brokers"},
        {"stampReference": "P23D0499183P", "client": "Sterling & Associates Risk Management"},
        {"stampReference": "L23L0674884M", "client": "Guildhall Insurance Company Ltd"},
    ],
    2024: [
        {"stampReference": "L24R0398625L", "client": "Britannia Risk Underwriters"},
        {"stampReference": "P24R0934458M", "client": "Chancery Lane Insurance Brokers"},
        {"stampReference": "B24R0397988R", "client": "Britannia Risk Underwriters"},
        {"stampReference": "L24R0398625M", "client": "Leadenhall Underwriting Ltd"},
        {"stampReference": "L24R0404186M", "client": "Chancery Lane Insurance Brokers"},
    ],
    2025: [
        {"stampReference": "L25R0398625L", "client": "Britannia Risk Underwriters"},
        {"stampReference": "P25R0934458M", "client": "Chancery Lane Insurance Brokers"},
        {"stampReference": "B25R0397988R", "client": "Britannia Risk Underwriters"},
        {"stampReference": "L25R0398625M", "client": "Leadenhall Underwriting Ltd"},
        {"stampReference": "L25R0404186M", "client": "Chancery Lane Insurance Brokers"},
    ],    
}

# Models
class StampReferenceClient(BaseModel):
    stampReference: str
    client: str

    class Config:
        schema_extra = {
            "example": {"stampReference": "B23R9990008X", "client": "Leadenhall Underwriting Ltd"},
        }

class YearClientsResponse(BaseModel):
    year: int
    clients: List[StampReferenceClient]

    class Config:
        schema_extra = {
            "example": {
                "year": 2021,
                "clients": [
                    {"stampReference": "L24R0398625M", "client": "Chancery Lane Insurance Brokers"},
                    {"stampReference": "P24R0934458M", "client": "Crown Underwriting Agency"},
                ]
            }
        }

class StampReferenceClientResponse(BaseModel):
    year: int
    stampReference: str
    client: str

    class Config:
        schema_extra = {
            "example": {"stampReference": "L24R0398625M", "client": "Chancery Lane Insurance Brokers"}
        }

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the policy API!"}

# Endpoint to get clients for a specific year
@app.get("/clients/{year}", response_model=YearClientsResponse)
def get_year_clients(year: int):
    if year in policies:
        return {"year": year, "clients": policies[year]}
    return {"error": "Data not available for the requested year."}

# Endpoint to get clients for a specific year and stampReference
@app.get("/clients/{year}/{stampReference}", response_model=StampReferenceClientResponse)
def get_stampReference_client(year: int, stampReference : str):
    if year in policies:
        for stampReference_info in policies[year]:
            if stampReference_info["stampReference"].strip().lower() == stampReference.strip().lower():
                return {"year": year, "stampReference": stampReference, "client": stampReference_info["client"]}
        return {"error": "StampReference not found for the requested year."}
    return {"error": "Data not available for the requested year."}