"use client";
import { createContext, useContext, useState, useEffect, ReactNode } from "react";

interface User {
  id: number;
  email: string;
  nombre: string;
  apellido?: string;
  rol: "admin" | "abogado" | "asistente";
}

interface AuthContextType {
  user: User | null;
  token: string | null;
  login: (email: string, password: string) => Promise<void>;
  register: (data: { email: string; password: string; nombre: string; apellido?: string }) => Promise<void>;
  logout: () => void;
  isLoading: boolean;
}

const AuthContext = createContext<AuthContextType>({
  user: null,
  token: null,
  login: async () => {},
  register: async () => {},
  logout: () => {},
  isLoading: true,
});

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [token, setToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Usuario demo automático
    setUser({
      id: 1,
      email: "demo@inspol.com",
      nombre: "Demo",
      rol: "admin",
    });
    setToken("demo");
    setIsLoading(false);
  }, []);

  const login = async () => {};
  const register = async () => {};
  const logout = () => {
    setUser({
      id: 1,
      email: "demo@inspol.com",
      nombre: "Demo",
      rol: "admin",
    });
    setToken("demo");
  };

  return (
    <AuthContext.Provider value={{ user, token, login, register, logout, isLoading }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);
