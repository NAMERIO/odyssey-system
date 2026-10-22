import type { ReactNode } from "react";

export function MainLayout({ children }: { children: ReactNode }) {
    return (
        <>
            <header>
                <h1>Odyssey</h1>
                <p>Healthcare management system</p>
            </header>
            <main>{children}</main>
        </>
    );
}
