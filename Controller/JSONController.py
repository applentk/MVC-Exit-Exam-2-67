import json

class JSONController:
    def __init__(self, file_path):
        self.file_path = file_path
        self._load_json()

    def _load_json(self):
        """Load JSON data from the file."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.data = []  # Default to an empty list if file not found or invalid

    def _save_json(self):
        """Save JSON data to the file."""
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4)

    def view(self):
        """Return the JSON data."""
        return self.data

    def add(self, item):
        """Add a new item to the JSON list."""
        self.data.append(item)
        self._save_json()

    def edit(self, index, new_item):
        self.data[index] = new_item
        self._save_json()
        