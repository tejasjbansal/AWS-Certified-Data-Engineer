#!/usr/bin/env python3
"""
create_course_structure.py

Creates the folder structure for an AWS Data Engineering / Analytics course,
based on the section list from the course curriculum.

Each top-level section becomes a directory. A numbered prefix is added so
that the folders sort in the same order as the course outline. A simple
README.md placeholder is dropped inside each folder so the directories are
tracked by git (git does not track empty folders).

Usage:
    python create_course_structure.py [target_dir]

If target_dir is omitted, the structure is created in the current directory.
"""

import os
import sys

# Section name -> (lecture_count, duration)
SECTIONS = [
    ("Introduction", 5, "16min"),
    ("Data Ingestion", 6, "36min"),
    ("Querying with Athena", 6, "28min"),
    ("AWS Glue Deep Dive", 18, "1hr 48min"),
    ("Serverless Compute with Lambda", 3, "21min"),
    ("Data Streaming", 15, "1hr 58min"),
    ("Storage with S3", 20, "1hr 49min"),
    ("Other Storage Services", 6, "46min"),
    ("DynamoDB", 19, "2hr"),
    ("Redshift Datawarehouse", 29, "2hr 43min"),
    ("Other Database Services", 8, "46min"),
    ("Compute Services", 5, "29min"),
    ("Analytics", 23, "2hr 7min"),
    ("Machine Learning with SageMaker", 4, "25min"),
    ("Application Integration", 13, "1hr 20min"),
    ("Management, Monitoring, and Governance", 23, "2hr 8min"),
    ("Containers", 6, "37min"),
    ("Migration", 6, "33min"),
    ("VPCs", 5, "11min"),
    ("Security", 7, "38min"),
]


def slugify(name: str) -> str:
    """Turn a section title into a filesystem-friendly folder name."""
    keep = []
    for ch in name:
        if ch.isalnum() or ch in (" ", "-"):
            keep.append(ch)
    cleaned = "".join(keep).strip()
    return cleaned.replace(" ", "-")


def create_structure(base_dir: str) -> None:
    os.makedirs(base_dir, exist_ok=True)

    for index, (name, lectures, duration) in enumerate(SECTIONS, start=1):
        folder_name = f"{index:02d}-{slugify(name)}"
        folder_path = os.path.join(base_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Drop a small placeholder README so git tracks the (otherwise empty) folder
        readme_path = os.path.join(folder_path, "README.md")
        if not os.path.exists(readme_path):
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(f"# {name}\n\n")
                f.write(f"- Lectures: {lectures}\n")
                f.write(f"- Duration: {duration}\n")

        print(f"Created: {folder_path}")

    print(f"\nDone. {len(SECTIONS)} section directories created under '{base_dir}'.")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    create_structure(target)
