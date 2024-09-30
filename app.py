from flask import Flask, render_template
import asyncio

app = Flask(__name__)

# Flag to control bot's state
bot_running = False

# Route to render the landing page
@app.route('/')
def index():
    return render_template('index.html')

# Route to start the bot
@app.route('/start-bot', methods=['GET'])
def start_bot():
    global bot_running
    bot_running = True
    # You can call your bot logic here to start execution
    asyncio.create_task(run_bot_in_background())
    return "Bot started"

# Route to stop the bot
@app.route('/stop-bot', methods=['GET'])
def stop_bot():
    global bot_running
    bot_running = False
    # Logic to stop bot execution (optional)
    return "Bot stopped"

# The bot execution logic (this is your bot function that runs in the background)
async def run_bot_in_background():
    global bot_running
    while bot_running:
        # Your bot's trading logic goes here (e.g., analyzing market, making trades)
        print("Bot is running...")
        await asyncio.sleep(60)  # Example sleep time to simulate trade execution
    print("Bot stopped.")

if __name__ == "__main__":
    app.run(debug=True)
