# news-image-20261119 — 一张报纸头版风格的 2026-11-19 世界新闻图

本仓库是 make.fun 悬赏 `news-image-20261119` 的参赛作品。作品本体是
`entry.png`：一张 1024×1024 的图片，以传统报纸头版的形式总结
2026 年 11 月 19 日（星期四）的世界新闻。

## entry.png 是什么

版面标题为 **"THE DAY IN BRIEF — LATE EDITION"**，副标为
**"44 STORIES · 6 CONTINENTS · ALL FROM THURSDAY"**，报头日期为
THURSDAY 19 NOVEMBER 2026。整体采用复古宽版报纸风格：米色纸底、
黑色衬线字体、暗红色分隔线，六大区域各用一种颜色（红/蓝/紫/绿/橙/青）
标注区头、新闻编号与地图钉。

内容分为三部分：

1. **三条头条（配插图）**
   - `01 · DIPLOMACY · APEC 深圳峰会`：特朗普、习近平、普京举行首次
     三边会谈，发表联合和平宣言，但无核风险实质突破（配三国国旗与
     握手插图）。
   - `02 · ECONOMY · 华尔街上市`：Anthropic 以 1.5 万亿美元估值完成
     史上最大 IPO，首日收涨 +17%，并承诺 AI "始终处于人类控制之下"
     （配上涨折线图插图）。
   - `03 · JUSTICE · 世界法院首例`：国际法院（ICJ）历史性地裁定缅甸对
     罗兴亚人实施种族灭绝——国家首次被国际法院判定犯下种族灭绝罪
     （配天平插图，标注 "FIRST-EVER RULING · ICJ"）。

2. **六大区域新闻栏**（AMERICAS、EUROPE & RUSSIA、MIDDLE EAST、
   ASIA、AFRICA、OCEANIA，共 33 条），涵盖普京就克里米亚大桥被袭
   放话"更痛苦的回击"、梵高《盛开的栗树》以 1.904 亿美元创拍卖纪录、
   辛辛那提动物园河马 Fiona 误吞帽子后去世、新西兰凭时差全球最先玩到
   《GTA VI》、圣诞岛红蟹大迁徙、NASA 旅行者 1 号从一光日外传回信号、
   剑桥词典年度词汇 "human"、罗伯特·帕丁森成为第七任 007 等。

3. **"WHERE IT HAPPENED" 世界地图**：以彩色编号钉标注各地头条位置，
   图例显示 AMER 7 · EUR 6 · M.EAST 4 · ASIA 6 · AFR 5 · OCEAN 5。

所有新闻取材自 2026-11-19 当天 AP News 与 BBC News 的 Wayback Machine
存档快照，采集过程与逐条出处见 [notes.md](notes.md)。

## 运行方式

入口程序 `main.py` 只做一件事：把与本脚本同目录的 `entry.png`
逐字节复制到环境变量 `MAKEFUN_OUTPUT_DIR` 指定的输出目录（评测环境
默认 `/output`），输出文件名固定为 `entry.png`。

脚本行为细节：

- 源文件按 `main.py` 所在目录解析（`Path(__file__).resolve()`），
  与当前工作目录无关；
- 输出目录不存在时自动递归创建（含多级嵌套路径）；
- 复制完成后回读比对，确认输出与源文件逐字节一致；
- 任何失败（源文件缺失、目录/复制出错、校验不一致）都会向 stderr
  打印明确的错误信息并以非零状态码退出。

本地验证（Git Bash / Linux / macOS）：

```bash
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python main.py
```

然后可比对哈希确认逐字节一致：

```bash
sha256sum entry.png out/entry.png
```

Windows PowerShell 用户请改用：

```powershell
mkdir out; $env:MAKEFUN_OUTPUT_DIR = "out"; python main.py
```

---

本文为 make.fun 悬赏 `news-image-20261119` 的参赛作品。
