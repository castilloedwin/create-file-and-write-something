from pathlib import Path
import json

class Alert:
    def __init__(self):
        self.messages = json.loads( Path('messages.json').read_text() )