import boto3
import os

AWS_ACCESS_KEY=os.environ['AWS_ACCESS_KEY']
AWS_SECRET_KEY=os.environ['AWS_SECRET_KEY']
kms = boto3.client('kms', region_name='ap-northeast-2', aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
message = "Hello, This is test msg for kms."

def encryption(msg):
    response = kms.encrypt(KeyId=os.environ['KeyId'], Plaintext=msg)
    print(f'[*] Encryption Response: {response}')
    return response

def decryption(msg):
    response = kms.decrypt(CiphertextBlob=msg)
    print(f'[*] Decryption Response: {response}')
    return response['Plaintext']

if __name__ == "__main__":
    print(f'[*] Test for KMS Encryption / Decryption')
    print(f'[*] Message : {message}')
    data_key = kms.generate_data_key(KeyId=os.environ['KeyId'], KeySpec='AES_256')
    plaintext_data_key = data_key['Plaintext']
    encrypted_data_key = data_key['CiphertextBlob']
    print(f'[*] Data Key : {data_key}')

    # Encryption
    enc_res = encryption(message)

    # Decryption
    dec_res = decryption(enc_res['CiphertextBlob'])