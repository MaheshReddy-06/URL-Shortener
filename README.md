# URL-Shortener

A simple and fast URL shortener built using **Python and Django**. This project allows users to convert long URLs into shorter, more manageable links, making them easier to share, tweet, or send via email.

## Introduction

The **URL Shortener** is a web application that converts long URLs into short URLs using a **custom alias** provided by the user. Instead of using a randomly generated short link, users can choose an alias that is easy to remember.

For example:

**Original URL:**
```text
https://www.example.com/very/long/url
```

**Custom Alias:**
```text
example
```

**Short URL:**
```text
http://127.0.0.1:8000/s/example/
```

## Use Case

This project is useful when long URLs need to be made shorter, simpler, and easier to share. Custom aliases make the generated URLs more memorable and readable.

The URL Shortener can be useful for:

- Sharing links
- Social media
- Emails
- Documents and presentations
- Websites and blogs
- Creating memorable links

## Workflow
=======
# 🔗 URL Shortener

## Introduction

The **URL Shortener** is a web application developed using **Python and Django** that converts long URLs into short, easy-to-share links. Users can create a **custom alias** for their shortened URL instead of relying on automatically generated random links.

For example:

**Original URL:**  
`https://www.example.com/very/long/url`

**Short URL:**  
`http://127.0.0.1:8000/s/example/`

## 💡 Use Case

This project is useful when a long URL needs to be made shorter, simpler, and easier to share. Custom aliases also make URLs more memorable and readable. It can be useful for sharing links through social media, documents, presentations, websites, and other online platforms.

## 🔄 Workflow
>>>>>>> 56c73270a51288c1bcba2b6c19e9438507cf437a

```text
User
  │
  ▼
Enter Original URL
  │
  ▼
Enter Custom Alias
  │
  ▼
Submit
  │
  ▼
Django receives the data
  │
  ▼
Check whether alias already exists
  │
  ├── Yes ──► Show "Alias Already Taken"
  │
  └── No
       │
       ▼
   Save URL + Alias
       │
       ▼
   Generate Short URL
       │
       ▼
   Display Short URL
       │
       ▼
   User opens Short URL
       │
       ▼
   Django finds the alias
       │
       ▼
   Retrieve Original URL
       │
       ▼
   Redirect User
```

<<<<<<< HEAD
## Author

**Mahesh Reddy**

## Conclusion

The **URL Shortener** provides a simple and efficient way to create short URLs using custom aliases. The project demonstrates how Django can handle user input, validate aliases, store URL mappings, generate short links, and redirect users to the original URLs.
=======
## 👨‍💻 Author

**Mahesh Reddy**

## ✅ Conclusion

The **URL Shortener** provides a simple and efficient way to create short URLs with custom aliases. The project demonstrates how Django can handle user input, validate aliases, store URL mappings, generate short links, and redirect users to the original URLs.
>>>>>>> 56c73270a51288c1bcba2b6c19e9438507cf437a
