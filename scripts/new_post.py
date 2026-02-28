#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import os
import re
from pathlib import Path
import subprocess
import sys

FRONT_MATTER = """---
layout: post
type: blog
title: "{title}"
date: {date}
description:
tags: []
image:
external_image:
youtube:
pinned: -1
---
"""

def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[’']", "", s)                 # remove apostrophes
    s = re.sub(r"[^a-z0-9]+", "-", s)          # non-alnum -> hyphen
    s = re.sub(r"-{2,}", "-", s).strip("-")    # collapse
    return s or "untitled"

def main() -> int:
    ap = argparse.ArgumentParser(description="Create a new Jekyll blog post")
    ap.add_argument("title", nargs="+", help="Post title")
    ap.add_argument("--dir", default="_posts", help="Posts directory (default: _posts)")
    ap.add_argument("--date", default=None, help="Date YYYY-MM-DD (default: today)")
    ap.add_argument("--open", action="store_true", help="Print created file path")
    args = ap.parse_args()

    title = " ".join(args.title)

    now = dt.datetime.now().astimezone()
    post_date = now.isoformat(timespec="seconds")  # e.g. 2026-02-28T15:13:36+00:00
    file_date = now.strftime("%Y-%m-%d")

    slug = slugify(title)

    posts_dir = Path(args.dir)
    posts_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{file_date}-{slug}.md"
    path = posts_dir / filename

    if path.exists():
        raise SystemExit(f"Refusing to overwrite existing file: {path}")

    path.write_text(
        FRONT_MATTER.format(
            title=title.replace('"', '\\"'),
            date=post_date
        ),
        encoding="utf-8"
    )

    if args.open:
        print(str(path))
        # 1) Try VS Code CLI if available
        try:
            subprocess.run(["code", "-r", str(path)], check=False)
            return 0
        except FileNotFoundError:
            pass

        # 2) Fallback: use VS Code "open file" URI (works if VS Code is installed)
        uri = "vscode://file/" + str(path.resolve()).replace("\\", "/")
        os.startfile(uri)



    return 0

if __name__ == "__main__":
    raise SystemExit(main())