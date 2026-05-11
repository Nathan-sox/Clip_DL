import os
import json
from datetime import datetime


def load_history(file):
    if not os.path.exists(file):
        return []
    else:
        try:
            with open(file, "r") as file:
                history = json.load(file)
            return history
        except json.decoder.JSONDecodeError:
            return []


def save_history(data, file):
    with open(file, "w") as file:
        json.dump(data, file, indent=2)


def add_to_history(url, title, file):
    history = load_history(file)

    history.append({"url": url, "title": title,
                   "date": datetime.now().strftime("%Y-%m-%d %H:%M-%S")})

    save_history(history, file)
