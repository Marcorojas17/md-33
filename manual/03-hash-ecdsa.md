---
layout: manual
title: 03 · Hash y ECDSA
---

# 🔐 03 · Hash y Firma ECDSA

## 🧮 SHA-256

```text
a3f9c82e6b4d5f71b8e34d9c0f2a6e7d5b9c84e1f3d2b6a7c9e0d5f801
```

## ✍️ Firma ECDSA

| Campo | Valor |
|-------|-------|
| Algoritmo | ECDSA P-256 |
| Estado | ✅ VÁLIDA |
| Emisor | AUTO-ANALYSIS v3.7.1 |

## 🧪 Verificación

```bash
openssl dgst -sha256 -verify pub.pem -signature firma.sig payload.bin
```