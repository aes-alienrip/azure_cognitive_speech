# Azure Cognitive Speech Component

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

[English](https://github.com/aes-alienrip/azure_cognitive_speech/blob/main/README.md) | 简体中文 | [繁體中文](https://github.com/aes-alienrip/azure_cognitive_speech/blob/main/README_hant.md)

可以先试听一下语音合成的效果

https://github.com/aes-alienrip/azure_cognitive_speech/assets/73251414/0359c01b-96d7-423f-9fed-d5842d71e5c5

# 为什么会有这个集成
是的，Home Assistant自己就包含了Microsoft TTS组件，但组件支持的功能就是普通的TTS。而该组件通过Options可以额外指定由谁说话(voice)，还可以指定说话的风格、情绪(style)，甚至可以让一个女生模仿一个老年人说话(roleplay)。而实现以上功能，不仅不需要修改`configuration.yaml`文件，并重启Home Assistant，而是在调用TTS服务时通过Options实现，使得在家庭应用时适合不同的场景。
上边的试听mp3，是让Yunjian使用了体育解说激情的风格发声的，听起来似乎就来自于电视中的体育直播。


# 使用之前
- 使用该组件，首先需要一个[Microsoft Azure](https://azure.microsoft.com/)账号，如果你没有，请先注册一个。
- 录Azure后，转到[Azure主页](https://portal.azure.com/#home)
- 点击[资源组](https://portal.azure.com/#blade/HubsExtension/BrowseResourceGroups)，新建一个资源组，如果你是Azure新用户，可以获得一年的免费使用期限。区域选择你所在区域即可，中国用户可以选择东亚或者东南亚，加快以后网络访问速度。
- 创建资源组后，回到Azure主页，选择[创建资源](https://portal.azure.com/#create/hub)，搜索“语音”，在搜索到的语音标签上选择创建。
- 订阅仍旧可以选择免费试用，定价层选择“免费 F0”，资源组选择刚才新建的资源组，区域与之前的区域保持一致。
- 创建语音资源后，等待创建完成，返回Azure主页，你创建的语音认知服务已经出现在主页上。
- 点击该项资源，左侧的列表中，点击“资源管理”下的“密钥和终结点”，密钥和区域，终结点就会出现在屏幕上，记下以上信息，密钥共有两个，任意使用其中一个即可。

# 安装
使用HACS安装自定义存储库，或者从[Latest Release](https://github.com/aes-alienrip/azure_cognitive_speech/releases/latest)下载最新的发行版，并将其中的`custom_components/azure_cognitive_speech`目录下所有文件手动复制到你的Home Assistant下的`<Home Assistant config folder>/custom_components/azure_cognitive_speech`目录中，然后重启Home Assistant。

# 配置
## 基础配置
编辑你HomeAssistant中的configuration.yaml，增加以下配置行:
```
tts:
  - platform: azure_cognitive_speech
    api_key: "XXXXXXXXXXXXXXXXXXXXXXXXXXX"     # 这里是你申请的Azure Cognitive Speech语音服务的密钥
    region: "eastasia"                         # 这里是你申请的Azure Cognitive Speech语音服务的区域        
    default_voice: "Xiaoxiao"                  # 这里是默认使用的语音，Xiaoxiao是一个中文语音的模型名称
```
更多语音，请参照[这里](https://learn.microsoft.com/zh-cn/azure/cognitive-services/speech-service/language-support?tabs=tts)，其中的“文本转语音声音”，把前面区域设置```zh-CN-```及后面```Neural```去掉就是可用的语音参数

例子：```zh-CN-XiaoxiaoNeural```去掉头尾就是```Xiaoxiao```

特殊例子：除了四川话的声音名称```zh-CN-sichuan-YunxiNeural```跟原来的```zh-CN-YunxiNeural```重复了而需要使用```sichuan-Yunxi```

## 进阶配置
要更好地使用Home Assistant中的TTS服务，可以在配置项中增加以下内容：
```
- platform: azure_cognitive_speech
    api_key: "XXXXXXXXXXXXXXXXXXXXXXXXXXX"     # 这里是你申请的Azure Cognitive Speech语音服务的密钥
    region: "eastasia"                         # 这里是你申请的Azure Cognitive Speech语音服务的区域    
    default_voice: "Xiaoxiao"                  # 这里是默认使用的语音，Xiaoxiao是一个中文语音的模型名称
    cache: true                                # 缓存文本转语音的结果，下次播放同样内容时，就不再需要访问网络，会使得TTS更快
    cache_dir: tts                             # 缓存文件所在目录，该目录位于你Home Assistant宿主机中
    time_memory: 300                           # 内存中缓存时间
```

# 使用
Microsoft Azure Cognitive Speech服务除了一般的TTS，还可以为语音加入风格(Style)和角色模仿(Role)，比如对于“Xiaoxiao”这个语音来说, "sad"风格与"newscast"风格具有巨大的区别，同时还可以让Xiaoxiao模仿诸如老年人说话。
以上功能通过语音识别时的选项(Option)功能实现，可用的选项包括
- voice 选择的语音，可以选择默认语音之外的语音发音
- rate 说话的速度，可选值-100到100，正常应设置到-40到40之间
- style 风格
- role 角色演绎

关于可用的voice及其可用哪些style或者role，仍旧是参照[这里](https://learn.microsoft.com/zh-cn/azure/cognitive-services/speech-service/language-support?tabs=tts)

# 实例
使用如下Options，播放文字“在北京时间今天凌晨3点举行的一场欧洲杯半决赛中，意大利队与西班牙队在120分钟内站成1：1平。在点球大战中，意大利队以4：2（总比分5：3）击败西班牙队，挺进决赛。”
```
voice: Yunjian
rate: 0
style: sports-commentary-excited
```
[语音合成的效果]

https://github.com/aes-alienrip/azure_cognitive_speech/assets/73251414/0359c01b-96d7-423f-9fed-d5842d71e5c5
