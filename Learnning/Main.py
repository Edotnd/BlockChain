from blockchain import BlockChain

Ecoin = BlockChain()
print(Ecoin.chain) # genesis block이 만들어진 것을 볼 수 있다.

# Musk가 Edotnd엑 1000코인을 준다고 가정으로 transaction1로
# 새로운 블록 추가

transaction1 = {
    'Sender': 'Elon Musk',
    'Receiver': 'Edotnd',
    'Amount': 1000,
}

Ecoin.add_block(transaction1)
print(Ecoin.chain)
print(Ecoin.validate_chain())