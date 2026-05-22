"use client";
import { useState } from "react";

export default function ChatPage() {
  const [input, setInput] = useState("");
  const [reply, setReply] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;
    setLoading(true);
    setReply("");
    try {
      const res = await fetch("/api/v1/chat/mensaje", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input }),
      });
      if (!res.ok) throw new Error(`Error ${res.status}`);
      const data = await res.json();
      setReply(data.reply);
    } catch (err: any) {
      setReply(err.message || "Error al contactar con la IA");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">INSPOL LEGAL AI</h1>
      <p className="mb-2">Inteligencia Jurídica Mexicana</p>
      <textarea
        className="w-full border p-2 rounded"
        rows={4}
        placeholder="Pregúntale algo a la IA..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button
        className="mt-2 bg-blue-600 text-white px-4 py-2 rounded"
        onClick={sendMessage}
        disabled={loading}
      >
        {loading ? "Enviando..." : "Enviar"}
      </button>
      {reply && (
        <div className="mt-4 p-3 bg-gray-100 rounded">
          <strong>Respuesta:</strong> {reply}
        </div>
      )}
    </div>
  );
}
