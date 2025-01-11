import hashlib


def sha256_hash(message):
    message = message.encode('utf-8')
    sha256 = hashlib.sha256()
    sha256.update(message)
    hash_code = sha256.hexdigest()
    return hash_code
