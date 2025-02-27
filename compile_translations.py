import polib
from pathlib import Path

locale_dir = Path("bus_booking/locale")  # Adjust as needed

for po_file in locale_dir.rglob("*.po"):
    mo_file = po_file.with_suffix(".mo")
    po = polib.pofile(str(po_file), encoding="utf-8")  # Ensure UTF-8 encoding
    po.save_as_mofile(str(mo_file))
    print(f"Compiled: {po_file} → {mo_file}")

print("All .po files compiled successfully!")
