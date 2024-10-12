from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.luis_result import LuisResult
from openapi_server import util


async def prediction_resolve(request: web.Request, app_id, q, timezone_offset=None, verbose=None, staging=None, spell_check=None, bing_spell_check_subscription_key=None, log=None) -> web.Response:
    """prediction_resolve

    Gets predictions for a given utterance, in the form of intents and entities. The current maximum query size is 500 characters.

    :param app_id: The LUIS application ID (Guid).
    :type app_id: str
    :param q: The utterance to predict.
    :type q: str
    :param timezone_offset: The timezone offset for the location of the request.
    :type timezone_offset: 
    :param verbose: If true, return all intents instead of just the top scoring intent.
    :type verbose: bool
    :param staging: Use the staging endpoint slot.
    :type staging: bool
    :param spell_check: Enable spell checking.
    :type spell_check: bool
    :param bing_spell_check_subscription_key: The subscription key to use when enabling bing spell check
    :type bing_spell_check_subscription_key: str
    :param log: Log query (default is true)
    :type log: bool

    """
    return web.Response(status=200)


async def prediction_resolve2(request: web.Request, app_id, q, timezone_offset=None, verbose=None, staging=None, spell_check=None, bing_spell_check_subscription_key=None, log=None) -> web.Response:
    """prediction_resolve2

    Gets predictions for a given utterance, in the form of intents and entities. The current maximum query size is 500 characters.

    :param app_id: The LUIS application ID (guid).
    :type app_id: str
    :param q: The utterance to predict.
    :type q: str
    :param timezone_offset: The timezone offset for the location of the request.
    :type timezone_offset: 
    :param verbose: If true, return all intents instead of just the top scoring intent.
    :type verbose: bool
    :param staging: Use the staging endpoint slot.
    :type staging: bool
    :param spell_check: Enable spell checking.
    :type spell_check: bool
    :param bing_spell_check_subscription_key: The subscription key to use when enabling bing spell check
    :type bing_spell_check_subscription_key: str
    :param log: Log query (default is true)
    :type log: bool

    """
    return web.Response(status=200)
