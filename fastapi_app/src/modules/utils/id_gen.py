from uuid import uuid4

def gen_unique_id() -> str:
    return str(uuid4())
