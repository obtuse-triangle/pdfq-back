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
  chapters = AiService.generate_chapters(
    subjects
  )
  return {"filename": filename, "chapters": chapters}


if __name__ == "__main__":
  import uvicorn
  uvicorn.run("server:app", host="0.0.0.0", reload=True)
