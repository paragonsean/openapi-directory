from typing import List, Dict
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_active_service_type import TflApiPresentationEntitiesActiveServiceType
from openapi_server.models.tfl_api_presentation_entities_prediction import TflApiPresentationEntitiesPrediction
from openapi_server import util


async def mode_arrivals(request: web.Request, mode, count=None) -> web.Response:
    """Gets the next arrival predictions for all stops of a given mode

    

    :param mode: A mode name e.g. tube, dlr
    :type mode: str
    :param count: A number of arrivals to return for each stop, -1 to return all available.
    :type count: int

    """
    return web.Response(status=200)


async def mode_get_active_service_types(request: web.Request, ) -> web.Response:
    """Returns the service type active for a mode.              Currently only supports tube

    


    """
    return web.Response(status=200)
