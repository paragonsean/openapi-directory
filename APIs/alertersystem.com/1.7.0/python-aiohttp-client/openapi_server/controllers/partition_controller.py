from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_partition_get_collection200_response import ApiPartitionGetCollection200Response
from openapi_server.models.partition_get import PartitionGet
from openapi_server.models.partition_jsonld_get import PartitionJsonldGet
from openapi_server.models.partition_jsonld_post import PartitionJsonldPost
from openapi_server.models.partition_jsonld_put import PartitionJsonldPut
from openapi_server.models.partition_patch import PartitionPatch
from openapi_server.models.partition_post import PartitionPost
from openapi_server.models.partition_put import PartitionPut
from openapi_server import util


async def api_partition_get_collection(request: web.Request, page=None, data_segment_code=None, data_segment_code2=None, properties=None) -> web.Response:
    """Retrieves the collection of Partition resources.

    Retrieves the collection of Partition resources.

    :param page: The collection page number
    :type page: int
    :param data_segment_code: 
    :type data_segment_code: str
    :param data_segment_code2: 
    :type data_segment_code2: List[str]
    :param properties: Allows you to reduce the response to contain only the properties you need. If your desired property is nested, you can address it using nested arrays. Example: properties[]&#x3D;{propertyName}&amp;properties[]&#x3D;{anotherPropertyName}&amp;properties[{nestedPropertyParent}][]&#x3D;{nestedProperty}
    :type properties: List[str]

    """
    return web.Response(status=200)


async def api_partition_id_delete(request: web.Request, id) -> web.Response:
    """Removes the Partition resource.

    Removes the Partition resource.

    :param id: Partition identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_partition_id_get(request: web.Request, id) -> web.Response:
    """Retrieves a Partition resource.

    Retrieves a Partition resource.

    :param id: Partition identifier
    :type id: str

    """
    return web.Response(status=200)


async def api_partition_id_patch(request: web.Request, id, body) -> web.Response:
    """Updates the Partition resource.

    Updates the Partition resource.

    :param id: Partition identifier
    :type id: str
    :param body: The updated Partition resource
    :type body: dict | bytes

    """
    body = PartitionPatch.from_dict(body)
    return web.Response(status=200)


async def api_partition_id_put(request: web.Request, id, body) -> web.Response:
    """Replaces the Partition resource.

    Replaces the Partition resource.

    :param id: Partition identifier
    :type id: str
    :param body: The updated Partition resource
    :type body: dict | bytes

    """
    body = PartitionPut.from_dict(body)
    return web.Response(status=200)


async def api_partition_post(request: web.Request, body) -> web.Response:
    """Creates a Partition resource.

    Creates a Partition resource.

    :param body: The new Partition resource
    :type body: dict | bytes

    """
    body = PartitionPost.from_dict(body)
    return web.Response(status=200)
