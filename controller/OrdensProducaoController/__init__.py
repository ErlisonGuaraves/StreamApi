from tortoise.transactions import in_transaction
from fastapi import APIRouter, HTTPException, Query
from typing import List, Dict, Any
from utils.config import queries

# Crie o roteador fora da classe
router = APIRouter(prefix="/fiscaliza_resfriado", tags=["ordens de produção"])




@router.get("/")
async def get_fiscaliza_resfriado():
    try:
        async with in_transaction() as connection:
            result = await connection.execute_query_dict(queries["get_all_query"])
            
        return result
    except Exception as e:

        raise HTTPException(status_code=500, detail="Internal Server Error")





@router.get("/by_op/{op}", response_model=dict)
async def get_fiscaliza_resfriado_by_op(op: str):
    try:

        async with in_transaction() as connection:
        
            result = await connection.execute_query_dict(queries["get_by_op_query"], [op])
            if not result:

                raise HTTPException(status_code=404, detail="Record not found")
  
        return result[0]
    except HTTPException as e:
        raise e
    except Exception as e:
        
        raise HTTPException(status_code=500, detail="Internal Server Error")





@router.get("/by_date_range", response_model=List[Dict[str, Any]])
async def get_fiscaliza_resfriado_by_date_range(start_date: str = Query(...), end_date: str = Query(...)):
    try:

        async with in_transaction() as connection:
            result = await connection.execute_query_dict(queries["get_by_date_range_query"], [start_date, end_date])
            if not result:
                
                raise HTTPException(status_code=404, detail="Records not found")
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
