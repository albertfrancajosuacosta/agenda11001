import enum

# Definição dos estados da agenda
class EstadoAgenda(str, enum.Enum):
    RECEBIDO = "RECEBIDO"
    CONFIRMADO = "CONFIRMADO"
    ATENDIDO = "ATENDIDO"
    CANCELADO = "CANCELADO"