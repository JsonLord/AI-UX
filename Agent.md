# Deployment Agent Guidelines for `ux-mentor`

This file informs further agents about tricks and ongoing deployment best practices for the `ux-mentor` Space.

## 1. Deployment Configuration

### Target Space
- **Profile:** `Leon4gr45`
- **Space:** `ux-mentor`
- **Full Identifier:** `Leon4gr45/ux-mentor`
- **Frontend Port:** `7860` (mandatory for all Hugging Face Spaces)

### Deployment Method
- **SDK:** `docker` (chosen for maximum flexibility)

### HF Token
- The environment variable **`HF_TOKEN`** is used for deployment and monitoring.
- Never hardcode the token in the codebase.

### Required Files
- `Dockerfile`
- `README.md` with Hugging Face YAML frontmatter:
  ```yaml
  ---
  title: AI-UX Tester
  sdk: docker
  app_port: 7860
  ---
  ```
- `.hfignore` to exclude unnecessary files
- `Agent.md` (this file)

---

## 2. API Exposure and Documentation

### Mandatory Endpoints
Every deployment **must** expose:

- **`/health`**
  - Returns HTTP 200 when the app is ready.
  - Required for Hugging Face to transition the Space from *starting* → *running*.

- **`/api-docs`**
  - Documents **all** available API endpoints.
  - Reachable at: `https://Leon4gr45-ux-mentor.hf.space/api-docs`

### Functional Endpoints

#### `/`
- Method: GET
- Purpose: Landing page

#### `/upload_design/`
- Method: GET/POST
- Purpose: Main interface for uploading designs or providing Figma links for analysis.

#### `/health`
- Method: GET
- Purpose: Health check
- Response: `{"status": "ok"}`

#### `/api-docs`
- Method: GET
- Purpose: API documentation

---

## 3. Deployment Workflow

### Standard Deployment Command
```bash
hf upload Leon4gr45/ux-mentor --repo-type=space
```

### Monitoring Logs
- **Build Logs:**
  ```bash
  curl -N -H "Authorization: Bearer <TOKEN>" "https://huggingface.co/api/spaces/Leon4gr45/ux-mentor/logs/build"
  ```
- **Run Logs:**
  ```bash
  curl -N -H "Authorization: Bearer <TOKEN>" "https://huggingface.co/api/spaces/Leon4gr45/ux-mentor/logs/run"
  ```

### Troubleshooting
- If logs indicate `sqlite3.OperationalError`, ensure the database file and directory are writable by the container user.
- Ensure `ALLOWED_HOSTS` in Django settings includes the HF Space domain or `*`.
