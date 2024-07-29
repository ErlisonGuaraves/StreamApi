from fastapi import APIRouter, HTTPException, Query, WebSocket, WebSocketDisconnect
from fastapi.responses import StreamingResponse
from typing import List, Dict, Any

import logging

from utils.stream_data import stream_data  # Importar a função utilitária
from utils.fetch_data import fetch_data

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
    

    


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            logger.info(f"Received message: {data}")

            # Simulação de uma consulta baseada na mensagem recebida
            result = await fetch_data("get_all_query")

            # Enviar os dados ao cliente usando StreamingResponse
            # Convertendo dados para o formato necessário
            response_data = stream_data(result)
            for chunk in response_data:
                await websocket.send_text(chunk)

    except WebSocketDisconnect:
        logger.warning("Client disconnected")
    except Exception as e:
        logger.error(f"Error in websocket connection: {str(e)}")
        await websocket.close()
