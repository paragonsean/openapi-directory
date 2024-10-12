from typing import List, Dict
from aiohttp import web

from openapi_server.models.images_get200_response import ImagesGet200Response
from openapi_server.models.images_id_get200_response import ImagesIdGet200Response
from openapi_server.models.update_image_request import UpdateImageRequest
from openapi_server import util


async def images_get(request: web.Request, sort=None, type=None, status=None, bound_to=None, include_deprecated=None, name=None, label_selector=None, architecture=None) -> web.Response:
    """Get all Images

    Returns all Image objects. You can select specific Image types only and sort the results by using URI parameters.

    :param sort: Can be used multiple times.
    :type sort: str
    :param type: Can be used multiple times.
    :type type: str
    :param status: Can be used multiple times. The response will only contain Images matching the status.
    :type status: str
    :param bound_to: Can be used multiple times. Server ID linked to the Image. Only available for Images of type &#x60;backup&#x60;
    :type bound_to: str
    :param include_deprecated: Can be used multiple times.
    :type include_deprecated: bool
    :param name: Can be used to filter resources by their name. The response will only contain the resources matching the specified name
    :type name: str
    :param label_selector: Can be used to filter resources by labels. The response will only contain resources matching the label selector.
    :type label_selector: str
    :param architecture: Return only Images with the given architecture.
    :type architecture: str

    """
    return web.Response(status=200)


async def images_id_delete(request: web.Request, id) -> web.Response:
    """Delete an Image

    Deletes an Image. Only Images of type &#x60;snapshot&#x60; and &#x60;backup&#x60; can be deleted.

    :param id: ID of the Image
    :type id: int

    """
    return web.Response(status=200)


async def images_id_get(request: web.Request, id) -> web.Response:
    """Get an Image

    Returns a specific Image object.

    :param id: ID of the Image
    :type id: int

    """
    return web.Response(status=200)


async def images_id_put(request: web.Request, id, body=None) -> web.Response:
    """Update an Image

    Updates the Image. You may change the description, convert a Backup Image to a Snapshot Image or change the Image labels. Only Images of type &#x60;snapshot&#x60; and &#x60;backup&#x60; can be updated.  Note that when updating labels, the current set of labels will be replaced with the labels provided in the request body. So, for example, if you want to add a new label, you have to provide all existing labels plus the new label in the request body. 

    :param id: ID of the Image
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateImageRequest.from_dict(body)
    return web.Response(status=200)
