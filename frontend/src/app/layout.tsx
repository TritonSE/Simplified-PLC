import type { Metadata } from "next";

import "./globals.css";

export const metadata: Metadata = {
  title: "Simplified PLC",
  description: "A Next.js app with the new app router",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
