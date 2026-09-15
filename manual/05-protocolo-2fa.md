
---

## 📄 Archivo 18 — `manual/05-protocolo-2fa.md`

```markdown
---
layout: manual
title: 05 · Protocolo 2FA
---

# 05 · Protocolo de Sucesión 2FA

## Regla

Nadie puede validar la firma `a3f9c82e…` sin:

1. **Factor 1** — Biometría del titular de ALMACEN_07.
2. **Factor 2** — Clave física `XT-77G` en Muelle 42, Newark.

## Dead Man's Switch

Si el contenedor se abre sin el Factor 1, el sistema genera acta automática ante la Fiscalía y bloquea el hash globalmente.

---
layout: acta
title: Actas
---

# Índice de Actas

- [Acta de Cadena de Custodia](acta-cadena-custodia.html)
- [Testamento Digital](testamento-digital.html)


---
layout: acta
title: Acta de Cadena de Custodia
---

## I. Datos Generales

| Campo | Valor |
|-------|-------|
| Entidad | Ciudad de México |
| Autoridad | Fiscalía General del Estado |
| Unidad | Criminalística de Campo |
| Fecha | 14 de septiembre de 2026, 09:35 h |

## II. Datos del Indicio

**Número:** IND-MD33-2026-0147

Dispositivo de almacenamiento USB, color negro, 32GB, serie SN: USB32684721.

## III. Registro de Cadena de Custodia

| Etapa | Responsable | Fecha | Acción |
|-------|-------------|-------|--------|
| 1. Levantamiento | Lic. Mariana Torres Delgado | 14/09/2026 09:35 | Embalaje en bolsa B-8847 |
| 2. Traslado | C. Roberto Hernández Vega | 14/09/2026 10:20 | Traslado seguro |
| 3. Recepción | Mtra. Claudia Reyes Soto | 14/09/2026 11:05 | Verificación e ingreso a LIMS |

## IV. Verificación Digital

- **SHA-256:** `3F1B8C9E7A5D2F6B4A9C1E8D0F4A6B2C7E5D9F3A1B6C8D4E0F7`
- **Firma ECDSA:** VÁLIDA

> Documento ficticio para simulación (ARG). Formato MD-33 rev. 2026-09.


---
layout: acta
title: Testamento Digital
---

## Declaración

Yo, titular del **Fideicomiso Ciego 07**, declaro que el Cristal MD-33 (Serial MD33-91B7-K889) se rige por las siguientes cláusulas.

## Cláusulas

1. **Transferencia Condicionada** — Requiere Factor 1 (biometría) + Factor 2 (clave XT-77G).
2. **Dead Man's Switch** — Apertura no autorizada activa acta automática.
3. **Administración** — GLASSLAB-MD, S.A. de C.V. actúa como fachada legal.

## Firma

- **Hash:** `3F1B8C9E7A5D2F6B4A9C1E8D0F4A6B2C7E5D9F3A1B6C8D4E0F7`
- **ECDSA:** VÁLIDA
- **Sello:** 2026-09-14 03:21:20 UTC

> Documento ficticio para simulación (ARG).

---
layout: manual
title: Evidencia
---

# Evidencia Digital

## Log de trazabilidad

```text
[2025-09-14 03:21:12] TRACE INIT...
[2025-09-14 03:21:13] HASH OK.
[2025-09-14 03:21:14] ESTEGO: Payload 48 bytes. INTEGRIDAD CONFIRMADA.
[2025-09-14 03:21:15] TRAZABILIDAD COMPLETA.

4D 44 33 33 0D 0A 4F 52 49 47 45 4E 3A 41 4C 4D
41 43 45 4E 5F 30 37 7C 44 45 53 54 3A 4C 41 42
5F 51 33 7C 43 4C 41 56 45 3A 58 54 2D 37 37 47

a3f9c82e6b4d5f71b8e34d9c0f2a6e7d5b9c84e1f3d2b6a7c9e0d5f801