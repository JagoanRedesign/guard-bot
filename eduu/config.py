import os.path

from typing import List, Optional


API_ID: int = 14672956
API_HASH: str = "115e8242ea0423893160bb61a9e05eab"
TOKEN: str = "5562779594:AAG8y1A2lnoXxU_DIE_bQq4sdxu-GQzHsmk"

log_chat: int = -1001306851903
sudoers: List[int] = [5166575484, 1659580762]
super_sudoers: List[int] = [5166575484, 1659580762]

prefix: List[str] = ["/", "!", ".", "$", "-"]

disabled_plugins: List[str] = []

WORKERS = 24

DATABASE_PATH = os.path.join("eduu", "database", "eduu.db")

TENOR_API_KEY: Optional[str] = "X9HD35B7ZGP6"

sudoers.extend(super_sudoers)
