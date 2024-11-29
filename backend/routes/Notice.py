from fastapi import APIRouter 
from models.Notice import Notice


notice_router = APIRouter ()

notice={}


@notice_router.get("/NoticeInfra")
async def get_NoticeInfra():
      notices  = await Notice.find_all().to_list() #문서반환

      return {"notices": notices}


@notice_router.post("/NoticeInfPost")
async def post_NoticeInfra(title: str, content: str):
      new_notice = Notice(
           title=title,
           content=content,
    
      )
      await new_notice.insert() 

      return {"message": "Notice created successfully"}