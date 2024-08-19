from typing import List, Dict
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_place import TflApiPresentationEntitiesPlace
from openapi_server import util


async def bike_point_get(request: web.Request, id) -> web.Response:
    """Gets the bike point with the given id.

    

    :param id: A bike point id (a list of ids can be obtained from the above BikePoint call)
    :type id: str

    """
    return web.Response(status=200)


async def bike_point_get_all(request: web.Request, ) -> web.Response:
    """Gets all bike point locations. The Place object has an addtionalProperties array which contains the nbBikes, nbDocks and nbSpaces              numbers which give the status of the BikePoint. A mismatch in these numbers i.e. nbDocks - (nbBikes + nbSpaces) !&#x3D; 0 indicates broken docks.

    


    """
    return web.Response(status=200)


async def bike_point_search(request: web.Request, query) -> web.Response:
    """Search for bike stations by their name, a bike point&#39;s name often contains information about the name of the street              or nearby landmarks, for example. Note that the search result does not contain the PlaceProperties i.e. the status              or occupancy of the BikePoint, to get that information you should retrieve the BikePoint by its id on /BikePoint/id.

    

    :param query: The search term e.g. \&quot;St. James\&quot;
    :type query: str

    """
    return web.Response(status=200)
