from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def features_feature_id_get(request: web.Request, feature_id) -> web.Response:
    """Get a feature by its featureId

    Get information about the geographical feature with the specified featureId.

    :param feature_id: The unique identifier for a feature
    :type feature_id: int

    """
    return web.Response(status=200)
