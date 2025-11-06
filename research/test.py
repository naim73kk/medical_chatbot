import os
from openai import OpenAI, AuthenticationError, APIConnectionError, RateLimitError

# === Step 1: Set your OpenRouter API key here (or use env var) ===
os.environ["OPENROUTER_API_KEY"] = "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"

api_key = os.getenv("OPENROUTER_API_KEY")

# === Step 2: Verify that the key exists ===
if not api_key:
    print("❌ No OpenRouter API key found. Please set OPENROUTER_API_KEY.")
    exit(1)

# === Step 3: Initialize the OpenRouter client ===
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# === Step 4: Send a small test message ===
try:
    response = client.chat.completions.create(
        model="openrouter/auto",  # or a specific model from OpenRouter
        messages=[
            {"role": "user", "content": "Say 'OK, OpenRouter works' in one short sentence."}
        ],
        max_tokens=32,  # 🔴 IMPORTANT: must be >= 16 for some providers
    )
    print("✅ API key is valid. Response:")
    print(response.choices[0].message.content)

except AuthenticationError:
    print("❌ Invalid or unauthorized OpenRouter API key.")
except RateLimitError:
    print("⚠️ Rate limit or free quota exceeded. Try again later or change model.")
except APIConnectionError:
    print("⚠️ Network connection error. Check your internet connection.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")