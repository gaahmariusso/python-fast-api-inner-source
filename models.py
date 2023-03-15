from redis_om import get_redis_connection, HashModel
from typing import Optional

redis_db = get_redis_connection(
    host = '',
    port = '',
    password = '',
    decode_responses = True
)

# Model
class Task(HashModel):
    name: str
    complete: Optional[bool] = 0

    class Meta:
        database = redis_db