#!/usr/bin/env python3
"""Audit a repository against production AI product foundations."""

from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import asdict, dataclass
from pathlib import Path


IGNORED_DIRECTORIES = {
    ".git",
    ".next",
    ".turbo",
    ".venv",
    "coverage",
    "dist",
    "node_modules",
    "skills",
    "vendor",
}

TEXT_SUFFIXES = {
    ".cjs",
    ".css",
    ".go",
    ".html",
    ".java",
    ".js",
    ".json",
    ".jsx",
    ".md",
    ".mjs",
    ".py",
    ".rb",
    ".rs",
    ".scss",
    ".sh",
    ".sql",
    ".toml",
    ".ts",
    ".tsx",
    ".yaml",
    ".yml",
}

PLACEHOLDER_PATTERNS = (
    ("unfinished marker", re.compile(r"\b(?:TO" + r"DO|TBD|FIXME)\b", re.IGNORECASE)),
    ("filler copy", re.compile(r"lorem\s+ipsum", re.IGNORECASE)),
    ("generic placeholder", re.compile(r"\bplaceholder\s+(?:text|content|copy)\b", re.IGNORECASE)),
)

PROFILE_FILES = {
    "product": ("README.md", "AGENTS.md", "PRODUCT.md", "DESIGN.md"),
    "os": (
        "README.md",
        "AGENTS.md",
        "CODEX.md",
        "PRODUCT.md",
        "DESIGN.md",
        "CONTRIBUTING.md",
        "LICENSE",
    ),
}

OS_DIRECTORIES = (
    "docs",
    "design-system",
    "component-bible",
    "prompt-library",
    "templates",
    "review",
    "references",
    ".github",
    "scripts",
    "examples",
)


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: str
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check repository foundations and unfinished generated content."
    )
    parser.add_argument("repository", type=Path, help="Repository root to inspect")
    parser.add_argument(
        "--profile",
        choices=tuple(PROFILE_FILES),
        default="product",
        help="Expected repository contract",
    )
    parser.add_argument("--json", action="store_true", help="Emit machine-readable output")
    return parser.parse_args()


def iter_text_files(root: Path):
    for current_root, directory_names, file_names in os.walk(root):
        directory_names[:] = [
            name for name in directory_names if name not in IGNORED_DIRECTORIES
        ]
        current = Path(current_root)
        for file_name in file_names:
            path = current / file_name
            if path.suffix.lower() in TEXT_SUFFIXES or file_name in {"LICENSE"}:
                yield path


def inspect(root: Path, profile: str) -> list[Finding]:
    findings: list[Finding] = []
    for relative_path in PROFILE_FILES[profile]:
        path = root / relative_path
        if not path.is_file():
            findings.append(
                Finding("P1", "missing-core-file", relative_path, "Required source of truth is missing.")
            )
        elif path.stat().st_size < 80:
            findings.append(
                Finding("P1", "empty-core-file", relative_path, "Core document is too small to define a useful contract.")
            )

    if profile == "os":
        for relative_path in OS_DIRECTORIES:
            path = root / relative_path
            if not path.is_dir():
                findings.append(
                    Finding("P2", "missing-system-directory", relative_path, "Expected operating-system capability is absent.")
                )

    for path in iter_text_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        relative_path = str(path.relative_to(root))
        for label, pattern in PLACEHOLDER_PATTERNS:
            match = pattern.search(text)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                findings.append(
                    Finding(
                        "P1",
                        "unfinished-content",
                        f"{relative_path}:{line}",
                        f"Found {label}; replace it with real project content.",
                    )
                )

    return sorted(findings, key=lambda item: (item.severity, item.path, item.code))


def main() -> int:
    args = parse_args()
    root = args.repository.expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"Repository does not exist or is not a directory: {root}")

    findings = inspect(root, args.profile)
    if args.json:
        print(
            json.dumps(
                {
                    "repository": str(root),
                    "profile": args.profile,
                    "finding_count": len(findings),
                    "findings": [asdict(finding) for finding in findings],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    elif findings:
        for finding in findings:
            print(f"[{finding.severity}] {finding.code} {finding.path}: {finding.message}")
        print(f"\n{len(findings)} finding(s).")
    else:
        print(f"No baseline findings for the {args.profile} profile: {root}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
