# Changelog

## v1.2.0 — 省上下文版本

**问题**：`STATUS.md` 会随事件无限增长（示例工程已到 983 行 / 62 KB），`workflow.py status` 又把整份历史打到终端，接手时等于每次读一遍全量流水；`Start or Resume` 的“检查项目及其文档”也容易被理解成通读全部文档。

**改动**

- `STATUS.md` 改为**紧凑看板**：版本、当前模块、模块队列、**Acceptance Decisions**（每个已验收模块一行用户原话）、最近 10 条事件、证据清单（哈希截断为 8 位）。
- 全量事件日志（含载荷与完整哈希）移到 `LOG.md`，文件头写明 AI 不读；`export` 导出的 `IMPLEMENTATION_LOG.md` 仍为全量。
- `workflow.py status` 输出同步变短：同一工程 983 行 → 66 行。
- 新增 `## Reading Budget` 一节：按项目 `docs/README.md` 索引只读当前模块需要的 1-3 份文档，证据用 grep 定位，不整份读 JSON / 日志 / 证据。
- 新增回归测试 `test_status_board_is_compact_and_log_keeps_full_history`，锁住“看板必须短、LOG 必须全”。

### 升级影响

- **状态格式不变**，`workflow.json` 无需迁移，已交付版本照常可读。
- 新增生成文件 `LOG.md`；旧的 `STATUS.md` 会在下一次成功写入时被紧凑版覆盖（历史不丢，全在 `workflow.json` 与 `LOG.md`）。
- 若外部脚本仍以 `STATUS.md` 作为唯一检索来源，需改读 `LOG.md` 或 `workflow.json`。

## v1.1.0 — 更名版本

**改名**：仓库名与 skill 名从 `vibe-game-ai-coding` 改为 `codex-game-dev-skill`，显示名从 `Vibe Game AI Coding` 改为 `Codex Game Dev Skill`。

原因：原名里的 `vibe coding` 容易被理解成“一句话生成整个游戏”，与分阶段验收的实际流程不符，搜进来的人预期对不上；新名字覆盖 `codex`、`game dev`、`skill` 三个检索词，和实际用法一致。

### 升级影响

- 调用名变更：`$vibe-game-ai-coding` → `$codex-game-dev-skill`。
- 安装目录变更：`~/.codex/skills/codex-game-dev-skill`。旧的 `vibe-game-ai-coding` 目录需要重命名或重新安装。
- GitHub 旧地址 `sn246akeak/vibe-game-ai-coding` 会 301 跳转到新地址。
- 工程内 `docs/ai-coding-workflow/` 的状态格式**不变**，`workflow.json` 无需迁移，已交付版本照常可读。
- `references/subskills.json` 的 `orchestrator` 字段已同步更新。内容锁 `subskills.lock.json` 只记录上游依赖的内容摘要，不含本仓库自身哈希，无需重新生成。

### 其他

- 新增 MIT LICENSE。
- README 增加“适合谁”小节，把适用场景写清楚，减少误搜进来的人。

## v1.0.0

首个可用版本：引导规范、可执行状态机、内容变更检查、专项 skill 路由。
