# SilenceMonitor

This repository contains a Python script to fetch trending topics on Twitter in Italy and search each trend using the Twitter API. If specific errors, such as those related to blocked searches, are encountered, the script sends a notification via Telegram.

![Logo](./logo.png)

## File Structure

- **`demon.py`**: The main script that handles the entire process, from retrieving trending topics to searching Twitter and sending Telegram notifications if specific errors occur.
- **`twitter_client.py`**: Contains the `TwitterClient` class responsible for communicating with the Twitter API to perform searches and fetch trending topics via web scraping.
- **`config.json`**: A configuration file that stores cookies, headers, and Telegram credentials required to run the script.

## Requirements

Make sure you have Python 3.x installed. To install the necessary dependencies, use `pip`:

```bash
pip install requests beautifulsoup4
```

## Configuration

### config.json

The `config.json` file must contain your Twitter credentials (cookies and headers) and Telegram configuration information. Below is an example:

```json
{
    "cookies": {
        "guest_id": "",  // Twitter guest ID (e.g., "v1%3A169635946273467053")
        "night_mode": "",  // Night mode preference (e.g., "0" for off, "1" for on)
        "twid": "",  // Twitter user ID encoded (e.g., "u%3D174553974")
        "auth_token": "",  // Twitter authentication token
        "ct0": "",  // CSRF token for Twitter
        "d_prefs": "",  // Twitter preference settings
        "guest_id_ads": "",  // Guest ID for ads (same as guest_id)
        "guest_id_marketing": "",  // Guest ID for marketing (same as guest_id)
        "personalization_id": "",  // Personalization ID for Twitter (e.g., ""v1_R3M5M985L3hi8X3TKxe6YA=="")
        "_ga": "",  // Google Analytics ID used by Twitter
        "lang": ""  // Language preference (e.g., "it" for Italian)
    },
    "headers": {
        "User-Agent": "",  // User-Agent string of your browser (e.g., "Mozilla/5.0...")
        "Accept": "*/*",  // Accepted content types (usually leave as "*/*")
        "Accept-Language": "",  // Language preference for your requests (e.g., "it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3")
        "Referer": "",  // Referrer URL (e.g., "https://x.com/search?q=test&src=recent_search_click")
        "content-type": "application/json",  // Content type for the request
        "x-twitter-auth-type": "OAuth2Session",  // Authorization type (usually "OAuth2Session")
        "x-csrf-token": "",  // CSRF token to prevent request forgery
        "x-twitter-client-language": "",  // Client language setting (e.g., "it" for Italian)
        "x-twitter-active-user": "yes",  // Active user flag (usually "yes")
        "x-client-transaction-id": "",  // Transaction ID for tracking requests
        "Sec-Fetch-Dest": "empty",  // Security fetch destination (usually "empty")
        "Sec-Fetch-Mode": "cors",  // Security fetch mode (usually "cors")
        "Sec-Fetch-Site": "same-origin",  // Security fetch site (usually "same-origin")
        "authorization": "",  // Bearer token for OAuth2 authentication
        "Connection": "keep-alive"  // Connection type (usually "keep-alive")
    },
    "telegram_token": "",  // Your Telegram bot token
    "telegram_chat_id": ""  // Your Telegram chat ID where you want to receive notifications
}
```

### Filling out the `config.json`

1. **Cookies**:
   - Gather these values from your browser while logged in to Twitter.
   - Use tools like the browser's DevTools to access the cookies.

2. **Headers**:
   - These can also be obtained via DevTools while making a request on Twitter.
   - Ensure to copy the exact `User-Agent` and `authorization` (Bearer token) for proper authentication.

3. **Telegram**:
   - **telegram_token**: Obtain this token by creating a bot on Telegram via BotFather.
   - **telegram_chat_id**: This is the chat ID (can be a group or individual chat) where the bot will send messages. You can use a Telegram bot to obtain the chat ID.

## How to Run

Once you have configured the `config.json` file, you can run the `demon.py` script to start monitoring Twitter trending topics:

```bash
python demon.py
```

The script will perform the following steps:
1. Retrieve trending topics via web scraping.
2. Search for each trending topic on Twitter.
3. If a specific error ("denylisted") is encountered, the script will send a notification via Telegram and stop execution.

# Demonization: Scheduling the Script with Crontab

This guide explains how to run your `demon.py` script automatically every two hours using `crontab` on a Unix-like system.

## Steps to Schedule the Script

### 1. Open Crontab
To begin, you'll need to open your crontab file in edit mode. You can do this by running the following command in your terminal:

```bash
crontab -e
```

### 2. Add the Following Line to Schedule the Script
Add the following line at the end of the crontab file to schedule your script to run every two hours:

```bash
0 */2 * * * /usr/bin/python3 /path/to/your/script/demon.py >> /path/to/your/log/demon.log 2>&1
```

#### Explanation:
- **`0 */2 * * *`**: This cron expression schedules the script to run every two hours at the start of the hour (e.g., 00:00, 02:00, 04:00, etc.).
- **`/usr/bin/python3`**: This is the path to the Python 3 interpreter. Ensure that this path is correct for your system.
- **`/path/to/your/script/demon.py`**: Replace this with the full path to your `demon.py` script.
- **`>> /path/to/your/log/demon.log 2>&1`**: This redirects both the standard output (stdout) and the standard error (stderr) to a log file. Replace `/path/to/your/log/` with the path to the directory where you want to store the log file.

### 3. Save and Exit
After adding the line to the crontab file, save the changes and exit the editor. Your script is now scheduled to run automatically every two hours.

## Additional Notes
- **Log Rotation**: Over time, the log file can grow large. Consider setting up log rotation to manage log file size and avoid running out of disk space.
- **Testing**: You can test the crontab entry by temporarily changing the timing to run the script every minute (`* * * * *`) and then checking if it behaves as expected.

By following these steps, your script will run at regular intervals without any manual intervention, ensuring continuous operation.

## Important Notes

- **Rate Limits**: The Twitter API is subject to request limits. Ensure you respect the rate limits to avoid being blocked.
- **Cookies and Headers Changes**: Cookies and headers in the configuration file may change periodically. Ensure to update them regularly to keep the script functioning.

---

This README provides all the necessary information to set up and use the project. If you have further questions or need assistance, feel free to ask!
