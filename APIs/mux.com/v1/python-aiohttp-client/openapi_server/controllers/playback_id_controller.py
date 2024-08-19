from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_asset_or_live_stream_id_response import GetAssetOrLiveStreamIdResponse
from openapi_server import util


async def get_asset_or_livestream_id(request: web.Request, playback_id) -> web.Response:
    """Retrieve an Asset or Live Stream ID

    Retrieves the Identifier of the Asset or Live Stream associated with the Playback ID.

    :param playback_id: The live stream&#39;s playback ID.
    :type playback_id: str

    """
    return web.Response(status=200)
