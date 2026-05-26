"use client";

import { useState } from "react";

export default function Home() {

  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  async function generateApp() {

    setLoading(true);

    try {

      const response = await fetch(
        "http://127.0.0.1:8000/generate",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            prompt: prompt,
          }),
        }
      );

      const data = await response.json();

      setResult(data);

    } catch (err) {

      console.log(err);

    }

    setLoading(false);
  }

  return (

    <main style={{
      minHeight: "100vh",
      background: "#0f172a",
      color: "white",
      padding: "40px",
      fontFamily: "Arial"
    }}>

      <div style={{
        maxWidth: "1000px",
        margin: "0 auto"
      }}>

        <h1 style={{
          fontSize: "42px",
          marginBottom: "10px"
        }}>
          AI App Compiler
        </h1>

        <p style={{
          color: "#94a3b8",
          marginBottom: "30px"
        }}>
          Generate application architecture using AI compiler pipelines
        </p>

        <textarea
          rows={6}
          placeholder="Describe your app..."
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          style={{
            width: "100%",
            padding: "20px",
            borderRadius: "12px",
            border: "1px solid #334155",
            background: "#111827",
            color: "white",
            fontSize: "16px",
            outline: "none"
          }}
        />

        <br /><br />

        <button
          onClick={generateApp}
          style={{
            padding: "14px 28px",
            borderRadius: "10px",
            border: "none",
            background: "#2563eb",
            color: "white",
            fontSize: "16px",
            cursor: "pointer"
          }}
        >
          {loading ? "Generating..." : "Generate App"}
        </button>

        <br /><br />

        {result && (

          <div style={{
            marginTop: "30px"
          }}>

            <h2>Generated Output</h2>

            <pre style={{
              background: "#020617",
              color: "#22c55e",
              padding: "24px",
              borderRadius: "14px",
              overflowX: "scroll",
              border: "1px solid #1e293b",
              fontSize: "14px"
            }}>
              {JSON.stringify(result, null, 2)}
            </pre>

          </div>
        )}

      </div>

    </main>
  );
}