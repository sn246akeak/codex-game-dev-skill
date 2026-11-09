# Changelog

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
