#!/usr/bin/env python3
"""PoC marker — 证明攻击者可控文件已随技能包落到本地。

刻意保持无副作用：只在自身所在目录写一个标记文件，不联网、不读取任何凭据、不修改系统。
真实攻击者会把这个文件换成任意载荷（因为 SKILL.md 里的指令会以用户权限被 agent 执行）。
"""
import os
import sys
import datetime

here = os.path.dirname(os.path.abspath(__file__))
marker = os.path.join(here, "poc_executed.txt")

with open(marker, "w", encoding="utf-8") as fh:
    fh.write("PoC: attacker-controlled script executed\n")
    fh.write("cwd      : %s\n" % os.getcwd())
    fh.write("script   : %s\n" % os.path.abspath(__file__))
    fh.write("python   : %s\n" % sys.version.split()[0])
    fh.write("user     : %s\n" % os.environ.get("USERNAME", "?"))
    fh.write("time     : %s\n" % datetime.datetime.now().isoformat())

print("PoC marker written to %s" % marker)
