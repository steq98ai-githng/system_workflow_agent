# AI 中文版 (Project G-Assist) 使用手冊

## 🎯 這是什麼？

這是專為 NVIDIA Project G-Assist 打造的「中文大腦」，讓原本只能聽懂英文的 G-Assist，現在可以直接用流利的中文對長（例如：接受「初始化」、「關閉」等中文指令）並用中文回報結果！

## 🚀 如何安裝與啟動

1. 進入工作區資料夾：`d:\AI_Tools\Antigravity-repo\workspace\projects\NVIDIA\ai_chinese_mode`
2. **點兩下 `install.bat`**：腳本會自動請求系統權限，並將編譯好的外掛及設定檔複製到 G-Assist 的核心資料夾內。
3. 重新啟動 **NVIDIA App** 與 **Project G-Assist**。
4. 直接對著 G-Assist 輸入或語音說出中文指令，例如：
   - 「請幫我初始化系統」或「啟動」
   - 「系統狀態」或「狀態」
   - 「關閉」或「停止」
   - 「幫助」
5. G-Assist 將會自動辨識您的中文意圖，執行對應功能，並以中文回覆您。

## ⚠️ 注意事項

- **已知限制**：目前第一版先行實作了「初始化」、「關閉」、「重啟」、「狀態」、「幫助」這五種核心指令的意圖辨識，其餘指令會先直接回傳收到訊息以待後續擴充。
- **系統依賴說明**：產生執行檔的過程復用了您系統中的 Python 環境與 PyInstaller。因安裝外掛需寫入 `C:\ProgramData`，`install.bat` 設有自動提權機制，點擊後請務必於跳出的視窗點選「是」。
