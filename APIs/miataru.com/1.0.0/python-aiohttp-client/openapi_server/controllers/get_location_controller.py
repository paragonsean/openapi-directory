from typing import List, Dict
from aiohttp import web

from openapi_server.models.miataru_get_location_geo_json_response import MiataruGetLocationGeoJSONResponse
from openapi_server.models.miataru_get_location_history_request import MiataruGetLocationHistoryRequest
from openapi_server.models.miataru_get_location_history_response import MiataruGetLocationHistoryResponse
from openapi_server.models.miataru_get_location_request import MiataruGetLocationRequest
from openapi_server.models.miataru_get_location_response import MiataruGetLocationResponse
from openapi_server import util


async def get_location(request: web.Request, body) -> web.Response:
    """get_location

    To retrieve a specific devices latest known location the /GetLocation method is used. Please note that the MiataruConfig portion is optional. RequestMiataruDeviceID should be the ID of the device the request is sent from (or an identifier like an URL).

    :param body: the complex JSON formatted datastructure to get the location of one or more devices.
    :type body: dict | bytes

    """
    body = MiataruGetLocationRequest.from_dict(body)
    return web.Response(status=200)


async def get_location_geo_json(request: web.Request, device_id) -> web.Response:
    """get_location_geo_json

    Retrieves a devices Location in GeoJSON format.

    :param device_id: the unique device ID of the device the location is requested from
    :type device_id: str

    """
    return web.Response(status=200)


async def get_location_history(request: web.Request, body) -> web.Response:
    """get_location_history

    Location History is stored on the server only if the client told the server to do so using the “EnableLocationHistory” setting in the Location Update requests. For transitions of enabling/disabling that functionality - Everytime a Location Update is received by the server with “EnableLocationHistory&#x3D;false” the server removes all stored Location History till that point. There is a server-side setting that controls up to how many Location Updates the server is storing in the Location History before it removes the oldest one. To request the Location History of a particular device the client sends the following POST request to the GetLocationHistory service URL. Please note that the MiataruConfig portion is optional. RequestMiataruDeviceID should be the ID of the device the request is sent from (or an identifier like an URL).

    :param body: the complex JSON formatted datastructure to get the location history of one device
    :type body: dict | bytes

    """
    body = MiataruGetLocationHistoryRequest.from_dict(body)
    return web.Response(status=200)
