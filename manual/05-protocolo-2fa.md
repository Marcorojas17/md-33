---
layout: manual
title: 05 · Protocolo 2FA
---

# 🛡️ 05 · Protocolo de Sucesión 2FA

## 📜 Regla

Nadie puede validar la firma `a3f9c82e…` sin:

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  [ FACTOR 1 ]  🧬  Biometría del titular de ALMACEN_07                        │
│  [ FACTOR 2 ]  🔑  Clave física XT-77G en Muelle 42, Newark                   │
└──────────────────────────────────────────────────────────────────────────────┘
```

## 💀 Dead Man's Switch

Si el contenedor se abre sin el **Factor 1**, el sistema genera acta automática ante la Fiscalía y bloquea el hash globalmente.