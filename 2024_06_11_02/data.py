import requests
from requests import Response
from pydantic import BaseModel, Field

def __download_json():
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

    try:
        res:Response = requests.get(url)
        res.raise_for_status()
    except requests.exceptions.RequestException:
        raise Exception("連線失敗")
    else:
        print(res.json())
        return res.json()
    
class Info(BaseModel):
    sna: str
    sarea: str
    mday: str
    ar: str
    act: str
    updateTime: str
    total: int
    available_rent_bikes: int = Field(alias="rent_bikes")
    latitude: float = Field(alias="lat")
    longitude: float = Field(alias="lng")
    available_return_bikes: int = Field(alias="retuen_bikes")

def load_data() -> list[dict]:
    all_data = __download_json()
    stations = all_data["retVal"]
    youbike_data = [Info(**station) for station in stations]
    return [station.dict() for station in youbike_data]
