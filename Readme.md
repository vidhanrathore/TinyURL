# TinyURL Generator Project

## ✨ Project Overview
This is a full-stack web application that allows users to shorten long URLs into tiny URLs with an optional custom alias. Built using Flask, MySQL (remote DB via PyMySQL), and Bootstrap 5, the app generates, stores, and manages short URL redirections.

---

## 🔧 Tech Stack
- **Backend**: Python (Flask)
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Database**: MySQL (hosted remotely, accessed via `pymysql`)
- **ORM/Connector**: PyMySQL
- **Deployment**: [Render.com](https://render.com/)

---

## 📂 Project Structure




---

## ⚙️ Features & Functions

### `/ (GET, POST)` - `index()`
- Displays the form to enter a long URL.
- Accepts optional fields:
  - **Length**: Controls random short code length.
  - **Alias**: Custom alias instead of random code.
- Stores in the database and flashes back the short URL.

### `/<short_code>` - `redirect_to_long_url()`
- Redirects to the original long URL if the code exists.
- Returns `404` if code not found.

### `generate_short_code(length)`
- Randomly creates a unique alphanumeric short code.

### `get_db_connection()`
- Establishes connection to a remote MySQL DB using PyMySQL.

---

## Future Enhancements
- User authentication (to manage personal links)
- Analytics (click count per short URL)
- Expiry for temporary short URLs
- API endpoints for programmatic use
