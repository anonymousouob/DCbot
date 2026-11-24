# 🤖 Discord 股票與藝術機器人（Discord Stock & Art Bot）

一個以 **Python** 開發的 **Discord Bot** 專案，結合股票資訊查詢與藝術/創意互動功能，適合作為專題展示或社群伺服器的多功能機器人。

---

## 🔍 專案分析

### 1. 系統定位與核心功能
從倉庫描述與檔案結構來看，這是一個兼具金融查詢與趣味/藝術互動的 Discord 機器人專案：
- **股票資訊查詢**：專案說明提及作為專題 Discord 機器人，支援搜尋股票相關資訊，方便社群成員在聊天頻道中快速查詢行情或標的資料。
- **藝術與創意功能模組**：根目錄包含 `artbot.py`，對應倉庫描述中的「Art Bot」，推測提供圖像/藝術相關指令或生成/展示互動。
- **多模組 / 實驗性腳本**：除 `artbot.py` 外，尚有 `wtf.py` 與 `dcbot/` 子資料夾，顯示專案在開發過程中將不同機器人功能或測試腳本拆分為獨立檔案/模組。

### 2. 專案結構摘要
- **機器人主程式與功能腳本**：`artbot.py`、`wtf.py`
- **子模組目錄**：`dcbot/`
- **版本控管與說明文件**：`.gitignore`、`README.md`

### 3. 工程現況與改進建議
- **優點**：功能主題鮮明（股票查詢 + Art Bot），適合快速驗證 Discord API 互動與指令設計。
- **建議改進**：
  1. 整理 `dcbot/`、`artbot.py` 與 `wtf.py` 的職責邊界，明確標註哪一個檔案為主要啟動入口，並加上 `requirements.txt`。
  2. 務必將 Discord Bot Token 與任何第三方股票／AI API 金鑰存放於環境變數或 `.env`（並加入 `.gitignore`），避免外洩。
  3. 在說明文件中列出可用指令清單與範例輸出，降低他人試用門檻。

---

## 🛠️ 安裝與使用說明

### 1. 前置準備
1. 前往 [Discord Developer Portal](https://discord.com/developers/applications) 建立應用程式與機器人（Bot），取得 **Bot Token**，並開啟所需的 **Intents**（如 Message Content Intent，視指令需求而定）。
2. 使用 OAuth2 產生邀請連結，將機器人加入你的 Discord 測試伺服器。

### 2. 安裝與啟動
```bash
git clone https://github.com/anonymousouob/DCbot.git
cd DCbot
```
安裝所需的 Python 套件（例如 `discord.py` 或 `py-cord`，以及股票查詢或繪圖相關套件），設定好 Bot Token 後，依專案實際入口執行對應腳本（例如 `python artbot.py` 或 `dcbot/` 內的主程式）。
