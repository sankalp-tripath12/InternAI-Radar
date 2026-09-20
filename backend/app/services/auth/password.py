from passlib.context import CryptContext

# CryptContext handles the actual bcrypt work: generating a random salt,
# hashing, and later verifying a plaintext attempt against the stored hash.
# "deprecated=auto" means if we ever change hashing schemes in the future,
# passlib can detect and re-hash old-scheme passwords transparently.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(plain_password: str) -> str:
    """Hash a plaintext password for storage. Never store plain_password itself."""
    return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Check a login attempt's plaintext password against the stored hash."""
    return pwd_context.verify(plain_password, hashed_password)
