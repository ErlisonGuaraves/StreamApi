from tortoise import fields, models

class OrdensProducao(models.Model):
    data_entrega = fields.CharField(max_length=8)
    prodesc = fields.TextField()
    op = fields.TextField()
    quantidade_pedido = fields.FloatField(null=True)
    quantidade_op_aberta = fields.FloatField(null=True)
    quantidade_unitizada = fields.FloatField(null=True)
    quantidade_apontada = fields.FloatField(null=True)
    quantidade_carregada = fields.FloatField(null=True)
    recebido_logistica = fields.FloatField(null=True)

    class Meta:
        table = "dmt_fiscaliza_resfriado"
        schema = "dmt"
