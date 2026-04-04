# System Architecture

## High-Level Design

The automation system separates responsibilities into independent components.

### 1. Data Layer
Google Sheets acts as a lightweight database storing:
- Recipient information
- Generated messages
- Execution status

### 2. Workflow Orchestration (n8n)

Responsible for:
- Filtering unsent records
- Looping through entries
- Generating AI content
- Updating workflow state
- Triggering backend execution

### 3. Execution Service (Flask API)

Receives webhook calls with parameters such as:
- batch size
- execution trigger

Responsibilities:
- Process batch requests
- Send emails
- Update execution status

### 4. Communication Layer

SMTP-based email delivery system.

---

## Design Principles

- Idempotency
- Separation of concerns
- Restart-safe workflow
- Controlled automation