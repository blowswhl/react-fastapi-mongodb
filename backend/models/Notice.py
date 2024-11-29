from beanie import Document
from pydantic import BaseModel, BaseSettings,Field



class Notice(Document):
    title: str 
    content: str
    created_at: str 


    class settings:
        name = "NoticeInfra"