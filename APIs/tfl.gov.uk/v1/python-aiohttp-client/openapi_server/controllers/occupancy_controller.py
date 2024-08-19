from typing import List, Dict
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_bike_point_occupancy import TflApiPresentationEntitiesBikePointOccupancy
from openapi_server.models.tfl_api_presentation_entities_car_park_occupancy import TflApiPresentationEntitiesCarParkOccupancy
from openapi_server.models.tfl_api_presentation_entities_charge_connector_occupancy import TflApiPresentationEntitiesChargeConnectorOccupancy
from openapi_server import util


async def occupancy_car_park_get(request: web.Request, ) -> web.Response:
    """Gets the occupancy for all car parks that have occupancy data

    


    """
    return web.Response(status=200)


async def occupancy_get(request: web.Request, id) -> web.Response:
    """Gets the occupancy for a car park with a given id

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def occupancy_get_all_charge_connector_status(request: web.Request, ) -> web.Response:
    """Gets the occupancy for all charge connectors

    


    """
    return web.Response(status=200)


async def occupancy_get_bike_points_occupancies(request: web.Request, ids) -> web.Response:
    """Get the occupancy for bike points.

    

    :param ids: 
    :type ids: List[str]

    """
    return web.Response(status=200)


async def occupancy_get_charge_connector_status(request: web.Request, ids) -> web.Response:
    """Gets the occupancy for a charge connectors with a given id (sourceSystemPlaceId)

    

    :param ids: 
    :type ids: List[str]

    """
    return web.Response(status=200)
