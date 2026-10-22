create table if not exists public.ping_test (
    id bigint generated always as identity primary key,
    created_at timestamptz not null default now()
);

alter table public.ping_test enable row level security;
