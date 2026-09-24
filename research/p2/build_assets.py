"""Build the reproducible assets used by the P2 stress-test page."""

from pathlib import Path
import html
import json
import re

import matplotlib.pyplot as plt
import plotly.graph_objects as go


ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
ASSETS = DOCS / "assets" / "p2"
GENERATED = DOCS / "_generated"


def parse_bibtex_entry(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    return dict(re.findall(r"\s+(\w+)\s*=\s*\{([^{}]*)\}", text))


def build_static_plot() -> None:
    x_values = [1, 2, 3, 4, 5, 6]
    y_values = [1.1, 1.8, 3.2, 4.7, 6.1, 7.4]
    figure, axis = plt.subplots(figsize=(7, 4), dpi=150)
    axis.plot(x_values, y_values, marker="o", color="#1f6f78", linewidth=2)
    axis.set_title("Статический результат эксперимента")
    axis.set_xlabel("Номер измерения")
    axis.set_ylabel("Значение метрики")
    axis.grid(alpha=0.25)
    figure.tight_layout()
    figure.savefig(ASSETS / "static-result.png", bbox_inches="tight")
    plt.close(figure)


def build_interactive_plot() -> None:
    x_values = [1, 2, 3, 4, 5, 6]
    y_values = [1.1, 1.8, 3.2, 4.7, 6.1, 7.4]
    figure = go.Figure(
        go.Scatter(
            x=x_values,
            y=y_values,
            mode="lines+markers",
            name="Метрика",
            line={"color": "#b44b38", "width": 3},
        )
    )
    figure.update_layout(
        title="Интерактивный результат эксперимента",
        xaxis_title="Номер измерения",
        yaxis_title="Значение метрики",
        template="plotly_white",
        margin={"l": 50, "r": 20, "t": 60, "b": 45},
    )
    figure.write_html(
        ASSETS / "interactive-result.html",
        include_plotlyjs="cdn",
        full_html=False,
    )


def build_bibliography() -> None:
    entry = parse_bibtex_entry(Path(__file__).with_name("references.bib"))
    authors = html.escape(entry["author"].replace(" and ", ", "))
    title = html.escape(entry["title"])
    journal = html.escape(entry["journal"])
    url = html.escape(entry["url"], quote=True)
    content = (
        f"1. {authors}. {title}. *{journal}*, {entry['year']}, "
        f"{entry['volume']}, {entry['pages']}. "
        f"[Источник]({url})\n"
    )
    GENERATED.mkdir(parents=True, exist_ok=True)
    (GENERATED / "p2-bibliography.md").write_text(content, encoding="utf-8")


def main() -> None:
    ASSETS.mkdir(parents=True, exist_ok=True)
    build_static_plot()
    build_interactive_plot()
    build_bibliography()
    manifest = {
        "static_plot": "docs/assets/p2/static-result.png",
        "interactive_plot": "docs/assets/p2/interactive-result.html",
        "bibliography": "docs/_generated/p2-bibliography.md",
    }
    (GENERATED / "p2-manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
