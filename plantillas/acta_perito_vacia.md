---
layout: acta
title: Acta Perito (Plantilla)
---

# ACTA OFICIAL DE CADENA DE CUSTODIA FORENSE
# OFFICIAL FORENSIC CHAIN OF CUSTODY RECORD

**FORMATO / FORMAT:** MD-33 · Estándar Internacional v1.0

---

## I. DATOS GENERALES / GENERAL DATA

| Campo / Field | Valor / Value |
|---------------|---------------|
| Folio Único / Unique File Number | `___________________________` |
| Entidad Federativa / State | `___________________________` |
| Autoridad Requirente / Requesting Authority | `___________________________` |
| Unidad Responsable / Responsible Unit | `___________________________` |
| Fecha y Hora / Date & Time (UTC) | `___________________________` |
| Lugar de los Hechos / Scene Location | `___________________________` |
| Coordenadas GPS / GPS Coordinates | `___°N, ___°W` |

---

## II. DATOS DEL INDICIO / EVIDENCE DATA

| Campo / Field | Valor / Value |
|---------------|---------------|
| Número de Indicio / Evidence Number | `IND-____-____-______` |
| Tipo / Type | `___________________________` |
| Descripción / Description | `___________________________` |
| Marca / Brand | `___________________________` |
| Modelo / Model | `___________________________` |
| Número de Serie / Serial Number | `___________________________` |
| Estado / Condition | `___________________________` |

---

## III. REGISTRO DE CADENA DE CUSTODIA / CHAIN OF CUSTODY LOG

| Etapa / Stage | Responsable / Officer | Fecha y Hora / Date & Time | Acción / Action | Firma / Signature |
|---------------|----------------------|---------------------------|-----------------|-------------------|
| 1. Levantamiento / Collection | `_________________` | `_________________` | `_________________` | `_________` |
| 2. Traslado / Transfer | `_________________` | `_________________` | `_________________` | `_________` |
| 3. Recepción / Receipt | `_________________` | `_________________` | `_________________` | `_________` |
| 4. Análisis / Analysis | `_________________` | `_________________` | `_________________` | `_________` |
| 5. Resguardo / Storage | `_________________` | `_________________` | `_________________` | `_________` |

---

## IV. VERIFICACIÓN DE INTEGRIDAD DIGITAL / DIGITAL INTEGRITY VERIFICATION

| Algoritmo / Algorithm | Valor / Value |
|-----------------------|---------------|
| **SHA-256** | `___________________________________________________________` |
| **SHA-1** (referencia) | `________________________________________` |
| **MD5** (referencia) | `________________________________` |
| **Firma ECDSA** | `MEUCIQ...` (base64) |
| **Clave Pública / Public Key** | `___________________________` |
| **Timestamp RFC 3161** | `___________________________` |

**Método de firma / Signature Method:**
- Algoritmo: ☐ ECDSA P-256  ☐ RSA 2048  ☐ Ed25519  ☐ Otro: `_______`
- Herramienta / Tool: ☐ openssl  ☐ GPG  ☐ Otro: `_______`

---

## V. ANCLAJE EXTERNO / EXTERNAL ANCHORING

| Servicio / Service | Identificador / ID | URL / Link |
|--------------------|---------------------|------------|
| ☐ Safe Creative | `_________________` | `_________________` |
| ☐ OpenTimestamps (Bitcoin) | `_________________` | `_________________` |
| ☐ Ethereum (EIP-191) | `0x_______________` | `_________________` |
| ☐ IPFS | `Qm_______________` | `_________________` |
| ☐ Otro / Other | `_________________` | `_________________` |

---

## VI. OBSERVACIONES / OBSERVATIONS

```text
_______________________________________________________________________________

_______________________________________________________________________________

_______________________________________________________________________________
```

---

## VII. FIRMAS / SIGNATURES

| Rol / Role | Nombre / Name | Cédula / ID | Firma / Signature |
|------------|---------------|-------------|-------------------|
| Perito / Expert | `_________________` | `_________` | `_________` |
| Custodio / Custodian | `_________________` | `_________` | `_________` |
| Testigo / Witness | `_________________` | `_________` | `_________` |

---

## VIII. VERIFICACIÓN FINAL / FINAL VERIFICATION

- [ ] Folio registrado en el sistema oficial / File registered in official system
- [ ] Hash SHA-256 verificado / SHA-256 hash verified
- [ ] Firma digital validada / Digital signature validated
- [ ] Timestamp coherente / Timestamp coherent
- [ ] Anclaje blockchain verificado / Blockchain anchor verified
- [ ] Cadena de custodia completa / Complete chain of custody

**Veredicto / Verdict:**

☐ **AUTÉNTICO / AUTHENTIC** — Integridad confirmada
☐ **FALSO / FALSIFIED** — Documento alterado
☐ **INCOMPLETO / INCOMPLETE** — Falta verificación

---

> **Documento generado con el framework MD-33 v1.0**
> Estándares: ISO/IEC 27037 · ISO/IEC 17025 · RFC 3161 · EIP-191
> Framework: https://github.com/Marcorojas17/md-33
> Licencia: CC0 1.0 Universal + Cláusula Comercial MD-33

> ⚠ Esta es una plantilla vacía. El caso MD-33 demostrativo es ficción. El framework es real y usable.