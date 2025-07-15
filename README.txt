 Reddit Persona Generator (with Ollama + LLaMA 3)

This project creates detailed, human-like persona summaries for Reddit users using their public profiles and recent comments. It leverages the power of **LLaMA 3 via Ollama** to generate insightful descriptions.

---

## 🔧Features

- ✅ Extracts Reddit **username**, **karma**, **profile details**, and recent **comments**
- ✅ Sends data to **LLaMA 3** using **Ollama**
- ✅ Generates a natural-language **persona summary**
- ✅ Saves results to `.txt` in a structured `output/` folder

---


### 1. Clone the repository


```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt`:
```txt
requests
ollama
```

### 3. Set up Ollama

1. Download Ollama: [https://ollama.com/download](https://ollama.com/download)  
2. Start the Ollama server:

```bash
ollama serve
```

3. Pull the LLaMA 3 model (if you haven’t already):

```bash
ollama pull llama3
```

---

##  How It Works

1. **Input:** Enter a Reddit profile URL (e.g. `https://www.reddit.com/user/spez`)
2. **Scraping:** The script fetches the user's profile info + recent comments using Reddit’s public API
3. **AI Generation:** The data is passed to LLaMA 3 via Ollama to craft a persona summary
4. **Output:** The result is saved as a text file in the `output/` directory

---

## Folder Structure

```
reddit-persona-generator/
│
├── main.py             # Main execution script
├── requirements.txt    # Required packages
├── output/             # Folder for saved persona summaries
└── README.md           # Project documentation
```

---

##  Example Output

Sample output: `output/kojied.txt`

```txt
Meet u/kojied, a seasoned Redditor with a knack for sharing valuable insights and experiences within their community. 
With over 2,000 karma points, this user has established themselves as a trusted voice among fellow enthusiasts.
----
---
---

## ▶️ Running the Tool

```bash
python main.py
```

You'll be asked to input a Reddit profile URL — the script takes care of the rest.

---


- This tool uses Reddit’s **public API** (no authentication needed).
- Personas are fictional summaries derived from limited public data.
- Use ethically and for non-commercial purposes only.

---

##  Acknowledgements

- 🧠 AI powered by [Ollama](https://ollama.com/) & [LLaMA 3](https://ollama.com/library/llama3)
- 📡 Reddit data fetched via their public API

---

