import logging

logger = logging.getLogger("pagos")


class BancoNacionalProcesador:
    def pagar(self, monto) -> bool:
        print(f"[BANCO] Cobro real de ${monto} procesado por Banco Nacional.")
        logger.info("BANCO: pago de $%s procesado", monto)
        return True