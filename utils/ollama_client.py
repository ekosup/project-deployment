import json
import os
from typing import List
from urllib import error, request

DEFAULT_OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")


class OllamaError(Exception):
    """Raised when Ollama API calls fail."""


def _post_json(url: str, payload: dict, timeout: int = 60) -> dict:
    data = json.dumps(payload).encode("utf-8")
    req = request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def _get_json(url: str, timeout: int = 15) -> dict:
    req = request.Request(url, method="GET")
    with request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def list_models(host: str = DEFAULT_OLLAMA_HOST) -> List[str]:
    try:
        payload = _get_json(f"{host.rstrip('/')}/api/tags")
        return [model.get("name", "") for model in payload.get("models", []) if model.get("name")]
    except (error.URLError, error.HTTPError, TimeoutError, json.JSONDecodeError) as exc:
        raise OllamaError(f"Tidak bisa mengambil daftar model dari Ollama: {exc}") from exc


def generate_text(prompt: str, model: str, host: str = DEFAULT_OLLAMA_HOST, timeout: int = 60) -> str:
    if not prompt.strip():
        raise OllamaError("Prompt tidak boleh kosong.")

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
    }

    try:
        data = _post_json(f"{host.rstrip('/')}/api/generate", payload, timeout=timeout)
    except error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="ignore")
        raise OllamaError(f"HTTP error dari Ollama: {exc.code} {detail}") from exc
    except (error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        raise OllamaError(f"Gagal menghubungi Ollama di {host}: {exc}") from exc

    response_text = data.get("response", "").strip()
    if not response_text:
        raise OllamaError("Ollama tidak mengembalikan respons teks.")

    return response_text
