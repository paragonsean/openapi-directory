from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_volume_request import CreateVolumeRequest
from openapi_server.models.update_volume_request import UpdateVolumeRequest
from openapi_server.models.volumes_get200_response import VolumesGet200Response
from openapi_server.models.volumes_id_get200_response import VolumesIdGet200Response
from openapi_server.models.volumes_post201_response import VolumesPost201Response
from openapi_server import util


async def volumes_get(request: web.Request, status=None, sort=None, name=None, label_selector=None) -> web.Response:
    """Get all Volumes

    Gets all existing Volumes that you have available.

    :param status: Can be used multiple times. The response will only contain Volumes matching the status.
    :type status: str
    :param sort: Can be used multiple times.
    :type sort: str
    :param name: Can be used to filter resources by their name. The response will only contain the resources matching the specified name
    :type name: str
    :param label_selector: Can be used to filter resources by labels. The response will only contain resources matching the label selector.
    :type label_selector: str

    """
    return web.Response(status=200)


async def volumes_id_delete(request: web.Request, id) -> web.Response:
    """Delete a Volume

    Deletes a volume. All Volume data is irreversibly destroyed. The Volume must not be attached to a Server and it must not have delete protection enabled.

    :param id: ID of the Volume
    :type id: str

    """
    return web.Response(status=200)


async def volumes_id_get(request: web.Request, id) -> web.Response:
    """Get a Volume

    Gets a specific Volume object.

    :param id: ID of the Volume
    :type id: int

    """
    return web.Response(status=200)


async def volumes_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update a Volume

    Updates the Volume properties.  Note that when updating labels, the volume’s current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body. 

    :param id: ID of the Volume to update
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateVolumeRequest.from_dict(body)
    return web.Response(status=200)


async def volumes_post(request: web.Request, body=None) -> web.Response:
    """Create a Volume

    Creates a new Volume attached to a Server. If you want to create a Volume that is not attached to a Server, you need to provide the &#x60;location&#x60; key instead of &#x60;server&#x60;. This can be either the ID or the name of the Location this Volume will be created in. Note that a Volume can be attached to a Server only in the same Location as the Volume itself.  Specifying the Server during Volume creation will automatically attach the Volume to that Server after it has been initialized. In that case, the &#x60;next_actions&#x60; key in the response is an array which contains a single &#x60;attach_volume&#x60; action.  The minimum Volume size is 10GB and the maximum size is 10TB (10240GB).  A volume’s name can consist of alphanumeric characters, dashes, underscores, and dots, but has to start and end with an alphanumeric character. The total length is limited to 64 characters. Volume names must be unique per Project.  #### Call specific error codes  | Code                                | Description                                         | |-------------------------------------|-----------------------------------------------------| | &#x60;no_space_left_in_location&#x60;         | There is no volume space left in the given location | 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateVolumeRequest.from_dict(body)
    return web.Response(status=200)
