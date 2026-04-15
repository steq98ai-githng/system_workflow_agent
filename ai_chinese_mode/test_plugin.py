# -*- coding: utf-8 -*-
"""
System Workflow Agent v4.0.3 (Plus Ultra) — 自動化測試腳本
1. 驗證 V4.0 Manifest (100% 系統導向)
2. 測驗 GitKraken MCP 註冊狀態
3. 模擬背景執行緒啟動邏輯
"""

import json
import os
import sys
import unittest
from unittest.mock import MagicMock, patch

# Mock Windows dependencies for Linux testing
import ctypes
ctypes.windll = MagicMock()

# 加入專案路徑
_test_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _test_dir)
_libs_path = os.path.join(_test_dir, "libs")
if os.path.exists(_libs_path): sys.path.insert(0, _libs_path)

class TestSystemWorkflowAgent(unittest.TestCase):

    def setUp(self):
        # 由於 plugin 模組在 import 時會執行初始化，我們需要 mock 掉可能失敗的部分
        pass

    def test_manifest_v4_purity(self):
        """驗證 Manifest 是否已徹底移除遊戲標籤與功能。"""
        manifest_path = os.path.join(_test_dir, "manifest.json")
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
        
        self.assertEqual(manifest["version"], "4.0.0")
        self.assertIn("workflow", manifest["functions"][0]["tags"])
        
        game_keywords = ["game", "fps", "optimize", "weather", "discord"]
        desc = manifest["functions"][0]["description"].lower()
        for kw in game_keywords:
            self.assertNotIn(kw, desc, f"Manifest 包含遊戲標籤: {kw}")

    def test_mcp_config(self):
        """驗證預設設定是否包含 GitKraken MCP。"""
        # 直接從檔案讀取或 import (import 已在 v4.0.3 修正權限問題)
        from plugin import DEFAULT_CONFIG
        servers = [s["name"] for s in DEFAULT_CONFIG["mcp_servers"]]
        self.assertIn("GitKraken", servers)

    def test_agent_background_thread(self):
        """驗證 Agent 啟動時是否開啟背景執行緒。"""
        with patch('threading.Thread') as mock_thread:
            import plugin
            plugin.init_mcp_bridge()
            self.assertTrue(mock_thread.called)

    def test_vision_diagnostic_mapping(self):
        """驗證功能映射中是否存在系統診斷。"""
        manifest_path = os.path.join(_test_dir, "manifest.json")
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = json.load(f)
        
        func_names = [f["name"] for f in manifest["functions"]]
        self.assertIn("vision_diagnostic", func_names)

if __name__ == "__main__":
    unittest.main()
