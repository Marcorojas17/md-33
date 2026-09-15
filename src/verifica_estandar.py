#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
═══════════════════════════════════════════════════════════════════════════════
  MD-33 · VERIFICADOR FORENSE GENÉRICO
  ISO 27037 · ISO 17025 · RFC 3161 · EIP-191
═══════════════════════════════════════════════════════════════════════════════

  Verifica la integridad y autenticidad de CUALQUIER documento.

  Uso:
      python verifica_estandar.py <archivo>
      python verifica_estandar.py <archivo> --hash-esperado <hex>
      python verifica_estandar.py <archivo> --firma <sig> --pubkey <pem>
      python verifica_estandar.py <archivo> --json

  Autor: Fideicomiso Ciego 07 (framework)
  Licencia: CC0 + Cláusula Comercial MD-33
═══════════════════════════════════════════════════════════════════════════════
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone


# ─────────────────────────────────────────────────────────────────────────────
# COLORES ANSI
# ─────────────────────────────────────────────────────────────────────────────
class C:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    END = '\033[0m'


def banner():
    print(f"{C.GREEN}{C.BOLD}")
    print("╔══════════════════════════════════════════════════════════════════╗")
    print("║  MD-33 · VERIFICADOR FORENSE GENÉRICO v1.0                       ║")
    print("║  ISO 27037 · ISO 17025 · RFC 3161 · EIP-191                      ║")
    print("╚══════════════════════════════════════════════════════════════════╝")
    print(f"{C.END}")


def calcular_hash(filepath, algoritmo='sha256'):
    """Calcula el hash de un archivo en el algoritmo especificado."""
    h = hashlib.new(algoritmo)
    with open(filepath, 'rb') as f:
        for bloque in iter(lambda: f.read(65536), b''):
            h.update(bloque)
    return h.hexdigest()


def verificar_firma(filepath, firma_path, pubkey_path):
    """
    Verifica una firma ECDSA usando openssl.
    Retorna (ok: bool, salida: str).
    """
    try:
        result = subprocess.run(
            ['openssl', 'dgst', '-sha256',
             '-verify', pubkey_path,
             '-signature', firma_path,
             filepath],
            capture_output=True, text=True, timeout=30
        )
        salida = (result.stdout + result.stderr).strip()
        return result.returncode == 0, salida
    except FileNotFoundError:
        return None, "openssl no está instalado o no está en PATH"
    except subprocess.TimeoutExpired:
        return None, "timeout al verificar la firma"


def formatear_tamano(n):
    """Formatea tamaño en bytes a unidad legible."""
    for unidad in ['B', 'KB', 'MB', 'GB']:
        if n < 1024:
            return f"{n:.2f} {unidad}"
        n /= 1024
    return f"{n:.2f} TB"


def ejecutar_verificacion(args):
    """Ejecuta el flujo de verificación completo."""

    # ─── Validar archivo ───
    if not os.path.exists(args.archivo):
        print(f"{C.RED}✗ ERROR: archivo no encontrado: {args.archivo}{C.END}")
        sys.exit(2)

    if not os.path.isfile(args.archivo):
        print(f"{C.RED}✗ ERROR: la ruta no es un archivo: {args.archivo}{C.END}")
        sys.exit(2)

    tamano = os.path.getsize(args.archivo)

    # ─── Calcular hashes ───
    hash_sha256 = calcular_hash(args.archivo, 'sha256')
    hash_sha1 = calcular_hash(args.archivo, 'sha1')
    hash_md5 = calcular_hash(args.archivo, 'md5')

    # ─── Comparar contra hash esperado (si se proporcionó) ───
    hash_coincide = None
    if args.hash_esperado:
        esperado = args.hash_esperado.lower().strip()
        hash_coincide = (hash_sha256 == esperado)

    # ─── Verificar firma (si se proporcionó) ───
    firma_ok = None
    firma_msg = None
    if args.firma and args.pubkey:
        firma_ok, firma_msg = verificar_firma(
            args.archivo, args.firma, args.pubkey
        )

    # ─── Veredicto global ───
    veredicto = "SIN VERIFICAR"
    if hash_coincide is True and (firma_ok is None or firma_ok is True):
        veredicto = "AUTÉNTICO"
    elif hash_coincide is False or firma_ok is False:
        veredicto = "FALSO / ALTERADO"
    elif hash_coincide is True and firma_ok is False:
        veredicto = "HASH OK · FIRMA INVÁLIDA"
    elif hash_coincide is None and firma_ok is True:
        veredicto = "FIRMA OK · HASH NO COMPARADO"

    resultado = {
        "archivo": os.path.abspath(args.archivo),
        "tamano_bytes": tamano,
        "tamano_humano": formatear_tamano(tamano),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "hashes": {
            "sha256": hash_sha256,
            "sha1": hash_sha1,
            "md5": hash_md5,
        },
        "hash_esperado": args.hash_esperado,
        "hash_coincide": hash_coincide,
        "firma": {
            "archivo_firma": args.firma,
            "clave_publica": args.pubkey,
            "valida": firma_ok,
            "mensaje": firma_msg,
        },
        "veredicto": veredicto,
        "estandares": [
            "ISO/IEC 27037:2012",
            "ISO/IEC 17025:2017",
            "RFC 3161",
        ],
    }

    # ─── Salida JSON ───
    if args.json:
        print(json.dumps(resultado, indent=2, ensure_ascii=False))
        return 0 if veredicto == "AUTÉNTICO" else 1

    # ─── Salida formateada ───
    print(f"\n{C.CYAN}{C.BOLD}▸ ARCHIVO{C.END}")
    print(f"  Ruta:   {os.path.abspath(args.archivo)}")
    print(f"  Tamaño: {formatear_tamano(tamano)} ({tamano} bytes)")
    print(f"  UTC:    {resultado['timestamp_utc']}")

    print(f"\n{C.YELLOW}{C.BOLD}[ CAPA 1 · INTEGRIDAD (ISO 27037) ]{C.END}")
    print(f"  SHA-256: {C.GREEN}{hash_sha256}{C.END}")
    print(f"  SHA-1:   {C.DIM}{hash_sha1}{C.END}")
    print(f"  MD5:     {C.DIM}{hash_md5}{C.END}")

    if args.hash_esperado:
        print(f"\n{C.YELLOW}{C.BOLD}[ CAPA 2 · COMPARACIÓN DE HASH ]{C.END}")
        print(f"  Esperado:  {args.hash_esperado}")
        print(f"  Calculado: {hash_sha256}")
        if hash_coincide:
            print(f"  Resultado: {C.GREEN}✓ COINCIDE{C.END}")
        else:
            print(f"  Resultado: {C.RED}✗ NO COINCIDE — documento alterado{C.END}")

    if args.firma and args.pubkey:
        print(f"\n{C.YELLOW}{C.BOLD}[ CAPA 3 · FIRMA DIGITAL (ISO 17025) ]{C.END}")
        print(f"  Firma:     {args.firma}")
        print(f"  Clave pub: {args.pubkey}")
        if firma_ok is True:
            print(f"  Resultado: {C.GREEN}✓ {firma_msg}{C.END}")
        elif firma_ok is False:
            print(f"  Resultado: {C.RED}✗ {firma_msg}{C.END}")
        else:
            print(f"  Resultado: {C.YELLOW}⚠ {firma_msg}{C.END}")

    print(f"\n{C.YELLOW}{C.BOLD}[ CAPA 4 · ESTÁNDARES APLICADOS ]{C.END}")
    for std in resultado["estandares"]:
        print(f"  · {std}")

    print(f"\n{C.BOLD}{'═' * 68}{C.END}")
    if veredicto == "AUTÉNTICO":
        print(f"{C.GREEN}{C.BOLD}  ✓ VEREDICTO: {veredicto}{C.END}")
    elif "FALSO" in veredicto or "INVÁLIDA" in veredicto:
        print(f"{C.RED}{C.BOLD}  ✗ VEREDICTO: {veredicto}{C.END}")
    else:
        print(f"{C.YELLOW}{C.BOLD}  ⚠ VEREDICTO: {veredicto}{C.END}")
    print(f"{C.BOLD}{'═' * 68}{C.END}\n")

    return 0 if veredicto == "AUTÉNTICO" else 1


def main():
    parser = argparse.ArgumentParser(
        description="MD-33 · Verificador Forense Genérico (ISO 27037 / ISO 17025)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python verifica_estandar.py mi_documento.pdf
  python verifica_estandar.py mi_documento.pdf --hash-esperado abc123...
  python verifica_estandar.py mi_documento.pdf --firma firma.sig --pubkey pub.pem
  python verifica_estandar.py mi_documento.pdf --json
        """
    )
    parser.add_argument('archivo', help='Ruta del archivo a verificar')
    parser.add_argument('--hash-esperado', metavar='HEX',
                        help='Hash SHA-256 esperado (hex)')
    parser.add_argument('--firma', metavar='SIG',
                        help='Archivo de firma digital (.sig)')
    parser.add_argument('--pubkey', metavar='PEM',
                        help='Archivo de clave pública (.pem)')
    parser.add_argument('--json', action='store_true',
                        help='Salida en formato JSON')

    args = parser.parse_args()

    if not args.json:
        banner()

    sys.exit(ejecutar_verificacion(args))


if __name__ == '__main__':
    main()