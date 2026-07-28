from google import genai

client = genai.Client(api_key="")

SYSTEM_PROMPT = """
You are Study Buddy AI.

Rules:
- Always be friendly.
- Explain programming like the user is a beginner.
- Use simple English.
- Give examples whenever possible.
- Keep answers concise.
"""

print("=" * 40)
print("📚 Welcome to Study Buddy AI")
print("Type 'exit' to quit.")
print("=" * 40)

while True:
    user = input("\nYou: ")

    if user.lower() == "exit":
        print("Goodbye!")
        break

    prompt = f"""
{SYSTEM_PROMPT}

User: {user}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",  # or the model that worked in your test
        contents=prompt
    )

    print("\nStudy Buddy AI:")
    print(response.text)