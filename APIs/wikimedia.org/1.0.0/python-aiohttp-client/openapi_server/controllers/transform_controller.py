from typing import List, Dict
from aiohttp import web

from openapi_server.models.cx_dict import CxDict
from openapi_server.models.cx_languagepairs import CxLanguagepairs
from openapi_server.models.cx_list_tools import CxListTools
from openapi_server.models.cx_mt import CxMt
from openapi_server.models.problem import Problem
from openapi_server import util


async def transform_html_from_from_lang_to_to_lang_post(request: web.Request, from_lang, to_lang, html) -> web.Response:
    """Machine-translate content

    Fetches the machine translation for the posted content from the source to the destination language.  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

    :param from_lang: The source language code
    :type from_lang: str
    :param to_lang: The target language code
    :type to_lang: str
    :param html: The HTML content to translate
    :type html: str

    """
    return web.Response(status=200)


async def transform_html_from_from_lang_to_to_lang_provider_post(request: web.Request, from_lang, to_lang, provider, html) -> web.Response:
    """Machine-translate content

    Fetches the machine translation for the posted content from the source to the destination language.  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

    :param from_lang: The source language code
    :type from_lang: str
    :param to_lang: The target language code
    :type to_lang: str
    :param provider: The machine translation provider id
    :type provider: str
    :param html: The HTML content to translate
    :type html: str

    """
    return web.Response(status=200)


async def transform_list_languagepairs_get(request: web.Request, ) -> web.Response:
    """Lists the language pairs supported by the back-end

    Fetches the list of language pairs the back-end service can translate  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 


    """
    return web.Response(status=200)


async def transform_list_pair_from_to_get(request: web.Request, _from, to) -> web.Response:
    """Lists the tools available for a language pair

    Fetches the list of tools that are available for the given pair of languages.  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

    :param _from: The source language code
    :type _from: str
    :param to: The target language code
    :type to: str

    """
    return web.Response(status=200)


async def transform_list_tool_tool_from_get(request: web.Request, tool, _from) -> web.Response:
    """Lists the tools and language pairs available for the given tool category

    Fetches the list of tools and all of the language pairs it can translate  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

    :param tool: The tool category to list tools and language pairs for
    :type tool: str
    :param _from: The source language code
    :type _from: str

    """
    return web.Response(status=200)


async def transform_list_tool_tool_from_to_get(request: web.Request, tool, _from, to) -> web.Response:
    """Lists the tools and language pairs available for the given tool category

    Fetches the list of tools and all of the language pairs it can translate  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

    :param tool: The tool category to list tools and language pairs for
    :type tool: str
    :param _from: The source language code
    :type _from: str
    :param to: The target language code
    :type to: str

    """
    return web.Response(status=200)


async def transform_list_tool_tool_get(request: web.Request, tool) -> web.Response:
    """Lists the tools and language pairs available for the given tool category

    Fetches the list of tools and all of the language pairs it can translate  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

    :param tool: The tool category to list tools and language pairs for
    :type tool: str

    """
    return web.Response(status=200)


async def transform_word_from_from_lang_to_to_lang_word_get(request: web.Request, from_lang, to_lang, word) -> web.Response:
    """Fetch the dictionary meaning of a word

    Fetches the dictionary meaning of a word from a language and displays it in the target language.  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

    :param from_lang: The source language code
    :type from_lang: str
    :param to_lang: The target language code
    :type to_lang: str
    :param word: The word to lookup
    :type word: str

    """
    return web.Response(status=200)


async def transform_word_from_from_lang_to_to_lang_word_provider_get(request: web.Request, from_lang, to_lang, word, provider) -> web.Response:
    """Fetch the dictionary meaning of a word

    Fetches the dictionary meaning of a word from a language and displays it in the target language.  Stability: [unstable](https://www.mediawiki.org/wiki/API_versioning#Unstable) 

    :param from_lang: The source language code
    :type from_lang: str
    :param to_lang: The target language code
    :type to_lang: str
    :param word: The word to lookup
    :type word: str
    :param provider: The dictionary provider id
    :type provider: str

    """
    return web.Response(status=200)
