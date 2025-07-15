import os
import json
import ollama
import requests

# ===== UTILITY FUNCTIONS ===== #

def extract_username(url):
    """Extracts the Reddit username from a profile URL."""
    return url.rstrip('/').split('/')[-1]

def fetch_user_data(username):
    """Fetches basic user profile and comments data using Reddit's public API."""
    headers = {'User-Agent': 'RedditPersonaGenerator/0.1'}
    
    try:
        # Fetch user about
        about_url = f"https://www.reddit.com/user/{username}/about.json"
        about_res = requests.get(about_url, headers=headers)
        about_data = about_res.json().get('data', {})

        # Fetch user comments
        comments_url = f"https://www.reddit.com/user/{username}/comments.json?limit=10"
        comments_res = requests.get(comments_url, headers=headers)
        comments_data = [c['data']['body'] for c in comments_res.json().get('data', {}).get('children', [])]

        return {
            "about": about_data,
            "recent_comments": comments_data
        }

    except Exception as e:
        print(f"❌ Error fetching Reddit data: {e}")
        return None

def generate_persona(user_data, username):
    """Generates a persona using Ollama (e.g., LLaMA 3 model)."""
    prompt = f"""
You're an AI that creates human-like personas based on Reddit activity.
Generate a persona for the Reddit user '{username}' using the following data:

ABOUT:
{json.dumps(user_data.get("about", {}), indent=2)}

RECENT COMMENTS:
{json.dumps(user_data.get("recent_comments", []), indent=2)}

Write a compelling and accurate persona summary in 200–300 words.
"""
    try:
        response = ollama.chat(
            model='llama3',
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response['message']['content']
    except Exception as e:
        print(f"❌ Ollama error: {e}")
        return None

def save_to_file(username, persona):
    """Saves the generated persona to a text file."""
    os.makedirs("output", exist_ok=True)
    filepath = f"output/{username}_persona.txt"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(persona)
    print(f"✅ Persona saved for {username} at {filepath}")

# ===== MAIN ===== #
if __name__ == "__main__":
    url = input("Enter Reddit profile URL: ").strip()
    username = extract_username(url)
    user_data = fetch_user_data(username)

    if user_data:
        persona = generate_persona(user_data, username)
        if persona:
            save_to_file(username, persona)
        else:
            print("❌ Persona generation failed.")
    else:
        print("❌ No data found for this user.")
