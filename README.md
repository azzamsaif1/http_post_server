# HTTP POST Form Server

A simple HTTP server written in raw Python using sockets.  
This project simulates a basic form submission without using any frameworks like Flask or Django.

---

## Features

- Accepts HTTP GET and POST requests
- Displays a simple HTML form
- Parses POST body data manually
- Returns a dynamic HTML response based on submitted form data

---

## How it Works

1. The browser sends a GET request → server returns a form.
2. When the form is submitted (POST), the server:
   - Parses the raw HTTP request
   - Extracts the `name` value from the body
   - Displays a personalized greeting

---

## Technologies

- Python
- socket module
- HTML (embedded)

---

## Where this can be extended

You can build upon this project by:

- Adding multiple input fields (name, age, email, etc.)
- Validating input data manually
- Saving submitted data to a file or database
- Serving static HTML files instead of embedding HTML in code
- Using this as a base for learning Flask

---

## Getting Started

```bash
python http_post_form_server.py
