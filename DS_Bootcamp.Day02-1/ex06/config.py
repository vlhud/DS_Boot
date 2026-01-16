NUM_OF_STEPS=3

REPORT_TEMPLATE=("We have made {total} observations from tossing a coin: {tails} of them were tails and {heads} of them were heads. The probabilities are {fr_tails:.2f}% and {fr_heads:.2f}%, respectively. Our forecast is that in the next {num_steps} observations we will have: {predicted_tails} tail and {predicted_heads} heads.")
LOG_FILE="analytics.log"
TELEGRAM_WEBHOOK_URL='https://api.telegram.org/bot7584802854:AAG9KnaT0uWGszBOO7uxY3aKKq1Y-824oso/sendMessage'
CHAT_ID='867550527'