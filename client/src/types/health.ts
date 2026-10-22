// Matches HealthResponse in server/src/schemas/health.py
export interface HealthResponse {
    status: "ok" | "error";
    database: "connected" | "disconnected" | "not_configured";
    timestamp: string;
}
