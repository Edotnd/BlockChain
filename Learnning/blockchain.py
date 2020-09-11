from block import Block

class BlockChain(object):
    def __init__(self):
        self.chain = [] # 모든 블록 저장
        self.all_transactions = [] # chain과 모든 transaction 데이터를 저장

    def genesis_block(self):
        transactions = {}
        block = Block(transaction, 0)
        self.chain.append(block)
        return self.chain

    def add_block(self, transactions):
        previous_block_hash = self.chain[len(self.chain)-1].hash
        new_block = Block(transactions, previous_block_hash)
        proof = self.proof_of_work(new_block)
        self.chain.append(new_block)
        return proof, new_block

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            if current.hash != current.generate_hash():
                print("[!] 블록의 현재 해시가 블록의 생성된 해시와 같지 않습니다.")
                return False
            if previous.hash != previous.generate_hash():
                print("[!] 이전 블록의 해시는 현재 블록에 저장된 이전 해시 값과 일치하지 않습니다.")
                return False
            if current.previous_hash != previous.hash:
                return False
        return True
        
    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()

        while proof[:2] != '0'*difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        return proof

    