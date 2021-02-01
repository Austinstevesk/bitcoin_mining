from hashlib import sha256

Max_Nonce = 1000000

#An example hashing function
def Sha256(text):
    return sha256(text.encode('ascii')).hexdigest()


#Will need block number, transactions and previous hash
def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str =  '0'*prefix_zeros
    for nonce in range(Max_Nonce):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = Sha256(text)
        if new_hash.startswith(prefix_str):
            #managed to get the nonce value
            print("Successfully mined the bitcoins with nonce value: ", nonce)
            return new_hash
    raise BaseException("Couldn't find the correct hash after trying ", Max_Nonce, " times")


if __name__ == '__main__':

    transactions = """
    Steve->Austin->20
    James->Sam->50
    """
    difficulty = 5 #No of zeros || Increasing this takes more computations
    import time
    start_time = time.time()
    print("Start mining")
    new_hash = mine(5,transactions,'000000xc3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78', difficulty )
    total_time = str(time.time() - start_time)
    print(total_time)
    print(new_hash)