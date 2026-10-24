# Бот без сторонних библиотек: только стандартная библиотека Python 3.8+
# Запуск: BOT_TOKEN=... WEBAPP_URL=https://ваш-сайт/ python3 bot.py
import os, json, time, urllib.request

TOKEN, URL = os.environ["8624056894:AAFPMSnAP4mcXiNsajMdXFABRZFKJ0B6g3E"], os.environ["WEBAPP_URL"]
API = f"https://api.telegram.org/bot{TOKEN}/"

def call(method, **params):
    req = urllib.request.Request(API + method, json.dumps(params).encode(),
                                 {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=70) as r:
        return json.load(r)["result"]

KB = {"inline_keyboard": [[{"text": "Открыть Patrick analysis", "web_app": {"url": URL}}]]}
call("setChatMenuButton", menu_button={"type": "web_app", "text": "Patrick analysis",
                                       "web_app": {"url": URL}})
offset = 0
while True:
    try:
        for u in call("getUpdates", offset=offset, timeout=50):
            offset = u["update_id"] + 1
            if "message" in u:
                call("sendMessage", chat_id=u["message"]["chat"]["id"],
                     text="Patrick analysis — анализ пропорций лица.\nНажми кнопку, загрузи фото и расставь точки.",
                     reply_markup=KB)
    except Exception as e:
        print("error:", e)
        time.sleep(3)
