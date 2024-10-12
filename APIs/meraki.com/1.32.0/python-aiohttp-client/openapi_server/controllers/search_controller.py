from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_organization_clients_search_2(request: web.Request, organization_id, mac, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return the client details in an organization

    Return the client details in an organization

    :param organization_id: 
    :type organization_id: str
    :param mac: The MAC address of the client. Required.
    :type mac: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 5. Default is 5.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)
