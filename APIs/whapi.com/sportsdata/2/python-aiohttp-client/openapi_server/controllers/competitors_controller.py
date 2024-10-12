from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors_wrapper import ErrorsWrapper
from openapi_server.models.event_competitors_wrapper import EventCompetitorsWrapper
from openapi_server import util


async def get_event_competitors(request: web.Request, api_key, event_id, fields=None, include=None, exclude=None) -> web.Response:
    """Retrieves competitors for a single event by ID.

    Retrieves competitors for a single event by ID.

    :param api_key: Your API Key available from your developer portal
    :type api_key: str
    :param event_id: The event ID to retrieve information for.
    :type event_id: str
    :param fields: Specify an absolute field list to return (Comma-Separated List)
    :type fields: List[str]
    :param include: Specify fields in addition to the default to return (Comma-Separated List)
    :type include: List[str]
    :param exclude: Specify fields from the default to exclude (Comma-Separated List)
    :type exclude: List[str]

    """
    return web.Response(status=200)
