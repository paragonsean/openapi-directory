from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.detected_language import DetectedLanguage
from openapi_server.models.screen import Screen
from openapi_server import util


async def text_moderation_detect_language(request: web.Request, content_type, text_content) -> web.Response:
    """text_moderation_detect_language

    This operation will detect the language of given input content. Returns the &lt;a href&#x3D;\&quot;http://www-01.sil.org/iso639-3/codes.asp\&quot;&gt;ISO 639-3 code&lt;/a&gt; for the predominant language comprising the submitted text. Over 110 languages supported.

    :param content_type: The content type.
    :type content_type: str
    :param text_content: Content to screen.
    :type text_content: 

    """
    return web.Response(status=200)


async def text_moderation_screen_text(request: web.Request, content_type, text_content, language=None, autocorrect=None, pii=None, list_id=None, classify=None) -> web.Response:
    """Detect profanity and match against custom and shared blacklists

    Detects profanity in more than 100 languages and match against custom and shared blacklists.

    :param content_type: The content type.
    :type content_type: str
    :param text_content: Content to screen.
    :type text_content: 
    :param language: Language of the text.
    :type language: str
    :param autocorrect: Autocorrect text.
    :type autocorrect: bool
    :param pii: Detect personal identifiable information.
    :type pii: bool
    :param list_id: The list Id.
    :type list_id: str
    :param classify: Classify input.
    :type classify: bool

    """
    return web.Response(status=200)
