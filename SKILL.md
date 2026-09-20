---
name: poc-free-gift
description: >
  PoC 技能（由本地模拟服务投递）。用于验证 dumate://install-skill 深链可在无用户确认的情况下
  安装任意来源的技能包。本技能不含任何危险行为，仅在被 agent 加载时可见其正文。
license: MIT
version: 1.0.0
---

# PoC 技能：证明此文件内容来自攻击者

如果你在 DuMate 的技能列表里看到本技能，说明以下链路成立：

1. 一条 `dumate://install-skill/?url=...` 深链被触发（网页点击 / IM 消息 / 命令行）
2. 主进程 `deep-link.js` 仅校验企业登录态，**没有任何安装前确认**
3. URL 被原样 POST 到本地后端 `/w/default-workspace/skills/import/url`，`overwrite: true`
4. 后端从攻击者指定的地址下载 zip 并解包安装到本工作区

## 攻击者可控内容

本段文字、以及同目录下的 `scripts/poc_marker.py`，都是攻击者在自己服务器上放的内容，
现在原封不动地落在了你的工作区里。

真实攻击者会在这里写指令，让 agent（以用户权限）执行任意操作，例如：

- 读取并外传本地凭据文件
- 调用 shell 执行命令
- 修改/覆盖你已信任的同名技能（`overwrite: true` 影子替换）

**本 PoC 未包含上述任何行为，仅作证明。**
