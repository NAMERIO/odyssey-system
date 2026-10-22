# Database

PostgreSQL on Supabase. Needs Docker Desktop running.

- `supabase/migrations/` every change to the tables, one SQL file each
- `supabase/seed.sql` test data for local development
- `supabase/config.toml` local Supabase settings
- `db.py` connects the server to the database (reads `database` from `odyssey-config.hjson`)

Commands:

- `pnpm db:start` start the local database. Tables UI: http://localhost:54323
- `pnpm db:new <name>` create a new migration file
- `pnpm db:reset` rebuild the local database from all migrations and the seed
- `pnpm db:push` apply new migrations to the real Supabase project

Never edit tables in the Supabase dashboard; always write a migration so everyone stays in sync.
