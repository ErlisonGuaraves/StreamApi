from utils.config import queries
from tortoise.transactions import in_transaction
from typing import List


# Função auxiliar assíncrona para consulta de dados
async def fetch_data(query_key: str, params: List = None):
    async with in_transaction() as connection:
        result = await connection.execute_query_dict(queries.get(query_key, ""), params or [])
    return result


