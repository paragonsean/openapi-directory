from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_deployed_devices_certificate_response import ListDeployedDevicesCertificateResponse
from openapi_server.models.preview_deployed_devices_fleet_certificate import PreviewDeployedDevicesFleetCertificate
from openapi_server import util


async def create_deployed_devices_certificate(request: web.Request, fleet_sid, certificate_data, device_sid=None, friendly_name=None) -> web.Response:
    """create_deployed_devices_certificate

    Enroll a new Certificate credential to the Fleet, optionally giving it a friendly name and assigning to a Device.

    :param fleet_sid: 
    :type fleet_sid: str
    :param certificate_data: Provides a URL encoded representation of the public certificate in PEM format.
    :type certificate_data: str
    :param device_sid: Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential.
    :type device_sid: str
    :param friendly_name: Provides a human readable descriptive text for this Certificate credential, up to 256 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)


async def delete_deployed_devices_certificate(request: web.Request, fleet_sid, sid) -> web.Response:
    """delete_deployed_devices_certificate

    Unregister a specific Certificate credential from the Fleet, effectively disallowing any inbound client connections that are presenting it.

    :param fleet_sid: 
    :type fleet_sid: str
    :param sid: Provides a 34 character string that uniquely identifies the requested Certificate credential resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_deployed_devices_certificate(request: web.Request, fleet_sid, sid) -> web.Response:
    """fetch_deployed_devices_certificate

    Fetch information about a specific Certificate credential in the Fleet.

    :param fleet_sid: 
    :type fleet_sid: str
    :param sid: Provides a 34 character string that uniquely identifies the requested Certificate credential resource.
    :type sid: str

    """
    return web.Response(status=200)


async def list_deployed_devices_certificate(request: web.Request, fleet_sid, device_sid=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_deployed_devices_certificate

    Retrieve a list of all Certificate credentials belonging to the Fleet.

    :param fleet_sid: 
    :type fleet_sid: str
    :param device_sid: Filters the resulting list of Certificates by a unique string identifier of an authenticated Device.
    :type device_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_deployed_devices_certificate(request: web.Request, fleet_sid, sid, device_sid=None, friendly_name=None) -> web.Response:
    """update_deployed_devices_certificate

    Update the given properties of a specific Certificate credential in the Fleet, giving it a friendly name or assigning to a Device.

    :param fleet_sid: 
    :type fleet_sid: str
    :param sid: Provides a 34 character string that uniquely identifies the requested Certificate credential resource.
    :type sid: str
    :param device_sid: Provides the unique string identifier of an existing Device to become authenticated with this Certificate credential.
    :type device_sid: str
    :param friendly_name: Provides a human readable descriptive text for this Certificate credential, up to 256 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)
