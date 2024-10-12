from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_result import ActionResult
from openapi_server.models.default_error import DefaultError
from openapi_server.models.error_gateway_unreachable import ErrorGatewayUnreachable
from openapi_server import util


async def device_run(request: web.Request, device_id, action, functionalities, arguments) -> web.Response:
    """Run actions

    Run an *Action* on zero, one or multiple Functionalities selected with tags. 

    :param device_id: Unique identifier of a *Device*.
    :type device_id: str
    :param action: Identifier of an *Action* inside a *Functionality*.
    :type action: str
    :param functionalities: Functionality selector: Functionality tags or functionality class (optionally, &#39;@&#39; followed by a endpoint in decimal) or &#39;*&#39; for all. Multiple values are separated by &#39;|&#39; and are interpreted as « OR ». 
    :type functionalities: str
    :param arguments: 
    :type arguments: List[]

    """
    return web.Response(status=200)


async def functionality_run(request: web.Request, functionality_id, action, arguments) -> web.Response:
    """Run an action

    Run an action on the Functionality. 

    :param functionality_id: Unique identifier of a *Functionality*.
    :type functionality_id: str
    :param action: Identifier of an *Action* inside a *Functionality*.
    :type action: str
    :param arguments: 
    :type arguments: List[]

    """
    return web.Response(status=200)


async def place_run(request: web.Request, place_id, action, devices, functionalities, arguments) -> web.Response:
    """Run actions

    Run an *Action* on zero, one or multiple *Functionalities* selected with tags.  *Device* and *Functionality* selection are combined with « AND ».  If no functionality is matched by the device/functionality selection, an empty array is returned. 

    :param place_id: Unique identifier of a *Place*.
    :type place_id: str
    :param action: Identifier of an *Action* inside a *Functionality*.
    :type action: str
    :param devices: Devices selector. Device tags or device classes or device ids or &#39;*&#39; for any. Multiple values are separated by &#39;|&#39; and interpreted as « OR ».
    :type devices: str
    :param functionalities: Functionality selector: Functionality tags or functionality class (optionally, &#39;@&#39; followed by a endpoint in decimal) or &#39;*&#39; for all. Multiple values are separated by &#39;|&#39; and are interpreted as « OR ». 
    :type functionalities: str
    :param arguments: 
    :type arguments: List[]

    """
    return web.Response(status=200)
