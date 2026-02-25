# AI Email Generator

An AI-powered Streamlit application that generates professional emails based on a topic, sender, recipient, and writing style — powered by Azure OpenAI.

---

## Overview

This tool allows users to quickly generate well-structured emails by providing a topic, sender and recipient names, and selecting a writing style. Azure OpenAI handles the content generation, adapting the tone and language to match the chosen style.

---

## Features

-  AI-generated emails tailored to your topic
-  Multiple writing styles (Formal, Appreciating, Not Satisfied, Neutral)
-  Customizable sender and recipient names
-  Instant email generation with a single click
-  Clean and minimal Streamlit UI

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| LLM | Azure OpenAI (Chat model) |
| Prompt Orchestration | LangChain Core (`ChatPromptTemplate`) |

---

## Project Structure
```
├── app.py              # Main Streamlit app with email generation logic
├── requirements.txt    # Python dependencies
└── README.md
```

---

## Prerequisites

- Python 3.9+
- An [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service) account with a chat model deployment (e.g., `gpt-4o` or `gpt-35-turbo`)

---

## Installation

**1. Clone the repository**
```bash
git clone <your-repo-url>
cd <repo-folder>
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure secrets**

Create a `.streamlit/secrets.toml` file in the project root:
```toml
AZURE_OPENAI_ENDPOINT   = "https://your-resource.openai.azure.com/"
AZURE_OPENAI_API_KEY    = "your-azure-openai-api-key"
AZURE_OPENAI_DEPLOYMENT = "your-chat-deployment-name"
```

---

## Usage

**1. Run the app**
```bash
streamlit run app.py
```

**2. In the browser UI:**
- Enter the **email topic** in the text area
- Enter the **Sender Name**
- Enter the **Recipient Name**
- Select a **Writing Style** from the dropdown
- Click **"Generate"**

**3. Results:** A fully composed email is displayed instantly on the page.

---

## Writing Styles

| Style | Description |
|---|---|
| Formal | Professional and structured tone |
| Appreciating | Warm and grateful tone |
| Not Satisfied | Assertive and critical tone |
| Neutral | Balanced and objective tone |

---

## How It Works
```
User Input (Topic + Sender + Recipient + Style)
            ↓
  ChatPromptTemplate → Builds Structured Prompt
            ↓
  Azure OpenAI → Generates Email Content
            ↓
    Display in Streamlit UI
```

1. The user provides an email topic, sender/recipient names, and selects a writing style.
2. A `ChatPromptTemplate` constructs the prompt with a system message and human message.
3. Azure OpenAI generates a complete email tailored to the inputs.
4. The generated email is displayed directly in the Streamlit UI.

---

## Notes

> - `temperature` is set to `0.9` for varied and creative outputs — lower it in `app.py` for more consistent results.
> - The system prompt instructs the model to act as a professional email writing assistant.
> - No email is actually sent — the app only generates the email text for you to copy and use.

---
End of Documentation
---
