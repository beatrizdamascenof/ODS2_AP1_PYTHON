from Block import Block
from typing import List
from datetime import datetime
import time

class Blockchain:
    def __init__(self, difficulty: int):
        self.difficulty = difficulty
        self.blocks: List[Block] = []

        # cria o primeiro block
        b = Block(0, int(time.time()), None, "Bloco gênesis")
        b.proof_of_work(self.difficulty)
        self.blocks.append(b)

    def get_difficulty(self) -> int:
        return self.difficulty

    def latest_block(self) -> Block:
        return self.blocks[-1]

    def new_block(self, data: str) -> Block:
        latest_block = self.latest_block()
        return Block(latest_block.get_index() + 1, int(time.time()), latest_block.get_hash(), data)

    def add_block(self, b: Block) -> None:
        if b is not None:
            b.proof_of_work(self.difficulty)
            self.blocks.append(b)

    def get_blocks(self) -> List[Block]:
        return self.blocks

    def is_first_block_valid(self) -> bool:
        first_block = self.blocks[0]
        if first_block.get_index() != 0:
            return False
        if first_block.get_previous_hash() is not None:
            return False
        if first_block.get_hash() is None or first_block.calculate_hash() != first_block.get_hash():
            return False
        return True

    def is_valid_new_block(self, new_block: Block, previous_block: Block) -> bool:
        if new_block is not None and previous_block is not None:
            if previous_block.get_index() + 1 != new_block.get_index():
                return False
            if new_block.get_previous_hash() is None or new_block.get_previous_hash() != previous_block.get_hash():
                return False
            if new_block.get_hash() is None or new_block.calculate_hash() != new_block.get_hash():
                return False
            return True
        return False

    def is_blockchain_valid(self) -> bool:
        if not self.is_first_block_valid():
            return False
        for i in range(1, len(self.blocks)):
            current_block = self.blocks[i]
            previous_block = self.blocks[i - 1]
            if not self.is_valid_new_block(current_block, previous_block):
                return False
        return True

    def contains_block(self, text: str) -> bool:
        for block in self.blocks:
            if text in block.get_data():
                return True
        return False

    def __str__(self) -> str:
        return '\n'.join(str(block) for block in self.blocks)
    
    def blockchain_to_dict(self):
        data = []
        for block in self.get_blocks():
            block_data = {
                "Index": block.get_index(),
                "Timestamp": datetime.fromtimestamp(block.get_timestamp()).strftime('%Y-%m-%d %H:%M:%S'),
                "Previous Hash": block.get_previous_hash(),
                "Data": block.get_data(),
                "Hash": block.get_hash(),
                "Nonce": block.nonce  # Asegúrate de tener un método para obtener el nonce si no es público
            }
            data.append(block_data)
        return data
     
