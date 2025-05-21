# Chat-backup-self-bot

This bot automatically backs up all incoming private messages to a Telegram channel, including the sender's full name, username, and user ID.

<h2> EN </h2>
-----
This bot automatically **backs up all incoming private messages** to a **Telegram channel**, including the sender’s:

* 👤 **Full name**
* 🪪 **Username**
* 🆔 **User ID**

Messages are sent with these details to a backup channel in real-time.

---

## 📋 Requirements

* A Telegram **user account** (not a bot token)
* Python 3.7+
* API ID & API Hash from [https://my.telegram.org](https://my.telegram.org)

---

## 📦 Install Required Library

Run this command in your terminal or command prompt:

```bash
pip install telethon
```

---

## ⚙️ How to Use

1. Create a file named `bot.py` and paste the complete bot code inside (the one shared earlier).

2. Replace these values with your own:

```python
api_id = 123456789  # your API ID
api_hash = '------'  # your API Hash
backup_channel = -1122334455  # your backup channel’s numeric ID
```

📌 **How to get your channel's numeric ID:**

* Add the bot [@userinfobot](https://t.me/userinfobot) to your channel as admin.
* Send `/start` and then `/id` to get the numeric ID.
* Channel IDs are negative and start with `-100`.

3. Run the bot:

```bash
python bot.py
```

On first run, you'll be asked to enter your phone number and the login code sent to your Telegram.

---

## ⛓️ Important Notes

* Your account must be a **member and admin** in the backup channel.
* This is a **self-bot** using your **user account**, not a bot token.
* It only backs up messages from **private chats** (not groups, channels, or bots).
* A delay is added between messages to avoid flood errors or bans.
* Only **new messages** received after the bot starts are processed.

---

## 🛡️ Disclaimer

Using this self-bot in violation of Telegram's terms (e.g., scraping without user consent) is unethical and may lead to account restrictions. You are fully responsible for how you use this script.

---

If you'd like to extend the bot to support features like saving to a database, Google Drive uploads, or building a REST API, feel free to ask — I’d be happy to help.





<h2> FA </h2>


---


این ربات به‌صورت **خودکار تمامی پیام‌های خصوصی (PV)** دریافتی شما را در یک **کانال تلگرام** پشتیبان ذخیره می‌کند و مشخصات کامل فرستنده شامل:

* 👤 **نام کامل**
* 🪪 **یوزرنیم**
* 🆔 **آیدی عددی**

را به همراه پیام در آن کانال ارسال می‌کند.

---

## 📋 پیش‌نیازها

* حساب کاربری تلگرام (نه بات)
* Python نسخه ۳.۷ به بالا
* ایجاد API ID و API Hash از سایت [https://my.telegram.org](https://my.telegram.org)

---

## 📦 نصب کتابخانه موردنیاز

در ترمینال یا CMD اجرا کنید:

```bash
pip install telethon
```

---

## ⚙️ نحوه استفاده

۱. فایل `bot.py` را ایجاد کرده و کد کامل ربات را در آن قرار دهید (کدی که قبلاً ارائه شد).

۲. مقدارهای زیر را جایگزین کنید:

```python
api_id = 123456789  # آی‌دی API شما
api_hash = '----------'  # هش API شما
backup_channel = -10012345678  # آیدی عددی کانال مقصد (حتماً عددی و منفی باشد)
```

📌 برای گرفتن آیدی عددی کانال:

* ربات [@userinfobot](https://t.me/userinfobot) را در کانال ادمین کنید.
* در چت با آن بنویسید `/start` و سپس `/id` را بفرستید تا ID را بگیرید.

۳. اجرای ربات:

```bash
python bot.py
```

بار اول از شما شماره تلفن می‌خواهد و کد ورود را از تلگرام‌تان دریافت می‌کنید.

---

## ⛓️ نکات مهم

* باید اکانت شما عضو و ادمین کانال بکاپ باشد.
* این یک **سلف‌بات** است و با حساب کاربری شما کار می‌کند، نه بات‌توکن.
* پیام‌های دریافتی از گروه‌ها، کانال‌ها یا ربات‌ها نادیده گرفته می‌شوند.
* بین ارسال پیام‌ها تاخیر وجود دارد تا از Flood جلوگیری شود.
* پیام‌های قبلی ارسال نمی‌شوند، فقط پیام‌های جدیدی که بعد از اجرای ربات دریافت می‌کنید.

---

## 🛡️ مسئولیت استفاده

استفاده نادرست از این ربات (مثلاً برای جمع‌آوری داده کاربران بدون اجازه) برخلاف قوانین تلگرام و اخلاقی است. مسئولیت کامل استفاده بر عهده کاربر می‌باشد.

---

اگر خواستید این ربات را توسعه دهید (مثلاً ذخیره در دیتابیس، ارسال فایل‌ها به گوگل درایو، یا تبدیل به API)، خوشحال می‌شوم کمکتان کنم.

---

