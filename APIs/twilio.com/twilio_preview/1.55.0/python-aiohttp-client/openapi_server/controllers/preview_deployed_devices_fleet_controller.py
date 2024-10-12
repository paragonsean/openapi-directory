from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_deployed_devices_fleet_response import ListDeployedDevicesFleetResponse
from openapi_server.models.preview_deployed_devices_fleet import PreviewDeployedDevicesFleet
from openapi_server import util


async def create_deployed_devices_fleet(request: web.Request, friendly_name=None) -> web.Response:
    """create_deployed_devices_fleet

    Create a new Fleet for scoping of deployed devices within your account.

    :param friendly_name: Provides a human readable descriptive text for this Fleet, up to 256 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)


async def delete_deployed_devices_fleet(request: web.Request, sid) -> web.Response:
    """delete_deployed_devices_fleet

    Delete a specific Fleet from your account, also destroys all nested resources: Devices, Deployments, Certificates, Keys.

    :param sid: Provides a 34 character string that uniquely identifies the requested Fleet resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_deployed_devices_fleet(request: web.Request, sid) -> web.Response:
    """fetch_deployed_devices_fleet

    Fetch information about a specific Fleet in your account.

    :param sid: Provides a 34 character string that uniquely identifies the requested Fleet resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_deployed_devices_fleet(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_deployed_devices_fleet

    Retrieve a list of all Fleets belonging to your account.

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_deployed_devices_fleet(request: web.Request, sid, default_deployment_sid=None, friendly_name=None) -> web.Response:
    """update_deployed_devices_fleet

    Update the friendly name property of a specific Fleet in your account.

    :param sid: Provides a 34 character string that uniquely identifies the requested Fleet resource.
    :type sid: str
    :param default_deployment_sid: Provides a string identifier of a Deployment that is going to be used as a default one for this Fleet.
    :type default_deployment_sid: str
    :param friendly_name: Provides a human readable descriptive text for this Fleet, up to 256 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)
