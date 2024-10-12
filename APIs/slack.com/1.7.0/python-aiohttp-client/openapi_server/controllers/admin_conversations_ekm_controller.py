from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def admin_conversations_ekm_list_original_connected_channel_info(request: web.Request, token, channel_ids=None, team_ids=None, limit=None, cursor=None) -> web.Response:
    """admin_conversations_ekm_list_original_connected_channel_info

    List all disconnected channels—i.e., channels that were once connected to other workspaces and then disconnected—and the corresponding original channel IDs for key revocation with EKM.

    :param token: Authentication token. Requires scope: &#x60;admin.conversations:read&#x60;
    :type token: str
    :param channel_ids: A comma-separated list of channels to filter to.
    :type channel_ids: str
    :param team_ids: A comma-separated list of the workspaces to which the channels you would like returned belong.
    :type team_ids: str
    :param limit: The maximum number of items to return. Must be between 1 - 1000 both inclusive.
    :type limit: int
    :param cursor: Set &#x60;cursor&#x60; to &#x60;next_cursor&#x60; returned by the previous call to list items in the next page.
    :type cursor: str

    """
    return web.Response(status=200)
