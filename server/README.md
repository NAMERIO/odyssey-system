# Server

Python API (FastAPI). Runs at http://localhost:3001 with `pnpm dev:server`.
API docs: http://localhost:3001/api/docs

- `src/routes/` API endpoints (register new ones in `src/main.py`)
- `src/schemas/` shapes of request and response data
- `src/services/` logic and database queries (connect with `import db`, see `database/db.py`)
- `tests/` tests, run with `pnpm test`

Add a Python package: `uv --directory server add <package>`.
