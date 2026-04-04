# AI Outreach Automation System

An AI-driven workflow automation system that generates personalized outreach messages and executes controlled batch communication using workflow orchestration and webhook-based microservices.

---

## 🚀 Overview

This project explores how modern AI systems can be combined with workflow automation tools to build reliable, restart-safe automation pipelines.

The system automatically:

- Reads structured data from Google Sheets
- Filters records based on execution state
- Generates personalized outreach content using an LLM
- Maintains execution status to prevent duplicates
- Triggers a Python backend via webhook
- Sends emails in controlled batches

---

## 🧩 System Architecture

The system follows a microservice-style architecture:

Key design principles:

- Idempotent execution
- Batch control
- State tracking
- Human-in-the-loop optionality
- AI-assisted content generation

---

## ⚙️ Tech Stack

- Python
- Flask
- n8n
- Google Sheets API
- Webhooks
- SMTP Email Automation
- LLM-based Content Generation

---

## 🔥 Key Features

- Stateful workflow automation
- Controlled batch execution
- Resume-safe processing
- Duplicate prevention
- AI-assisted personalization
- Modular backend execution

---

## 📂 Repository Contents

| Folder | Description |
|---|---|
| workflow/ | Example n8n workflow |
| backend/ | Flask webhook server |

---

# Setup Guide

## Requirements

- Python 3.10+
- n8n instance
- Google Cloud credentials
- Gmail App Password

---

## Backend Setup

```bash
pip install flask gspread google-auth pyngrok
```

## 📈 Learning Goals

This project focuses on system orchestration rather than model development, highlighting how real-world AI products integrate multiple services into a unified automation pipeline.

---

## ⚠️ Disclaimer

This repository demonstrates workflow automation architecture for educational purposes only.

---

## 👨‍💻 Author

Sachin Bhati  
B.Tech Computer Science Engineering  
GitHub: https://github.com/Sachin-bhati3824  
LinkedIn: https://www.linkedin.com/in/sachinbhati