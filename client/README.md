# Client

React app. Runs at http://localhost:3000 with `pnpm dev:client`.

- `src/pages/` one file per screen
- `src/components/` reusable pieces used by pages
- `src/layouts/` header, sidebar
- `src/hooks/` load data for pages (`useHealth`)
- `src/services/` calls to the server API
- `src/types/` shapes of the data the server sends (keep in sync with `server/src/schemas/`)
- `src/styles/`, `src/assets/`, `src/utils/`

The desktop app in `electron/` just shows this client in a window.
