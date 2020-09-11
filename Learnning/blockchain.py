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

    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()

        while proof[:2] != '0'*difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        return proof

    