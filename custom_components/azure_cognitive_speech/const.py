DOMAIN = "azure_cognitive_speech"
OPT_VOICE = "voice"
OPT_STYLE = "style"
OPT_ROLE = "role"
OPT_RATE = "rate"
CONF_DEFAULT_VOICE = "default_voice"
DEFAULT_LANGUAGE = "en-US"
DEFAULT_VOICE = "JennyMultilingualV2Neural"
ENDPOINT_URI = "https://{}.api.cognitive.microsoft.com/sts/v1.0/issuetoken"
TTS_URL = "https://{}.tts.speech.microsoft.com/cognitiveservices/v1"
TOKEN_OUTDATE = 720
# https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=tts#supported-languages
SUPPORT_LANGUAGES = [
    "ar-EG",
    "ar-SA",
    "bg-BG",
    "ca-ES",
    "cs-CZ",
    "cy-GB",
    "da-DK",
    "de-AT",
    "de-CH",
    "de-DE",
    "el-GR",
    "en-AU",
    "en-CA",
    "en-GB",
    "en-HK",
    "en-IE",
    "en-IN",
    "en-NZ",
    "en-PH",
    "en-SG",
    "en-US",
    "en-ZA",
    "es-AR",
    "es-CO",
    "es-ES",
    "es-MX",
    "es-US",
    "et-EE",
    "fi-FI",
    "fr-BE",
    "fr-CA",
    "fr-CH",
    "fr-FR",
    "ga-IE",
    "gu-IN",
    "he-IL",
    "hi-IN",
    "hr-HR",
    "hu-HU",
    "id-ID",
    "it-IT",
    "ja-JP",
    "ko-KR",
    "lt-LT",
    "lv-LV",
    "mr-IN",
    "ms-MY",
    "mt-MT",
    "nb-NO",
    "nl-BE",
    "nl-NL",
    "pl-PL",
    "pt-BR",
    "pt-PT",
    "ro-RO",
    "ru-RU",
    "sk-SK",
    "sl-SI",
    "sv-SE",
    "sw-KE",
    "ta-IN",
    "te-IN",
    "th-TH",
    "tr-TR",
    "uk-UA",
    "ur-PK",
    "vi-VN",
    "wuu-CN",
    "yue-CN",
    "zh-CN",
    "zh-CN-henan",
    "zh-CN-liaoning",
    "zh-CN-shaanxi",
    "zh-CN-shandong",
    "zh-CN-sichuan",
    "zh-HK",
    "zh-TW"
]

# https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=tts#voice-styles-and-roles
VOICES_LIST = {
    "Salma": {
        "ShortName": "ar-EG-SalmaNeural",
        "Gender": "Female",
        "Locale": "ar-EG"
    },
    "Shakir": {
        "ShortName": "ar-EG-ShakirNeural",
        "Gender": "Male",
        "Locale": "ar-EG"
    },
    "Hamed": {
        "ShortName": "ar-SA-HamedNeural",
        "Gender": "Male",
        "Locale": "ar-SA"
    },
    "Naayf": {
        "ShortName": "ar-SA-Naayf",
        "Gender": "Male",
        "Locale": "ar-SA"
    },
    "Banu": {
        "ShortName": "az-AZ-BanuNeural",
        "Gender": "Female",
        "Locale": "az-AZ"
    },
    "Babek": {
        "ShortName": "az-AZ-BabekNeural",
        "Gender": "Male",
        "Locale": "az-AZ"
    },
    "Kalina": {
        "ShortName": "bg-BG-KalinaNeural",
        "Gender": "Female",
        "Locale": "bg-BG"
    },
    "Borislav": {
        "ShortName": "bg-BG-BorislavNeural",
        "Gender": "Male",
        "Locale": "bg-BG"
    },

    "Nabanita": {
        "ShortName": "bn-BD-NabanitaNeural",
        "Gender": "Female",
        "Locale": "bn-BD"
    },
    "Pradeep": {
        "ShortName": "bn-BD-PradeepNeural",
        "Gender": "Male",
        "Locale": "bn-BD"
    },
    "Tanishaa": {
        "ShortName": "bn-IN-TanishaaNeural",
        "Gender": "Female",
        "Locale": "bn-IN"
    },
    "Bashkar": {
        "ShortName": "bn-IN-BashkarNeural",
        "Gender": "Male",
        "Locale": "bn-IN"
    },
    "Vesna": {
        "ShortName": "bs-BA-VesnaNeural",
        "Gender": "Female",
        "Locale": "bs-BA"
    },
    "Goran": {
        "ShortName": "bs-BA-GoranNeural",
        "Gender": "Male",
        "Locale": "bs-BA"
    },
    "Joana": {
        "ShortName": "ca-ES-JoanaNeural",
        "Gender": "Female",
        "Locale": "ca-ES"
    },
    "Enric": {
        "ShortName": "ca-ES-EnricNeural",
        "Gender": "Male",
        "Locale": "ca-ES"
    },
    "Alba": {
        "ShortName": "ca-ES-AlbaNeural",
        "Gender": "Female",
        "Locale": "ca-ES"
    },
    "Herena": {
        "ShortName": "ca-ES-HerenaRUS",
        "Gender": "Female",
        "Locale": "ca-ES"
    },

    "Vlasta": {
        "ShortName": "cs-CZ-VlastaNeural",
        "Gender": "Female",
        "Locale": "cs-CZ"
    },
    "Antonin": {
        "ShortName": "cs-CZ-AntoninNeural",
        "Gender": "Male",
        "Locale": "cs-CZ"
    },
    "Nia": {
        "ShortName": "cy-GB-NiaNeural",
        "Gender": "Female",
        "Locale": "cy-GB"
    },
    "Aled": {
        "ShortName": "cy-GB-AledNeural",
        "Gender": "Male",
        "Locale": "cy-GB"
    },
    "Christel": {
        "ShortName": "da-DK-ChristelNeural",
        "Gender": "Female",
        "Locale": "da-DK"
    },
    "Jeppe": {
        "ShortName": "da-DK-JeppeNeural",
        "Gender": "Male",
        "Locale": "da-DK"
    },
    "Ingrid": {
        "ShortName": "de-AT-IngridNeural",
        "Gender": "Female",
        "Locale": "de-AT"
    },
    "Jonas": {
        "ShortName": "de-AT-JonasNeural",
        "Gender": "Male",
        "Locale": "de-AT"
    },
    "Leni": {
        "ShortName": "de-CH-LeniNeural",
        "Gender": "Female",
        "Locale": "de-CH"
    },
    "Jan": {
        "ShortName": "de-CH-JanNeural",
        "Gender": "Male",
        "Locale": "de-CH"
    },
    "Katja": {
        "ShortName": "de-DE-KatjaNeural",
        "Gender": "Female",
        "Locale": "de-DE"
    },
    "Conrad": {
        "ShortName": "de-DE-ConradNeural",
        "Gender": "Male",
        "Locale": "de-DE",
        "StyleList": [
            "cheerful"
        ]
    },
    "Amala": {
        "ShortName": "de-DE-AmalaNeural",
        "Gender": "Female",
        "Locale": "de-DE"
    },
    "Bernd": {
        "ShortName": "de-DE-BerndNeural",
        "Gender": "Male",
        "Locale": "de-DE"
    },
    "Christoph": {
        "ShortName": "de-DE-ChristophNeural",
        "Gender": "Male",
        "Locale": "de-DE"
    },
    "Elke": {
        "ShortName": "de-DE-ElkeNeural",
        "Gender": "Female",
        "Locale": "de-DE"
    },
    "Gisela": {
        "ShortName": "de-DE-GiselaNeural",
        "Gender": "Female",
        "Locale": "de-DE"
    },
      "Kasper": {
        "ShortName": "de-DE-KasperNeural",
        "Gender": "Male",
        "Locale": "de-DE"
    },  
      "Killian": {
        "ShortName": "de-DE-KillianNeural",
        "Gender": "Male",
        "Locale": "de-DE"
    },  
    "Klarissa": {
        "ShortName": "de-DE-KlarissaNeural",
        "Gender": "Female",
        "Locale": "de-DE"
    },
      "Klaus": {
        "ShortName": "de-DE-KlausNeural",
        "Gender": "Male",
        "Locale": "de-DE"
    },  
    "Louisa": {
        "ShortName": "de-DE-LouisaNeural",
        "Gender": "Female",
        "Locale": "de-DE"
    },
    "Maja": {
        "ShortName": "de-DE-MajaNeural",
        "Gender": "Female",
        "Locale": "de-DE"
    },
      "Ralf": {
        "ShortName": "de-DE-RalfNeural",
        "Gender": "Male",
        "Locale": "de-DE"
    },  
    "Tanja": {
        "ShortName": "de-DE-TanjaNeural",
        "Gender": "Female",
        "Locale": "de-DE"
    },
    "Athina": {
        "ShortName": "el-GR-AthinaNeural",
        "Gender": "Female",
        "Locale": "el-GR"
    },
    "Nestoras": {
        "ShortName": "el-GR-NestorasNeural",
        "Gender": "Male",
        "Locale": "el-GR"
    },
    "Natasha": {
        "ShortName": "en-AU-NatashaNeural",
        "Gender": "Female",
        "Locale": "en-AU"
    },
    "William": {
        "ShortName": "en-AU-WilliamNeural",
        "Gender": "Male",
        "Locale": "en-AU"
    },
    "Annette": {
        "ShortName": "en-AU-AnnetteNeural",
        "Gender": "Female",
        "Locale": "en-AU"
    },
    "Carly": {
        "ShortName": "en-AU-CarlyNeural",
        "Gender": "Female",
        "Locale": "en-AU"
    },
    "Darren": {
        "ShortName": "en-AU-DarrenNeural",
        "Gender": "Male",
        "Locale": "en-AU"
    },
    "Duncan": {
        "ShortName": "en-AU-DuncanNeural",
        "Gender": "Male",
        "Locale": "en-AU"
    },
    "Elsie": {
        "ShortName": "en-AU-ElsieNeural",
        "Gender": "Female",
        "Locale": "en-AU"
    },
    "Freya": {
        "ShortName": "en-AU-FreyaNeural",
        "Gender": "Female",
        "Locale": "en-AU"
    },
    "Joanne": {
        "ShortName": "en-AU-JoanneNeural",
        "Gender": "Female",
        "Locale": "en-AU"
    },
    "Ken": {
        "ShortName": "en-AU-KenNeural",
        "Gender": "Male",
        "Locale": "en-AU"
    },
    "Kim": {
        "ShortName": "en-AU-KimNeural",
        "Gender": "Female",
        "Locale": "en-AU"
    },
    "Neil": {
        "ShortName": "en-AU-NeilNeural",
        "Gender": "Male",
        "Locale": "en-AU"
    },
    "Tim": {
        "ShortName": "en-AU-TimNeural",
        "Gender": "Male",
        "Locale": "en-AU"
    },
    "Tina": {
        "ShortName": "en-AU-TinaNeural",
        "Gender": "Female",
        "Locale": "en-AU"
    },
    "Clara": {
        "ShortName": "en-CA-ClaraNeural",
        "Gender": "Female",
        "Locale": "en-CA"
    },
    "Liam": {
        "ShortName": "en-CA-LiamNeural",
        "Gender": "Male",
        "Locale": "en-CA"
    },
    "Sonia": {
        "ShortName": "en-GB-SoniaNeural",
        "Gender": "Female",
        "Locale": "en-GB",
        "StyleList": [
            "cheerful",
            "sad"
        ]
    },
    "Ryan": {
        "ShortName": "en-GB-RyanNeural",
        "Gender": "Male",
        "Locale": "en-GB",
        "StyleList": [
            "chat",
            "cheerful"
        ]
    },
    "Libby": {
        "ShortName": "en-GB-LibbyNeural",
        "Gender": "Female",
        "Locale": "en-GB"
    },
    "Abbi": {
        "ShortName": "en-GB-AbbiNeural",
        "Gender": "Female",
        "Locale": "en-GB"
    },
    "Alfie": {
        "ShortName": "en-GB-AlfieNeural",
        "Gender": "Male",
        "Locale": "en-GB"
    },
    "Bella": {
        "ShortName": "en-GB-BellaNeural",
        "Gender": "Female",
        "Locale": "en-GB"
    },
    "Elliot": {
        "ShortName": "en-GB-ElliotNeural",
        "Gender": "Male",
        "Locale": "en-GB"
    },
    "Ethan": {
        "ShortName": "en-GB-EthanNeural",
        "Gender": "Male",
        "Locale": "en-GB"
    },
    "Hollie": {
        "ShortName": "en-GB-HollieNeural",
        "Gender": "Female",
        "Locale": "en-GB"
    },
    "Maisie": {
        "ShortName": "en-GB-MaisieNeural",
        "Gender": "Female",
        "Locale": "en-GB"
    },
    "Noah": {
        "ShortName": "en-GB-NoahNeural",
        "Gender": "Male",
        "Locale": "en-GB"
    },
    "Oliver": {
        "ShortName": "en-GB-OliverNeural",
        "Gender": "Male",
        "Locale": "en-GB"
    },
    "Olivia": {
        "ShortName": "en-GB-OliviaNeural",
        "Gender": "Female",
        "Locale": "en-GB"
    },
    "Thomas": {
        "ShortName": "en-GB-ThomasNeural",
        "Gender": "Male",
        "Locale": "en-GB"
    },
    "Yan": {
        "ShortName": "en-HK-YanNeural",
        "Gender": "Female",
        "Locale": "en-HK"
    },
    "Sam": {
        "ShortName": "en-HK-SamNeural",
        "Gender": "Male",
        "Locale": "en-HK"
    },
    "Emily": {
        "ShortName": "en-IE-EmilyNeural",
        "Gender": "Female",
        "Locale": "en-IE"
    },
    "Connor": {
        "ShortName": "en-IE-ConnorNeural",
        "Gender": "Male",
        "Locale": "en-IE"
    },
    "Neerja": {
        "ShortName": "en-IN-NeerjaNeural",
        "Gender": "Female",
        "Locale": "en-IN"
    },
    "Prabhat": {
        "ShortName": "en-IN-PrabhatNeural",
        "Gender": "Male",
        "Locale": "en-IN"
    },
    "Asilia": {
        "ShortName": "en-KE-AsiliaNeural",
        "Gender": "Female",
        "Locale": "en-KE"
    },
    "Chilemba": {
        "ShortName": "en-KE-ChilembaNeural",
        "Gender": "Male",
        "Locale": "en-KE"
    },
    "Ezinne": {
        "ShortName": "en-NG-EzinneNeural",
        "Gender": "Female",
        "Locale": "en-NG"
    },
    "Abeo": {
        "ShortName": "en-NG-AbeoNeural",
        "Gender": "Male",
        "Locale": "en-NG"
    },
    "Molly": {
        "ShortName": "en-NZ-MollyNeural",
        "Gender": "Female",
        "Locale": "en-NZ"
    },
    "Mitchell": {
        "ShortName": "en-NZ-MitchellNeural",
        "Gender": "Male",
        "Locale": "en-NZ"
    },
    "Rosa": {
        "ShortName": "en-PH-RosaNeural",
        "Gender": "Female",
        "Locale": "en-PH"
    },
    "James": {
        "ShortName": "en-PH-JamesNeural",
        "Gender": "Male",
        "Locale": "en-PH"
    },
    "Luna": {
        "ShortName": "en-SG-LunaNeural",
        "Gender": "Female",
        "Locale": "en-SG"
    },
    "Wayne": {
        "ShortName": "en-SG-WayneNeural",
        "Gender": "Male",
        "Locale": "en-SG"
    },
    "Imani": {
        "ShortName": "en-TZ-ImaniNeural",
        "Gender": "Female",
        "Locale": "en-TZ"
    },
    "Elimu": {
        "ShortName": "en-TZ-ElimuNeural",
        "Gender": "Male",
        "Locale": "en-TZ"
    },
    "JennyMultilingual": {
        "ShortName": "en-US-JennyMultilingualNeural",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Jenny": {
        "ShortName": "en-US-JennyNeural",
        "Gender": "Female",
        "Locale": "en-US",
        "StyleList": [
            "angry",
            "assistant",
            "chat",
            "cheerful",
            "customerservice",
            "excited",
            "friendly",
            "hopeful",
            "newscast",
            "sad",
            "shouting",
            "terrified",
            "unfriendly",
            "whispering"
        ]
    },
    "Guy": {
        "ShortName": "en-US-GuyNeural",
        "Gender": "Male",
        "Locale": "en-US",
        "StyleList": [
            "angry",
            "cheerful",
            "excited",
            "friendly",
            "hopeful",
            "newscast",
            "sad",
            "shouting",
            "terrified",
            "unfriendly",
            "whispering"
        ]
    },
    "Aria": {
        "ShortName": "en-US-AriaNeural",
        "Gender": "Female",
        "Locale": "en-US",
        "StyleList": [
            "angry",
            "chat",
            "cheerful",
            "customerservice",
            "empathetic",
            "excited",
            "friendly",
            "hopeful",
            "narration-professional",
            "newscast-casual",
            "newscast-formal",
            "sad",
            "shouting",
            "terrified",
            "unfriendly",
            "whispering"
        ]
    },
    "Davis": {
        "ShortName": "en-US-DavisNeural",
        "Gender": "Male",
        "Locale": "en-US",
        "StyleList": [
            "angry",
            "chat",
            "cheerful",
            "excited",
            "friendly",
            "hopeful",
            "sad",
            "shouting",
            "terrified",
            "unfriendly",
            "whispering"
        ]
    },
    "Amber": {
        "ShortName": "en-US-AmberNeural",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Ana": {
        "ShortName": "en-US-AnaNeural",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Ashley": {
        "ShortName": "en-US-AshleyNeural",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Brandon": {
        "ShortName": "en-US-BrandonNeural",
        "Gender": "Male",
        "Locale": "en-US"
    },
    "Christopher": {
        "ShortName": "en-US-ChristopherNeural",
        "Gender": "Male",
        "Locale": "en-US"
    },
    "Cora": {
        "ShortName": "en-US-CoraNeural",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Elizabeth": {
        "ShortName": "en-US-ElizabethNeural",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Eric": {
        "ShortName": "en-US-EricNeural",
        "Gender": "Male",
        "Locale": "en-US"
    },
    "Jacob": {
        "ShortName": "en-US-JacobNeural",
        "Gender": "Male",
        "Locale": "en-US"
    },
    "Jane": {
        "ShortName": "en-US-JaneNeural",
        "Gender": "Female",
        "Locale": "en-US",
        "StyleList": [
            "angry",
            "cheerful",
            "excited",
            "friendly",
            "hopeful",
            "sad",
            "shouting",
            "terrified",
            "unfriendly",
            "whispering"
        ]
    },
    "Jason": {
        "ShortName": "en-US-JasonNeural",
        "Gender": "Male",
        "Locale": "en-US",
        "StyleList": [
            "angry",
            "cheerful",
            "excited",
            "friendly",
            "hopeful",
            "sad",
            "shouting",
            "terrified",
            "unfriendly",
            "whispering"
        ]
    },
    "JennyMultilingualV2": {
        "ShortName": "en-US-JennyMultilingualV2Neural",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Michelle": {
        "ShortName": "en-US-MichelleNeural",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Monica": {
        "ShortName": "en-US-MonicaNeural",
        "Gender": "Female",
        "Locale": "en-US"
    },
    "Nancy": {
        "ShortName": "en-US-NancyNeural",
        "Gender": "Female",
        "Locale": "en-US",
        "StyleList": [
            "angry",
            "cheerful",
            "excited",
            "friendly",
            "hopeful",
            "sad",
            "shouting",
            "terrified",
            "unfriendly",
            "whispering"
        ]
    },
    "Roger": {
        "ShortName": "en-US-RogerNeural",
        "Gender": "Male",
        "Locale": "en-US"
    },
    "RyanMultilingual": {
        "ShortName": "en-US-RyanMultilingualNeural",
        "Gender": "Male",
        "Locale": "en-US"
    },
    "Sara": {
        "ShortName": "en-US-SaraNeural",
        "Gender": "Female",
        "Locale": "en-US",
        "StyleList": [
            "angry",
            "cheerful",
            "excited",
            "friendly",
            "hopeful",
            "sad",
            "shouting",
            "terrified",
            "unfriendly",
            "whispering"
        ]
    },
    "Steffan": {
        "ShortName": "en-US-SteffanNeural",
        "Gender": "Male",
        "Locale": "en-US"
    },
    "Tony": {
        "ShortName": "en-US-TonyNeural",
        "Gender": "Male",
        "Locale": "en-US",
        "StyleList": [
            "angry",
            "cheerful",
            "excited",
            "friendly",
            "hopeful",
            "sad",
            "shouting",
            "terrified",
            "unfriendly",
            "whispering"
        ]
    },
    "AIGenerate1": {
        "ShortName": "en-US-AIGenerate1Neural",
        "Gender": "Male",
        "Locale": "en-US"
    },
    "AIGenerate2": {
        "ShortName": "en-US-AIGenerate2Neural",
        "Gender": "Male",
        "Locale": "en-US"
    },
    "Blue": {
        "ShortName": "en-US-BlueNeural",
        "Gender": "Neutral",
        "Locale": "en-US"
    },
    "Leah": {
        "ShortName": "en-ZA-LeahNeural",
        "Gender": "Female",
        "Locale": "en-ZA"
    },
    "Luke": {
        "ShortName": "en-ZA-LukeNeural",
        "Gender": "Male",
        "Locale": "en-ZA"
    },
    "Elena": {
        "ShortName": "es-AR-ElenaNeural",
        "Gender": "Female",
        "Locale": "es-AR"
    },
    "Tomas": {
        "ShortName": "es-AR-TomasNeural",
        "Gender": "Male",
        "Locale": "es-AR"
    },
    "Sofia": {
        "ShortName": "es-BO-SofiaNeural",
        "Gender": "Female",
        "Locale": "es-BO"
    },
    "Marcelo": {
        "ShortName": "es-BO-MarceloNeural",
        "Gender": "Male",
        "Locale": "es-BO"
    },
    "Catalina": {
        "ShortName": "es-CL-CatalinaNeural",
        "Gender": "Female",
        "Locale": "es-CL"
    },
    "Lorenzo": {
        "ShortName": "es-CL-LorenzoNeural",
        "Gender": "Male",
        "Locale": "es-CL"
    },
    "Salome": {
        "ShortName": "es-CO-SalomeNeural",
        "Gender": "Female",
        "Locale": "es-CO"
    },
    "Gonzalo": {
        "ShortName": "es-CO-GonzaloNeural",
        "Gender": "Male",
        "Locale": "es-CO"
    },
    "Maria": {
        "ShortName": "es-CR-MariaNeural",
        "Gender": "Female",
        "Locale": "es-CR"
    },
    "Juan": {
        "ShortName": "es-CR-JuanNeural",
        "Gender": "Male",
        "Locale": "es-CR"
    },
    "Belkys": {
        "ShortName": "es-CU-BelkysNeural",
        "Gender": "Female",
        "Locale": "es-CU"
    },
    "Manuel": {
        "ShortName": "es-CU-ManuelNeural",
        "Gender": "Male",
        "Locale": "es-CU"
    },
    "Ramona": {
        "ShortName": "es-DO-RamonaNeural",
        "Gender": "Female",
        "Locale": "es-DO"
    },
    "Emilio": {
        "ShortName": "es-DO-EmilioNeural",
        "Gender": "Male",
        "Locale": "es-DO"
    },
    "Andrea": {
        "ShortName": "es-EC-AndreaNeural",
        "Gender": "Female",
        "Locale": "es-EC"
    },
    "Luis": {
        "ShortName": "es-EC-LuisNeural",
        "Gender": "Male",
        "Locale": "es-EC"
    },
    "Elvira": {
        "ShortName": "es-ES-ElviraNeural",
        "Gender": "Female",
        "Locale": "es-ES"
    },
    "Alvaro": {
        "ShortName": "es-ES-AlvaroNeural",
        "Gender": "Male",
        "Locale": "es-ES"
    },
    "Abril": {
        "ShortName": "es-ES-AbrilNeural",
        "Gender": "Female",
        "Locale": "es-ES"
    },
    "Arnau": {
        "ShortName": "es-ES-ArnauNeural",
        "Gender": "Male",
        "Locale": "es-ES"
    },
    "Dario": {
        "ShortName": "es-ES-DarioNeural",
        "Gender": "Male",
        "Locale": "es-ES"
    },
    "Elias": {
        "ShortName": "es-ES-EliasNeural",
        "Gender": "Male",
        "Locale": "es-ES"
    },
    "Estrella": {
        "ShortName": "es-ES-EstrellaNeural",
        "Gender": "Female",
        "Locale": "es-ES"
    },
    "Irene": {
        "ShortName": "es-ES-IreneNeural",
        "Gender": "Female",
        "Locale": "es-ES"
    },
    "Laia": {
        "ShortName": "es-ES-LaiaNeural",
        "Gender": "Female",
        "Locale": "es-ES"
    },
    "Lia": {
        "ShortName": "es-ES-LiaNeural",
        "Gender": "Female",
        "Locale": "es-ES"
    },
    "Nil": {
        "ShortName": "es-ES-NilNeural",
        "Gender": "Male",
        "Locale": "es-ES"
    },
    "Saul": {
        "ShortName": "es-ES-SaulNeural",
        "Gender": "Male",
        "Locale": "es-ES"
    },
    "Teo": {
        "ShortName": "es-ES-TeoNeural",
        "Gender": "Male",
        "Locale": "es-ES"
    },
    "Triana": {
        "ShortName": "es-ES-TrianaNeural",
        "Gender": "Female",
        "Locale": "es-ES"
    },
    "Vera": {
        "ShortName": "es-ES-VeraNeural",
        "Gender": "Female",
        "Locale": "es-ES"
    },
    "Teresa": {
        "ShortName": "es-GQ-TeresaNeural",
        "Gender": "Female",
        "Locale": "es-GQ"
    },
    "Javier": {
        "ShortName": "es-GQ-JavierNeural",
        "Gender": "Male",
        "Locale": "es-GQ"
    },
    "Marta": {
        "ShortName": "es-GT-MartaNeural",
        "Gender": "Female",
        "Locale": "es-GT"
    },
    "Andres": {
        "ShortName": "es-GT-AndresNeural",
        "Gender": "Male",
        "Locale": "es-GT"
    },
    "Karla": {
        "ShortName": "es-HN-KarlaNeural",
        "Gender": "Female",
        "Locale": "es-HN"
    },
    "Carlos": {
        "ShortName": "es-HN-CarlosNeural",
        "Gender": "Male",
        "Locale": "es-HN"
    },
    "Dalia": {
        "ShortName": "es-MX-DaliaNeural",
        "Gender": "Female",
        "Locale": "es-MX"
    },
    "Jorge": {
        "ShortName": "es-MX-JorgeNeural",
        "Gender": "Male",
        "Locale": "es-MX",
        "StyleList": [
            "chat",
            "cheerful"
        ]
    },
    "Beatriz": {
        "ShortName": "es-MX-BeatrizNeural",
        "Gender": "Female",
        "Locale": "es-MX"
    },
    "Candela": {
        "ShortName": "es-MX-CandelaNeural",
        "Gender": "Female",
        "Locale": "es-MX"
    },
    "Carlota": {
        "ShortName": "es-MX-CarlotaNeural",
        "Gender": "Female",
        "Locale": "es-MX"
    },
    "Cecilio": {
        "ShortName": "es-MX-CecilioNeural",
        "Gender": "Male",
        "Locale": "es-MX"
    },
    "Gerardo": {
        "ShortName": "es-MX-GerardoNeural",
        "Gender": "Male",
        "Locale": "es-MX"
    },
    "Larissa": {
        "ShortName": "es-MX-LarissaNeural",
        "Gender": "Female",
        "Locale": "es-MX"
    },
    "Liberto": {
        "ShortName": "es-MX-LibertoNeural",
        "Gender": "Male",
        "Locale": "es-MX"
    },
    "Luciano": {
        "ShortName": "es-MX-LucianoNeural",
        "Gender": "Male",
        "Locale": "es-MX"
    },
    "Marina": {
        "ShortName": "es-MX-MarinaNeural",
        "Gender": "Female",
        "Locale": "es-MX"
    },
    "Nuria": {
        "ShortName": "es-MX-NuriaNeural",
        "Gender": "Female",
        "Locale": "es-MX"
    },
    "Pelayo": {
        "ShortName": "es-MX-PelayoNeural",
        "Gender": "Male",
        "Locale": "es-MX"
    },
    "Renata": {
        "ShortName": "es-MX-RenataNeural",
        "Gender": "Female",
        "Locale": "es-MX"
    },
    "Yago": {
        "ShortName": "es-MX-YagoNeural",
        "Gender": "Male",
        "Locale": "es-MX"
    },
    "Yolanda": {
        "ShortName": "es-NI-YolandaNeural",
        "Gender": "Female",
        "Locale": "es-NI"
    },
    "Federico": {
        "ShortName": "es-NI-FedericoNeural",
        "Gender": "Male",
        "Locale": "es-NI"
    },
    "Margarita": {
        "ShortName": "es-PA-MargaritaNeural",
        "Gender": "Female",
        "Locale": "es-PA"
    },
    "Roberto": {
        "ShortName": "es-PA-RobertoNeural",
        "Gender": "Male",
        "Locale": "es-PA"
    },
    "Camila": {
        "ShortName": "es-PE-CamilaNeural",
        "Gender": "Female",
        "Locale": "es-PE"
    },
    "Alex": {
        "ShortName": "es-PE-AlexNeural",
        "Gender": "Male",
        "Locale": "es-PE"
    },
    "Karina": {
        "ShortName": "es-PR-KarinaNeural",
        "Gender": "Female",
        "Locale": "es-PR"
    },
    "Victor": {
        "ShortName": "es-PR-VictorNeural",
        "Gender": "Male",
        "Locale": "es-PR"
    },
    "Tania": {
        "ShortName": "es-PY-TaniaNeural",
        "Gender": "Female",
        "Locale": "es-PY"
    },
    "Mario": {
        "ShortName": "es-PY-MarioNeural",
        "Gender": "Male",
        "Locale": "es-PY"
    },
    "Lorena": {
        "ShortName": "es-SV-LorenaNeural",
        "Gender": "Female",
        "Locale": "es-SV"
    },
    "Rodrigo": {
        "ShortName": "es-SV-RodrigoNeural",
        "Gender": "Male",
        "Locale": "es-SV"
    },
    "Paloma": {
        "ShortName": "es-US-PalomaNeural",
        "Gender": "Female",
        "Locale": "es-US"
    },
    "Alonso": {
        "ShortName": "es-US-AlonsoNeural",
        "Gender": "Male",
        "Locale": "es-US"
    },
    "Valentina": {
        "ShortName": "es-UY-ValentinaNeural",
        "Gender": "Female",
        "Locale": "es-UY"
    },
    "Mateo": {
        "ShortName": "es-UY-MateoNeural",
        "Gender": "Male",
        "Locale": "es-UY"
    },
    "Paola": {
        "ShortName": "es-VE-PaolaNeural",
        "Gender": "Female",
        "Locale": "es-VE"
    },
    "Sebastian": {
        "ShortName": "es-VE-SebastianNeural",
        "Gender": "Male",
        "Locale": "es-VE"
    },
    "Anu": {
        "ShortName": "et-EE-AnuNeural",
        "Gender": "Female",
        "Locale": "et-EE"
    },
    "Kert": {
        "ShortName": "et-EE-KertNeural",
        "Gender": "Male",
        "Locale": "et-EE"
    },
    "Ainhoa": {
        "ShortName": "eu-ES-AinhoaNeural",
        "Gender": "Female",
        "Locale": "eu-ES"
    },
    "Ander": {
        "ShortName": "eu-ES-AnderNeural",
        "Gender": "Male",
        "Locale": "eu-ES"
    },
    "Dilara": {
        "ShortName": "fa-IR-DilaraNeural",
        "Gender": "Female",
        "Locale": "fa-IR"
    },
    "Farid": {
        "ShortName": "fa-IR-FaridNeural",
        "Gender": "Male",
        "Locale": "fa-IR"
    },
    "Selma": {
        "ShortName": "fi-FI-SelmaNeural",
        "Gender": "Female",
        "Locale": "fi-FI"
    },
    "Harri": {
        "ShortName": "fi-FI-HarriNeural",
        "Gender": "Male",
        "Locale": "fi-FI"
    },
    "Noora": {
        "ShortName": "fi-FI-NooraNeural",
        "Gender": "Female",
        "Locale": "fi-FI"
    },
    "Blessica": {
        "ShortName": "fil-PH-BlessicaNeural",
        "Gender": "Female",
        "Locale": "fil-PH"
    },
    "Angelo": {
        "ShortName": "fil-PH-AngeloNeural",
        "Gender": "Male",
        "Locale": "fil-PH"
    },
    "Charline": {
        "ShortName": "fr-BE-CharlineNeural",
        "Gender": "Female",
        "Locale": "fr-BE"
    },
    "Gerard": {
        "ShortName": "fr-BE-GerardNeural",
        "Gender": "Male",
        "Locale": "fr-BE"
    },
    "Sylvie": {
        "ShortName": "fr-CA-SylvieNeural",
        "Gender": "Female",
        "Locale": "fr-CA"
    },
    "Jean": {
        "ShortName": "fr-CA-JeanNeural",
        "Gender": "Male",
        "Locale": "fr-CA"
    },
    "Antoine": {
        "ShortName": "fr-CA-AntoineNeural",
        "Gender": "Male",
        "Locale": "fr-CA"
    },
    "Ariane": {
        "ShortName": "fr-CH-ArianeNeural",
        "Gender": "Female",
        "Locale": "fr-CH"
    },
    "Fabrice": {
        "ShortName": "fr-CH-FabriceNeural",
        "Gender": "Male",
        "Locale": "fr-CH"
    },
    "Denise": {
        "ShortName": "fr-FR-DeniseNeural",
        "Gender": "Female",
        "Locale": "fr-FR",
        "StyleList": [
            "cheerful",
            "sad"
        ]
    },
    "Henri": {
        "ShortName": "fr-FR-HenriNeural",
        "Gender": "Male",
        "Locale": "fr-FR",
        "StyleList": [
            "cheerful",
            "sad"
        ]
    },
    "Alain": {
        "ShortName": "fr-FR-AlainNeural",
        "Gender": "Male",
        "Locale": "fr-FR"
    },
    "Brigitte": {
        "ShortName": "fr-FR-BrigitteNeural",
        "Gender": "Female",
        "Locale": "fr-FR"
    },
    "Celeste": {
        "ShortName": "fr-FR-CelesteNeural",
        "Gender": "Female",
        "Locale": "fr-FR"
    },
    "Claude": {
        "ShortName": "fr-FR-ClaudeNeural",
        "Gender": "Male",
        "Locale": "fr-FR"
    },
    "Coralie": {
        "ShortName": "fr-FR-CoralieNeural",
        "Gender": "Female",
        "Locale": "fr-FR"
    },
    "Eloise": {
        "ShortName": "fr-FR-EloiseNeural",
        "Gender": "Female",
        "Locale": "fr-FR"
    },
    "Jacqueline": {
        "ShortName": "fr-FR-JacquelineNeural",
        "Gender": "Female",
        "Locale": "fr-FR"
    },
    "Jerome": {
        "ShortName": "fr-FR-JeromeNeural",
        "Gender": "Male",
        "Locale": "fr-FR"
    },
    "Josephine": {
        "ShortName": "fr-FR-JosephineNeural",
        "Gender": "Female",
        "Locale": "fr-FR"
    },
    "Maurice": {
        "ShortName": "fr-FR-MauriceNeural",
        "Gender": "Male",
        "Locale": "fr-FR"
    },
    "Yves": {
        "ShortName": "fr-FR-YvesNeural",
        "Gender": "Male",
        "Locale": "fr-FR"
    },
    "Yvette": {
        "ShortName": "fr-FR-YvetteNeural",
        "Gender": "Female",
        "Locale": "fr-FR"
    },
    "Orla": {
        "ShortName": "ga-IE-OrlaNeural",
        "Gender": "Female",
        "Locale": "ga-IE"
    },
    "Colm": {
        "ShortName": "ga-IE-ColmNeural",
        "Gender": "Male",
        "Locale": "ga-IE"
    },
    "Sabela": {
        "ShortName": "gl-ES-SabelaNeural",
        "Gender": "Female",
        "Locale": "gl-ES"
    },
    "Roi": {
        "ShortName": "gl-ES-RoiNeural",
        "Gender": "Male",
        "Locale": "gl-ES"
    },
    "Dhwani": {
        "ShortName": "gu-IN-DhwaniNeural",
        "Gender": "Female",
        "Locale": "gu-IN"
    },
    "Niranjan": {
        "ShortName": "gu-IN-NiranjanNeural",
        "Gender": "Male",
        "Locale": "gu-IN"
    },
    "Avri": {
        "ShortName": "he-IL-AvriNeural",
        "Gender": "Male",
        "Locale": "he-IL"
    },
    "Hila": {
        "ShortName": "he-IL-HilaNeural",
        "Gender": "Female",
        "Locale": "he-IL"
    },
    "Swara": {
        "ShortName": "hi-IN-SwaraNeural",
        "Gender": "Female",
        "Locale": "hi-IN"
    },
    "Madhur": {
        "ShortName": "hi-IN-MadhurNeural",
        "Gender": "Male",
        "Locale": "hi-IN"
    },
    "Gabrijela": {
        "ShortName": "hr-HR-GabrijelaNeural",
        "Gender": "Female",
        "Locale": "hr-HR"
    },
    "Srecko": {
        "ShortName": "hr-HR-SreckoNeural",
        "Gender": "Male",
        "Locale": "hr-HR"
    },
    "Noemi": {
        "ShortName": "hu-HU-NoemiNeural",
        "Gender": "Female",
        "Locale": "hu-HU"
    },
    "Tamas": {
        "ShortName": "hu-HU-TamasNeural",
        "Gender": "Male",
        "Locale": "hu-HU"
    },
    "Anahit": {
        "ShortName": "hy-AM-AnahitNeural",
        "Gender": "Female",
        "Locale": "hy-AM"
    },
    "Hayk": {
        "ShortName": "hy-AM-HaykNeural",
        "Gender": "Male",
        "Locale": "hy-AM"
    },
    "Gadis": {
        "ShortName": "id-ID-GadisNeural",
        "Gender": "Female",
        "Locale": "id-ID"
    },
    "Ardi": {
        "ShortName": "id-ID-ArdiNeural",
        "Gender": "Male",
        "Locale": "id-ID"
    },
    "Gudrun": {
        "ShortName": "is-IS-GudrunNeural",
        "Gender": "Female",
        "Locale": "is-IS"
    },
    "Gunnar": {
        "ShortName": "is-IS-GunnarNeural",
        "Gender": "Male",
        "Locale": "is-IS"
    },
    "Elsa": {
        "ShortName": "it-IT-ElsaNeural",
        "Gender": "Female",
        "Locale": "it-IT"
    },
    "Isabella": {
        "ShortName": "it-IT-IsabellaNeural",
        "Gender": "Female",
        "Locale": "it-IT",
        "StyleList": [
            "chat",
            "cheerful"
        ]
    },
    "Diego": {
        "ShortName": "it-IT-DiegoNeural",
        "Gender": "Male",
        "Locale": "it-IT"
    },
    "Benigno": {
        "ShortName": "it-IT-BenignoNeural",
        "Gender": "Male",
        "Locale": "it-IT"
    },
    "Calimero": {
        "ShortName": "it-IT-CalimeroNeural",
        "Gender": "Male",
        "Locale": "it-IT"
    },
    "Cataldo": {
        "ShortName": "it-IT-CataldoNeural",
        "Gender": "Male",
        "Locale": "it-IT"
    },
    "Fabiola": {
        "ShortName": "it-IT-FabiolaNeural",
        "Gender": "Female",
        "Locale": "it-IT"
    },
    "Fiamma": {
        "ShortName": "it-IT-FiammaNeural",
        "Gender": "Female",
        "Locale": "it-IT"
    },
    "Gianni": {
        "ShortName": "it-IT-GianniNeural",
        "Gender": "Male",
        "Locale": "it-IT"
    },
    "Imelda": {
        "ShortName": "it-IT-ImeldaNeural",
        "Gender": "Female",
        "Locale": "it-IT"
    },
    "Irma": {
        "ShortName": "it-IT-IrmaNeural",
        "Gender": "Female",
        "Locale": "it-IT"
    },
    "Lisandro": {
        "ShortName": "it-IT-LisandroNeural",
        "Gender": "Male",
        "Locale": "it-IT"
    },
    "Palmira": {
        "ShortName": "it-IT-PalmiraNeural",
        "Gender": "Female",
        "Locale": "it-IT"
    },
    "Pierina": {
        "ShortName": "it-IT-PierinaNeural",
        "Gender": "Female",
        "Locale": "it-IT"
    },
    "Rinaldo": {
        "ShortName": "it-IT-RinaldoNeural",
        "Gender": "Male",
        "Locale": "it-IT"
    },
    "Nanami": {
        "ShortName": "ja-JP-NanamiNeural",
        "Gender": "Female",
        "Locale": "ja-JP",
        "StyleList": [
            "chat",
            "cheerful",
            "customerservice"
        ]
    },
    "Keita": {
        "ShortName": "ja-JP-KeitaNeural",
        "Gender": "Male",
        "Locale": "ja-JP"
    },
    "Aoi": {
        "ShortName": "ja-JP-AoiNeural",
        "Gender": "Female",
        "Locale": "ja-JP"
    },
    "Daichi": {
        "ShortName": "ja-JP-DaichiNeural",
        "Gender": "Male",
        "Locale": "ja-JP"
    },
    "Mayu": {
        "ShortName": "ja-JP-MayuNeural",
        "Gender": "Female",
        "Locale": "ja-JP"
    },
    "Naoki": {
        "ShortName": "ja-JP-NaokiNeural",
        "Gender": "Male",
        "Locale": "ja-JP"
    },
    "Shiori": {
        "ShortName": "ja-JP-ShioriNeural",
        "Gender": "Female",
        "Locale": "ja-JP"
    },
    "Siti": {
        "ShortName": "jv-ID-SitiNeural",
        "Gender": "Female",
        "Locale": "jv-ID"
    },
    "Dimas": {
        "ShortName": "jv-ID-DimasNeural",
        "Gender": "Male",
        "Locale": "jv-ID"
    },
    "Eka": {
        "ShortName": "ka-GE-EkaNeural",
        "Gender": "Female",
        "Locale": "ka-GE"
    },
    "Giorgi": {
        "ShortName": "ka-GE-GiorgiNeural",
        "Gender": "Male",
        "Locale": "ka-GE"
    },
    "Aigul": {
        "ShortName": "kk-KZ-AigulNeural",
        "Gender": "Female",
        "Locale": "kk-KZ"
    },
    "Daulet": {
        "ShortName": "kk-KZ-DauletNeural",
        "Gender": "Male",
        "Locale": "kk-KZ"
    },
    "Sreymom": {
        "ShortName": "km-KH-SreymomNeural",
        "Gender": "Female",
        "Locale": "km-KH"
    },
    "Piseth": {
        "ShortName": "km-KH-PisethNeural",
        "Gender": "Male",
        "Locale": "km-KH"
    },
    "Sapna": {
        "ShortName": "kn-IN-SapnaNeural",
        "Gender": "Female",
        "Locale": "kn-IN"
    },
    "Gagan": {
        "ShortName": "kn-IN-GaganNeural",
        "Gender": "Male",
        "Locale": "kn-IN"
    },
    "SunHi": {
        "ShortName": "ko-KR-SunHiNeural",
        "Gender": "Female",
        "Locale": "ko-KR"
    },
    "InJoon": {
        "ShortName": "ko-KR-InJoonNeural",
        "Gender": "Male",
        "Locale": "ko-KR"
    },
    "BongJin": {
        "ShortName": "ko-KR-BongJinNeural",
        "Gender": "Male",
        "Locale": "ko-KR"
    },
    "GookMin": {
        "ShortName": "ko-KR-GookMinNeural",
        "Gender": "Male",
        "Locale": "ko-KR"
    },
    "JiMin": {
        "ShortName": "ko-KR-JiMinNeural",
        "Gender": "Female",
        "Locale": "ko-KR"
    },
    "SeoHyeon": {
        "ShortName": "ko-KR-SeoHyeonNeural",
        "Gender": "Female",
        "Locale": "ko-KR"
    },
    "SoonBok": {
        "ShortName": "ko-KR-SoonBokNeural",
        "Gender": "Female",
        "Locale": "ko-KR"
    },
    "YuJin": {
        "ShortName": "ko-KR-YuJinNeural",
        "Gender": "Female",
        "Locale": "ko-KR"
    },
    "Keomany": {
        "ShortName": "lo-LA-KeomanyNeural",
        "Gender": "Female",
        "Locale": "lo-LA"
    },
    "Chanthavong": {
        "ShortName": "lo-LA-ChanthavongNeural",
        "Gender": "Male",
        "Locale": "lo-LA"
    },
    "Ona": {
        "ShortName": "lt-LT-OnaNeural",
        "Gender": "Female",
        "Locale": "lt-LT"
    },
    "Leonas": {
        "ShortName": "lt-LT-LeonasNeural",
        "Gender": "Male",
        "Locale": "lt-LT"
    },
    "Everita": {
        "ShortName": "lv-LV-EveritaNeural",
        "Gender": "Female",
        "Locale": "lv-LV"
    },
    "Nils": {
        "ShortName": "lv-LV-NilsNeural",
        "Gender": "Male",
        "Locale": "lv-LV"
    },
    "Marija": {
        "ShortName": "mk-MK-MarijaNeural",
        "Gender": "Female",
        "Locale": "mk-MK"
    },
    "Aleksandar": {
        "ShortName": "mk-MK-AleksandarNeural",
        "Gender": "Male",
        "Locale": "mk-MK"
    },
    "Sobhana": {
        "ShortName": "ml-IN-SobhanaNeural",
        "Gender": "Female",
        "Locale": "ml-IN"
    },
    "Midhun": {
        "ShortName": "ml-IN-MidhunNeural",
        "Gender": "Male",
        "Locale": "ml-IN"
    },
    "Yesui": {
        "ShortName": "mn-MN-YesuiNeural",
        "Gender": "Female",
        "Locale": "mn-MN"
    },
    "Bataa": {
        "ShortName": "mn-MN-BataaNeural",
        "Gender": "Male",
        "Locale": "mn-MN"
    },
    "Aarohi": {
        "ShortName": "mr-IN-AarohiNeural",
        "Gender": "Female",
        "Locale": "mr-IN"
    },
    "Manohar": {
        "ShortName": "mr-IN-ManoharNeural",
        "Gender": "Male",
        "Locale": "mr-IN"
    },
    "Yasmin": {
        "ShortName": "ms-MY-YasminNeural",
        "Gender": "Female",
        "Locale": "ms-MY"
    },
    "Osman": {
        "ShortName": "ms-MY-OsmanNeural",
        "Gender": "Male",
        "Locale": "ms-MY"
    },
    "Grace": {
        "ShortName": "mt-MT-GraceNeural",
        "Gender": "Female",
        "Locale": "mt-MT"
    },
    "Joseph": {
        "ShortName": "mt-MT-JosephNeural",
        "Gender": "Male",
        "Locale": "mt-MT"
    },
    "Nilar": {
        "ShortName": "my-MM-NilarNeural",
        "Gender": "Female",
        "Locale": "my-MM"
    },
    "Thiha": {
        "ShortName": "my-MM-ThihaNeural",
        "Gender": "Male",
        "Locale": "my-MM"
    },
    "Pernille": {
        "ShortName": "nb-NO-PernilleNeural",
        "Gender": "Female",
        "Locale": "nb-NO"
    },
    "Finn": {
        "ShortName": "nb-NO-FinnNeural",
        "Gender": "Male",
        "Locale": "nb-NO"
    },
    "Iselin": {
        "ShortName": "nb-NO-IselinNeural",
        "Gender": "Female",
        "Locale": "nb-NO"
    },
    "Hemkala": {
        "ShortName": "ne-NP-HemkalaNeural",
        "Gender": "Female",
        "Locale": "ne-NP"
    },
    "Sagar": {
        "ShortName": "ne-NP-SagarNeural",
        "Gender": "Male",
        "Locale": "ne-NP"
    },
    "Dena": {
        "ShortName": "nl-BE-DenaNeural",
        "Gender": "Female",
        "Locale": "nl-BE"
    },
    "Arnaud": {
        "ShortName": "nl-BE-ArnaudNeural",
        "Gender": "Male",
        "Locale": "nl-BE"
    },
    "Fenna": {
        "ShortName": "nl-NL-FennaNeural",
        "Gender": "Female",
        "Locale": "nl-NL"
    },
    "Maarten": {
        "ShortName": "nl-NL-MaartenNeural",
        "Gender": "Male",
        "Locale": "nl-NL"
    },
    "Colette": {
        "ShortName": "nl-NL-ColetteNeural",
        "Gender": "Female",
        "Locale": "nl-NL"
    },
    "Hanna": {
        "ShortName": "nl-NL-HannaRUS",
        "Gender": "Female",
        "Locale": "nl-NL"
    },
    "Agnieszka": {
        "ShortName": "pl-PL-AgnieszkaNeural",
        "Gender": "Female",
        "Locale": "pl-PL"
    },
    "Marek": {
        "ShortName": "pl-PL-MarekNeural",
        "Gender": "Male",
        "Locale": "pl-PL"
    },
    "Zofia": {
        "ShortName": "pl-PL-ZofiaNeural",
        "Gender": "Female",
        "Locale": "pl-PL"
    },
    "Latifa": {
        "ShortName": "ps-AF-LatifaNeural",
        "Gender": "Female",
        "Locale": "ps-AF"
    },
    "GulNawaz": {
        "ShortName": "ps-AF-GulNawazNeural",
        "Gender": "Male",
        "Locale": "ps-AF"
    },
    "Francisca": {
        "ShortName": "pt-BR-FranciscaNeural",
        "Gender": "Female",
        "Locale": "pt-BR",
        "StyleList": [
            "calm"
        ]
    },
    "Antonio": {
        "ShortName": "pt-BR-AntonioNeural",
        "Gender": "Male",
        "Locale": "pt-BR"
    },
    "Brenda": {
        "ShortName": "pt-BR-BrendaNeural",
        "Gender": "Female",
        "Locale": "pt-BR"
    },
    "Donato": {
        "ShortName": "pt-BR-DonatoNeural",
        "Gender": "Male",
        "Locale": "pt-BR"
    },
    "Elza": {
        "ShortName": "pt-BR-ElzaNeural",
        "Gender": "Female",
        "Locale": "pt-BR"
    },
    "Fabio": {
        "ShortName": "pt-BR-FabioNeural",
        "Gender": "Male",
        "Locale": "pt-BR"
    },
    "Giovanna": {
        "ShortName": "pt-BR-GiovannaNeural",
        "Gender": "Female",
        "Locale": "pt-BR"
    },
    "Humberto": {
        "ShortName": "pt-BR-HumbertoNeural",
        "Gender": "Male",
        "Locale": "pt-BR"
    },
    "Julio": {
        "ShortName": "pt-BR-JulioNeural",
        "Gender": "Male",
        "Locale": "pt-BR"
    },
    "Leila": {
        "ShortName": "pt-BR-LeilaNeural",
        "Gender": "Female",
        "Locale": "pt-BR"
    },
    "Leticia": {
        "ShortName": "pt-BR-LeticiaNeural",
        "Gender": "Female",
        "Locale": "pt-BR"
    },
    "Manuela": {
        "ShortName": "pt-BR-ManuelaNeural",
        "Gender": "Female",
        "Locale": "pt-BR"
    },
    "Nicolau": {
        "ShortName": "pt-BR-NicolauNeural",
        "Gender": "Male",
        "Locale": "pt-BR"
    },
    "Valerio": {
        "ShortName": "pt-BR-ValerioNeural",
        "Gender": "Male",
        "Locale": "pt-BR"
    },
    "Yara": {
        "ShortName": "pt-BR-YaraNeural",
        "Gender": "Female",
        "Locale": "pt-BR"
    },
    "Raquel": {
        "ShortName": "pt-PT-RaquelNeural",
        "Gender": "Female",
        "Locale": "pt-PT"
    },
    "Duarte": {
        "ShortName": "pt-PT-DuarteNeural",
        "Gender": "Male",
        "Locale": "pt-PT"
    },
    "Fernanda": {
        "ShortName": "pt-PT-FernandaNeural",
        "Gender": "Female",
        "Locale": "pt-PT"
    },
    "Alina": {
        "ShortName": "ro-RO-AlinaNeural",
        "Gender": "Female",
        "Locale": "ro-RO"
    },
    "Emil": {
        "ShortName": "ro-RO-EmilNeural",
        "Gender": "Male",
        "Locale": "ro-RO"
    },
    "Svetlana": {
        "ShortName": "ru-RU-SvetlanaNeural",
        "Gender": "Female",
        "Locale": "ru-RU"
    },
    "Dmitry": {
        "ShortName": "ru-RU-DmitryNeural",
        "Gender": "Male",
        "Locale": "ru-RU"
    },
    "Dariya": {
        "ShortName": "ru-RU-DariyaNeural",
        "Gender": "Female",
        "Locale": "ru-RU"
    },
    "Thilini": {
        "ShortName": "si-LK-ThiliniNeural",
        "Gender": "Female",
        "Locale": "si-LK"
    },
    "Sameera": {
        "ShortName": "si-LK-SameeraNeural",
        "Gender": "Male",
        "Locale": "si-LK"
    },
    "Viktoria": {
        "ShortName": "sk-SK-ViktoriaNeural",
        "Gender": "Female",
        "Locale": "sk-SK"
    },
    "Lukas": {
        "ShortName": "sk-SK-LukasNeural",
        "Gender": "Male",
        "Locale": "sk-SK"
    },
    "Petra": {
        "ShortName": "sl-SI-PetraNeural",
        "Gender": "Female",
        "Locale": "sl-SI"
    },
    "Rok": {
        "ShortName": "sl-SI-RokNeural",
        "Gender": "Male",
        "Locale": "sl-SI"
    },
    "Ubax": {
        "ShortName": "so-SO-UbaxNeural",
        "Gender": "Female",
        "Locale": "so-SO"
    },
    "Muuse": {
        "ShortName": "so-SO-MuuseNeural",
        "Gender": "Male",
        "Locale": "so-SO"
    },
    "Anila": {
        "ShortName": "sq-AL-AnilaNeural",
        "Gender": "Female",
        "Locale": "sq-AL"
    },
    "Ilir": {
        "ShortName": "sq-AL-IlirNeural",
        "Gender": "Male",
        "Locale": "sq-AL"
    },
    "Nicholas": {
        "ShortName": "sr-Latn-RS-NicholasNeural",
        "Gender": "Male",
        "Locale": "sr-LATN-RS"
    },
    "Sophie": {
        "ShortName": "sr-Latn-RS-SophieNeural",
        "Gender": "Female",
        "Locale": "sr-LATN-RS"
    },
    "Sophie": {
        "ShortName": "sr-RS-SophieNeural",
        "Gender": "Female",
        "Locale": "sr-RS"
    },
    "Nicholas": {
        "ShortName": "sr-RS-NicholasNeural",
        "Gender": "Male",
        "Locale": "sr-RS"
    },
    "Tuti": {
        "ShortName": "su-ID-TutiNeural",
        "Gender": "Female",
        "Locale": "su-ID"
    },
    "Jajang": {
        "ShortName": "su-ID-JajangNeural",
        "Gender": "Male",
        "Locale": "su-ID"
    },
    "Sofie": {
        "ShortName": "sv-SE-SofieNeural",
        "Gender": "Female",
        "Locale": "sv-SE"
    },
    "Mattias": {
        "ShortName": "sv-SE-MattiasNeural",
        "Gender": "Male",
        "Locale": "sv-SE"
    },
    "Hillevi": {
        "ShortName": "sv-SE-HilleviNeural",
        "Gender": "Female",
        "Locale": "sv-SE"
    },
    "Zuri": {
        "ShortName": "sw-KE-ZuriNeural",
        "Gender": "Female",
        "Locale": "sw-KE"
    },
    "Rafiki": {
        "ShortName": "sw-KE-RafikiNeural",
        "Gender": "Male",
        "Locale": "sw-KE"
    },
    "Rehema": {
        "ShortName": "sw-TZ-RehemaNeural",
        "Gender": "Female",
        "Locale": "sw-TZ"
    },
    "Daudi": {
        "ShortName": "sw-TZ-DaudiNeural",
        "Gender": "Male",
        "Locale": "sw-TZ"
    },
    "Pallavi": {
        "ShortName": "ta-IN-PallaviNeural",
        "Gender": "Female",
        "Locale": "ta-IN"
    },
    "Valluvar": {
        "ShortName": "ta-IN-Valluvar",
        "Gender": "Male",
        "Locale": "ta-IN"
    },
    "Saranya": {
        "ShortName": "ta-LK-SaranyaNeural",
        "Gender": "Female",
        "Locale": "ta-LK"
    },
    "Kumar": {
        "ShortName": "ta-LK-KumarNeural",
        "Gender": "Male",
        "Locale": "ta-LK"
    },
    "Kani": {
        "ShortName": "ta-MY-KaniNeural",
        "Gender": "Female",
        "Locale": "ta-MY"
    },
    "Surya": {
        "ShortName": "ta-MY-SuryaNeural",
        "Gender": "Male",
        "Locale": "ta-MY"
    },
    "Venba": {
        "ShortName": "ta-SG-VenbaNeural",
        "Gender": "Female",
        "Locale": "ta-SG"
    },
    "Anbu": {
        "ShortName": "ta-SG-AnbuNeural",
        "Gender": "Male",
        "Locale": "ta-SG"
    },
    "Shruti": {
        "ShortName": "te-IN-ShrutiNeural",
        "Gender": "Female",
        "Locale": "te-IN"
    },
    "Mohan": {
        "ShortName": "te-IN-MohanNeural",
        "Gender": "Male",
        "Locale": "te-IN"
    },
    "Premwadee": {
        "ShortName": "th-TH-PremwadeeNeural",
        "Gender": "Female",
        "Locale": "th-TH"
    },
    "Niwat": {
        "ShortName": "th-TH-NiwatNeural",
        "Gender": "Male",
        "Locale": "th-TH"
    },
    "Achara": {
        "ShortName": "th-TH-AcharaNeural",
        "Gender": "Female",
        "Locale": "th-TH"
    },
    "Emel": {
        "ShortName": "tr-TR-EmelNeural",
        "Gender": "Female",
        "Locale": "tr-TR"
    },
    "Ahmet": {
        "ShortName": "tr-TR-AhmetNeural",
        "Gender": "Male",
        "Locale": "tr-TR"
    },
    "Polina": {
        "ShortName": "uk-UA-PolinaNeural",
        "Gender": "Female",
        "Locale": "uk-UA"
    },
    "Ostap": {
        "ShortName": "uk-UA-OstapNeural",
        "Gender": "Male",
        "Locale": "uk-UA"
    },
    "Gul": {
        "ShortName": "ur-IN-GulNeural",
        "Gender": "Female",
        "Locale": "ur-IN"
    },
    "Salman": {
        "ShortName": "ur-IN-SalmanNeural",
        "Gender": "Male",
        "Locale": "ur-IN"
    },
    "Uzma": {
        "ShortName": "ur-PK-UzmaNeural",
        "Gender": "Female",
        "Locale": "ur-PK"
    },
    "Asad": {
        "ShortName": "ur-PK-AsadNeural",
        "Gender": "Male",
        "Locale": "ur-PK"
    },
    "Madina": {
        "ShortName": "uz-UZ-MadinaNeural",
        "Gender": "Female",
        "Locale": "uz-UZ"
    },
    "Sardor": {
        "ShortName": "uz-UZ-SardorNeural",
        "Gender": "Male",
        "Locale": "uz-UZ"
    },
    "HoaiMy": {
        "ShortName": "vi-VN-HoaiMyNeural",
        "Gender": "Female",
        "Locale": "vi-VN"
    },
    "NamMinh": {
        "ShortName": "vi-VN-NamMinhNeural",
        "Gender": "Male",
        "Locale": "vi-VN"
    },
    "Xiaotong": {
        "ShortName": "wuu-CN-XiaotongNeural",
        "Gender": "Female",
        "Locale": "wuu-CN"
    },
    "Yunzhe": {
        "ShortName": "wuu-CN-YunzheNeural",
        "Gender": "Male",
        "Locale": "wuu-CN"
    },
    "Xiaoxiao": {
        "ShortName": "zh-CN-XiaoxiaoNeural",
        "Gender": "Female",
        "Locale": "zh-CN",
        "StyleList": [
            "affectionate",
            "angry",
            "assistant",
            "calm",
            "chat",
            "cheerful",
            "customerservice",
            "disgruntled",
            "fearful",
            "friendly",
            "gentle",
            "lyrical",
            "newscast",
            "poetry-reading",
            "sad",
            "serious"
        ]
    },
    "Yunxi": {
        "ShortName": "zh-CN-YunxiNeural",
        "Gender": "Male",
        "Locale": "zh-CN",
        "StyleList": [
            "angry",
            "assistant",
            "chat",
            "cheerful",
            "depressed",
            "disgruntled",
            "embarrassed",
            "fearful",
            "narration-relaxed",
            "newscast",
            "sad",
            "serious"
        ],
        "RolePlayList": [
            "Boy",
            "Narrator",
            "YoungAdultMale"
        ]
    },
    "Yunjian": {
        "ShortName": "zh-CN-YunjianNeural",
        "Gender": "Male",
        "Locale": "zh-CN",
        "StyleList": [
            "narration-relaxed",
            "sports-commentary",
            "sports-commentary-excited"
        ]
    },
    "Xiaoyi": {
        "ShortName": "zh-CN-XiaoyiNeural",
        "Gender": "Female",
        "Locale": "zh-CN",
        "StyleList": [
            "affectionate",
            "angry",
            "cheerful",
            "disgruntled",
            "embarrassed",
            "fearful",
            "gentle",
            "sad",
            "serious"
        ]
    },
    "Yunyang": {
        "ShortName": "zh-CN-YunyangNeural",
        "Gender": "Male",
        "Locale": "zh-CN",
        "StyleList": [
            "customerservice",
            "narration-professional",
            "newscast-casual"
        ]
    },
    "Xiaochen": {
        "ShortName": "zh-CN-XiaochenNeural",
        "Gender": "Female",
        "Locale": "zh-CN"
    },
    "Xiaohan": {
        "ShortName": "zh-CN-XiaohanNeural",
        "Gender": "Female",
        "Locale": "zh-CN",
        "StyleList": [
            "affectionate",
            "angry",
            "calm",
            "cheerful",
            "disgruntled",
            "embarrassed",
            "fearful",
            "gentle",
            "sad",
            "serious"
        ]
    },
    "Xiaomeng": {
        "ShortName": "zh-CN-XiaomengNeural",
        "Gender": "Female",
        "Locale": "zh-CN",
        "StyleList": [
            "chat"
        ]
    },
    "Xiaomo": {
        "ShortName": "zh-CN-XiaomoNeural",
        "Gender": "Female",
        "Locale": "zh-CN",
        "StyleList": [
            "affectionate",
            "angry",
            "calm",
            "cheerful",
            "depressed",
            "disgruntled",
            "embarrassed",
            "envious",
            "fearful",
            "gentle",
            "sad",
            "serious"
        ],
        "RolePlayList": [
            "Boy",
            "Girl",
            "OlderAdultFemale",
            "OlderAdultMale",
            "SeniorFemale",
            "SeniorMale",
            "YoungAdultFemale",
            "YoungAdultMale"
        ]
    },
    "Xiaoqiu": {
        "ShortName": "zh-CN-XiaoqiuNeural",
        "Gender": "Female",
        "Locale": "zh-CN"
    },
    "Xiaorui": {
        "ShortName": "zh-CN-XiaoruiNeural",
        "Gender": "Female",
        "Locale": "zh-CN",
        "StyleList": [
            "angry",
            "calm",
            "fearful",
            "sad"
        ]
    },
    "Xiaoshuang": {
        "ShortName": "zh-CN-XiaoshuangNeural",
        "Gender": "Female",
        "Locale": "zh-CN",
        "StyleList": [
            "chat"
        ]
    },
    "Xiaoxuan": {
        "ShortName": "zh-CN-XiaoxuanNeural",
        "Gender": "Female",
        "Locale": "zh-CN",
        "StyleList": [
            "angry",
            "calm",
            "cheerful",
            "depressed",
            "disgruntled",
            "fearful",
            "gentle",
            "serious"
        ],
        "RolePlayList": [
            "Boy",
            "Girl",
            "OlderAdultFemale",
            "OlderAdultMale",
            "SeniorFemale",
            "SeniorMale",
            "YoungAdultFemale",
            "YoungAdultMale"
        ]
    },
    "Xiaoyan": {
        "ShortName": "zh-CN-XiaoyanNeural",
        "Gender": "Female",
        "Locale": "zh-CN"
    },
    "Xiaoyou": {
        "ShortName": "zh-CN-XiaoyouNeural",
        "Gender": "Female",
        "Locale": "zh-CN"
    },
    "Xiaozhen": {
        "ShortName": "zh-CN-XiaozhenNeural",
        "Gender": "Female",
        "Locale": "zh-CN",
        "StyleList": [
            "angry",
            "cheerful",
            "disgruntled",
            "fearful",
            "sad",
            "serious"
        ]
    },
    "Yunfeng": {
        "ShortName": "zh-CN-YunfengNeural",
        "Gender": "Male",
        "Locale": "zh-CN",
        "StyleList": [
            "angry",
            "cheerful",
            "depressed",
            "disgruntled",
            "fearful",
            "sad",
            "serious"
        ]
    },
    "Yunhao": {
        "ShortName": "zh-CN-YunhaoNeural",
        "Gender": "Male",
        "Locale": "zh-CN",
        "StyleList": [
            "advertisement-upbeat"
        ]
    },
    "Yunxia": {
        "ShortName": "zh-CN-YunxiaNeural",
        "Gender": "Male",
        "Locale": "zh-CN",
        "StyleList": [
            "angry",
            "calm",
            "cheerful",
            "fearful",
            "sad"
        ]
    },
    "Yunye": {
        "ShortName": "zh-CN-YunyeNeural",
        "Gender": "Male",
        "Locale": "zh-CN",
        "StyleList": [
            "angry",
            "calm",
            "cheerful",
            "disgruntled",
            "embarrassed",
            "fearful",
            "sad",
            "serious"
        ],
        "RolePlayList": [
            "Boy",
            "Girl",
            "OlderAdultFemale",
            "OlderAdultMale",
            "SeniorFemale",
            "SeniorMale",
            "YoungAdultFemale",
            "YoungAdultMale"
        ]
    },
    "Yunze": {
        "ShortName": "zh-CN-YunzeNeural",
        "Gender": "Male",
        "Locale": "zh-CN",
        "StyleList": [
            "angry",
            "calm",
            "cheerful",
            "depressed",
            "disgruntled",
            "documentary-narration",
            "fearful",
            "sad",
            "serious"
        ],
        "RolePlayList": [
            "OlderAdultMale",
            "SeniorMale"
        ]
    },
    "Yundeng": {
        "ShortName": "zh-CN-henan-YundengNeural",
        "Gender": "Male",
        "Locale": "zh-CN-henan"
    },
    "Xiaobei": {
        "ShortName": "zh-CN-liaoning-XiaobeiNeural",
        "Gender": "Female",
        "Locale": "zh-CN-liaoning"
    },
    "Xiaoni": {
        "ShortName": "zh-CN-shaanxi-XiaoniNeural",
        "Gender": "Female",
        "Locale": "zh-CN-shaanxi"
    },
    "Yunxiang": {
        "ShortName": "zh-CN-shandong-YunxiangNeural",
        "Gender": "Male",
        "Locale": "zh-CN-shandong"
    },
    "sichuan-Yunxi": {
        "ShortName": "zh-CN-sichuan-YunxiNeural",
        "Gender": "Male",
        "Locale": "zh-CN-sichuan"
    },
    "Huihui": {
        "ShortName": "zh-CN-HuihuiRUS",
        "Gender": "Female",
        "Locale": "zh-CN"
    },
    "Kangkang": {
        "ShortName": "zh-CN-Kangkang",
        "Gender": "Male",
        "Locale": "zh-CN"
    },
    "Yaoyao": {
        "ShortName": "zh-CN-Yaoyao",
        "Gender": "Female",
        "Locale": "zh-CN"
    },
    "HiuMaan": {
        "ShortName": "zh-HK-HiuMaanNeural",
        "Gender": "Female",
        "Locale": "zh-HK"
    },
    "HiuGaai": {
        "ShortName": "zh-HK-HiuGaaiNeural",
        "Gender": "Female",
        "Locale": "zh-HK"
    },
    "WanLung": {
        "ShortName": "zh-HK-WanLungNeural",
        "Gender": "Male",
        "Locale": "zh-HK"
    },
    "XiaoMin": {
        "ShortName": "yue-CN-XiaoMinNeural",
        "Gender": "Female",
        "Locale": "yue-CN"
    },
    "YunSong": {
        "ShortName": "yue-CN-YunSongNeural",
        "Gender": "Male",
        "Locale": "yue-CN"
    },
    "Danny": {
        "ShortName": "zh-HK-Danny",
        "Gender": "Male",
        "Locale": "zh-HK"
    },
    "Tracy": {
        "ShortName": "zh-HK-TracyRUS",
        "Gender": "Female",
        "Locale": "zh-HK"
    },
    "HsiaoChen": {
        "ShortName": "zh-TW-HsiaoChenNeural",
        "Gender": "Female",
        "Locale": "zh-TW"
    },
    "HsiaoYu": {
        "ShortName": "zh-TW-HsiaoYuNeural",
        "Gender": "Female",
        "Locale": "zh-TW"
    },
    "YunJhe": {
        "ShortName": "zh-TW-YunJheNeural",
        "Gender": "Male",
        "Locale": "zh-TW"
    },
    "HanHan": {
        "ShortName": "zh-TW-HanHanRUS",
        "Gender": "Female",
        "Locale": "zh-TW"
    },
    "Yating": {
        "ShortName": "zh-TW-Yating",
        "Gender": "Female",
        "Locale": "zh-TW"
    },
    "Zhiwei": {
        "ShortName": "zh-TW-Zhiwei",
        "Gender": "Male",
        "Locale": "zh-TW"
    }
}
