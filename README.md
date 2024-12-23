# Instabot: Get Unfollowers List

This Python-based Instabot retrieves a list of users who are not following you back on Instagram. It uses Selenium to automate the process of identifying your unfollowers, making it easier to manage your follower list.

## Features
- Fetch your followers and following lists using web automation.
- Compare the lists to identify unfollowers.
- Generate an easy-to-read report of users who don’t follow you back.

## Prerequisites
- Python 3.7 or later
- An Instagram account
- Google Chrome and ChromeDriver installed

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/instabot-unfollowers.git
    cd instabot-unfollowers
    ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the environment:
    - Download the appropriate version of ChromeDriver from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads) and place it in your system PATH or the project directory.

4. Update the configuration file:
    - Add your Instagram login credentials in a `.env` file:
      ```env
      INSTAGRAM_USERNAME=your_username
      INSTAGRAM_PASSWORD=your_password
      ```

## Usage

1. Run the script:
    ```bash
    python instabot.py
    ```

2. The bot will log in to your Instagram account, fetch your followers and following lists, and generate a report of unfollowers.

3. The unfollowers list will be saved as `unfollowers_report.txt` in the project directory.

## Example Output

After running the script, you might see an output like:
```
Unfollowers:
1. username1
2. username2
3. username3
```

## Customization

- **Output Format**: Modify the script to save the unfollowers list in a different format (e.g., CSV or JSON).
- **Filtering**: Add filters to exclude specific accounts from the unfollowers report.

## Contributing

Contributions are welcome! If you’d like to contribute:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer

This project is for educational purposes only. Use it responsibly and ensure compliance with Instagram's Terms of Use and API guidelines.


