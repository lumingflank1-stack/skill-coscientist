#!/usr/bin/env python3
"""Create a reusable biomedical co-scientist report scaffold."""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


def slugify(text: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "-", text.strip()).strip("-").lower()
    return slug or "co-scientist-project"


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def create_hypothesis_cards(project: str, count: int) -> str:
    blocks = [f"# Hypothesis Cards: {project}\n"]
    for idx in range(1, count + 1):
        blocks.append(
            f"""## H{idx}. Mechanistic Name

- Core mechanism:
- Predicted molecular or cellular axis:
- Primary evidence:
- Evidence tier:
- Key predictions:
- Critical weakness:
- Alternative explanation:
- Bioinformatics tests:
- Decisive experiment:
- Falsification criteria:
- Translational angle:
- Current status: candidate
"""
        )
    return "\n".join(blocks)


def create_analysis_plan(project: str) -> str:
    return f"""# Bioinformatics Analysis Plan: {project}

## Analysis Objective

## Input Data

## Required Metadata

## Preprocessing and QC

## Main Model or Comparison

## Covariates and Confounders

## Decision Rules

## Expected Tables

## Expected Figures

## Failure Modes
"""


def create_final_report(project: str) -> str:
    return f"""# Co-Scientist Report: {project}

## Research Question

## Evidence Ledger Summary

## Prioritized Hypotheses

## Critical Review

## Bioinformatics Findings

## Revised Hypothesis Set

## Wet-Lab Validation Plan

## Translational Strategy

## Manuscript or Grant Framing
"""


def write_csv(path: Path, rows: list[list[str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, help="Project name for headings.")
    parser.add_argument("--out", help="Output directory. Defaults to ./<project-slug>.")
    parser.add_argument("--hypotheses", type=int, default=5, help="Number of hypothesis cards.")
    args = parser.parse_args()

    if args.hypotheses < 1:
        raise SystemExit("--hypotheses must be at least 1")

    out_dir = Path(args.out or slugify(args.project)).expanduser().resolve()
    if out_dir.exists():
        raise SystemExit(f"Refusing to overwrite existing directory: {out_dir}")

    out_dir.mkdir(parents=True)

    write_text(out_dir / "hypothesis_cards.md", create_hypothesis_cards(args.project, args.hypotheses))
    write_text(out_dir / "analysis_plan.md", create_analysis_plan(args.project))
    write_text(out_dir / "final_report.md", create_final_report(args.project))

    write_csv(
        out_dir / "evidence_ledger.csv",
        [
            ["claim", "source", "evidence_class", "strength", "limitations", "notes"],
        ],
    )
    write_csv(
        out_dir / "prioritization.csv",
        [
            [
                "rank",
                "hypothesis",
                "novelty",
                "evidence",
                "feasibility",
                "causal_testability",
                "translation",
                "total",
                "decision",
            ],
        ],
    )

    print(f"Created scaffold: {out_dir}")


if __name__ == "__main__":
    main()
