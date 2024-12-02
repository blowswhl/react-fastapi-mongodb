from typing import List, Optional
from fastapi import APIRouter, HTTPException 
from models.Notice import Notice3,Notice4
from datetime import datetime, timezone, timedelta


Dev_notice_router = APIRouter( tags=["DevNotice"]);

utc_now = datetime.now(timezone.utc) #UTC 전세계 표준시간

kst_now = utc_now + timedelta(hours=9) # 한국시간은 +9시간 더해야함

notices = []

#개발자
#공지사항파트
@Dev_notice_router.get("/NoticeDevelop")
async def get_NoticeInfra():
      notices  = await Notice3.find_all().to_list() #문서반환

      return {"notices": notices}


@Dev_notice_router.post("/NoticeDevPost")
async def post_NoticeInfra(title: str, content: str):
      
      notice_count = await Notice3.find().to_list()
      notice_number = len(notice_count) + 1

      new_notice = Notice3(
           title=title,
           content=content,
           created_at = kst_now,
           notice_number=notice_number 
    
      )
      await new_notice.insert() 

      return {"message": "Notice created successfully"}

@Dev_notice_router.put("/NoticeDevUpdate/{notice_number}")
async def update_NoticeInfra2(notice_number: int, title: Optional[str] = None, content: Optional[str] = None):
    notice = await Notice3.find_one({"notice_number": notice_number})
    if not notice:
        raise HTTPException(status_code=404, detail="번호에 해당하는 게시물이 없습니다")
    
    if title:
        notice.title = title
    if content:
        notice.content = content

    await notice.save()
    
    return {"message": "성공적으로 업데이트되었습니다."}

 
@Dev_notice_router.delete("/NoticeDevDelete/{notice_number}")
async def delete_NoticeInfra(notice_number: int):
    # notice_number로 공지사항을 찾습니다.
    notice = await Notice3.find_one({"notice_number": notice_number})
    if not notice:
        raise HTTPException(status_code=404, detail="Notice not found")

    # 공지사항 삭제
    await notice.delete()

    return {"프로젝트 현황이 삭제되었습니다."}

@Dev_notice_router.get("/Notices3", response_model=List[Notice3])
async def get_notices():
      notices = await Notice3.find().sort([("created_at", -1)]).limit(5).to_list() #최신 5개 반환
      print(notices)
      return notices 

#리소스 요청사항파트 모델을 또 추가해야함
@Dev_notice_router.get("/NoticeDevelop2")
async def get_NoticeInfra():
      notices  = await Notice4.find_all().to_list() #문서반환

      return {"notices": notices}


@Dev_notice_router.post("/NoticeDevPost2")
async def post_NoticeInfra(title: str, content: str):
      
      notice_count = await Notice4.find().to_list()
      notice_number = len(notice_count) + 1

      new_notice = Notice4(
           title=title,
           content=content,
           created_at = kst_now,
           notice_number=notice_number 
    
      )
      await new_notice.insert() 

      return {"message": "작성 완료"}

@Dev_notice_router.put("/NoticeDevUpdate2/{notice_number}")
async def update_NoticeInfra2(notice_number: int, title: Optional[str] = None, content: Optional[str] = None):
    notice = await Notice4.find_one({"notice_number": notice_number})
    if not notice:
        raise HTTPException(status_code=404, detail="번호에 해당하는 게시물이 없습니다")
    
    if title:
        notice.title = title
    if content:
        notice.content = content

    await notice.save()
    
    return {"message": "성공적으로 업데이트되었습니다."}

 
@Dev_notice_router.delete("/NoticeDevDelete2/{notice_number}")
async def delete_NoticeInfra(notice_number: int):
    # notice_number로 공지사항을 찾습니다.
    notice = await Notice4.find_one({"notice_number": notice_number})
    if not notice:
        raise HTTPException(status_code=404, detail="Notice not found")

    # 공지사항 삭제
    await notice.delete()

    return {"프로젝트 현황이 삭제되었습니다."}

@Dev_notice_router.get("/Notices4", response_model=List[Notice4])
async def get_notices():
      notices = await Notice4.find().sort([("created_at", -1)]).limit(5).to_list() #최신 5개 반환
      print(notices)
      return notices 