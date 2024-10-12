from typing import List, Dict
from aiohttp import web

from openapi_server.models.attribute_value import AttributeValue
from openapi_server.models.default_error import DefaultError
from openapi_server.models.error_entity import ErrorEntity
from openapi_server.models.error_sub_entity import ErrorSubEntity
from openapi_server.models.functionality import Functionality
from openapi_server.models.functionality_created import FunctionalityCreated
from openapi_server.models.functionality_item import FunctionalityItem
from openapi_server.models.functionality_new import FunctionalityNew
from openapi_server.models.functionality_patch import FunctionalityPatch
from openapi_server.models.metadata_patch import MetadataPatch
from openapi_server.models.tags_patch import TagsPatch
from openapi_server import util


async def device_add_functionality_0(request: web.Request, device_id, functionality_info) -> web.Response:
    """Add dynamically a functionality

    Add a *Functionality* to the device.  Required parameters are : - functionality class - endpoint  Each device class has its own restrictions on which Functionality classes can be added and on which endpoints. Only a few devices allow to add Functionalities.  |Device class|Functionality class|Endpoints| |------------|-------------------|---------| |MINT        |CurrentPeriod      |1,2,3    | |MINT        |ElectricityRates   |1,2,3    | |MINT        |GenericRate        |1,2,3    |  **Note**: requires full access to the *Account*. 

    :param device_id: Unique identifier of a *Device*.
    :type device_id: str
    :param functionality_info: 
    :type functionality_info: dict | bytes

    """
    functionality_info = FunctionalityNew.from_dict(functionality_info)
    return web.Response(status=200)


async def functionalities_get(request: web.Request, functionality_id) -> web.Response:
    """Information about a Functionality

    Get the *Functionality*.

    :param functionality_id: Unique identifier of a *Functionality*.
    :type functionality_id: str

    """
    return web.Response(status=200)


async def functionality_get_metadata(request: web.Request, functionality_id) -> web.Response:
    """List metadata

    Get the metadata.

    :param functionality_id: Unique identifier of a *Functionality*.
    :type functionality_id: str

    """
    return web.Response(status=200)


async def functionality_get_tags(request: web.Request, functionality_id) -> web.Response:
    """List tags

    Get the tags of a *Functionality*.

    :param functionality_id: Unique identifier of a *Functionality*.
    :type functionality_id: str

    """
    return web.Response(status=200)


async def functionality_patch(request: web.Request, functionality_id, functionality_patch) -> web.Response:
    """Modify a Functionality

    Modify information about a *Functionality*: its name. 

    :param functionality_id: Unique identifier of a *Functionality*.
    :type functionality_id: str
    :param functionality_patch: 
    :type functionality_patch: dict | bytes

    """
    functionality_patch = FunctionalityPatch.from_dict(functionality_patch)
    return web.Response(status=200)


async def functionality_patch_metadata(request: web.Request, functionality_id, metadata_patch) -> web.Response:
    """Modify metadata

    Modify the metadata. Keys are limited to the same format as tags (up to 21 characters, [a-z0-9], starting with [a-z]). Values can be any JSON value. 

    :param functionality_id: Unique identifier of a *Functionality*.
    :type functionality_id: str
    :param metadata_patch: Modifications to apply to the metadata of the resource. 
    :type metadata_patch: dict | bytes

    """
    metadata_patch = MetadataPatch.from_dict(metadata_patch)
    return web.Response(status=200)


async def functionality_patch_tags(request: web.Request, functionality_id, tags_patch) -> web.Response:
    """Modify tags

    Modify the tags of a *Functionality*.

    :param functionality_id: Unique identifier of a *Functionality*.
    :type functionality_id: str
    :param tags_patch: Modifications to apply to the tags list of the resource. 
    :type tags_patch: dict | bytes

    """
    tags_patch = TagsPatch.from_dict(tags_patch)
    return web.Response(status=200)


async def functionality_set(request: web.Request, functionality_id, attribute_name, value) -> web.Response:
    """Modify an Attribute value

    Modify the value of the *Attribute*.

    :param functionality_id: Unique identifier of a *Functionality*.
    :type functionality_id: str
    :param attribute_name: Identifier of an *Attribute* inside a *Functionality*.
    :type attribute_name: str
    :param value: New value for the *Attribute*.
    :type value: 

    """
    return web.Response(status=200)


async def functionality_value(request: web.Request, functionality_id, attribute_name) -> web.Response:
    """Get an Attribute value

    Get the *Attribute* value and the last time when it changed.

    :param functionality_id: Unique identifier of a *Functionality*.
    :type functionality_id: str
    :param attribute_name: Identifier of an *Attribute* inside a *Functionality*.
    :type attribute_name: str

    """
    return web.Response(status=200)


async def functionality_values(request: web.Request, functionality_id, names=None, _from=None, to=None, surround=None) -> web.Response:
    """Get history of multiple attributes

    Get the values of multiple *Attributes* and their history.  If the &#x60;names&#x60; parameter is not given, all the attributes of the *Functionality* are returned. As the list may be huge, this must be avoided.  If the &#x60;to&#x60; parameter is set, &#x60;from&#x60; must also be set.  If &#x60;from&#x60; is not set, only the last value is returned.  The &#x60;surround&#x60; parameter allows to ask also for one value beyond each interval boundaries.  The request may fail if too many values are asked. 

    :param functionality_id: Unique identifier of a *Functionality*.
    :type functionality_id: str
    :param names: One or multiple *Attribute* names separated by commas
    :type names: List[str]
    :param _from: Beginning of the time interval.
    :type _from: str
    :param to: End of the interval. Default: now. 
    :type to: str
    :param surround: If true, return also one value before from and one value after to
    :type surround: bool

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def place_functionalities(request: web.Request, place_id, devices=None, functionalities=None, embed_metadata=None) -> web.Response:
    """List Functionalities

    Get the list of *Functionalities* available in this *Place*.

    :param place_id: Unique identifier of a *Place*.
    :type place_id: str
    :param devices: Devices selector. Device tags or device classes or device ids or &#39;*&#39; for any. Multiple values are separated by &#39;|&#39; and interpreted as « OR ».
    :type devices: str
    :param functionalities: Functionality selector: Functionality tags or functionality class (optionally, &#39;@&#39; followed by a endpoint in decimal) or &#39;*&#39; for all. Multiple values are separated by &#39;|&#39; and are interpreted as « OR ». 
    :type functionalities: str
    :param embed_metadata: Request to include the given keys of metadata in the response. If a key doesn&#39;t exist on the resource it is ignored. **Note:** This only applies to the top level resources. 
    :type embed_metadata: List[str]

    """
    return web.Response(status=200)
