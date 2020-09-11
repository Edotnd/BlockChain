from datetime import datetime
from hashlib import sha256

'''
- timestamp: 언제 만들어졌는지
- hash: 현재 블로그이 해시값
- previous hash: 이전 블록의 해시값
- nonce: 논스
- transaction: 실제 데이터 정보인 트랙젠션
'''

class Block(object):
    def __init__(self, transactions, previous_hash, nonce=0):
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        # generate_hash() 함수를 만들어서 해시를 생성
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()

    def print_block(self):
        pass
