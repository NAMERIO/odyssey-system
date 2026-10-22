import { StatusCard } from "../components/StatusCard";
import { useHealth } from "../hooks/useHealth";

export function HomePage() {
    const { health, error } = useHealth();

    return <StatusCard health={health} error={error} />;
}
