# 📥 YouTube Comments Extractor

This is a simple Python script that extracts all top-level comments from a YouTube video using the **YouTube Data API v3**. It fetches comments in batches and saves them to a `.txt` file.

---

## 📌 Features

- Uses official `google-api-python-client`
- Supports pagination to get **all** comments
- Saves comments to `youtube_comments.txt`
- CLI-based with user prompts for API key and video ID

---

## 🛠 Requirements

Install the required package using:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Use

1. Get a YouTube Data API key from [Google Cloud Console](https://console.cloud.google.com/)
2. Run the script:

```bash
python youtube_comments_extractor.py
```

3. Enter:
   - Your **API key**
   - The **YouTube video ID** (e.g. `dQw4w9WgXcQ`)

4. The script will fetch comments and save them to `youtube_comments.txt`

---

## 📂 Output

A file named `youtube_comments.txt` will be created with one comment per line.

---

## ⚠️ Notes

- Only **top-level comments** are fetched (no replies).
- Make sure your API key has quota and YouTube Data API v3 enabled.
- If a video has thousands of comments, it may take a while.

---

## 📄 License

MIT License. Feel free to use, modify, and share.
