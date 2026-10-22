import { useEffect, useState } from "react";
import { getHealth } from "../services/api";
import type { HealthResponse } from "../types/health";

export function useHealth() {
    const [health, setHealth] = useState<HealthResponse | null>(null);
    const [error, setError] = useState(false);

    useEffect(() => {
        getHealth()
            .then(setHealth)
            .catch(() => setError(true));
    }, []);

    return { health, error };
}
