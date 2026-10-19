# BLUE REVOLVER: DOUBLE ACTION 简体中文汉化包

《BLUE REVOLVER: DOUBLE ACTION》的非官方简体中文汉化。

基于游戏官方预留的用户本地化机制（userlocs，见游戏目录 `README.txt`），**不修改游戏本体任何文件**，删除汉化文件即可完全还原英文原版。

## 安装

1. 从 [Releases](https://github.com/Cyclin15/blue-revolver-double-action-chinese/releases) 下载 `BRDA-Chinese-v1.0.zip` 并完整解压
2. 双击 `install.bat`（或按包内《安装说明.txt》手动安装：把 `userlocs`、`game` 两个文件夹复制到 `%APPDATA%\blue-revolver-double-action`）
3. 启动游戏，OPTIONS → LANGUAGE → 中文

## 卸载

双击 `uninstall.bat`（自动把语言切回 English 并删除汉化文件）。

## 说明

- 适用 Steam 版 v1.52，其他版本未测试
- 覆盖全部游戏文本（604 条）；与官方日文版策略一致：弹幕招式名、BOSS 名、机体名、武器名保留英文，菜单、对话、教学、结算等全部翻译
- 游戏的字体配置不含中文分支（中文会显示为方块），因此附带 `game/fonts.lua`（基于 v1.52 原版修改），使中文使用游戏自带的 Silver.ttf 字体（Thaleah / Poppy Works 制作，完整覆盖简体中文）
- 游戏更新后若界面字体异常，删除存档目录里的 `game/fonts.lua` 即可临时恢复默认，等待本包更新

## 从源码构建

```bash
cd tools
python build_translation.py   # 生成 汉化包/userlocs/中文.json（需 Python 3）
```

构建脚本会合并 `tools/` 下的翻译表与从游戏 exe（LÖVE fused zip）提取的原文 `tools/extracted/strings/english.json`，并自动校验：

- `%s` / `%d` 等格式符与原文一一对应（缺失会导致游戏内格式化报错）
- 译文每个字符在 Silver.ttf 中都有字形（缺字形的措辞已改写）

## 版权

- 游戏内容与素材 © STELLAR CIRCLE，请通过 [Steam](https://store.steampowered.com/app/439490) 购买正版后使用本汉化
- 汉化文本采用 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.zh) 授权
- 本项目为非官方粉丝作品，与游戏开发者无关
