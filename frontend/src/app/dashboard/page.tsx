"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import Link from "next/link";
import Navbar from "@/components/layout/Navbar";

type Profile = {
  full_name: string;
  location: string | null;
  target_role: string | null;
  graduation_year: number | null;
};

export default function DashboardPage() {
  const router = useRouter();
  const [profile, setProfile] = useState<Profile | null>(null);
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    const token = localStorage.getItem("token");

    if (!token) {
      router.push("/login");
      return;
    }

    fetch(`${process.env.NEXT_PUBLIC_API_BASE_URL}/profiles/me`, {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then(async (res) => {
        if (res.status === 401) {
          localStorage.removeItem("token");
          router.push("/login");
          return;
        }
        if (res.status === 404) {
          setMessage("No profile yet.");
          return;
        }
        setProfile(await res.json());
      })
      .catch(() => setMessage("Cannot reach the server. Is the backend running?"));
  }, [router]);

  return (
    <div>
      <Navbar />
      <main className="mx-auto max-w-2xl p-6">
        {!profile ? (
          <div className="rounded-lg border border-gray-200 bg-white p-6 shadow-sm">
            <p>{message}</p>
            {message === "No profile yet." && (
              <Link
                href="/profile"
                className="mt-3 inline-block rounded bg-blue-600 px-3 py-2 text-sm font-medium text-white hover:bg-blue-700"
              >
                Create your profile
              </Link>
            )}
          </div>
        ) : (
          <div className="rounded-lg border border-gray-200 bg-white p-6 shadow-sm">
            <h1 className="mb-4 text-xl font-semibold">Dashboard</h1>
            <dl className="grid grid-cols-[140px_1fr] gap-y-2 text-sm">
              <dt className="text-gray-500">Name</dt>
              <dd>{profile.full_name}</dd>
              <dt className="text-gray-500">Location</dt>
              <dd>{profile.location ?? "Not set"}</dd>
              <dt className="text-gray-500">Target role</dt>
              <dd>{profile.target_role ?? "Not set"}</dd>
              <dt className="text-gray-500">Graduation year</dt>
              <dd>{profile.graduation_year ?? "Not set"}</dd>
            </dl>
            <Link
              href="/profile"
              className="mt-5 inline-block text-sm text-blue-600 hover:underline"
            >
              Edit profile
            </Link>
          </div>
        )}
      </main>
    </div>
  );
}
