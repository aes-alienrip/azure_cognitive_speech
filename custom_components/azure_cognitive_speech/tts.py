import logging
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.components.tts import PLATFORM_SCHEMA, Provider
from homeassistant.const import CONF_API_KEY, CONF_REGION
from .const import (
    DEFAULT_LANGUAGE, SUPPORT_LANGUAGES,
    OPT_VOICE, OPT_STYLE, OPT_ROLE,
    OPT_RATE, CONF_DEFAULT_VOICE
)
from .speech import CognitiveSpeech

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_API_KEY): cv.string,
        vol.Required(CONF_REGION): cv.string,
        vol.Required(CONF_DEFAULT_VOICE): cv.string,
        vol.Optional(OPT_RATE, default=0): vol.All(
            vol.Coerce(int), vol.Range(-100, 100)
        )
    }
)


async def async_get_engine(hass, config, discovery_info=None):
    return CognitiveProvider(hass, config)

class CognitiveProvider(Provider):
    def __init__(self, hass, config):
        self.hass = hass
        self.name = "Azure Cognitive Speech"
        self._apikey = config.get(CONF_API_KEY)
        self._region = config.get(CONF_REGION)
        self._default_voice = config.get(CONF_DEFAULT_VOICE)

    @property
    def default_language(self):
        return DEFAULT_LANGUAGE

    @property
    def supported_languages(self):
        return SUPPORT_LANGUAGES

    @property
    def supported_options(self):
        return [OPT_VOICE, OPT_STYLE, OPT_ROLE, OPT_RATE]

    @property
    def default_options(self):
        return {OPT_VOICE: self._default_voice, OPT_RATE: 0}

    def get_tts_audio(self, message, language, options=None):
        voice = options.get(OPT_VOICE) if options is not None else None
        style = options.get(OPT_STYLE) if options is not None else None
        role = options.get(OPT_ROLE) if options is not None else None
        rate = options.get(OPT_RATE) if options is not None else None
        speech = CognitiveSpeech(self.hass, self._region, self._apikey, self._default_voice)
        r = speech.speech(message, voice=voice, style=style, role=role, rate=rate)
        if r is not None:
            return "mp3", r
        return None, None

