
from tortoise.transactions import in_transaction
from fastapi import APIRouter, HTTPException, Query
from typing import List, Dict, Any

# Crie o roteador fora da classe
router = APIRouter(prefix="/fiscaliza_resfriado", tags=["ordens de produção"])

@router.get("/")
async def get_fiscaliza_resfriado():
    try:
        async with in_transaction() as connection:
            query = """
                SELECT
                    OP,
                    PRODESC,
                    DATAENTREGA,
                    QUANTIDADE_PEDIDO,
                    QUANTIDADE_OP_ABERTA,
                    QUANTIDADE_UNITIZADA,
                    QUANTIDADE_APONTADA,
                    QUANTIDADE_CARREGADA,
                    RECEBIDO_LOGISTICA
                FROM DMT.DMT_FISCALIZA_RESFRIADO
            """
            result = await connection.execute_query_dict(query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/by_op/{op}", response_model=dict)
async def get_fiscaliza_resfriado_by_op(op: str):
    try:
        async with in_transaction() as connection:
            query = """
                SELECT
                    OP,
                    PRODESC,
                    DATAENTREGA,
                    QUANTIDADE_PEDIDO,
                    QUANTIDADE_OP_ABERTA,
                    QUANTIDADE_UNITIZADA,
                    QUANTIDADE_APONTADA,
                    QUANTIDADE_CARREGADA,
                    RECEBIDO_LOGISTICA
                FROM DMT.DMT_FISCALIZA_RESFRIADO
                WHERE OP = $1
            """
            result = await connection.execute_query_dict(query, [op])
            if not result:
                raise HTTPException(status_code=404, detail="Record not found")
        return result[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/by_date_range", response_model=List[Dict[str, Any]])
async def get_fiscaliza_resfriado_by_date_range(start_date: str = Query(...), end_date: str = Query(...)):
    try:
        async with in_transaction() as connection:
            query = """
                SELECT
                    OP,
                    PRODESC,
                    DATAENTREGA,
                    QUANTIDADE_PEDIDO,
                    QUANTIDADE_OP_ABERTA,
                    QUANTIDADE_UNITIZADA,
                    QUANTIDADE_APONTADA,
                    QUANTIDADE_CARREGADA,
                    RECEBIDO_LOGISTICA
                FROM DMT.DMT_FISCALIZA_RESFRIADO
                WHERE DATAENTREGA BETWEEN $1 AND $2
            """
            
            result = await connection.execute_query_dict(query, [start_date, end_date])
            
            if not result:
                raise HTTPException(status_code=404, detail="Records not found")  
                     
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")