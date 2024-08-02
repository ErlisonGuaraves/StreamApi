from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import StreamingResponse
from typing import List, Dict, Any

import logging

from utils.stream_data import stream_data 
from utils.fetch_data import fetch_data
from utils.count_rows import count_rows_updated, load_row_count, save_row_count

router = APIRouter(prefix="/fiscaliza_resfriado", tags=["ordens de produção"])

logger = logging.getLogger(__name__)





@router.get("/")
async def get_fiscaliza_resfriado():
    try:
        result = await fetch_data("get_all_query")
        return StreamingResponse(stream_data(result), media_type="application/json")
    
    except Exception as e:
        logger.error(f"Error in get_fiscaliza_resfriado: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")




@router.get("/by_op/{op}", response_model=dict)
async def get_fiscaliza_resfriado_by_op(op: str):
    try:
        result = await fetch_data("get_by_op_query", [op])
        if not result:
            raise HTTPException(status_code=404, detail="Record not found")
        
        return StreamingResponse(stream_data(result), media_type="application/json")
    
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error in get_fiscaliza_resfriado_by_op: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")




@router.get("/by_date_range", response_model=List[Dict[str, Any]])
async def get_fiscaliza_resfriado_by_date_range(
    start_date: str = Query(...),
    end_date: str = Query(...)
):
    try:
        result = await fetch_data("get_by_date_range_query", [start_date, end_date])
        if not result:
            raise HTTPException(status_code=404, detail="Records not found")
        return StreamingResponse(stream_data(result), media_type="application/json")
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error in get_fiscaliza_resfriado_by_date_range: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    




@router.get("/rows_updated")
async def get_rows_updated():
    try:
        # Fetch the current row count
        current_row_count_result = await fetch_data("count_query")
        if not current_row_count_result or 'count' not in current_row_count_result[0]:
            raise HTTPException(status_code=500, detail="Failed to fetch the current row count")
        
        current_row_count = current_row_count_result[0]['count']

        # Retrieve the last row count from the file
        last_row_count = load_row_count()

        change = count_rows_updated(last_row_count, current_row_count)

        # Save the current row count to the file
        save_row_count(current_row_count)

        return {
            'last_row_count': last_row_count,
            'current_row_count': current_row_count,
            'change': change,
        }
    except Exception as e:
        logger.error(f"Error in get_rows_updated: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    
