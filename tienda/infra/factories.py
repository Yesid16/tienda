import logging
import os
from .gateways import BancoNacionalProcesador

logger = logging.getLogger("pagos")


class MockPaymentProcessor:
    def pagar(self, monto) -> bool:
        print(f"[DEBUG] Mock Payment: Procesando pago de ${monto} sin cargo real.")
        logger.info("MOCK: pago de $%s procesado sin cargo real", monto)
        return True


class PaymentFactory:
    @staticmethod
    def get_processor():
        provider = os.getenv('PAYMENT_PROVIDER', 'BANCO')

        if provider == 'MOCK':
            return MockPaymentProcessor()

        return BancoNacionalProcesador()