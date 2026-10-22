import path from "node:path";
import { app, BrowserWindow } from "electron";

const isDev = process.argv.includes("--dev");
const devUrl = "http://localhost:3000";
const builtIndex = path.join(import.meta.dirname, "../../client/dist/index.html");

function createWindow() {
    const win = new BrowserWindow({
        width: 1280,
        height: 800,
        title: "Odyssey",
        webPreferences: {
            contextIsolation: true,
            nodeIntegration: false,
        },
    });

    if (isDev) {
        // The Vite dev server may still be starting, so keep retrying until it answers.
        win.webContents.on("did-fail-load", () => {
            setTimeout(() => win.loadURL(devUrl), 1000);
        });
        win.loadURL(devUrl);
    } else {
        win.loadFile(builtIndex);
    }
}

app.whenReady().then(() => {
    createWindow();
    app.on("activate", () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow();
    });
});

app.on("window-all-closed", () => {
    if (process.platform !== "darwin") app.quit();
});
