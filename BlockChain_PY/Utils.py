from Blockchain import Blockchain
from Block import Block

class Utils:
    @staticmethod
    def zeros(length: int) -> str:
        return "0" * length

    @staticmethod
    def contains_block(blockchain: Blockchain, data: str) -> bool:
        for block in blockchain.get_blocks():
            if data in block.get_data():
                return True
        return False

    @staticmethod
    def find_block(blockchain: Blockchain, data: str) -> Block:
        for block in blockchain.get_blocks():
            if data in block.get_data():
                return block
        return None
