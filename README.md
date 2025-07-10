# 🚀 SnapURL - URL Shortener Microservice Project

SnapURL is a scalable, modular, and containerized microservice-based **URL shortening system** similar to Bit.ly or TinyURL. It provides a simple and efficient way to shorten long URLs and redirect to the original link using FastAPI and Docker.

---

## ✨ Features

- 🔗 **Shorten Long URLs** using a base62 algorithm
- ↪️ **Redirection Service** for resolving shortened URLs
- 🗃️ **Persistent Storage** via Redis
- 🧱 **Microservice Architecture** with Docker Compose
- 🌐 **API Gateway** for unified access
- 💡 **Health Check Endpoints** for all services
- ⚙️ **Pluggable Slug Strategy** (Base62, Random, Hash, etc.)

---

## 🗂️ Project Structure
```plaintext
SnapURL/
├── api-gateway/ # API Gateway that forwards requests to services
│ └── main.py
│
├── shortener/ # Microservice to generate short codes
│ ├── main.py
│ ├── service/
│ │ └── shortner_service.py
│ └── strategies/
│ ├── base.py
│ └── base62.py
│
├── redirector/ # Microservice to redirect shortened codes
│ └── main.py
│
├── url-storage/ # Microservice to interact with Redis for storing links
│ └── main.py
│
├── docker-compose.yml # Docker setup for all services
└── README.md # Project documentation
```
---

## 🛠️ Technologies Used

- **Python 3.11**
- **FastAPI**
- **Redis**
- **Docker + Docker Compose**
- **HTTPX** for service communication

---

## 🌐 Microservice Communication

All microservices are isolated in their own containers and communicate via Docker's internal DNS.

### 🔄 Flow of Data

1. **User hits `/shorten?url=<long-url>` via API Gateway**
2. API Gateway forwards it to `shortener` service
3. `shortener` generates a slug and calls `url-storage` to persist the mapping
4. The shortened code is returned to the user

5. When user visits `/R3v1ON`, API Gateway routes it to `redirector`
6. `redirector` fetches the original URL from `url-storage` and redirects

---

## 🖼️ High-Level Design

```plaintext
                             +----------------+
                             |     Client     |
                             +--------+-------+
                                      |
                                      ▼
                         +------------+------------+
                         |      API Gateway        |
                         +------------+------------+
                                      |
        +-----------------------------+-----------------------------+
        |                                                           |
        ▼                                                           ▼
+-------------------+                                  +----------------------+
|   Shortener Svc   | ----> Generates slug             |   Redirector Svc     |
+-------------------+                                  +----------------------+
        |                                                           |
        | Store slug:url in Redis                                   |
        ▼                                                           ▼
+--------------------------+                           +--------------------------+
|      URL Storage Svc     | <-- GET/POST --> Redis    |      URL Storage Svc     |
+--------------------------+                           +--------------------------+

```
<img width="1536" height="1024" alt="ChatGPT Image Jul 10, 2025, 05_31_11 PM" src="https://github.com/user-attachments/assets/82c9ba74-65f7-4ae0-b250-79f40bbd5a42" />
---
📦 Running the Project

Prerequisites
 - Docker
 - Docker Compose

Run All Services
```bash

docker compose up --build
```

Then open:

API Gateway: http://localhost:8001

🔌 Example Usage
🔸 Shorten a URL
```bash

curl -X POST "http://localhost:8001/shorten?url=https://github.com"
```
🔹 Redirect
```bash
curl -I http://localhost:8001/{short_code_of_above_link}
```

❤️ Credits
Developed by Santosh Varma Addala

📜 License
This project is licensed under the MIT License.
