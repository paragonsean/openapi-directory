from typing import List, Dict
from aiohttp import web

from openapi_server.models.collection_response_marketing_event_external_unique_identifier_no_paging import CollectionResponseMarketingEventExternalUniqueIdentifierNoPaging
from openapi_server.models.error import Error
from openapi_server import util


async def get_marketing_v3_marketing_events_events_search_do_search(request: web.Request, q) -> web.Response:
    """Search for marketing events

    Search for marketing events that have an event id that starts with the query string

    :param q: The id of the marketing event in the external event application
    :type q: str

    """
    return web.Response(status=200)
