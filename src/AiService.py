import requests
import dotenv
import os
import json
from pydantic import BaseModel
from typing import List

dotenv.load_dotenv()
DifyChapterToken = os.getenv("DifyChapterToken")


class Chapter(BaseModel):
  title: str
  sections: List[str]


class ChaptersResponse(BaseModel):
  chapters: List[Chapter]


def generate_chapters(subjects: list[str]) -> ChaptersResponse:
  titles = []
  for i in subjects:
    if i.startswith("#"):
      titles.append(i.split("\n")[0])
  res = requests.post(
    "https://dify.obtuse.kr/v1/completion-messages",
    headers={
      'Authorization': f'Bearer {DifyChapterToken}',
      'Content-Type': 'application/json'
    },
    json={
      "inputs": {
        "query": "\n".join(titles),
      },
      "response_mode": "blocking",
      "user": "asdf-1234"
    }
  )
  res = res.json()
  return json.loads(res['answer'])
