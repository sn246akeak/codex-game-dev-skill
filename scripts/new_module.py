#!/usr/bin/env python3
"""Create a micro-PRD handoff document for one game module."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value)
    return value.strip("-") or "module"


MODULE_TEMPLATE = """# Module Handoff: {name}

## Metadata / 工作约定

- Created: {today}
- State: intake_needed
- Owner: user + AI
- Source of Truth: {source}
- Document: discussion draft / 讨论稿，填充并审查后才能作为开发规格
- Delivery: daily Markdown / 日常开发模式；公司输出另读 company-delivery.md
- Rule owner / revision: 本文件定义本模块规则；共享规则注明归属文件与版本

## Objective

{purpose}

## Player-Facing Behavior

TBD

## Core Loop Touchpoint

TBD

## Scope / Non-goals

- Allowed changes: TBD
- Out of scope: TBD

## Operation and Lifecycle

- Trigger and ordered checks: TBD
- Success / state and data changes: TBD
- Invalid action / failure / cancel: TBD
- Exit / recovery, when applicable: TBD

## States Touched

- TBD

## Data Schema

| Field | Type | Required | Notes |
|---|---|---:|---|
| id | string | yes | Stable module/content ID |

区分运行时状态、静态配置与计算结果；自有配置写明用途、粒度、主键、字段约束与读取位置。公共规则引用其归属，不重复造表。无独立数据记录时删去示例 id 行。

## UI / Scene Touchpoints

- TBD

说明实际入口与去向、默认/选中/不可操作状态、处理中输入限制、成功/失败后的刷新。已完整复用的公共组件只写绑定及差异。不适用的项直接省略。

## Feedback Requirements

- Visual: TBD
- Audio: TBD
- Animation: TBD

实际文案与资源按需关联到状态；仅在项目多语言或公司交付要求下生成文案 ID/CSV。

## Acceptance Criteria

- {gate}

## Validation

- Automated: TBD
- Manual: TBD

关键验收写明输入、操作、预期结果；文档审查与程序验证、用户验收分别记录。

## Working Decisions / 仅讨论阶段保留

- Unresolved consequential decisions: TBD
- Existing approvals / evidence: TBD
- Routine implementation choices: TBD

已有授权沿用；重大未决项集中询问，继续无依赖工作。正式终稿前将问题和推导移入工作记录，保留确定规则与来源链接。

## Implementation Notes

- Keep this module independently disableable or deferrable where practical.
- Read external files or diffs before implementation if the user updates data outside AI.

## Review Question

Should this module move to `accepted`, or should it stay in iteration?
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create docs/ai-coding-workflow/modules/<module>.md as a module micro-PRD."
    )
    parser.add_argument("name", help="Module name, such as 'card system'.")
    parser.add_argument("--project", default=".", help="Project root. Defaults to current directory.")
    parser.add_argument("--purpose", default="TBD", help="Why this module exists.")
    parser.add_argument("--source", default="TBD", help="Source of truth, such as cards.xlsx or assets/art_manifest.csv.")
    parser.add_argument("--gate", default="Module works in-engine and is accepted by the user.", help="Acceptance gate.")
    parser.add_argument("--force", action="store_true", help="Overwrite an existing module file.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project = Path(args.project).expanduser().resolve()
    modules_dir = project / "docs" / "ai-coding-workflow" / "modules"
    module_path = modules_dir / f"{slugify(args.name)}.md"

    if module_path.exists() and not args.force:
        print(f"exists: {module_path}")
        print("Use --force to overwrite.")
        return 2

    modules_dir.mkdir(parents=True, exist_ok=True)
    module_path.write_text(
        MODULE_TEMPLATE.format(
            name=args.name,
            today=date.today().isoformat(),
            source=args.source,
            purpose=args.purpose,
            gate=args.gate,
        ),
        encoding="utf-8",
        newline="\n",
    )
    print(f"created: {module_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
