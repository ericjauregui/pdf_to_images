from __future__ import annotations

import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
INPUT_DIR = PROJECT_ROOT / "input"
OUTPUT_DIR = PROJECT_ROOT / "output"


def ensure_directories() -> None:
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def get_input_pdfs() -> list[Path]:
    return sorted(
        path
        for path in INPUT_DIR.iterdir()
        if path.is_file() and path.suffix.lower() == ".pdf"
    )


def sanitize_stem(name: str) -> str:
    sanitized = re.sub(r"[^A-Za-z0-9_-]+", "_", name).strip("_")
    return sanitized or "file"


def convert_pdfs_to_images(pdf_files: list[Path]) -> None:
    from pdf2image import convert_from_path

    for pdf_path in pdf_files:
        safe_stem = sanitize_stem(pdf_path.stem)
        pages = convert_from_path(str(pdf_path))
        for count, page in enumerate(pages, start=1):
            output_file = OUTPUT_DIR / f"{safe_stem}{count}.png"
            page.save(output_file, "PNG")
            print(f"Saved {output_file.relative_to(PROJECT_ROOT)}")


def main() -> int:
    ensure_directories()

    pdf_files = get_input_pdfs()
    if not pdf_files:
        print("No PDF files found in input/. Add one or more .pdf files to input/ and run again.")
        return 1

    try:
        convert_pdfs_to_images(pdf_files)
    except Exception as exc:
        print(f"Failed to convert PDFs: {exc}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())