"use client";
import { useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";

export default function DocumentView() {
  const searchParams = useSearchParams();
  const id = searchParams.get("id");
  const [content, setContent] = useState("Cargando...");

  useEffect(() => {
    if (id) {
      // Aquí puedes cargar el documento desde el backend si lo deseas
      setContent(`Documento ID: ${id} (simulado)`);
    }
  }, [id]);

  return (
    <div style={{ padding: 20 }}>
      <h1>Vista de Documento</h1>
      <p>{content}</p>
    </div>
  );
}
