from __future__ import annotations

import requests


DEFAULT_OLLAMA_HOST = "http://localhost:11434"


class OllamaError(Exception):
    """Raised when Ollama API calls fail."""


def list_models(host: str = DEFAULT_OLLAMA_HOST) -> list[str]:
    url = f"{host.rstrip('/')}/api/tags"

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
    except requests.Timeout as exc:
        raise OllamaError("Request daftar model ke Ollama timeout.") from exc
    except requests.RequestException as exc:
        detail = ""
        if exc.response is not None:
            detail = f" - {exc.response.text}"
        raise OllamaError(f"Gagal mengambil daftar model Ollama{detail}") from exc

    try:
        payload = response.json()
        models = payload.get("models", [])
        names = [item["name"] for item in models if isinstance(item, dict) and item.get("name")]
    except (TypeError, ValueError, KeyError) as exc:
        raise OllamaError("Format respons daftar model Ollama tidak valid.") from exc

    return names


def generate_text(prompt: str, model: str, host: str = DEFAULT_OLLAMA_HOST, timeout: int = 60) -> str:
    if not prompt.strip():
        raise OllamaError("Prompt tidak boleh kosong.")

    if not model.strip():
        raise OllamaError("Model Ollama tidak boleh kosong.")

    url = f"{host.rstrip('/')}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }

    try:
        response = requests.post(url, json=payload, timeout=timeout)
        response.raise_for_status()
    except requests.Timeout as exc:
        raise OllamaError("Request generate ke Ollama timeout.") from exc
    except requests.RequestException as exc:
        detail = ""
        if exc.response is not None:
            detail = f" - {exc.response.text}"
        raise OllamaError(f"Gagal memanggil Ollama{detail}") from exc

    try:
        data = response.json()
        result = data.get("response", "")
    except (TypeError, ValueError) as exc:
        raise OllamaError("Format respons generate Ollama tidak valid.") from exc

    if not isinstance(result, str) or not result.strip():
        raise OllamaError("Ollama mengembalikan respons kosong.")

    return result
