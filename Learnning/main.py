class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # 새로운 블록을 만들고 체인 연결
        pass

    def new_transaction(self):
        # 거래 목록에 새 거래 추가
        pass

    @staticmethod
    def hash(block):
        # hashes a Block
        pass

    @property
    def last_block(self):
        # 마지막 블록 return
        pass