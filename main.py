from logic import check_signal
from telegram_bot import send_telegram
import yfinance as yf, time, json

with open('config.json') as f:
    cfg = json.load(f)

PAIR = 'XAUUSD=X'
INTERVAL = 60  # 1 phút

last_signal = None

while True:
    data = yf.download(PAIR, period='5m', interval='1m')
    close = data['Close'].tolist()

    signal = check_signal(close)

    if signal and signal != last_signal:
        send_telegram(cfg['bot_token'], cfg['chat_id'], f'{PAIR} tín hiệu: {signal}')
        last_signal = signal

    print(f"XAUUSD: {close[-1]:.2f} | Signal: {signal}")
    time.sleep(INTERVAL)
