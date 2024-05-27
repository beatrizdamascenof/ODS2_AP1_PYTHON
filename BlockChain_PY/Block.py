import hashlib
from datetime import datetime

class Block:
    def __init__(self, index, timestamp, previous_hash, data):
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = 0
        self.hash = self.calculate_hash()

    def get_index(self):
        return self.index

    def get_timestamp(self):
        return self.timestamp

    def get_hash(self):
        return self.hash

    def get_previous_hash(self):
        return self.previous_hash

    def get_data(self):
        return self.data

    def __str__(self):
        return f"Block #{self.index} [previousHash : {self.previous_hash}, timestamp : {datetime.fromtimestamp(self.timestamp)}, data : {self.data}, hash : {self.hash}]"

    def calculate_hash(self):
        txt = f"{self.index}{self.timestamp}{self.previous_hash}{self.data}{self.nonce}"
        return hashlib.sha256(txt.encode()).hexdigest()

    def proof_of_work(self, difficulty):
        self.nonce = 0
        
        while not self.get_hash()[:difficulty] == "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
