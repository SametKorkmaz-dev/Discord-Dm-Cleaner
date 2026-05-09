# Discord-Dm-Cleaner


#Discord-DM-Cleaner 🧹

 DM Cleaner is a Python-based automation tool that helps you safely and efficiently clean up your Discord direct messages (DMs) in bulk.

## Usage 🛠️

This tool is designed to help users manage their own data and reduce their digital footprint more easily.

## Requirements ⚡

* **OS:** Windows 10/11
* **Python:** 3.9 or higher

### Modules:

```bash
pip install requests
```

## How to use? ❄️

1. Make sure Python is installed.
2. Open Terminal (CMD/PowerShell).
3. Navigate to the project folder and run:

```bash
python DmCleaner.py
```

4. Enter the requested Discord Token and Target ID information.

---

## 📌 What is a Discord Token?

A Discord Token is the digital key to your account. It allows you to log in and perform actions through the Discord API.

**Warning:** Never share your token with anyone. If someone gains access to it, they can take control of your account.

---

## 🌐 How DM Cleaning Works

* The tool connects to the Discord API using the token you provide.
* It scans the message history between you and the specified user ID.
* It identifies and deletes only the messages sent by you, one by one.
* Built-in rate limit protection ensures actions are performed at safe intervals.

---

## ⚙️ Why It's Useful

* **Privacy:** Quickly clean old conversations instead of deleting them manually.
* **Automation:** Eliminates the hassle of deleting messages one by one.
* **Control:** Only interacts with your own messages, preserving conversation integrity.

---

## ⚠️ Security & Risks

### Self-Botting

Discord may consider automated account activity (self-botting) a violation of its Terms of Service. Using this tool may put your account at risk.

### Rate Limits

Performing actions too quickly can lead to temporary restrictions. For this reason, the tool includes safe delay intervals.

---

## 🛡️ How to Stay Safe

* Only use trusted and open-source tools.
* Enter your token at runtime instead of hardcoding it into the script.
* Always enable Two-Factor Authentication (2FA).

---

## 🧪 Educational Purpose

This project was created for educational purposes to demonstrate API integration and automation logic. It aims to help users understand how web protocols and automated data management work.

---

## ⚖️ Legal Notice

This tool should only be used to clean your own messages. Any unauthorized access or misuse is entirely the user's responsibility. The developer cannot be held responsible for account restrictions or penalties that may occur.
