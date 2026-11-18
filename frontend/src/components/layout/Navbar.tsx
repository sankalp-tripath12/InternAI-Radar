"use client";

import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";

export default function Navbar() {
  const router = useRouter();
  const pathname = usePathname();

  function handleLogout() {
    localStorage.removeItem("token");
    router.push("/login");
  }

  const linkClass = (href: string) =>
    `rounded px-3 py-1 text-sm font-medium ${
      pathname === href ? "bg-blue-100 text-blue-700" : "text-gray-600 hover:bg-gray-100"
    }`;

  return (
    <nav className="border-b border-gray-200 bg-white">
      <div className="mx-auto flex max-w-4xl items-center gap-2 px-6 py-3">
        <span className="mr-4 font-bold text-blue-700">InternAI Radar</span>
        <Link href="/dashboard" className={linkClass("/dashboard")}>
          Dashboard
        </Link>
        <Link href="/profile" className={linkClass("/profile")}>
          Profile
        </Link>
        <button
          onClick={handleLogout}
          className="ml-auto rounded px-3 py-1 text-sm font-medium text-red-600 hover:bg-red-50"
        >
          Logout
        </button>
      </div>
    </nav>
  );
}
