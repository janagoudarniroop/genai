import json
import requests

def load_json_input():
    print("Paste your JSON input (single or multiline). Press Enter twice to finish:")
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        except EOFError:
            break
    try:
        data = json.loads("\n".join(lines))
        print("\n✅ Valid JSON detected.\n")
        return data
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return None

def ask_ollama_from_json(json_data):
    prompt = f"You're an expert endurance and sports coach. Here's a structured training request:\n{json.dumps(json_data, indent=2)}\n\nPlease generate a personalized 6-week endurance training plan based on this."
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        result = response.json()

        if "response" in result:
            return result["response"]
        else:
            print("⚠️ Full response from Ollama:")
            print(json.dumps(result, indent=2))
            return "⚠️ Unexpected response structure."
    except Exception as e:
        return f"⚠️ Error: {e}"

if __name__ == "__main__":
    json_data = load_json_input()
    if json_data:
        result = ask_ollama_from_json(json_data)
        print("\n🤖 Ollama Response:\n")
        print(result)

