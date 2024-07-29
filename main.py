import logging

def main():
    import uvicorn
    uvicorn.run(
        "routers:app",  
        host="127.0.0.1",
        port=8000,
        reload=True
    )

    # Configuração básica do logging
    logging.basicConfig(
        level=logging.INFO,  # Nível de log: DEBUG, INFO, WARNING, ERROR, CRITICAL
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("app.log"),  # Nome do arquivo de log
            logging.StreamHandler()  # Também imprime no console, opcional
        ]
    )

   






if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    main()

    

