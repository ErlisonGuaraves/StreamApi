from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from shared.database import TORTOISE_ORM

from controller.OrdensProducaoController import router as OrdensProducaoRouter
from controller.paginationController import router as PaginationRouter

app = FastAPI()

register_tortoise(
    app,
    db_url=TORTOISE_ORM["connections"]["default"],
    modules={"models": TORTOISE_ORM["apps"]["models"]["models"]},
    generate_schemas=True,
    add_exception_handlers=True
)


app.include_router(OrdensProducaoRouter)
app.include_router(PaginationRouter)