# 🎨 AI Image Generator

> **Type a prompt. Get an image. No API key required.**
> Powered by [DeepAI](https://deepai.org) via browser automation — completely free.

---

## ✨ What Is This?

A desktop application that lets you generate AI images just by describing what you want in plain English. It silently opens a headless browser, feeds your prompt to DeepAI's text-to-image model, downloads the result, and displays it — all without you ever opening a browser yourself.


| Front-end | Tech | Best for |
|---|---|---|
| **GUI App** | Python + Tkinter | Standalone use on Windows |

---

## 🖼️ Preview

---

<img width="702" height="992" alt="image" src="https://github.com/user-attachments/assets/1357467d-ebf5-4eb6-a432-39d0a6969482" />

## 📁 Project Structure

```
folder/
├── generate_image.py      ← Python: image scraper + Tkinter GUI
└── generated.jpg          ← Output (created after first run)
```

---

## 🔧 Requirements

### Python Side

| Package | Purpose | Install |
|---|---|---|
| `playwright` | Headless browser automation | `pip install playwright` |
| `pillow` | Image loading & display in Tkinter | `pip install pillow` |

After installing Playwright, also install the browser:

```bash
playwright install chromium
```



## 🚀 Getting Started

### Option 1 — Python GUI (recommended)

```bash
# Clone or copy the project folder
cd C:\Users\sachin\Documents\coding_c

# Install dependencies
pip install playwright pillow
playwright install chromium

# Launch the GUI
py generate_image.py
```

Type your prompt, hit **GENERATE →** or press `Enter`, and wait ~20–40 seconds for your image.

---

### Option 2 — CLI (Python only, no GUI)

Pass your prompt as a command-line argument:

```bash
py generate_image.py "a samurai fox under cherry blossoms at sunset"
```

The image is saved to `generated.jpg` in the same folder as the script.



## ⚙️ How It Works

```
User types prompt
        │
        ▼
  Tkinter GUI (generate_image.py)
        │
        ▼
  Playwright launches headless Chromium
        │
        ▼
  Navigates to deepai.org/machine-learning-model/text2img
        │
        ▼
  Fills prompt → clicks Generate → waits for result
        │
        ▼
  Grabs image URL from #main-image element
        │
        ▼
  Downloads image → saves as generated.jpg
        │
        ▼
  Tkinter displays image in the GUI window
```

---

## 🧩 Key Design Decisions

**Why browser automation instead of an API?**
DeepAI's free tier doesn't require an account or API key when accessed via the web. Playwright automates exactly what a human would do — making this completely free with no rate-limit worries on your end.

**Why run generation on a background thread?**
Playwright blocks for 20–40 seconds during image generation. Running it on a `threading.Thread` keeps the Tkinter window alive and responsive instead of freezing.


---



## 📝 Notes

- **Internet connection required** — DeepAI's servers do the actual image generation.
- **Generation time** varies from 15 to 60 seconds depending on DeepAI server load.
- **Images are 512×512** by default (DeepAI's free tier output size).
- Each new generation **overwrites** `generated.jpg`. Copy the file elsewhere if you want to keep it.

---

## 📄 License

This project is for personal / educational use. Image generation is handled by [DeepAI](https://deepai.org) — refer to their [Terms of Service](https://deepai.org/terms-of-service) for usage rights on generated images.
