# HelloWorld 🚀

![Build Status](https://github.com/thestrid3r/HelloWorld/actions/workflows/build-and-push.yml/badge.svg)

A retro-cosmic Flask web app that uses Redis to count visits and displays the hostname of the container — styled like a broadcast from a 2000s space terminal 👽

---

## 📦 Table of Contents

- [Features](#features)
- [Run with Docker Compose](#run-with-docker-compose)
- [DockerHub Image](#dockerhub-image)
- [Security Built In](#security-built-in)
- [Tech Stack](#tech-stack)
- [Preview](#preview)
- [License](#license)

---

## 🌌 Features

- 🌠 Flask app that:
  - Shows number of visits using Redis
  - Displays the hostname of the running container
  - Rotates randomly through cosmic quotes (Carl Sagan + others)
- 🖥️ Terminal-style UI with:
  - Animated starfield background
  - Typing sound effects
  - Monospace green-on-black retro design
- 🐳 Fully containerized with Docker and Docker Compose
- 🔀 Supports multi-arch Docker builds (`linux/amd64`, `linux/arm64`)
- 🛡️ Secured with DevSecOps pipeline:
  - Trivy vulnerability scanning
  - Syft SBOM generation
  - Cosign image signing

---

## 🐳 Run with Docker Compose

To build and run the app locally:

```bash
docker-compose up --build -d
# or
docker-compose up --build
