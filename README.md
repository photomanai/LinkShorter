# LinkShorter

LinkShorter is a lightweight, fast, and efficient URL shortening service built with **Python**, **Flask**, and **Redis**. It allows users to generate short aliases for long URLs with optional expiration times (1 hour, 1 day, 1 week, 1 month, or permanent).

## 🚀 Features

* **Custom Expiration:** Choose how long your links stay active.
* **Unique ID Generation:** Uses a collision-resistant random string generator.
* **Fast Performance:** Powered by Redis for high-speed key-value lookups.
* **Intermediate Landing Page:** Includes a "Go" page to redirect users safely.
* **Dynamic Host Detection:** Works out of the box on local or production environments.

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **Database:** Redis
* **Frontend:** HTML/Jinja2 templates

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

* Python 3.8 or higher
* Redis Server (Running on `localhost:6379`)

## 🔧 Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/photomanai/LinkShorter.git
cd LinkShorter

```


2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install flask redis

```


4. **Ensure Redis is running:**
```bash
# Example for Linux/macOS
redis-server

```


5. **Run the application:**
```bash
python app.py

```


The application will be available at `http://127.0.0.1:5000/panel`.

## 🖥️ Usage

1. Navigate to the `/panel` route.
2. Enter your long URL.
3. Select an expiration period.
4. Click "Shorten" and receive your unique link.
5. Share the generated link (e.g., `/go/abc12`).

## 📁 Project Structure

```text
LinkShorter/
├── app.py              # Main Flask application logic
├── templates/
│   ├── panel.html      # Dashboard for creating links
│   └── go.html         # Redirection/Intermediate page
├── README.md           # Documentation
└── .gitignore          # Files to ignore in Git

```

## ⚖️ License

This project is licensed under the **MIT License**. See the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.

---

### 📝 Note

> **Note:** This code and documentation were generated with the assistance of **AI**.
