# DuMate `install-skill` 深链 PoC（安全测试材料）

本仓库是**安全审计取证材料**，用于验证 DuMate 桌面端 `dumate://install-skill/` 深链
在**无安装前确认**的情况下导入技能包的行为。

- 技能名：`poc-free-gift`
- 内容：`SKILL.md`（仅说明性文字）+ `scripts/poc_marker.py`
  —— **惰性**脚本，只在自身所在目录写一个标记文件，不联网、不读取凭据、不修改系统
- 仓库根目录即技能根目录（`SKILL.md` 在顶层），以匹配导入器对 zip 结构的期望

## 这不是真实攻击载荷

不含命令执行、凭据窃取、持久化等任何真实攻击代码。验证完成后请删除本仓库。

## 对应问题

```
dumate://install-skill/?url=<任意 URL>
```

主进程 `deep-link.js` 仅校验企业登录态（`LOGIN_TYPE_ENTERPRISE` + 存在登录 cookie），
随后把 URL 原样 POST 到后端：

```
POST /w/default-workspace/skills/import/url
{"url":"<任意 URL>","scope":"project","source":"user","overwrite":true}
```

**安装前没有任何确认弹窗**，只在安装完成后提示「Skill 安装成功。」。
`overwrite: true` 意味着可覆盖（影子替换）受害者已信任的同名技能。
