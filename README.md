# pdf-to-images

Convert every `.pdf` file in `input/` into per-page `.png` images in `output/`.

## Behavior

- Creates `input/` and `output/` automatically if they do not exist.
- If no PDF files are found in `input/`, exits with an error message asking you to add files.
- Converts all pages from all PDFs in `input/`.
- Output naming format is `<pdf_file_name><count>.png` (for example: `catalog1.png`, `catalog2.png`).
- PDF file names are sanitized for output: spaces/special characters become `_`.

## Setup

```bash
uv sync
```

## Run

Preferred:

```bash
uv run python main.py
```

Also supported (if your venv is already activated):

```bash
python main.py
```

You can also run the script entrypoint:

```bash
uv run pdf-to-images
```
