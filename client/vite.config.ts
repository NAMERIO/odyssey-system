import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

export default defineConfig({
    plugins: [react()],
    // Relative asset paths so the built app also loads from file:// inside Electron.
    base: "./",
    server: {
        port: 3000,
        strictPort: true,
        proxy: {
            "/api": "http://localhost:3001",
        },
    },
});
