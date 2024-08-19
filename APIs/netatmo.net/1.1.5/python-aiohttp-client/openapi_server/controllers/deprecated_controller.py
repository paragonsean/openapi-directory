from typing import List, Dict
from aiohttp import web

from openapi_server.models.na_device_list_response import NADeviceListResponse
from openapi_server.models.na_therm_state_response import NAThermStateResponse
from openapi_server.models.na_user_response import NAUserResponse
from openapi_server import util


async def devicelist(request: web.Request, app_type=None, device_id=None, get_favorites=None) -> web.Response:
    """devicelist

    The method devicelist returns the list of devices owned by the user, and their modules. A device is identified by its _id (which is its mac address) and each device may have one, several or no modules, also identified by an _id. 

    :param app_type: Defines which device type will be returned by devicelist. It could be app_thermostat or app_station (by default if not provided)
    :type app_type: str
    :param device_id: Specify a device_id if you want to retrieve only this device informations.
    :type device_id: str
    :param get_favorites: When set to \&quot;true\&quot;, the favorite devices of the user are returned. This flag is available only if the devices requested are Weather Stations.
    :type get_favorites: bool

    """
    return web.Response(status=200)


async def getthermstate(request: web.Request, device_id, module_id) -> web.Response:
    """getthermstate

    The method getthermstate returns the last Thermostat measurements, its current weekly schedule, and, if present, its current manual temperature setpoint.

    :param device_id: The relay id
    :type device_id: str
    :param module_id: The thermostat id
    :type module_id: str

    """
    return web.Response(status=200)


async def getuser(request: web.Request, ) -> web.Response:
    """getuser

    The method getuser returns information about a user such as prefered language, prefered units, and list of devices. 


    """
    return web.Response(status=200)
