from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error import DefaultError
from openapi_server.models.device import Device
from openapi_server.models.device_item import DeviceItem
from openapi_server.models.device_patch import DevicePatch
from openapi_server.models.error_entity import ErrorEntity
from openapi_server.models.functionality_created import FunctionalityCreated
from openapi_server.models.functionality_new import FunctionalityNew
from openapi_server.models.metadata_patch import MetadataPatch
from openapi_server.models.tags_patch import TagsPatch
from openapi_server import util


async def device_add_functionality(request: web.Request, device_id, functionality_info) -> web.Response:
    """Add dynamically a functionality

    Add a *Functionality* to the device.  Required parameters are : - functionality class - endpoint  Each device class has its own restrictions on which Functionality classes can be added and on which endpoints. Only a few devices allow to add Functionalities.  |Device class|Functionality class|Endpoints| |------------|-------------------|---------| |MINT        |CurrentPeriod      |1,2,3    | |MINT        |ElectricityRates   |1,2,3    | |MINT        |GenericRate        |1,2,3    |  **Note**: requires full access to the *Account*. 

    :param device_id: Unique identifier of a *Device*.
    :type device_id: str
    :param functionality_info: 
    :type functionality_info: dict | bytes

    """
    functionality_info = FunctionalityNew.from_dict(functionality_info)
    return web.Response(status=200)


async def device_get_metadata(request: web.Request, device_id) -> web.Response:
    """List metadata

    Get the metadata.

    :param device_id: Unique identifier of a *Device*.
    :type device_id: str

    """
    return web.Response(status=200)


async def device_get_tags(request: web.Request, device_id) -> web.Response:
    """List tags

    Get the tags of a *Device*.

    :param device_id: Unique identifier of a *Device*.
    :type device_id: str

    """
    return web.Response(status=200)


async def device_patch_metadata(request: web.Request, device_id, metadata_patch) -> web.Response:
    """Modify metadata

    Modify the metadata. Keys are limited to the same format as tags (up to 21 characters, [a-z0-9], starting with [a-z]). Values can be any JSON value. 

    :param device_id: Unique identifier of a *Device*.
    :type device_id: str
    :param metadata_patch: Modifications to apply to the metadata of the resource. 
    :type metadata_patch: dict | bytes

    """
    metadata_patch = MetadataPatch.from_dict(metadata_patch)
    return web.Response(status=200)


async def device_patch_tags(request: web.Request, device_id, tags_patch) -> web.Response:
    """Modify tags

    Modify the tags of a *Device*.

    :param device_id: Unique identifier of a *Device*.
    :type device_id: str
    :param tags_patch: Modifications to apply to the tags list of the resource. 
    :type tags_patch: dict | bytes

    """
    tags_patch = TagsPatch.from_dict(tags_patch)
    return web.Response(status=200)


async def devices_get(request: web.Request, device_id) -> web.Response:
    """Information about a Device

    Get information about a *Device*.

    :param device_id: Unique identifier of a *Device*.
    :type device_id: str

    """
    return web.Response(status=200)


async def devices_patch(request: web.Request, device_id, device_patch) -> web.Response:
    """Update a Device

    Modify information about a *Device*: its name. 

    :param device_id: Unique identifier of a *Device*.
    :type device_id: str
    :param device_patch: 
    :type device_patch: dict | bytes

    """
    device_patch = DevicePatch.from_dict(device_patch)
    return web.Response(status=200)


async def place_devices(request: web.Request, place_id, devices=None, embed_metadata=None) -> web.Response:
    """List of Devices

    Get the list of *Devices* available in this *Place*.

    :param place_id: Unique identifier of a *Place*.
    :type place_id: str
    :param devices: Devices selector. Device tags or device classes or device ids or &#39;*&#39; for any. Multiple values are separated by &#39;|&#39; and interpreted as « OR ».
    :type devices: str
    :param embed_metadata: Request to include the given keys of metadata in the response. If a key doesn&#39;t exist on the resource it is ignored. **Note:** This only applies to the top level resources. 
    :type embed_metadata: List[str]

    """
    return web.Response(status=200)
