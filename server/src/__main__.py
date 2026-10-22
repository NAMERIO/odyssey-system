import sys

import uvicorn

from src.config import SERVER_PORT

reload = "--reload" in sys.argv

uvicorn.run(
    "src.main:app",
    host="0.0.0.0",
    port=SERVER_PORT,
    reload=reload,
    reload_dirs=["src"] if reload else None,
)
