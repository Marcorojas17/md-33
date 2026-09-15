<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- MD-33 · ESTÁNDAR FORENSE INTERNACIONAL · v1.0                          -->
<!-- Caso de estudio demostrativo + Framework real                          -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->

<div align="center">

```text
╔══════════════════════════════════════════════════════════════════════════════╗
║ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ║
║ ▓                                                                          ▓ ║
║ ▓   ███╗   ███╗██████╗        ██████╗ ██████╗                             ▓ ║
║ ▓   ████╗ ████║██╔══██╗      ██╔════╝ ╚════██╗                            ▓ ║
║ ▓   ██╔████╔██║██║  ██║█████╗███████╗  █████╔╝                            ▓ ║
║ ▓   ██║╚██╔╝██║██║  ██║╚════╝╚════██║  ╚═══██╗                            ▓ ║
║ ▓   ██║ ╚═╝ ██║██████╔╝      ██████╔╝ ██████╔╝                            ▓ ║
║ ▓   ╚═╝     ╚═╝╚═════╝       ╚═════╝  ╚═════╝                             ▓ ║
║ ▓                                                                          ▓ ║
║ ▓   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   ▓ ║
║ ▓   E S T Á N D A R   I N T E R N A C I O N A L   ·   v 1 . 0              ▓ ║
║ ▓   C A S O   D E   E S T U D I O   +   F R A M E W O R K   R E A L        ▓ ║
║ ▓   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   ▓ ║
║ ▓                                                                          ▓ ║
║ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

[![Estándar MD-33 v1.0](https://img.shields.io/badge/Est%C3%A1ndar-MD--33%20v1.0-00ff41?style=for-the-badge&labelColor=0a0d10)](MANUAL_PERITO_INTERNACIONAL_MD33.md)
[![ISO 27037](https://img.shields.io/badge/ISO-27037-00ff41?style=for-the-badge&labelColor=0a0d10)](https://www.iso.org/standard/44381.html)
[![ISO 17025](https://img.shields.io/badge/ISO-17025-ffcc00?style=for-the-badge&labelColor=0a0d10)](https://www.iso.org/standard/66912.html)
[![RFC 3161](https://img.shields.io/badge/RFC-3161-8b5cf6?style=for-the-badge&labelColor=0a0d10)](https://datatracker.ietf.org/doc/html/rfc3161)
[![CC0](https://img.shields.io/badge/license-CC0%20%2B%20Comercial-00ffff?style=for-the-badge&labelColor=0a0d10)](LICENSE)

</div>

---

## ⚠️ Aviso de transparencia

**MD-33 (cristal, Muelle 42, Fideicomiso Ciego 07, AUTO-ANALYSIS v3.7.1) es un caso de estudio demostrativo y ficticio.** Los elementos narrativos — el cristal, el robo, la cadena de custodia, el acta, el testamento — fueron construidos como escenario de prueba para validar un framework de verificación forense.

**Lo que SÍ es 100% real, verificable y usable en casos reales:**

- ✅ Protocolo de verificación conforme a **ISO/IEC 27037:2012** e **ISO/IEC 17025:2017**
- ✅ Comandos universales: `sha256sum`, `openssl dgst`, `ots verify`, `cast tx`
- ✅ Script funcional `src/verifica_estandar.py` (genérico, acepta cualquier documento)
- ✅ Plantilla de acta bilingüe ES/EN en `plantillas/acta_perito_vacia.md`
- ✅ Modelo de cadena de custodia digital con hash + firma + timestamp
- ✅ Tabla de cumplimiento legal por país (México, USA, UE, Israel)

**Puedes clonar este framework y aplicarlo a casos reales** (verificación de contratos, actas, evidencias digitales, notarización blockchain) sin ninguna restricción legal. La ficción narrativa es el vehículo; el framework es la carga útil.

---

## 📖 ¿Qué es este repositorio?

Este repo contiene **dos capas separadas**:

| Capa | Descripción | Estado |
|------|-------------|--------|
| **Narrativa (MD-33)** | Caso demostrativo con lore, actas y evidencia ficcional | 🎭 Ficción |
| **Framework (Estándar)** | Protocolo de verificación forense ISO + RFC + blockchain | ⚙️ Real y usable |

La narrativa sirve como **banco de pruebas** del framework. El framework sirve como **herramienta real** para peritos, auditores y desarrolladores.

---

## 🚀 Inicio rápido

### 1. Clonar

```bash
git clone https://github.com/Marcorojas17/md-33.git
cd md-33
```

### 2. Verificar un documento cualquiera

```bash
# Solo calcular hash
python src/verifica_estandar.py mi_documento.pdf

# Comparar contra hash esperado
python src/verifica_estandar.py mi_documento.pdf --hash-esperado abc123...

# Verificar firma ECDSA
python src/verifica_estandar.py mi_documento.pdf --firma firma.sig --pubkey pub.pem

# Salida JSON (para integración con otros sistemas)
python src/verifica_estandar.py mi_documento.pdf --json
```

### 3. Usar la plantilla de acta

Copia `plantillas/acta_perito_vacia.md`, llena los campos, y aplica el protocolo de verificación. La plantilla es **bilingüe ES/EN** y cumple con el formato de cadena de custodia para MX, USA, UE e Israel.

---

## 📂 Estructura

```text
md-33/
├── README.md                              ← este archivo
├── LICENSE                                ← CC0 + Cláusula Comercial MD-33
├── MANUAL_PERITO_INTERNACIONAL_MD33.md    ← protocolo forense v1.0
├── _config.yml                            ← Jekyll
├── index.md                               ← landing page del sitio
│
├── plantillas/
│   └── acta_perito_vacia.md               ← plantilla bilingüe editable
│
├── src/
│   └── verifica_estandar.py               ← verificador genérico
│
├── manual/                                ← caso demostrativo (ficción)
├── actas/                                 ← caso demostrativo (ficción)
├── evidencia/                             ← caso demostrativo (ficción)
├── assets/                                ← CSS, JS, imágenes
├── _includes/                             ← componentes HTML
└── _layouts/                              ← plantillas Jekyll
```

---

## 📊 Capas de verificación

| Capa | Estándar | Verificable por |
|------|----------|-----------------|
| Documental | ISO 27037 | Cualquier perito |
| Criptográfica | ISO 17025 | Cualquier perito con clave pública |
| Temporal | RFC 3161 | TSA autorizada |
| Blockchain | EIP-191 | Cualquier nodo Ethereum |
| Cultural (opcional) | Gematría + Atbash | Perito con conocimiento de cábala |

---

## ⚖️ Cumplimiento legal por país

| País | Ley aplicable | Autoridad | Registro |
|------|---------------|-----------|----------|
| 🇲🇽 México | LFDA · CNPP Art. 227 | INDAUTOR · Fiscalía | Oficio + sello digital |
| 🇺🇸 USA | FRE 902(13)-(14) | NIST · FBI | Hash + cadena de custodia |
| 🇪🇺 UE | eIDAS 910/2014 | ENISA | Firma cualificada |
| 🇮🇱 Israel | Evidence Ordinance | Ministry of Justice | Certificado digital |

---

## 🤝 Contribuir

1. Haz fork del repositorio
2. Aplica el framework a un caso real (documento público, contrato, acta)
3. Documenta el proceso siguiendo el manual
4. Envía un Pull Request con tu caso

---

## ⚖️ Licencia

**CC0 1.0 Universal + Cláusula Comercial MD-33.** Ver [LICENSE](LICENSE).

Puedes copiar, modificar, distribuir y usar comercialmente el framework sin permiso previo.

---

<div align="center">

```text
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   FRAMEWORK MD-33 · v1.0 · 2026-09-14                                        ║
║   Caso demostrativo: ficción · Framework: real                               ║
║   ISO 27037 · ISO 17025 · RFC 3161 · EIP-191                                 ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

</div>