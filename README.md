# Odyssey

Healthcare management system: React frontend, Python (FastAPI) backend, PostgreSQL on Supabase.

## Who works where

- Alani: `client/`
- Molly: `server/`
- Natan: `database/`

Each folder has its own README with what's inside and the commands you need.

## Setup

You need Node.js, pnpm, [uv](https://docs.astral.sh/uv/) and Docker Desktop.

```sh
pnpm install:all
cp odyssey-config.example.hjson odyssey-config.hjson
pnpm db:start
pnpm dev
```

`pnpm dev` runs the server, client and desktop app together. `pnpm test` runs the tests and
`pnpm lint` fixes formatting.
