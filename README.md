# 🆔 Validador de RUT Chileno

> Calculadora y validador del dígito verificador del RUT chileno mediante el algoritmo **módulo 11**, escrito en Python con programación modular.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/estado-funcional-brightgreen)

---

## 📖 ¿Qué hace? / What it does

**ES:** Programa de consola que calcula y valida el dígito verificador (DV) del RUT chileno. Permite calcular el DV de un cuerpo, validar un RUT completo, formatearlo con puntos y guion, y validar varios RUT a la vez.

**EN:** A command-line program that calculates and validates the Chilean RUT check digit. It can compute the check digit for a number, validate a full RUT, format it with dots and a dash, and validate several RUTs at once.

---

## ⚙️ El algoritmo (módulo 11)

Los dígitos del cuerpo se multiplican de derecha a izquierda por la serie **2, 3, 4, 5, 6, 7** (que se repite). Se suman los productos y se calcula:

```
DV = 11 − (suma mód 11)
```

Casos especiales: si el resultado es **11 → 0**, si es **10 → K**.

**Ejemplo:** para el cuerpo `12.678.579` el dígito verificador es **8** → `12.678.579-8`.

---

## 🚀 Uso / Usage

```bash
# Clonar el repositorio
git clone https://github.com/gianca675/validador-rut-chile.git
cd validador-rut-chile

# Ejecutar
python validador_rut.py
```

Aparecerá un menú interactivo:

```
==========================================
   VALIDADOR DE RUT CHILENO — Módulo 11
==========================================
  1. Calcular dígito verificador
  2. Validar un RUT completo
  3. Formatear un RUT (puntos y guion)
  4. Validar varios RUT (lote)
  5. Salir
```

### Usarlo como módulo / Use it as a library

```python
from validador_rut import calcular_digito_verificador, validar_rut, formatear_rut

calcular_digito_verificador("12678579")   # -> "8"
validar_rut("12.678.579-8")               # -> True
formatear_rut("126785798")                # -> "12.678.579-8"
```

---

## 🧩 Funciones principales

| Función | Descripción |
|---------|-------------|
| `limpiar_rut(rut)` | Quita puntos, guion y espacios. |
| `calcular_digito_verificador(cuerpo)` | Calcula el DV con módulo 11. |
| `validar_rut(rut)` | Verifica que un RUT completo sea válido. |
| `formatear_rut(rut)` | Devuelve el RUT con puntos y guion. |
| `procesar_lote(ruts)` | Valida una lista de RUT. |

---

## 👤 Autor

**Giancarlos Alfaro** — [@gianca675](https://github.com/gianca675) · [Portafolio](https://gianca675.github.io)

## 📄 Licencia

MIT — libre para uso personal y educativo.
