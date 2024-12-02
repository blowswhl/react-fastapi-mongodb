import logging
from typing import List, Optional
from fastapi import APIRouter, HTTPException 
from models.Notice import Notice,Notice2,Counter
from datetime import datetime, timezone, timedelta


utc_now = datetime.now(timezone.utc) #UTC 전세계 표준시간

kst_now = utc_now + timedelta(hours=9) # 한국시간은 +9시간 더해야함

notice_router = APIRouter ( tags=["Notice"] )

notice={}

#인프라
#공지사항파트
@notice_router.get("/NoticeInfra")
async def get_NoticeInfra():
      notices  = await Notice.find_all().to_list() #문서반환

      return {"notices": notices}


@notice_router.post("/NoticeInfPost")
async def post_NoticeInfra(title: str, content: str):

      notice_count = await Notice.find().to_list()  # 전체 문서 리스트 가져오 #현재 "Notice"
      notice_number = len(notice_count) + 1
            
      
      new_notice = Notice(
           title=title,
           content=content,
           created_at = kst_now,
           notice_number=notice_number 
    
      )
      await new_notice.insert() 

      return {"message": "Notice created successfully"}

# 공지사항 수정
@notice_router.put("/NoticeInfUpdate/{notice_number}")
async def update_NoticeInfra(notice_number: int, title: Optional[str] = None, content: Optional[str] = None):
    # notice_number로 공지사항을 찾습니다.
    notice = await Notice.find_one({"notice_number": notice_number})
    if not notice:
        raise HTTPException(status_code=404, detail="Notice not found")

    # 수정할 필드가 있으면 업데이트
    if title:
        notice.title = title
    if content:
        notice.content = content

    # 수정된 공지사항을 저장
    await notice.save()

    return {"message": "Notice updated successfully", "notice_number": notice_number}


# 공지사항 삭제
@notice_router.delete("/NoticeInfDelete/{notice_number}")
async def delete_NoticeInfra(notice_number: int):
    # notice_number로 공지사항을 찾습니다.
    notice = await Notice.find_one({"notice_number": notice_number})
    if not notice:
        raise HTTPException(status_code=404, detail="Notice not found")

    # 공지사항 삭제
    await notice.delete()

    return {"message": "Notice deleted successfully", "notice_number": notice_number}


@notice_router.get("/Notices", response_model=List[Notice])
async def get_notices():
      notices = await Notice.find().sort([("created_at", -1)]).limit(5).to_list() #최신 5개 반환
      print(notices)
      return notices 

#리소스 요청사항파트 모델을 또 추가해야함
@notice_router.get("/NoticeInfra2")
async def get_NoticeInfra():
      notices  = await Notice2.find_all().to_list() #문서반환

      return {"notices": notices}


@notice_router.post("/NoticeInfPost2")
async def post_NoticeInfra(title: str, content: str):
      
      notice_count = await Notice2.find().to_list() 
      notice_number = len(notice_count) + 1 

      new_notice = Notice2(
           title=title,
           content=content,
           created_at = kst_now,
           notice_number=notice_number 
    
      )
      await new_notice.insert() 

      return {"message": "Notice created successfully"}

@notice_router.put("/NoticeInUpdate2/{notice_number}")
async def update_NoticeInfra2(notice_number: int, title: Optional[str] = None, content: Optional[str] = None):
    notice = await Notice2.find_one({"notice_number": notice_number})
    if not notice:
        raise HTTPException(status_code=404, detail="번호에 해당하는 게시물이 없습니다")
    
    if title:
        notice.title = title
    if content:
        notice.content = content

    await notice.save()
    
    return {"message": "성공적으로 업데이트되었습니다."}

 
@notice_router.delete("/NoticeInfDelete2/{notice_number}")
async def delete_NoticeInfra(notice_number: int):
    # notice_number로 공지사항을 찾습니다.
    notice = await Notice2.find_one({"notice_number": notice_number})
    if not notice:
        raise HTTPException(status_code=404, detail="Notice not found")

    # 공지사항 삭제
    await notice.delete()

    return {"리소스 요청사항이 삭제되었습니다."}

@notice_router.get("/Notices2", response_model=List[Notice])
async def get_notices():
      notices = await Notice2.find().sort([("created_at", -1)]).limit(5).to_list() #최신 5개 반환
      print(notices)
      return notices 


