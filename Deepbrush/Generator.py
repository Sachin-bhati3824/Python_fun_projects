import asyncio
from playwright.async_api import async_playwright
import time
import sys
import os
import urllib.request
import threading
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

import subprocess
import sys
import os

def ensure_playwright():
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            p.chromium.launch()
    except Exception:
        print("Installing Playwright browsers...")
        subprocess.run([sys.executable, "-m", "playwright", "install","chromium"])

ensure_playwright()



# ── Output path: same folder as this script ──────────────────────────────────
SCRIPT_DIR  = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "generated.jpg")


# ── Core async scraper (unchanged logic) ─────────────────────────────────────
async def generate_image_async(prompt: str) -> str:
    """Scrape DeepAI, download the result, return the saved path."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page    = await browser.new_page()

        await page.goto("https://deepai.org/machine-learning-model/text2img")
        await page.fill(
            'textarea[placeholder="Describe what you\'d like to generate"]',
            prompt,
        )
        await page.get_by_role("button", name="Generate").click()

        download_btn = page.locator('button#download-button[imagewasgenerated="True"]')
        await download_btn.wait_for(state="visible")

        image_loc = page.locator("#main-image")
        await image_loc.wait_for(state="visible")
        time.sleep(5)
        await image_loc.wait_for(state="visible")

        image_url = await image_loc.get_attribute("src")
        urllib.request.urlretrieve(image_url, OUTPUT_PATH)
        await browser.close()

    return OUTPUT_PATH


# ── Tkinter UI ────────────────────────────────────────────────────────────────
class App(tk.Tk):
    # ── palette / sizes ───────────────────────────────────────────────────────
    BG          = "#0d0d0d"
    SURFACE     = "#161616"
    SURFACE2    = "#1f1f1f"
    ACCENT      = "#c8ff00"          # electric lime
    ACCENT_DIM  = "#8fb300"
    FG          = "#f0f0f0"
    FG_DIM      = "#888888"
    FONT_TITLE  = ("Georgia", 22, "bold")
    FONT_LABEL  = ("Courier New", 10)
    FONT_BTN    = ("Courier New", 11, "bold")
    FONT_STATUS = ("Courier New", 9)
    IMG_W       = 512
    IMG_H       = 512

    def __init__(self):
        super().__init__()
        self.title("AI Image Generator")
        self.configure(bg=self.BG)
        self.resizable(False, False)

        # internal state
        self._photo_ref = None          # keep a reference so GC won't collect it
        self._generating = False

        self._build_ui()
        self._center_window()

    # ── layout ────────────────────────────────────────────────────────────────
    def _build_ui(self):
        pad = dict(padx=24)

        # title bar
        title_frame = tk.Frame(self, bg=self.BG)
        title_frame.pack(fill="x", pady=(28, 0), **pad)

        tk.Label(
            title_frame, text="Deepbrush", font=self.FONT_TITLE,
            bg=self.BG, fg=self.ACCENT,
        ).pack(side="left")

        tk.Label(
            title_frame, text="powered by DeepAI", font=self.FONT_STATUS,
            bg=self.BG, fg=self.FG_DIM,
        ).pack(side="right", anchor="s", pady=(0, 4))

        # thin accent line
        tk.Frame(self, bg=self.ACCENT, height=2).pack(fill="x", padx=24, pady=(10, 20))

        # prompt label
        tk.Label(
            self, text="ENTER PROMPT", font=self.FONT_LABEL,
            bg=self.BG, fg=self.FG_DIM, anchor="w",
        ).pack(fill="x", **pad)

        # prompt entry row
        entry_frame = tk.Frame(self, bg=self.SURFACE2, highlightbackground=self.ACCENT,
                               highlightthickness=1)
        entry_frame.pack(fill="x", padx=24, pady=(6, 0))

        self.prompt_var = tk.StringVar()
        self.entry = tk.Entry(
            entry_frame, textvariable=self.prompt_var,
            font=("Courier New", 12),
            bg=self.SURFACE2, fg=self.FG, insertbackground=self.ACCENT,
            relief="flat", bd=0,
        )
        self.entry.pack(side="left", fill="x", expand=True, padx=12, pady=10)
        self.entry.bind("<Return>", lambda _e: self._on_generate())

        # generate button
        self.btn = tk.Button(
            entry_frame, text="GENERATE →", font=self.FONT_BTN,
            bg=self.ACCENT, fg="#000000", activebackground=self.ACCENT_DIM,
            activeforeground="#000000", relief="flat", bd=0, cursor="hand2",
            padx=18, pady=0,
            command=self._on_generate,
        )
        self.btn.pack(side="right", fill="y")

        # image canvas
        canvas_frame = tk.Frame(self, bg=self.SURFACE, highlightbackground="#333",
                                highlightthickness=1)
        canvas_frame.pack(padx=24, pady=18)

        self.canvas = tk.Canvas(
            canvas_frame, width=self.IMG_W, height=self.IMG_H,
            bg=self.SURFACE, highlightthickness=0,
        )
        self.canvas.pack()
        self._draw_placeholder()

        # status bar
        self.status_var = tk.StringVar(value="Ready.")
        tk.Label(
            self, textvariable=self.status_var, font=self.FONT_STATUS,
            bg=self.BG, fg=self.FG_DIM, anchor="w",
        ).pack(fill="x", padx=24, pady=(0, 20))

    def _draw_placeholder(self):
        """Draw a dark placeholder with crosshair lines."""
        self.canvas.delete("all")
        w, h = self.IMG_W, self.IMG_H
        self.canvas.create_rectangle(0, 0, w, h, fill=self.SURFACE, outline="")
        # dashed cross
        dash = (6, 6)
        self.canvas.create_line(w//2, 0, w//2, h,
                                fill="#2a2a2a", dash=dash)
        self.canvas.create_line(0, h//2, w, h//2,
                                fill="#2a2a2a", dash=dash)
        self.canvas.create_text(
            w//2, h//2, text="image will appear here",
            fill="#333333", font=("Courier New", 11),
        )

    # ── generation flow ───────────────────────────────────────────────────────
    def _on_generate(self):
        if self._generating:
            return
        prompt = self.prompt_var.get().strip()
        if not prompt:
            messagebox.showwarning("Empty Prompt", "Please enter a prompt first.")
            return

        self._set_busy(True)
        self._draw_placeholder()
        self.status_var.set("⏳  Generating — this may take 20–40 seconds…")

        # run async work on a background thread so the UI stays alive
        thread = threading.Thread(target=self._worker, args=(prompt,), daemon=True)
        thread.start()

    def _worker(self, prompt: str):
        """Background thread: run the async scraper, post result to main thread."""
        try:
            path = asyncio.run(generate_image_async(prompt))
            self.after(0, self._on_success, path)
        except Exception as exc:
            self.after(0, self._on_error, str(exc))

    def _on_success(self, path: str):
        try:
            img = Image.open(path).resize((self.IMG_W, self.IMG_H), Image.LANCZOS)
            self._photo_ref = ImageTk.PhotoImage(img)
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, anchor="nw", image=self._photo_ref)
            self.status_var.set(f"✓  Saved → {path}")
        except Exception as exc:
            self._on_error(f"Image load failed: {exc}")
        finally:
            self._set_busy(False)

    def _on_error(self, msg: str):
        messagebox.showerror("Generation Failed", msg)
        self.status_var.set("✗  Generation failed. Check your connection and try again.")
        self._set_busy(False)

    def _set_busy(self, busy: bool):
        self._generating = busy
        if busy:
            self.btn.config(state="disabled", bg=self.ACCENT_DIM, text="WORKING…")
            self.entry.config(state="disabled")
        else:
            self.btn.config(state="normal", bg=self.ACCENT, text="GENERATE →")
            self.entry.config(state="normal")
            self.entry.focus()

    # ── helpers ───────────────────────────────────────────────────────────────
    def _center_window(self):
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        self.geometry(f"+{(sw - w) // 2}+{(sh - h) // 2}")


# ── entry point ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # CLI mode (called from C++ with a prompt argument)
    if len(sys.argv) > 1:
        cli_prompt = " ".join(sys.argv[1:])
        asyncio.run(generate_image_async(cli_prompt))
    # GUI mode
    else:
        app = App()
        app.mainloop()
