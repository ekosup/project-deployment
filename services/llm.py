import requests


def dummy_llm_response(prompt: str, mode: str = "dummy") -> str:
    prompt_lower = prompt.lower()
    if "ringkas" in prompt_lower:
        return (
            "Ringkasan: performa layanan stabil, fokus perbaikan pada unit dengan SLA rata-rata tertinggi "
            "dan kepuasan terendah."
        )
    if "rekomendasi" in prompt_lower:
        return (
            "Rekomendasi: 1) tambah validasi input, 2) buat alert SLA, 3) aktifkan log audit API, "
            "4) siapkan fallback endpoint."
        )
    return (
        f"[Simulasi {mode}] Prompt diterima: '{prompt}'. "
        "Gunakan kata 'ringkas' atau 'rekomendasi' untuk output khusus."
    )


def call_generic_endpoint(url: str, prompt: str, api_key: str, timeout: int) -> str:
    headers = {"Content-Type": "application/json"}
    if api_key.strip():
        headers["Authorization"] = f"Bearer {api_key.strip()}"

    payload = {
        "prompt": prompt,
        "temperature": 0.2,
        "max_tokens": 300,
    }

    response = requests.post(url, json=payload, headers=headers, timeout=timeout)
    response.raise_for_status()
    body = response.json()

    if isinstance(body, dict):
        for candidate in ["response", "output", "text", "answer"]:
            if candidate in body and body[candidate]:
                return str(body[candidate])
    return str(body)
