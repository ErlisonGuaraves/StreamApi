import logging
import uvicorn


def main():
    
    uvicorn.run(
        "routers:app",  
        host="127.0.0.1",
        port=8000,
        reload=True
    )

    
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=logging.FileHandler("logs/app.log")
    )



if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    main()
    

    

