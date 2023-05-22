# Telegram Bot - Photo Resizer (abc model)

This is a Telegram bot that allows users to resize photos and apply filters.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Olegsmm2092/telegram-bot-foto-cc.git
   ```
2. Create a virtual environment:
   ```bash
   virtualenv -p python3.11 venv
   ```

2. Activate the virtual environment:
   ```bash
   source venv/Script/activate
   ```


2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a Telegram Bot:
    
   * Create a new bot on Telegram and obtain a bot token from the BotFather bot on Telegram.
   * Update the config.py file with your bot token.

## Implement the Bot Functionality

1. Refactor the code and organize it into modules. Here's an example structure:
    ````hljs
    project/
    ├── bot.py
    ├── functions.py
    ├── keyboard.py
    ├── database.py
    └── README.md
    ````


## Usage

1. Run the bot:
    ```bash
    python bot.py
    ```

2. Open Telegram and search for your bot.

3. Start a conversation with the bot.

4. Send a photo to the bot:

    * If using the camera: Take a photo and send it to the bot.
    * If using a file: Send the photo file to the bot.

5. Resize the photo:

    * Use the /resize command followed by the desired dimensions (e.g., /resize 200 200).
    * Select the desired dimensions from the provided keyboard options.

6. Apply filters to the photo:

    * Use the /filter command followed by the filter name (e.g., /filter grayscale).
    * Select the desired filter from the provided keyboard options.

7. Explore additional commands:

    * Use the /help command to get a list of available commands and instructions.
    * Use the /about command to learn more about the bot.

## Examples
    
* To resize a photo to 300x300 pixels:
    ```bash
        /resize 300 300
    ```

* To apply a grayscale filter to a photo:
    ```bash
        /filter grayscale
    ```

## License
This project is licensed under the [MIT License](https://github.com/Olegsmm2092/telegram-bot-foto-cc/blob/main/LICENSE).
