from typing import List, Dict
from aiohttp import web

from openapi_server.models.endpoint_get_autocompletes import EndpointGetAutocompletes
from openapi_server import util


async def autocompletes_get(request: web.Request, query=None) -> web.Response:
    """autocompletes_get

    Retrieve an array of names and locations, filtered by category, that begin with the query string passed in. Ideally used for search autocomplete dropdowns, as the search functionality filters against name and location. The four potential categories are: &#x60;conversations&#x60; for names of users you are in existing conversations with; &#x60;matches&#x60; for names of users you have previously skipped over; &#x60;people&#x60; for names of all other users; &#x60;locations&#x60; for locations of users. Only users and their locations who exist with the current access token&#39;s bubble are considered.

    :param query: 
    :type query: str

    """
    return web.Response(status=200)
