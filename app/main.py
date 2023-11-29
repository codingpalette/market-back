from fastapi import FastAPI
from typing import Optional
from routes import auth
import uvicorn


description = """
<div>
    -------------------------------<br>
    <a href="/docs">[ 기본api ]</a><br>
    <a href="/api/auth/docs">[ 유저 api ]</a><br>
    -------------------------------
</div>
"""

def create_app():
    app = FastAPI(title="기본 api", description=description, docs_url="/docs", redoc_url=None, swagger_ui_parameters={"defaultModelsExpandDepth": -1})
    auth_app = FastAPI(title="유저 api", description=description, docs_url="/docs", redoc_url=None, swagger_ui_parameters={"defaultModelsExpandDepth": -1})

    @app.get("/")
    def read_root():
        return {"Hello": "World!"}

    @app.get("/items/{item_id}")
    def read_item(item_id: int, q: Optional[str] = None):
        return {"item_id": item_id, "q": q}

    # 유저 api
    auth_app.include_router(auth.router)
    app.mount("/api/auth", auth_app)

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True, workers=4)
