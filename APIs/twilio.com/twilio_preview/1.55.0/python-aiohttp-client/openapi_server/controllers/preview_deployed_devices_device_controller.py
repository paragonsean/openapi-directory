from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_deployed_devices_device_response import ListDeployedDevicesDeviceResponse
from openapi_server.models.preview_deployed_devices_fleet_device import PreviewDeployedDevicesFleetDevice
from openapi_server import util


async def create_deployed_devices_device(request: web.Request, fleet_sid, deployment_sid=None, enabled=None, friendly_name=None, identity=None, unique_name=None) -> web.Response:
    """create_deployed_devices_device

    Create a new Device in the Fleet, optionally giving it a unique name, friendly name, and assigning to a Deployment and/or human identity.

    :param fleet_sid: 
    :type fleet_sid: str
    :param deployment_sid: Specifies the unique string identifier of the Deployment group that this Device is going to be associated with.
    :type deployment_sid: str
    :param enabled: 
    :type enabled: bool
    :param friendly_name: Provides a human readable descriptive text to be assigned to this Device, up to 256 characters long.
    :type friendly_name: str
    :param identity: Provides an arbitrary string identifier representing a human user to be associated with this Device, up to 256 characters long.
    :type identity: str
    :param unique_name: Provides a unique and addressable name to be assigned to this Device, to be used in addition to SID, up to 128 characters long.
    :type unique_name: str

    """
    return web.Response(status=200)


async def delete_deployed_devices_device(request: web.Request, fleet_sid, sid) -> web.Response:
    """delete_deployed_devices_device

    Delete a specific Device from the Fleet, also removing it from associated Deployments.

    :param fleet_sid: 
    :type fleet_sid: str
    :param sid: Provides a 34 character string that uniquely identifies the requested Device resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_deployed_devices_device(request: web.Request, fleet_sid, sid) -> web.Response:
    """fetch_deployed_devices_device

    Fetch information about a specific Device in the Fleet.

    :param fleet_sid: 
    :type fleet_sid: str
    :param sid: Provides a 34 character string that uniquely identifies the requested Device resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_deployed_devices_device(request: web.Request, fleet_sid, deployment_sid=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_deployed_devices_device

    Retrieve a list of all Devices belonging to the Fleet.

    :param fleet_sid: 
    :type fleet_sid: str
    :param deployment_sid: Filters the resulting list of Devices by a unique string identifier of the Deployment they are associated with.
    :type deployment_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_deployed_devices_device(request: web.Request, fleet_sid, sid, deployment_sid=None, enabled=None, friendly_name=None, identity=None) -> web.Response:
    """update_deployed_devices_device

    Update the given properties of a specific Device in the Fleet, giving it a friendly name, assigning to a Deployment, or a human identity.

    :param fleet_sid: 
    :type fleet_sid: str
    :param sid: Provides a 34 character string that uniquely identifies the requested Device resource.
    :type sid: str
    :param deployment_sid: Specifies the unique string identifier of the Deployment group that this Device is going to be associated with.
    :type deployment_sid: str
    :param enabled: 
    :type enabled: bool
    :param friendly_name: Provides a human readable descriptive text to be assigned to this Device, up to 256 characters long.
    :type friendly_name: str
    :param identity: Provides an arbitrary string identifier representing a human user to be associated with this Device, up to 256 characters long.
    :type identity: str

    """
    return web.Response(status=200)
