from datetime import datetime, timedelta, timezone
import logging
from typing import Optional
from beanie import Document

from pydantic import BaseModel, BaseSettings,Field


# 카운터 모델 (자동 증가 관리용)
class Counter(Document):
    name: str = Field(..., unique=True)  # 필수 필드로 지정
    counter_value: int = Field(default=0)  # 'count' 대신 'counter_value' 사용

    @classmethod
    async def get_next_sequence(cls, name: str) -> int:
        try:
            # 카운터를 찾기 전에 로그를 찍어봅니다.
            logging.info(f"Looking for counter with name: {name}")
            
            # 먼저 카운터를 찾습니다
            counter = await cls.find_one({"name": name})
            logging.info(f"Counter search result: {counter}")  # counter가 무엇인지 로그

            if counter:
                # 카운터가 있을 경우
                logging.info(f"Found counter: {counter.name} with value: {counter.counter_value}")
                counter.counter_value += 1  # counter_value 증가
                await counter.save()  # 카운터 값 저장
                logging.info(f"Counter incremented: {counter.name} - {counter.counter_value}")
                return counter.counter_value  # 증가된 값 반환
            else:
                # 카운터가 없다면 새로 생성
                logging.info(f"No counter found, creating a new counter with name: {name}")
                new_counter = Counter(name=name, counter_value=1)  # 카운터 값 1부터 시작
                await new_counter.insert()  # 새 카운터 값 삽입
                logging.info(f"New counter created: {new_counter.name} - {new_counter.counter_value}")
                return 1  # 첫 번째 번호를 반환
        except Exception as e:
            # 예외가 발생하면 해당 예외 로그를 찍어봅니다.
            logging.error(f"Error generating notice number: {e}")
            raise ValueError("Error generating notice number")  # 예외를 다시 던져서 호출자에게 알림


#인프라 
#공지사항 모델 
class Notice(Document):
    title: str 
    content: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(hours=9))))  # UTC로 설정
    notice_number: Optional[int] = Field(default=None) #공지사항 번호 


    class Settings:
        name = "NoticeInfra"

#리소스요청사항 모델 
class Notice2(Document):
    title: str 
    content: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(hours=9))))  # UTC로 설정
    notice_number: Optional[int] = Field(default=None) #공지사항 번호 



    class Settings:
        name = "NoticeInfra2"


#개발자
#공지사항 모델 
class Notice3(Document):
    title: str 
    content: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(hours=9))))  # UTC로 설정
    notice_number: Optional[int] = Field(default=None) #공지사항 번호 



    class Settings:
        name = "NoticeDev"

#프로젝트현황 모델 
class Notice4(Document):
    title: str 
    content: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone(timedelta(hours=9))))  # UTc로 설정
    notice_number: Optional[int] = Field(default=None) #공지사항 번호 



    class Settings:
        name = "NoticeDev2"
        