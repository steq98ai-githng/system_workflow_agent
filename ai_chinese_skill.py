"""
AI 中文控制 Skill
可在 IDE / Agent / 本地 AI 系統中直接使用
"""

from typing import Dict, Optional


class AIChineseControlSkill:

    # =========================
    # 中文 → 英文 映射表
    # =========================
    COMMAND_MAP = {
        "初始化": "initialize",
        "啟動": "initialize",
        "開始": "initialize",

        "關閉": "shutdown",
        "停止": "shutdown",
        "結束": "shutdown",

        "重啟": "restart",
        "重新啟動": "restart",

        "狀態": "status",
        "系統狀態": "status",

        "幫助": "help",
        "說明": "help"
    }

    # =========================
    # Skill 入口
    # =========================
    def handle(self, user_input: str) -> Dict[str, Optional[str]]:
        if not user_input:
            return self._failure("未提供指令內容。")

        detected_command = self._detect_intent(user_input)

        if detected_command == "initialize":
            return self._initialize()

        if detected_command == "shutdown":
            return self._shutdown()

        if detected_command == "restart":
            return self._restart()

        if detected_command == "status":
            return self._status()

        if detected_command == "help":
            return self._help()

        return self._success(
            f"已接收中文輸入：「{user_input}」，但未匹配到已知指令。"
        )

    # =========================
    # 意圖判斷
    # =========================
    def _detect_intent(self, user_input: str) -> Optional[str]:
        for keyword, command in self.COMMAND_MAP.items():
            if keyword in user_input:
                return command
        return None

    # =========================
    # 功能實作
    # =========================
    def _initialize(self):
        return self._success("系統已成功初始化。")

    def _shutdown(self):
        return self._success("系統即將關閉。")

    def _restart(self):
        return self._success("系統已識別為重啟指令（尚未實作實際重啟）。")

    def _status(self):
        return self._success("系統目前運作正常。")

    def _help(self):
        return self._success(
            "可用中文指令：初始化、關閉、重啟、狀態、幫助。"
        )

    # =========================
    # 回應工具
    # =========================
    def _success(self, message: str):
        return {
            "success": True,
            "message": message
        }

    def _failure(self, message: str):
        return {
            "success": False,
            "message": message
        }