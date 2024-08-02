from tortoise.transactions import in_transaction
from typing import List, Dict, Any
import logging
from utils.config import queries

# Set up logging
logger = logging.getLogger(__name__)

async def fetch_data(query_key: str, params: List = None) -> List[Dict[str, Any]]:

    query = queries.get(query_key, "")
    
    logger.info(f"Executing query: {query} with params: {params}")
    
    async with in_transaction() as connection:
       
        result = await connection.execute_query_dict(query, params or [])
        
    # Log the result for debugging
    logger.info(f"Query result: {result}")
    
    
    return result

