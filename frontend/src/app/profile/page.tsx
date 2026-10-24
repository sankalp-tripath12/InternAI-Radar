"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

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
    }).then(async (res) => {
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
    });
  }, [router, api]);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError("");

    const token = localStorage.getItem("token");
    const res = await fetch(`${api}/profiles/me`, {
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

    if (!res.ok) {
      const data = await res.json();
      setError(typeof data.detail === "string" ? data.detail : "Could not save profile");
      return;
    }

    router.push("/dashboard");
  }

  return (
    <form onSubmit={handleSubmit}>
      <h1>Your profile</h1>
      <input
        placeholder="Full name"
        value={fullName}
        onChange={(e) => setFullName(e.target.value)}
        required
      />
      <input
        placeholder="Location"
        value={location}
        onChange={(e) => setLocation(e.target.value)}
      />
      <input
        placeholder="Target role"
        value={targetRole}
        onChange={(e) => setTargetRole(e.target.value)}
      />
      <input
        type="number"
        placeholder="Graduation year"
        value={graduationYear}
        onChange={(e) => setGraduationYear(e.target.value)}
      />
      {error && <p style={{ color: "red" }}>{error}</p>}
      <button type="submit">Save</button>
    </form>
  );
}
