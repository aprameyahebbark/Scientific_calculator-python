
from pathlib import Path

class History:
    def __init__(self):
        self.file = Path("history.txt")
        self.file.touch(exist_ok=True)

    def add(self, text):
        with self.file.open("a", encoding="utf-8") as f:
            f.write(text + "\n")

    def show(self):
        print("\n===== HISTORY =====")
        print(self.file.read_text(encoding="utf-8"))
