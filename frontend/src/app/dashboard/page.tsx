"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

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
    }).then(async (res) => {
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
    });
  }, [router]);

  if (!profile) {
    return <p>{message}</p>;
  }

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Name: {profile.full_name}</p>
      <p>Location: {profile.location}</p>
      <p>Target role: {profile.target_role}</p>
      <p>Graduation year: {profile.graduation_year}</p>
    </div>
  );
}
