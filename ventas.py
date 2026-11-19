def calcular_total(subtotal_centavos: int, descuento: int) -> int:
    if subtotal_centavos < 0:
        raise ValueError("El subtotal debe ser no negativo")

    if not 0 <= descuento <= 100:
        raise ValueError("El descuento debe estar entre 0 y 100")

    return (subtotal_centavos * (100 - descuento) + 50) // 100