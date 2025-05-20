import os
import re
from fastapi import HTTPException


def extract_titles(markdown: str) -> list[str]:
  lines = markdown.split("\n")
  titles = [line for line in lines if line.startswith("#")]
  return titles


def write_file(filename: str, content: str) -> None:
  if os.path.exists(f"uploads/{filename}"):
    raise HTTPException(status_code=400, detail="File already exists")
  with open(f"uploads/{filename}", "w") as f:
    f.write(content)


def upload_markdown(filename: str, markdown: bytes) -> None:
  if not filename.endswith(".md"):
    filename += ".md"
  write_file(filename, markdown.decode('utf-8'))
  return filename


def split_by_title(markdown: str) -> list[str]:
  pattern = r'(^#+ .*)'
  splits = re.split(pattern, markdown, flags=re.MULTILINE)
  subjects = []

  # Reconstruct sections: heading + content
  for i in range(1, len(splits), 2):
    heading = splits[i].strip()
    content = splits[i + 1].strip() if i + 1 < len(splits) else ""
    subjects.append(f"{heading}\n{content}")

  print(f"총 단원 개수: {len(subjects)}")
  return subjects
