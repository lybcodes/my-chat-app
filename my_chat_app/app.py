from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from .model import ChatModel
from pathlib import Path

app = FastAPI()

chat_model = ChatModel()

STATIC_DIR = Path(__file__).parent / "static"

# 主页路由：返回聊天界面
@app.get("/", response_class=HTMLResponse)
async def read_root():
    index_path = STATIC_DIR / "index.html"
    if not index_path.exists():
        return HTMLResponse(content="<h1>404 Not Found</h1>", status_code=404)
    with open(index_path, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

# 手动处理静态文件请求
@app.get("/static/{file_name}")
async def serve_static(file_name: str):
    file_path = STATIC_DIR / file_name
    if not file_path.exists():
        return Response(status_code=404)
    with open(file_path, "rb") as f:
        content = f.read()
    media_type = "image/x-icon" if file_name.endswith(".ico") else "text/html"
    return Response(content=content, media_type=media_type)

# 忽略 favicon.ico 请求（可选）
@app.get("/static/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(content="", media_type="image/x-icon")

# 聊天接口
@app.post("/chat")
async def chat(request: Request):
    try:
        # 获取用户输入
        data = await request.json()
        user_message = data.get("message", "").strip()
        if not user_message:
            return {"error": "Message is required"}

        # 调用模型生成回复
        response = chat_model.generate_response(user_message)
        return {"response": response}
    except Exception as e:
        return {"error": str(e)}