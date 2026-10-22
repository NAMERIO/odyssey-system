import type { HealthResponse } from "../types/health";

const baseUrl = import.meta.env.VITE_API_URL ?? "";

export async function getHealth(): Promise<HealthResponse> {
    const res = await fetch(`${baseUrl}/api/health`);
    return res.json();
}
