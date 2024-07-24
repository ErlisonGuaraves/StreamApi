from fastapi import APIRouter, HTTPException, Query
from tortoise.transactions import in_transaction
from typing import Dict, Any
from utils.config import queries

router = APIRouter(
    prefix="/resfriado_paginated",
    tags=["endpoints paginados"]
)


@router.get("/")
async def get_fiscaliza_resfriado_paginated(page: int = Query(1, gt=0), size: int = Query(10, gt=0)) -> Dict[str, Any]:
    try:
        offset = (page - 1) * size

        async with in_transaction() as connection:    
            
            paginated_query = queries['paginated_query_template'].format(
                base_query=queries['get_all_query'],
                offset=offset,
                limit=size
            )
            result = await connection.execute_query_dict(paginated_query)
           
            return {
                "items": result,
                "page": page,
                "size": size
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
