import html
import shutil
from pathlib import Path

ROOT = Path(__file__).parent.parent
PROBLEMS = ROOT / "problems"
SCREENSHOTS = ROOT / "screenshots"
SITE = ROOT / "site"
ROMAN = {"ii", "iii", "iv"}

TEMPLATE = """<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>LeetCode Solutions</title>
<style>
body { font-family: system-ui, sans-serif; max-width: 860px; margin: 0 auto;
  padding: 24px; background: #f6f8fa; color: #1f2328; }
section { background: #fff; border: 1px solid #d0d7de; border-radius: 8px;
  padding: 16px 20px; margin-bottom: 20px; }
pre { background: #f6f8fa; padding: 12px; border-radius: 6px; overflow-x: auto; }
img { max-width: 100%; border-radius: 6px; }
</style>
</head>
<body>
<h1>LeetCode Solutions</h1>
<p>Решено задач: %COUNT%</p>
%CARDS%
</body>
</html>
"""


def parse_name(stem):
    *words, number = stem.split("_")
    title = " ".join(w.upper() if w in ROMAN else w.capitalize() for w in words)
    return int(number), title


def build():
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()
    if SCREENSHOTS.exists():
        shutil.copytree(SCREENSHOTS, SITE / "screenshots")

    items = []
    for path in PROBLEMS.glob("*.py"):
        if path.stem == "__init__":
            continue
        number, title = parse_name(path.stem)
        items.append((number, title, path))
    items.sort()

    cards = []
    for number, title, path in items:
        code = html.escape(path.read_text(encoding="utf-8"))
        img = ""
        if (SCREENSHOTS / f"task{number}.png").exists():
            img = f'<img src="screenshots/task{number}.png" alt="Task {number}">'
        cards.append(
            f"<section><h2>{number}. {title}</h2>"
            f"<pre><code>{code}</code></pre>{img}</section>"
        )

    page = TEMPLATE.replace("%COUNT%", str(len(items)))
    page = page.replace("%CARDS%", "\n".join(cards))
    (SITE / "index.html").write_text(page, encoding="utf-8")


if __name__ == "__main__":
    build()
