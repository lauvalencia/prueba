import json
import sys
from pathlib import Path

REQUIRED_LANGS = ("es", "en", "fr", "it")


def main() -> None:
    path = Path(__file__).resolve().parent / "test_localization.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ALERTA: No se encontró el archivo {path}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ALERTA: JSON inválido: {e}", file=sys.stderr)
        sys.exit(1)

    translations = data.get("translations")
    if translations is None:
        print(
            "ALERTA: No existe 'translations' o faltan idiomas. "
            f"Se requieren las claves: {', '.join(REQUIRED_LANGS)}"
        )
        sys.exit(1)

    if not isinstance(translations, dict):
        print("ALERTA: 'translations' debe ser un objeto (diccionario).")
        sys.exit(1)

    missing = [lang for lang in REQUIRED_LANGS if lang not in translations]
    if missing:
        print(f"ALERTA: Faltan los idiomas: {', '.join(missing)}")
        sys.exit(1)

    print("Localización completa")


if __name__ == "__main__":
    main()
