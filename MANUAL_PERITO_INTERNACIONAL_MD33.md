---
layout: manual
title: Manual Perito Internacional MD-33
---

<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- MD-33 · MANUAL PERITO INTERNACIONAL · v1.0                             -->
<!-- Estándar de verificación forense · ISO 27037 · ISO 17025               -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->

<div align="center">

```text
╔══════════════════════════════════════════════════════════════════════════════╗
║ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ║
║ ▓                                                                          ▓ ║
║ ▓   ███╗   ███╗██████╗        ██████╗ ██████╗   ██████╗ ██╗                ▓ ║
║ ▓   ████╗ ████║██╔══██╗      ██╔════╝ ╚════██╗ ██╔═══██╗██║                ▓ ║
║ ▓   ██╔████╔██║██║  ██║█████╗███████╗  █████╔╝ ██║   ██║██║                ▓ ║
║ ▓   ██║╚██╔╝██║██║  ██║╚════╝╚════██║  ╚═══██╗ ██║▄▄ ██║██║                ▓ ║
║ ▓   ██║ ╚═╝ ██║██████╔╝      ██████╔╝ ██████╔╝ ╚██████╔╝███████╗           ▓ ║
║ ▓   ╚═╝     ╚═╝╚═════╝       ╚═════╝  ╚═════╝   ╚══▀▀═╝ ╚══════╝           ▓ ║
║ ▓                                                                          ▓ ║
║ ▓   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   ▓ ║
║ ▓   P E R I T O   I N T E R N A C I O N A L   ·   v 1 . 0                  ▓ ║
║ ▓   I S O   2 7 0 3 7   ·   I S O   1 7 0 2 5   ·   R F C   3 1 6 1         ▓ ║
║ ▓   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━   ▓ ║
║ ▓                                                                          ▓ ║
║ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

[![ISO 27037](https://img.shields.io/badge/ISO-27037-00ff41?style=for-the-badge&labelColor=0a0d10)](https://www.iso.org/standard/44381.html)
[![ISO 17025](https://img.shields.io/badge/ISO-17025-ffcc00?style=for-the-badge&labelColor=0a0d10)](https://www.iso.org/standard/66912.html)
[![RFC 3161](https://img.shields.io/badge/RFC-3161-8b5cf6?style=for-the-badge&labelColor=0a0d10)](https://datatracker.ietf.org/doc/html/rfc3161)
[![RFC 8785](https://img.shields.io/badge/RFC-8785-ff00ff?style=for-the-badge&labelColor=0a0d10)](https://datatracker.ietf.org/doc/html/rfc8785)
[![CC0](https://img.shields.io/badge/license-CC0%20%2B%20Comercial-00ffff?style=for-the-badge&labelColor=0a0d10)](LICENSE)

</div>

---

## 📖 1. Propósito y Alcance

Este manual define el **estándar internacional de verificación forense** para el activo digital **MD-33** (Folio `2607086319439`). Su objetivo es que cualquier perito, en cualquier jurisdicción, pueda verificar de manera independiente:

1. La **autenticidad** del acta de cadena de custodia.
2. La **integridad** del activo digital (hash SHA-256).
3. La **validez** de la firma digital (ECDSA P-256).
4. La **existencia** del documento en una fecha determinada (timestamp y anclaje).
5. La **procedencia** legal del activo (registro y bloqueo).

Este estándar es **interoperable** entre México, Estados Unidos, Unión Europea e Israel, y no depende de software propietario.

---

## ⚖️ 2. Referencias Normativas

| Norma | Descripción | Aplicación en MD-33 |
|-------|-------------|---------------------|
| **ISO/IEC 27037:2012** | Guía para identificación, recolección, adquisición y preservación de evidencia digital | Cadena de custodia del activo MD-33 |
| **ISO/IEC 17025:2017** | Requisitos generales para la competencia de laboratorios de ensayo y calibración | Verificación de hash y firma |
| **RFC 3161** | Protocolo de sellado de tiempo (TSP) | Timestamp confiable |
| **RFC 8785** | JSON Canonicalization Scheme (JCS) | Serialización determinista |
| **RFC 7515** | JSON Web Signature (JWS) | Firma digital |
| **RFC 7517** | JSON Web Key (JWK) | Clave pública |
| **EIP-191** | Signed Data Standard (Ethereum) | Anclaje blockchain |
| **LFDA** (México) | Ley Federal del Derecho de Autor | Bloqueo INDAUTOR |
| **GDPR** (UE) | Protección de datos | Manejo de metadatos personales |

---

## 🔐 3. Definiciones

- **Activo digital:** Cristal MD-33 + acta + payload + firmware.
- **Hash SHA-256:** Huella criptográfica única de 64 caracteres hexadecimales.
- **Firma ECDSA:** Firma asimétrica con curva P-256.
- **Anclaje blockchain:** Registro público inmutable de la existencia del hash.
- **Cadena de custodia:** Registro cronológico de cada interacción con el activo.
- **Dead Man's Switch:** Mecanismo automático que se activa si el titular no valida en plazo.

---

## 🧪 4. Protocolo de Recolección (ISO 27037)

### 4.1 Identificación

El perito debe identificar:

- **Folio único:** `2607086319439`
- **Hash SHA-256:** `a3f9c82e6b4d5f71b8e34d9c0f2a6e7d5b9c84e1f3d2b6a7c9e0d5f801`
- **Firma ECDSA:** cadena Base64 (ver §6)
- **Serial interno:** `MD33-91B7-K889`
- **Lote:** `MD-33-2025-0912`
- **Composición química:** `SiO2 78% / B2O3 12% / Na2O 10%`
- **Peso:** `33.4 g ± 0.001 g`
- **Geolocalización de origen:** `ALMACEN_07 · 19.4326°N, 99.1332°W`
- **Geolocalización de destino:** `Muelle 42, Newark · 40.7205°N, 74.0137°W`
- **Timestamp UTC:** `2026-09-14T03:21:21Z`

### 4.2 Adquisición

El perito debe adquirir:

1. **Copia bit-a-bit** del acta original (formato PDF/A + MD).
2. **Volcado HEX** del payload (`4D 44 33 33 0D 0A...`).
3. **Captura de pantalla** del registro INDAUTOR.
4. **Comprobante de anclaje** en Ethereum y Safe Creative.
5. **Log de custodia** en formato JSON canonicalizado (RFC 8785).

### 4.3 Preservación

- Almacenar en **dos medios independientes** (uno offline).
- Calcular **hash de cada copia** y comparar con el original.
- Registrar **custodio, fecha, hora UTC, geolocalización**.
- Firmar el registro con la **clave privada del perito**.

---

## 🔬 5. Protocolo de Verificación (ISO 17025)

### 5.1 Verificación del hash SHA-256

**En Linux / macOS / WSL:**

```bash
# Del acta en markdown
sha256sum MANUAL_PERITO_INTERNACIONAL_MD33.md

# Del payload HEX
xxd -r -p payload_XT-77G.hex | sha256sum

# Comparación esperada
# a3f9c82e6b4d5f71b8e34d9c0f2a6e7d5b9c84e1f3d2b6a7c9e0d5f801
```

**En Windows (PowerShell):**

```powershell
Get-FileHash .\MANUAL_PERITO_INTERNACIONAL_MD33.md -Algorithm SHA256
```

**Criterio de aceptación:** el hash calculado debe coincidir **exactamente** con el hash registrado. Si difiere en un solo carácter, el documento es **falso**.

### 5.2 Verificación de la firma ECDSA

```bash
# Extraer firma y clave pública
openssl dgst -sha256 \
  -verify pubkey.pem \
  -signature firma_ecdsa.sig \
  payload_XT-77G.bin

# Salida esperada
# Verified OK
```

**Criterio de aceptación:** `Verified OK`. Si devuelve `Verification failure`, la firma es **inválida**.

### 5.3 Verificación del timestamp (RFC 3161)

```bash
openssl ts -verify \
  -in timestamp.tsr \
  -data payload_XT-77G.bin \
  -CAfile tsa_ca.pem
```

**Criterio de aceptación:** `Verification: OK`. El timestamp debe ser **posterior** a la creación del documento y **anterior** a su publicación.

---

## 🌐 6. Anclaje Internacional

El estándar MD-33 requiere **tres anclajes independientes**:

### 6.1 Safe Creative (España · UE)

- **Registro:** `2607086319439`
- **URL:** https://www.safecreative.org/certificate/2607086319439
- **Validez legal:** UE, LATAM, USA
- **Verificación:** consultar el certificado público.

### 6.2 OpenTimestamps (Bitcoin)

- **Archivo:** `payload_XT-77G.ots`
- **Verificación:**

```bash
ots verify payload_XT-77G.ots
# Salida esperada:
# Success! Bitcoin block 812345 attests existence as of 2026-09-14 UTC
```

### 6.3 Ethereum (EIP-191)

- **Transacción:** `0x8ca8e84e1258abac9acb29d14d25114e4775d782ecfda51ae29933247ed2970e`
- **Verificación:**

```bash
cast tx 0x8ca8e84e1258abac9acb29d14d25114e4775d782ecfda51ae29933247ed2970e --rpc-url https://eth.llamarpc.com
```

### 6.4 IPFS (opcional, recomendado)

```bash
ipfs add payload_XT-77G.bin
# Salida: QmXyZ...
ipfs pin add QmXyZ...
```

El hash IPFS debe registrarse en el acta.

---

## 📜 7. Acta Bilingüe ES/EN

El acta debe presentarse en **dos idiomas** para validez internacional. Estructura mínima:

### 7.1 Encabezado / Header

| Español (MX) | English (US/EU) |
|--------------|-----------------|
| ACTA OFICIAL DE CADENA DE CUSTODIA FORENSE | OFFICIAL FORENSIC CHAIN OF CUSTODY RECORD |
| FOLIO ÚNICO: 2607086319439 | UNIQUE FILE NUMBER: 2607086319439 |
| FECHA: 2026-09-14 09:35 h (UTC-6) | DATE: 2026-09-14 09:35 (UTC-6) |
| AUTORIDAD: Fiscalía General del Estado | AUTHORITY: State Attorney General's Office |

### 7.2 Cuerpo / Body

| Campo | Español | English |
|-------|---------|---------|
| Indicio | Dispositivo USB, 32GB, serie USB32684721 | USB storage device, 32GB, serial USB32684721 |
| Custodio 1 | Lic. Mariana Torres Delgado | Atty. Mariana Torres Delgado |
| Custodio 2 | C. Roberto Hernández Vega | Mr. Roberto Hernández Vega |
| Hash | a3f9c82e...5f801 | a3f9c82e...5f801 (same) |
| Firma | ECDSA P-256 | ECDSA P-256 (same) |

### 7.3 Pie / Footer

```
Documento ficticio para simulación (ARG). No constituye acto jurídico real.
Fictional document for simulation purposes (ARG). Not a legally binding instrument.
```

---

## 🔯 8. Capa Cabalística (Sello Único MD-33)

Este es el **elemento diferenciador** del estándar MD-33: una capa de verificación basada en **gematría hebrea y Atbash**, que ningún otro estándar internacional posee.

### 8.1 Fundamento

El folio `2607086319439` se descompone en pares y se aplica **Atbash** (Aleph↔Tav, Bet↔Shin, etc.) para generar un **nombre cabalístico** que actúa como sello mnemotécnico.

### 8.2 Ejemplo de verificación

```text
Folio: 2607086319439
Pares: 26 · 07 · 08 · 63 · 19 · 43 · 9
Atbash hebreo: תאאתששבבפזעוזעוף
Gematría: 1732
Nombre resultante: Jesed (חסד)
Significado: Misericordia · Lealtad · Pacto
```

### 8.3 Función forense

El sello cabalístico **no reemplaza** al hash ni a la firma ECDSA. Es una **capa adicional de memoria y verificación**:

- Si el perito recuerda el nombre `Jesed`, puede verificar el folio por gematría.
- Si el hash y la firma fallan, el sello cabalístico indica **manipulación intencional**.
- En caso de disputa legal, el sello es **prueba cultural** de autoría.

### 8.4 Verificación cruzada

| Capa | Tipo | Verificable por |
|------|------|-----------------|
| Hash SHA-256 | Matemática | Cualquier perito |
| Firma ECDSA | Criptográfica | Cualquier perito con clave pública |
| Timestamp | Temporal | TSA autorizada |
| Anclaje blockchain | Pública | Cualquier nodo |
| Sello cabalístico | Cultural | Perito con conocimiento de gematría |

---

## 📋 9. Plantilla para Casos Propios

Cualquier perito puede usar este manual como **plantilla** para crear su propio caso. Solo debe reemplazar:

```yaml
folio: "TU_FOLIO_AQUI"
hash_sha256: "TU_HASH_AQUI"
firma_ecdsa: "TU_FIRMA_AQUI"
serial: "TU_SERIAL_AQUI"
lote: "TU_LOTE_AQUI"
composicion: "TU_COMPOSICION_AQUI"
peso: "TU_PESO_AQUI"
geolocalizacion_origen: "TU_ORIGEN_AQUI"
geolocalizacion_destino: "TU_DESTINO_AQUI"
timestamp_utc: "TU_TIMESTAMP_AQUI"
safe_creative: "TU_REGISTRO_AQUI"
ethereum_tx: "TU_TX_AQUI"
ots_file: "TU_ARCHIVO_OTS_AQUI"
sello_cabalistico: "TU_SELLO_AQUI"
```

---

## ✅ 10. Checklist del Perito Internacional

- [ ] ¿El folio existe en el sistema de la Fiscalía?
- [ ] ¿El hash SHA-256 coincide con el registrado?
- [ ] ¿La firma ECDSA valida con la clave pública?
- [ ] ¿El timestamp es coherente con la fecha de creación?
- [ ] ¿El anclaje blockchain existe y es verificable?
- [ ] ¿El sello cabalístico coincide con el folio?
- [ ] ¿El peso y composición del cristal coinciden?
- [ ] ¿El micro-grabado es legible y coincide?
- [ ] ¿El acta está en dos idiomas?
- [ ] ¿El registro INDAUTOR está vigente?

Si **todas** las casillas están marcadas → el MD-33 es **auténtico**.
Si **alguna** falla → el MD-33 es **falso o está comprometido**.

---

## 📎 11. Anexos

### A. Comandos rápidos

```bash
# Todo en uno
sha256sum acta.md && \
openssl dgst -sha256 -verify pub.pem -signature firma.sig payload.bin && \
ots verify payload.ots && \
cast tx 0x8ca8e84e... --rpc-url https://eth.llamarpc.com
```

### B. Contacto del custodio

- **Titular:** Fideicomiso Ciego 07
- **Custodio físico:** ALMACEN_07 (CDMX)
- **Custodio digital:** AUTO-ANALYSIS v3.7.1
- **Custodio legal:** Fiscalía General del Estado

### C. Licencia

Este documento se publica bajo **CC0 + Uso Comercial**. Cualquier perito puede copiarlo, adaptarlo y usarlo sin restricciones.

---

<div align="center">

```text
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ESTÁNDAR MD-33 · v1.0 · 2026-09-14                                         ║
║   Verificable en México · USA · UE · Israel                                  ║
║   Hash: a3f9c82e...5f801 · Sello: Jesed · Folio: 2607086319439              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

> 📄 Documento ficticio para simulación (ARG). No constituye acto jurídico real.

</div>