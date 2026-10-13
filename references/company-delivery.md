# 公司正式文档交付模式

只在明确要求公司评审、公司模板或公司正式策划产物时启用；日常开发默认按 [document-specs.md](document-specs.md) 写简洁 Markdown。

## 定位与材料

复用已有文档类型、范围、格式、目录和讨论稿/终稿约定，执行前简述即可。只有缺失约定会实质影响交付时才集中询问；不另设状态机，不因换格式重复批准已确认规则。截图范围按 [copy-and-resources.md](copy-and-resources.md) 处理。

设计推演和正式规格是不同产物：XMind 可探索目的、玩家 Story、机制、核心乐趣与风险；不直接把其分支搬成 Word 目录。只在用户要求两种产物时分别交付，不强制每个模块先制作 XMind。

## 正式结构与样式

优先遵循用户目标文档或近期同类文档。没有其他约定时使用：前言（设计目的、功能概述）→ 界面逻辑（入口、界面/弹窗、必要区域）→ 功能逻辑 → 统计相关（适用时）→ 数值 → 表结构 → 资源。没有内容的章节按需省略。

默认使用原生标题与紧凑段落/多级列表，不使用 Word 表格，除非用户要求。公司 DOCX 列表按实心圆、实心方块、实心菱形的原生编号样式设置，保留悬挂缩进；不用手工字符伪装列表。Markdown 使用原生标题与列表，不模仿 Word 的符号形状。

不自动把内部 Story、机制链、问题表、风险矩阵或验收矩阵增加到公司 Word 目录；边界与异常放在对应模块或特殊处理。开发合同中的验收条件与验证计划仍保留在归属规格/验证记录并可追溯，不能因公司目录不显示而删除。

本功能自有配置说明用途、行粒度、主键、字段类型/语义/范围/默认值、引用与校验；默认按表名及字段段落说明，用户要求字段表时使用表格。公共配置只引用归属和使用关系，具体命名与存储遵循项目，不强制 GameConfig。

DOCX 使用 assets/company/ 中对应模板副本，保留模板样式并填充实际内容；XMind 使用同目录模板副本。调用环境中可用的文档/表格等专用能力，DOCX 完成后进行实际渲染核验；工具不可用时保留源文件并明确未完成的格式验证。模板存在不等于已确认全部业务内容。

## 来源与适配边界

内化来源：公司 write-game-design-docs，原始包 write-game-design-docs(10).zip，接收于水滴排序/外部skill，适配日期 2026-10-13。

吸收主规则及 functional-reconstruction、formal-writing-style、control-lifecycle-and-config-boundaries、specification-patterns、document-blueprints、review-checklists、interface-screenshot-guidelines 中与个人开发流程相关的原则。原包 SHA-256 与模板哈希记录在 assets/company/source-manifest.json；二进制模板按原样保留。原公司 skill 不作为外部运行依赖。

有意适配：确认沿用主流程授权；公司目录/列表/不用表格仅限公司模式；LanguageID 按项目需求启用；配置名沿用实际项目；网络、支付与运营维度按适用性检查。未来更新先比较来源与适配规则，不直接覆盖个人规范、workflow 历史或用户自定义。
