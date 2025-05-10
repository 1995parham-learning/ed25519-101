import base64
import time

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey


def main():
    private_key = Ed25519PrivateKey.generate()

    b = private_key.private_bytes_raw()
    print(base64.b64encode(b))

    now = time.time_ns()
    print(f"now: {now}")

    signature = private_key.sign(f"GET /api/v4/prices {now}".encode())
    public_key = private_key.public_key()
    public_key.verify(signature, f"GET /api/v4/prices {now}".encode())


if __name__ == "__main__":
    main()
