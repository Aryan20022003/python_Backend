import jwt
import datetime
from decouple import config

# read public and private keys from root dir named public_key.pem
# and private_key.pem
# PUBLIC_KEY = open("public_key.pem", "r").read()
# PRIVATE_KEY = open("private_key.pem", "r").read()


def tokenIssuer(userId: str, time: int = 15):  # time in minutes
    try:
        payload = {
            "userId": userId,
            "exp": (
                datetime.datetime.utcnow() + datetime.timedelta(minutes=time)
            ).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        return jwt.encode(payload, config("SECRET_KEY"), algorithm="HS256")
    except Exception as e:
        print(e)
        return None


def tokenVerifier(token: str):
    try:
        print(token, "token")
        payload = jwt.decode(token, config("SECRET_KEY"), algorithms="HS256")
        # assuming the user is valid one
        return True
    except jwt.ExpiredSignatureError:
        print("expired")
        return False
    except jwt.InvalidTokenError:
        print("invalid")
        return False
    except Exception as e:
        print(e)
        return False
