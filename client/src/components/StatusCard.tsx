import type { HealthResponse } from "../types/health";

interface StatusCardProps {
    health: HealthResponse | null;
    error: boolean;
}

export function StatusCard({ health, error }: StatusCardProps) {
    return (
        <section>
            <h2>System status</h2>
            {error && <p>Can't reach the server. Is it running?</p>}
            {!error && !health && <p>Checking…</p>}
            {health && (
                <ul>
                    <li>API: {health.status}</li>
                    <li>Database: {health.database}</li>
                </ul>
            )}
        </section>
    );
}
