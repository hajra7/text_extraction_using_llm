from openai import OpenAI
from dotenv import load_dotenv
import os, json
from pathlib import Path

# ---- Config ----
load_dotenv()

PROVIDER = (os.getenv("PROVIDER") or "openai").lower()   # "openai" or "gemini"
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

if PROVIDER == "openai":
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Set OPENAI_API_KEY in .env")
    client = OpenAI(api_key=api_key)  # default OpenAI base_url
    model = OPENAI_MODEL

elif PROVIDER == "gemini":
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Set GEMINI_API_KEY in .env")
    # Gemini’s OpenAI-compatible endpoint
    client = OpenAI(
        api_key=api_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )
    model = GEMINI_MODEL
else:
    raise ValueError("PROVIDER must be 'openai' or 'gemini'")

# ---- Inference ----
text = input("Enter a sentence: ").strip()


resp = client.chat.completions.create(
    model=model,
    temperature=0,
    messages=[
        {
            "role": "system",
            "content": (
                "Extract ONLY food and drink names from the user's text. "
                "Return a strict JSON list of strings (e.g., [\"김치찌개\",\"불고기\"]). "
                "No extra words."
            ),
        },
        {"role": "user", "content": text},
    ],
)

content = resp.choices[0].message.content

# Parse JSON, with fallback
try:
    parsed = json.loads(content)
    print("Foods found:", parsed)
except json.JSONDecodeError:
    # Fall back to raw content (still useful)
    print("Foods found (raw):", content)

output_dir = Path("food_outputs")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "extracted_foods.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(parsed, f, ensure_ascii=False, indent=2)

