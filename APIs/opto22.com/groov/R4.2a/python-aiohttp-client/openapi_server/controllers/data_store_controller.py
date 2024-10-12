from typing import List, Dict
from aiohttp import web

from openapi_server.models.data_store_device import DataStoreDevice
from openapi_server.models.tag_definition import TagDefinition
from openapi_server.models.tag_reference import TagReference
from openapi_server.models.tag_value import TagValue
from openapi_server import util


async def batch_read_tags(request: web.Request, tags) -> web.Response:
    """batch_read_tags

    Read selected tags from the data store. Authorized for admins and editors.

    :param tags: Tag references for the tags to read.
    :type tags: list | bytes

    """
    tags = [TagReference.from_dict(d) for d in tags]
    return web.Response(status=200)


async def list_all_tags(request: web.Request, ) -> web.Response:
    """list_all_tags

    List all data store tags defined in the project. Authorized for admins and editors.


    """
    return web.Response(status=200)


async def list_device_tags(request: web.Request, id) -> web.Response:
    """list_device_tags

    List tags of the given device. Authorized for admins and editors.

    :param id: ID of the device to use.
    :type id: 

    """
    return web.Response(status=200)


async def list_devices(request: web.Request, ) -> web.Response:
    """list_devices

    List devices available in the data store. Authorized for admins and editors.


    """
    return web.Response(status=200)


async def read_tag(request: web.Request, id, index=None, count=None) -> web.Response:
    """read_tag

    Read the current value of a single tag. Authorized for admins and editors.

    :param id: ID of the tag to read.
    :type id: 
    :param index: Table index to start reading at.
    :type index: 
    :param count: Number of elements to read from a table.
    :type count: 

    """
    return web.Response(status=200)


async def write_tag(request: web.Request, id, value, index=None) -> web.Response:
    """write_tag

    Writes a new value to the given tag. Authorized for admins and editors.

    :param id: ID of the tag to write.
    :type id: 
    :param value: Value to write to the tag. Must be a string, number, or boolean.
    :type value: str
    :param index: For array tags, the index to write the value to.
    :type index: 

    """
    return web.Response(status=200)
