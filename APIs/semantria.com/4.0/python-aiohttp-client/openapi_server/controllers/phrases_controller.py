from typing import List, Dict
from aiohttp import web

from openapi_server.models.phrase_response_version import PhraseResponseVersion
from openapi_server import util


async def add_phrases(request: web.Request, content_type, sentiment_phrases, config_id=None) -> web.Response:
    """Add sentiment-bearing phrases

    This method adds sentiment-bearing phrases on Semantria side.

    :param content_type: 
    :type content_type: str
    :param sentiment_phrases: List of parametrized JSON or XML objects.
    :type sentiment_phrases: 
    :param config_id: Identifier of configuration phrases linked to.
    :type config_id: str

    """
    return web.Response(status=200)


async def delete_phrases(request: web.Request, content_type, sentiment_phrase_ids, config_id=None) -> web.Response:
    """Remove sentiment-bearing phrases

    This method removes certain sentiment-bearing phrases by their names on Semantria side.

    :param content_type: 
    :type content_type: str
    :param sentiment_phrase_ids: List of sentiment-bearing phrase identifiers.
    :type sentiment_phrase_ids: List[str]
    :param config_id: Identifier of configuration phrases linked to.
    :type config_id: str

    """
    return web.Response(status=200)


async def get_phrases(request: web.Request, content_type, config_id=None) -> web.Response:
    """Retrieve sentiment-bearing phrases

    This method retrieves list of sentiment-bearing phrases available on Semantria side.

    :param content_type: 
    :type content_type: str
    :param config_id: Identifier of configuration phrases linked to.
    :type config_id: str

    """
    return web.Response(status=200)


async def update_phrases(request: web.Request, content_type, sentiment_phrases, config_id=None) -> web.Response:
    """Updates sentiment-bearing phrases

    This method updates sentiment-bearing phrases by unique IDs on Semantria side.

    :param content_type: 
    :type content_type: str
    :param sentiment_phrases: List of parametrized JSON or XML objects.
    :type sentiment_phrases: 
    :param config_id: Identifier of configuration phrases linked to.
    :type config_id: str

    """
    return web.Response(status=200)
