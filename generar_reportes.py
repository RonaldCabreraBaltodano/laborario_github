from html import escape
from os import getenv
from pathlib import Path

from ventas import calcular_total


def main():
    total = calcular_total(10000, 10)
    colones, centavos = divmod(total, 100)
    monto = f"{colones}.{centavos:02d}"
    revision = escape(getenv("GITHUB_SHA", "local")[:12])

    destino = Path("dist")
    destino.mkdir(exist_ok=True)

    pagina = f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Reporte de ventas</title>
</head>
<body>
  <main>
    <h1>Reporte de ventas</h1>
    <p>Subtotal ficticio: CRC 100.00</p>
    <p>Descuento: 10 %</p>
    <p>Total: CRC {monto}</p>
    <p>Versión: <code>{revision}</code></p>
  </main>
</body>
</html>
"""
    (destino / "index.html").write_text(pagina, encoding="utf-8")


if __name__ == "__main__":
    main()