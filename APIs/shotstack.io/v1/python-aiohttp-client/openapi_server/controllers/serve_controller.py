from typing import List, Dict
from aiohttp import web

from openapi_server.models.asset_render_response import AssetRenderResponse
from openapi_server.models.asset_response import AssetResponse
from openapi_server import util


async def delete_asset(request: web.Request, id) -> web.Response:
    """Delete Asset

    Delete an asset by its asset id. If a render creates multiple assets, such as thumbnail and poster images, each asset must be deleted individually by the asset id.  **base URL:** https://api.shotstack.io/serve/{version}

    :param id: The id of the asset in UUID format
    :type id: str

    """
    return web.Response(status=200)


async def get_asset(request: web.Request, id) -> web.Response:
    """Get Asset

    The Serve API is used to interact with, and delete hosted assets including videos, images, audio files,  thumbnails and poster images. Use this endpoint to fetch an asset by asset id. Note that an asset id is unique for each asset and different from the render id.  **base URL:** https://api.shotstack.io/serve/{version}

    :param id: The id of the asset in UUID format
    :type id: str

    """
    return web.Response(status=200)


async def get_asset_by_render_id(request: web.Request, id) -> web.Response:
    """Get Asset by Render ID

    A render may generate more than one file, such as a video, thumbnail and poster image. When the assets are created the only known id is the render id returned by the original [render request](#render-video), status  request or webhook. This endpoint lets you look up one or more assets by the render id.  **base URL:** https://api.shotstack.io/serve/{version}

    :param id: The render id associated with the asset in UUID format
    :type id: str

    """
    return web.Response(status=200)
