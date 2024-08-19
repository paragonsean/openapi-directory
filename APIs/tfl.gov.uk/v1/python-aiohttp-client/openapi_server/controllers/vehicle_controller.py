from typing import List, Dict
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_prediction import TflApiPresentationEntitiesPrediction
from openapi_server import util


async def vehicle_get(request: web.Request, ids) -> web.Response:
    """Gets the predictions for a given list of vehicle Id&#39;s.

    

    :param ids: A comma-separated list of vehicle ids e.g. LX58CFV,LX11AZB,LX58CFE. Max approx. 25 ids.
    :type ids: List[str]

    """
    return web.Response(status=200)
