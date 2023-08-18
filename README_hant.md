# Azure Cognitive Speech Component

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

[English](https://github.com/aes-alienrip/azure_cognitive_speech/blob/main/README.md) | [簡體中文](https://github.com/aes-alienrip/azure_cognitive_speech/blob/main/README_hans.md) | 繁體中文

可以先試聽一下語音合成的效果

https://github.com/aes-alienrip/azure_cognitive_speech/assets/73251414/0359c01b-96d7-423f-9fed-d5842d71e5c5


# 為什麼會有這個集成
是的，Home Assistant自己就包含了Microsoft TTS組件，但組件支持的功能就是普通的TTS。而該組件通過Options可以額外指定由誰說話(voice)，還可以指定說話的風格、情緒(style)，甚至可以讓一個女生模仿一個老年人說話(roleplay)。而實現以上功能，不僅不需要修改`configuration.yaml`文件，並重啟Home Assistant，而是在調用TTS服務時通過Options實現，使得在家庭應用時適合不同的場景。
上邊的試聽mp3，是讓Yunjian使用了體育評述激情的風格發聲的，聽起來似乎就來自於電視中的體育直播。


# 使用之前
- 使用該組件，首先需要一個[Microsoft Azure](https://azure.microsoft.com/)賬戶，如果你沒有，請先註冊一個。
- 錄Azure後，轉到[Azure首頁](https://portal.azure.com/#home)
- 點擊[資源群組](https://portal.azure.com/#view/HubsExtension/BrowseResourceGroups)，新建一個資源群組，如果你是Azure新用戶，可以獲得一年的免費使用期限。區域選擇你所在區域即可，香港用戶可以選擇 East US。
- 創建資源群組後，回到Azure主頁，選擇[建立資源](https://portal.azure.com/#create/hub)，搜索「語音」，在搜索到的語音標籤上選擇建立。
- 訂閱仍舊可以選擇免費試用，定價層選擇「免費 S0」，資源群組選擇剛才新建的資源群組，區域與之前的區域保持一致。
- 建立語音資源後，等待建立完成，返回Azure主頁，你建立的語音認知服務已經出現在主頁上。
- 點擊該項資源，左側的列表中，點擊「資源管理」下的「金鑰與端點」，密鑰和區域，端點就會出現在螢幕上，記下以上訊息，金鑰共有兩個，任意使用其中一個即可。

# 安裝
使用HACS安裝Custom repositories，或者從[Latest Release](https://github.com/aes-alienrip/azure_cognitive_speech/releases/latest)下載最新的發行版，並將其中的`custom_components/azure_cognitive_speech`目錄下所有文件手動複製到你的Home Assistant下的`<Home Assistant config folder>/custom_components/azure_cognitive_speech`目錄中，然後重啟Home Assistant。

# 配置
## 基本配置
編輯你HomeAssistant中的configuration.yaml，增加以下配置行:
```
tts:
  - platform: azure_cognitive_speech
    api_key: "XXXXXXXXXXXXXXXXXXXXXXXXXXX"     # 這裡是你申請的Azure Cognitive Speech語音服務的金鑰
    region: "eastus"                           # 這裡是你申請的Azure Cognitive Speech語音服務的區域        
    default_voice: "HiuMaan"                   # 這裡是預設使用的語音，HiuMaan是一個廣東話語音的模型名稱
```
更多語音，請參照[語言和語音支援](https://learn.microsoft.com/zh-hk/azure/cognitive-services/speech-service/language-support?tabs=tts)，其中的「文字轉換語音的語音」，把前面區域設置```zh-HK-```及後面```Neural```去掉就是可用的語音參數

例子：```zh-HK-HiuMaanNeural```去掉頭尾就是```HiuMaan```

特殊例子：四川話的語音名稱```zh-CN-sichuan-YunxiNeural```跟原來的```zh-CN-YunxiNeural```重複了而需要使用```sichuan-Yunxi```

## 進階配置
要更好地使用Home Assistant中的TTS服務，可以在配置項中增加以下內容：
```
- platform: azure_cognitive_speech
    api_key: "XXXXXXXXXXXXXXXXXXXXXXXXXXX"     # 這裡是你申請的Azure Cognitive Speech語音服務的金鑰
    region: "eastus"                           # 這裡是你申請的Azure Cognitive Speech語音服務的區域    
    default_voice: "HiuMaan"                   # 這裡是預設使用的語音，HiuMaan是一個廣東話語音的模型名稱
    cache: true                                # 快取文字轉語音的結果，下次播放同樣內容時，就不再需要訪問網絡，會使得TTS更快
    cache_dir: tts                             # 快取文件所在目錄，該目錄位於你Home Assistant宿主機中
    time_memory: 300                           # 記憶體中快取時間
```

# 使用
Microsoft Azure Cognitive Speech服務除了一般的TTS，還可以為語音加入風格(Style)和角色模仿(Role)，比如對於「Xiaoxiao」這個語音來說, "sad"風格與"newscast"風格具有巨大的區別，同時還可以讓Xiaoxiao模仿諸如老年人說話。
以上功能通過語音識別時的選項(Option)功能實現，可用的選項包括
- voice 選擇的語音，可以選擇默認語音之外的語音發音
- rate 說話的速度，可選值-100到100，正常應設置到-40到40之間
- style 風格
- role 角色模仿

關於可用的voice及其可用哪些style或者role，參照[語言和語音支援](https://learn.microsoft.com/zh-cn/azure/cognitive-services/speech-service/language-support?tabs=tts)

# 實例
使用如下Options，播放文字「在北京時間今天凌晨3點舉行的一場歐洲杯半決賽中，意大利隊與西班牙隊在120分鐘內站成1：1平。在點球大戰中，意大利隊以4：2（總比分5：3）擊敗西班牙隊，挺進決賽。」
```
voice: Yunjian
rate: 0
style: sports-commentary-excited
```
[語音合成的效果]

https://github.com/aes-alienrip/azure_cognitive_speech/assets/73251414/0359c01b-96d7-423f-9fed-d5842d71e5c5
