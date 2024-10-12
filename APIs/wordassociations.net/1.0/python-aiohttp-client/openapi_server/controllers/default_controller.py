from typing import List, Dict
from aiohttp import web

from openapi_server.models.body import Body
from openapi_server import util


async def json_search_get(request: web.Request, text, lang, type=None, limit=None, pos=None, indent=None) -> web.Response:
    """json_search_get

    Gets associations with the given word or phrase. 

    :param text: Word or phrase to find associations with. Tip. You can use multiple parameters &#39;text&#39; in a request (from 1 to 10 inclusive). This way you can get associations for several input words or phrases in one response. Restriction: regardless of the size of the text association lookup is always performed by the first 10 words of the text. 
    :type text: List[str]
    :param lang: Query language. Use language code for the language of the text: * de - German; * en - English; * es - Spanish; * fr - French; * it - Italian; * pt - Portuguese; * ru - Russian; 
    :type lang: str
    :param type: Type of result. Possible values:  * stimulus - an input data (the text parameter) is considered as a response word. The service returns a list of stimuli words, which evoke a given response word; * response - an input data (the text parameter) is considered as a stimulus word. The service returns a list of response words, which come to mind for a given stimulus word. 
    :type type: str
    :param limit: Maximum number of results to return. Allows to limit the number of results (associations) in response. The value of this parameter is an integer number from 1 to 300 inclusive. 
    :type limit: int
    :param pos: Parts of speech to return. Allows to limit results by specified parts of speech. The value of this parameter is a list of parts of speech separated by comma. The following parts of speech codes are supported: * noun * adjective * verb * adverb 
    :type pos: List[str]
    :param indent: Indentation switch for pretty printing of JSON response. Allows to either turn on or off space indentation for a response. The following values are allowed: * yes - turns indentation with spaces on; * no - turn indentation with spaces off; 
    :type indent: str

    """
    return web.Response(status=200)


async def json_search_post(request: web.Request, text, lang, type=None, limit=None, pos=None, indent=None) -> web.Response:
    """json_search_post

    Gets associations with the given word or phrase. 

    :param text: Word or phrase to find associations with. Tip. You can use multiple parameters &#39;text&#39; in a request (from 1 to 10 inclusive). This way you can get associations for several input words or phrases in one response. Restriction: regardless of the size of the text association lookup is always performed by the first 10 words of the text. 
    :type text: List[str]
    :param lang: Query language. Use language code for the language of the text: * de - German; * en - English; * es - Spanish; * fr - French; * it - Italian; * pt - Portuguese; * ru - Russian; 
    :type lang: str
    :param type: Type of result. Possible values:  * stimulus - an input data (the text parameter) is considered as a response word. The service returns a list of stimuli words, which evoke a given response word; * response - an input data (the text parameter) is considered as a stimulus word. The service returns a list of response words, which come to mind for a given stimulus word. 
    :type type: str
    :param limit: Maximum number of results to return. Allows to limit the number of results (associations) in response. The value of this parameter is an integer number from 1 to 300 inclusive. 
    :type limit: int
    :param pos: Parts of speech to return. Allows to limit results by specified parts of speech. The value of this parameter is a list of parts of speech separated by comma. The following parts of speech codes are supported: * noun * adjective * verb * adverb 
    :type pos: List[str]
    :param indent: Indentation switch for pretty printing of JSON response. Allows to either turn on or off space indentation for a response. The following values are allowed: * yes - turns indentation with spaces on; * no - turn indentation with spaces off; 
    :type indent: str

    """
    return web.Response(status=200)
