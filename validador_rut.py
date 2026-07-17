"""
Validador y calculador de dígito verificador de RUT chileno.
Algoritmo módulo 11.

Autor: Giancarlos Alfaro (@gianca675)
Licencia: MIT
"""


def limpiar_rut(rut: str) -> str:
    """Quita puntos, guion y espacios, y deja el RUT en mayúsculas."""
    return rut.replace(".", "").replace("-", "").replace(" ", "").upper()


def calcular_digito_verificador(cuerpo: str) -> str:
    """
    Calcula el dígito verificador de un cuerpo de RUT usando módulo 11.

    Se multiplican los dígitos de derecha a izquierda por la serie
    2, 3, 4, 5, 6, 7 (que se repite). Luego:
        dv = 11 - (suma % 11)
    Casos especiales: 11 -> '0', 10 -> 'K'.

    >>> calcular_digito_verificador("12678579")
    '8'
    """
    if not cuerpo.isdigit():
        raise ValueError("El cuerpo del RUT solo debe contener dígitos.")

    suma = 0
    multiplicador = 2
    for digito in reversed(cuerpo):
        suma += int(digito) * multiplicador
        multiplicador = 2 if multiplicador == 7 else multiplicador + 1

    resto = 11 - (suma % 11)
    if resto == 11:
        return "0"
    if resto == 10:
        return "K"
    return str(resto)


def validar_rut(rut: str) -> bool:
    """
    Valida un RUT completo (cuerpo + dígito verificador).

    >>> validar_rut("12.678.579-8")
    True
    >>> validar_rut("12.678.579-9")
    False
    """
    rut = limpiar_rut(rut)
    if len(rut) < 2:
        return False

    cuerpo, dv = rut[:-1], rut[-1]
    if not cuerpo.isdigit():
        return False

    try:
        return calcular_digito_verificador(cuerpo) == dv
    except ValueError:
        return False


def formatear_rut(rut: str) -> str:
    """
    Devuelve el RUT con puntos y guion.

    >>> formatear_rut("126785798")
    '12.678.579-8'
    """
    rut = limpiar_rut(rut)
    cuerpo, dv = rut[:-1], rut[-1]

    partes = []
    while len(cuerpo) > 3:
        partes.insert(0, cuerpo[-3:])
        cuerpo = cuerpo[:-3]
    partes.insert(0, cuerpo)

    return ".".join(partes) + "-" + dv


def procesar_lote(ruts: list[str]) -> None:
    """Valida una lista de RUT e imprime el resultado de cada uno."""
    print("\n--- Resultado del lote ---")
    for rut in ruts:
        estado = "✅ válido" if validar_rut(rut) else "❌ inválido"
        try:
            print(f"  {formatear_rut(rut):>15}  ->  {estado}")
        except Exception:
            print(f"  {rut:>15}  ->  ⚠️ formato incorrecto")


# ----------------------- Interfaz de consola ----------------------- #

def _menu() -> None:
    print("\n" + "=" * 42)
    print("   VALIDADOR DE RUT CHILENO — Módulo 11")
    print("=" * 42)
    print("  1. Calcular dígito verificador")
    print("  2. Validar un RUT completo")
    print("  3. Formatear un RUT (puntos y guion)")
    print("  4. Validar varios RUT (lote)")
    print("  5. Salir")


def main() -> None:
    while True:
        _menu()
        opcion = input("\nElige una opción (1-5): ").strip()

        if opcion == "1":
            cuerpo = limpiar_rut(input("Ingresa el cuerpo del RUT (sin dígito): "))
            try:
                dv = calcular_digito_verificador(cuerpo)
                print(f"➡️  Dígito verificador: {dv}   (RUT: {cuerpo}-{dv})")
            except ValueError as e:
                print(f"⚠️  {e}")

        elif opcion == "2":
            rut = input("Ingresa el RUT completo: ")
            print("✅ RUT válido" if validar_rut(rut) else "❌ RUT inválido")

        elif opcion == "3":
            rut = input("Ingresa el RUT: ")
            try:
                print(f"➡️  {formatear_rut(rut)}")
            except Exception:
                print("⚠️  No pude formatear ese RUT.")

        elif opcion == "4":
            entrada = input("Ingresa varios RUT separados por coma: ")
            procesar_lote([r for r in entrada.split(",") if r.strip()])

        elif opcion == "5":
            print("¡Hasta luego! 👋")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
