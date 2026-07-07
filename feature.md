# AI-UX Tester Features

This document lists the features and configuration requirements for the AI-UX Tester application.

## 🚀 Features

### 1. UX Analysis & Heatmaps
- **Endpoint:** `/generate_heatmap/` (POST)
- **Purpose:** Analyzes Figma designs and generates UX insights, including heatmaps, suggestions, and UX scores.
- **How it works:** Uses Gemini 1.5 Pro (or OpenAI GPT-4 fallback) to process Figma node data and identify usability strengths and weaknesses.

### 2. Figma File Integration
- **Endpoint:** `/fetch_figma_file/` (GET)
- **Purpose:** Retrieves the full JSON structure of a Figma file.
- **Endpoint:** `/fetch_figma_image_urls/` (POST)
- **Purpose:** Fetches high-resolution PNG image URLs for specific Figma nodes.

### 3. UX Simulation
- **Endpoint:** `/generate_simulation/` (POST)
- **Purpose:** Creates a step-by-step visual simulation of a user journey based on Figma prototype interactions.
- **Output:** A JSON script describing cursor movements, click effects, and transition overlays.

### 4. Design Iteration
- **Endpoint:** `/generate_iteration/` (POST)
- **Purpose:** Automatically generates an improved version of a design to fix identified UX drop-off points.
- **How it works:** Uses Gemini 2.0 Flash to "re-imagine" the design while preserving the original style and content.

### 5. Health & Documentation
- **Endpoint:** `/health/` (GET): Returns app status.
- **Endpoint:** `/api-docs/` (GET): Displays interactive API documentation.

---

## 🔐 Configuration & Secrets

To run this application on Hugging Face Spaces, the following environment variables must be set in the **Settings > Secrets** section:

### Mandatory API Keys
| Secret Name | Description |
|-------------|-------------|
| `GLOBAL_SEARCH_API_KEY` | Google Gemini API Key (Main engine for analysis) |
| `OPENAI_API_KEY_SULTAN` | OpenAI API Key (Used as fallback and for simulations) |

### Figma Configuration (Optional for predefined tokens)
| Secret Name | Description |
|-------------|-------------|
| `WAHAB_FIGMA_TOKEN` | Figma Personal Access Token for 'wahab' |
| `RAMSHA_FIGMA_TOKEN` | Figma Personal Access Token for 'ramsha' |
| `FARZAM_FIGMA_TOKEN` | Figma Personal Access Token for 'farzam' |

### Django Security
| Secret Name | Description |
|-------------|-------------|
| `SECRET_KEY` | Django secret key (If not set, a random one is generated) |

---

## 🛠 Programmable Usage

The app can be used programmatically by sending HTTP requests to `https://leon4gr45-ux-mentor.hf.space`.

Example (Python):
```python
import requests

url = "https://leon4gr45-ux-mentor.hf.space/generate_heatmap/"
payload = {
    "figma_data": {...}, # Figma JSON nodes
    "user_prompt": "Focus on mobile responsiveness"
}
response = requests.post(url, json=payload)
print(response.json())
```
