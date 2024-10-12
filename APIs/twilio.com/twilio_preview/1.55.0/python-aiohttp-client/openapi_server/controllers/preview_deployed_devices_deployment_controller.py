from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_deployed_devices_deployment_response import ListDeployedDevicesDeploymentResponse
from openapi_server.models.preview_deployed_devices_fleet_deployment import PreviewDeployedDevicesFleetDeployment
from openapi_server import util


async def create_deployed_devices_deployment(request: web.Request, fleet_sid, friendly_name=None, sync_service_sid=None) -> web.Response:
    """create_deployed_devices_deployment

    Create a new Deployment in the Fleet, optionally giving it a friendly name and linking to a specific Twilio Sync service instance.

    :param fleet_sid: 
    :type fleet_sid: str
    :param friendly_name: Provides a human readable descriptive text for this Deployment, up to 256 characters long.
    :type friendly_name: str
    :param sync_service_sid: Provides the unique string identifier of the Twilio Sync service instance that will be linked to and accessible by this Deployment.
    :type sync_service_sid: str

    """
    return web.Response(status=200)


async def delete_deployed_devices_deployment(request: web.Request, fleet_sid, sid) -> web.Response:
    """delete_deployed_devices_deployment

    Delete a specific Deployment from the Fleet, leaving associated devices effectively undeployed.

    :param fleet_sid: 
    :type fleet_sid: str
    :param sid: Provides a 34 character string that uniquely identifies the requested Deployment resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_deployed_devices_deployment(request: web.Request, fleet_sid, sid) -> web.Response:
    """fetch_deployed_devices_deployment

    Fetch information about a specific Deployment in the Fleet.

    :param fleet_sid: 
    :type fleet_sid: str
    :param sid: Provides a 34 character string that uniquely identifies the requested Deployment resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_deployed_devices_deployment(request: web.Request, fleet_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_deployed_devices_deployment

    Retrieve a list of all Deployments belonging to the Fleet.

    :param fleet_sid: 
    :type fleet_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_deployed_devices_deployment(request: web.Request, fleet_sid, sid, friendly_name=None, sync_service_sid=None) -> web.Response:
    """update_deployed_devices_deployment

    Update the given properties of a specific Deployment credential in the Fleet, giving it a friendly name or linking to a specific Twilio Sync service instance.

    :param fleet_sid: 
    :type fleet_sid: str
    :param sid: Provides a 34 character string that uniquely identifies the requested Deployment resource.
    :type sid: str
    :param friendly_name: Provides a human readable descriptive text for this Deployment, up to 64 characters long
    :type friendly_name: str
    :param sync_service_sid: Provides the unique string identifier of the Twilio Sync service instance that will be linked to and accessible by this Deployment.
    :type sync_service_sid: str

    """
    return web.Response(status=200)
