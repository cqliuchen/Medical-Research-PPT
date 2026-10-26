# Medical-Research-PPT

把论文、旧课件、脚本与批注整理为临床医生听得懂、证据可追溯、图像清晰且便于修改的科研汇报。

技能名称：`medical-research-ppt`。默认保留逐页提问审阅，使用临床问题驱动叙事；继承已批准样张，保护科研原图、病例视频和演讲稿备注。

## 团队安装

在支持 Codex Skills 的环境中对 Codex 说：

> 请使用 skill-installer，从 GitHub 仓库 cqliuchen/Medical-Research-PPT 的 skills/medical-research-ppt 目录安装技能。先检查已安装版本，已有版本请先备份再更新。

仓库若为私有，团队成员需先获得仓库读取权限，并在其电脑上配置 GitHub 访问。管理员只需授予需要的仓库权限；不要共享个人访问令牌。

也可以在已经克隆本仓库后，将 `skills/medical-research-ppt` 整个文件夹复制到自己的 `$CODEX_HOME/skills/`；未配置 `CODEX_HOME` 时默认为 `~/.codex/skills/`。已有同名技能先备份，安装后在下一轮会话确认技能可见。

## 安装后检查依赖

本仓库提供综合工作流及个人风格，**不捆绑第三方技能或其账户、模型服务和密钥**。安装综合技能不等于安装全部制作引擎。团队可以先进行内容规划和逐页决策，再按任务配置实际需要的能力。

在本仓库目录执行（Windows 也可用 `py`）：

```text
python skills/medical-research-ppt/scripts/check_dependencies.py --mode build
python skills/medical-research-ppt/scripts/check_dependencies.py --mode editable
```

该工具仅检查技能文件是否存在，不验证账户、OCR、图片模型或 PowerPoint 服务是否可用。输出缺项后，让 Codex 按当前安装环境和官方来源补齐；安装或配置后再按相应技能检查实际运行条件。

| 工作 | 按需准备的技能 |
|---|---|
| 查论文、元数据、作者角色和开放全文 | `academic-search`；读全文和科研图用 `pdf` |
| 普通互联网、网页和平台搜索 | `agent-reach` |
| 原生可编辑制作、合并换页、备注和视频保留 | `presentations` |
| GPT Image 统一视觉制作 | `codex-ppt`；独立插图用 `imagegen` |
| 图片 PPT 改为对象级可编辑 | `image-to-editable-ppt`，回装与整稿检查用 `presentations` |
| Word 大纲、批注和真实修订 | `documents` |
| 逐页提问 | 本仓库包含逐页决策规则；已安装时组合 `grill-me` / `grilling` / `grill-with-docs` / `domain-modeling` |

扩展技能、适用条件和调用顺序见[完整技能清单](skills/medical-research-ppt/references/skill-catalog.md)。部分技能随 Codex 插件提供，实际名称和路径以当前环境为准。

第三方项目来源（不随本仓库再分发）：

- Codex PPT：<https://github.com/ningzimu/codex-ppt-skill>
- Image to Editable PPT：<https://github.com/ningzimu/image-to-editable-ppt-skill>
- Agent Reach：<https://github.com/Panniantong/Agent-Reach>

其他技能请从团队认可的原始来源或已配置的 Codex 技能/插件目录安装。不同技能及依赖分别遵循各自许可。

## 直接调用

### 新建或整合

> 使用 $medical-research-ppt，阅读这两份课件和论文，先整理临床问题驱动的逐页图文大纲。每页给标题、上屏文字、主图、确切结论和布局，分轮向我提问。确认后制作可编辑PPT，保留科研原图、视频及备注。

### 图片课件转可编辑

> 使用 $medical-research-ppt，把指定第2—13页转为可编辑版本，其余页不变。文字、线条与色块原生编辑，图标和背景分层，科研原图和病例视频保留，另存新版。

### 临床化演讲稿

> 使用 $medical-research-ppt，对照每页真实内容打磨备注。面向神经内科医生，讲清看图位置、核心比较和临床解释，前后衔接。总时长20分钟，先逐页审阅。

## 团队使用约定

- 姓名、署名角色、个人经历以本次讲者为准。刘晨只是默认风格来源，团队成员不自动冒用其身份。
- 默认深蓝、白底、金色强调；本次指定样张优先。
- 科研数据原图不交生成模型重画；统计不显著和关键研究边界准确保留。
- 逐页提问默认开启；同一轮集中处理互不依赖的问题，已经确认的决定复用。
- 病例视频只遮挡人脸，保留躯干和四肢运动信息；病例材料按所在机构与项目规定处理。
- 每台电脑独立配置所需OCR、图片后端和Office运行条件。本仓库不包含任何项目数据、患者资料、论文全文或密钥。

## 更新与贡献

从 `main` 安装默认得到当前版本；正式汇报建议记录使用的提交或版本。更新前保留团队本地修改，可通过Pull Request提出改进。安装器通常不覆盖已有同名目录，应先备份再更新。

仓库内容为本工作流指令、说明和依赖检查脚本；引用到的第三方技能仍需单独安装。默认可在 GitHub 读取和使用；本仓库未额外授予第三方内容的再分发许可。

## 名称更新

本项目原名为 liuchen-medical-ppt-skill，现仓库与显示名称为 Medical-Research-PPT，技能调用标识为 medical-research-ppt（按技能命名规范使用小写）。已安装旧版的成员请先备份旧技能目录，再安装新目录，避免同时加载两份工作流。
