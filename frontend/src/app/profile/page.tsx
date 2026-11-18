"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import Navbar from "@/components/layout/Navbar";

const inputClass =
  "w-full rounded border border-gray-300 px-3 py-2 text-sm focus:border-blue-500 focus:outline-none";
const labelClass = "mb-1 block text-sm font-medium";

export default function ProfilePage() {
  const router = useRouter();
  const [fullName, setFullName] = useState("");
  const [location, setLocation] = useState("");
  const [targetRole, setTargetRole] = useState("");
  const [graduationYear, setGraduationYear] = useState("");
  const [error, setError] = useState("");

  const api = process.env.NEXT_PUBLIC_API_BASE_URL;

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      router.push("/login");
      return;
    }

    fetch(`${api}/profiles/me`, {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then(async (res) => {
        if (res.status === 401) {
          localStorage.removeItem("token");
          router.push("/login");
          return;
        }
        if (res.ok) {
          const profile = await res.json();
          setFullName(profile.full_name);
          setLocation(profile.location ?? "");
          setTargetRole(profile.target_role ?? "");
          setGraduationYear(profile.graduation_year?.toString() ?? "");
        }
      })
      .catch(() => setError("Cannot reach the server. Is the backend running?"));
  }, [router, api]);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError("");

    const token = localStorage.getItem("token");
    let res: Response;
    try {
      res = await fetch(`${api}/profiles/me`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          full_name: fullName,
          location: location || null,
          target_role: targetRole || null,
          graduation_year: graduationYear ? Number(graduationYear) : null,
        }),
      });
    } catch {
      setError("Cannot reach the server. Is the backend running?");
      return;
    }

    if (!res.ok) {
      const data = await res.json();
      setError(typeof data.detail === "string" ? data.detail : "Could not save profile");
      return;
    }

    router.push("/dashboard");
  }

  return (
    <div>
      <Navbar />
      <main className="mx-auto max-w-md p-6">
        <form
          onSubmit={handleSubmit}
          className="space-y-4 rounded-lg border border-gray-200 bg-white p-6 shadow-sm"
        >
          <h1 className="text-xl font-semibold">Your profile</h1>
          <div>
            <label htmlFor="full_name" className={labelClass}>
              Full name
            </label>
            <input
              id="full_name"
              value={fullName}
              onChange={(e) => setFullName(e.target.value)}
              className={inputClass}
              required
            />
          </div>
          <div>
            <label htmlFor="location" className={labelClass}>
              Location
            </label>
            <input
              id="location"
              value={location}
              onChange={(e) => setLocation(e.target.value)}
              className={inputClass}
            />
          </div>
          <div>
            <label htmlFor="target_role" className={labelClass}>
              Target role
            </label>
            <input
              id="target_role"
              value={targetRole}
              onChange={(e) => setTargetRole(e.target.value)}
              className={inputClass}
            />
          </div>
          <div>
            <label htmlFor="graduation_year" className={labelClass}>
              Graduation year
            </label>
            <input
              id="graduation_year"
              type="number"
              value={graduationYear}
              onChange={(e) => setGraduationYear(e.target.value)}
              className={inputClass}
            />
          </div>
          {error && <p className="text-sm text-red-600">{error}</p>}
          <button
            type="submit"
            className="w-full rounded bg-blue-600 px-3 py-2 text-sm font-medium text-white hover:bg-blue-700"
          >
            Save
          </button>
        </form>
      </main>
    </div>
  );
}
