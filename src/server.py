from fastapi import Body, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import dotenv
import markdownUtils
import AiService

dotenv.load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/upload/{filename}")
async def upload_markdown(filename: str, md: bytes = Body(...)):
  filename = markdownUtils.upload_markdown(filename, md)
  subjects = markdownUtils.split_by_title(
    md.decode('utf-8')
  )
  # chapters = AiService.generate_chapters(
  #   subjects
  # )
  chapters = {
      "chapters": [
          {
              "title": "운영체제 개요",
              "sections": [
                  "운영체제의 주요 목적",
                  "운영체제의 기능",
                  "운영체제의 기능 분류",
                  "운영체제의 구성 요소와 역할",
                  "운영체제 연산(커널과 시스템 호출)",
                  "트랩과 시스템 호출",
                  "사용자 모드와 커널 모드",
                  "운영체제 구조",
                  "운영체제의 발달 과정"
              ]
          },
          {
              "title": "프로세스 관리",
              "sections": [
                  "프로세스 개요",
                  "프로그램과 프로세스의 차이",
                  "프로세스의 메모리 구조",
                  "프로세스 제어 블록(PCB)",
                  "PCB의 주요 정보",
                  "PCB의 역할",
                  "프로세스 상태와 상태 전이",
                  "프로세스 상태",
                  "프로세스 상태 전이"
              ]
          },
          {
              "title": "프로세스와 스레드",
              "sections": [
                  "프로세스와 스레드 비교",
                  "프로세스",
                  "스레드",
                  "싱글 스레드와 멀티 스레드",
                  "싱글 스레드",
                  "멀티 스레드"
              ]
          },
          {
              "title": "스케줄링",
              "sections": [
                  "스케줄링 개요",
                  "스케줄링의 종류",
                  "기능별 분류",
                  "방법별 분류",
                  "CPU 스케줄링 알고리즘",
                  "선입선출 스케줄링(FCFS)",
                  "최단 작업 우선 스케줄링(SJF)",
                  "최단 잔여 시간 우선 스케줄링(SRT)",
                  "HRN 스케줄링",
                  "우선순위 스케줄링",
                  "라운드로빈 스케줄링(Round-Robin, RR)",
                  "다단계 큐 스케줄링(Multi-Level Queue, MLQ)",
                  "다단계 피드백 큐 스케줄링(Multi-Level Feedback Queue, MFQ)",
                  "기아(Starvation)와 에이징(Aging)"
              ]
          },
          {
              "title": "프로세스 동기화",
              "sections": [
                  "병행 프로세스",
                  "임계영역 문제",
                  "2개 프로세스 간 상호 배제",
                  "N개 프로세스 간 상호 배제"
              ]
          }
      ]
  }
  return {"filename": filename, **chapters}


if __name__ == "__main__":
  import uvicorn
  uvicorn.run("server:app", host="0.0.0.0", reload=True)
