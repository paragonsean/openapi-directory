from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_dogma_attributes_attribute_id_not_found import GetDogmaAttributesAttributeIdNotFound
from openapi_server.models.get_dogma_attributes_attribute_id_ok import GetDogmaAttributesAttributeIdOk
from openapi_server.models.get_dogma_dynamic_items_type_id_item_id_not_found import GetDogmaDynamicItemsTypeIdItemIdNotFound
from openapi_server.models.get_dogma_dynamic_items_type_id_item_id_ok import GetDogmaDynamicItemsTypeIdItemIdOk
from openapi_server.models.get_dogma_effects_effect_id_not_found import GetDogmaEffectsEffectIdNotFound
from openapi_server.models.get_dogma_effects_effect_id_ok import GetDogmaEffectsEffectIdOk
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server import util


async def get_dogma_attributes(request: web.Request, datasource=None, if_none_match=None) -> web.Response:
    """Get attributes

    Get a list of dogma attribute ids  --- Alternate route: &#x60;/dev/dogma/attributes/&#x60;  Alternate route: &#x60;/legacy/dogma/attributes/&#x60;  Alternate route: &#x60;/v1/dogma/attributes/&#x60;  --- This route expires daily at 11:05

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_dogma_attributes_attribute_id(request: web.Request, attribute_id, datasource=None, if_none_match=None) -> web.Response:
    """Get attribute information

    Get information on a dogma attribute  --- Alternate route: &#x60;/dev/dogma/attributes/{attribute_id}/&#x60;  Alternate route: &#x60;/legacy/dogma/attributes/{attribute_id}/&#x60;  Alternate route: &#x60;/v1/dogma/attributes/{attribute_id}/&#x60;  --- This route expires daily at 11:05

    :param attribute_id: A dogma attribute ID
    :type attribute_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_dogma_dynamic_items_type_id_item_id(request: web.Request, item_id, type_id, datasource=None, if_none_match=None) -> web.Response:
    """Get dynamic item information

    Returns info about a dynamic item resulting from mutation with a mutaplasmid.  --- Alternate route: &#x60;/dev/dogma/dynamic/items/{type_id}/{item_id}/&#x60;  Alternate route: &#x60;/legacy/dogma/dynamic/items/{type_id}/{item_id}/&#x60;  Alternate route: &#x60;/v1/dogma/dynamic/items/{type_id}/{item_id}/&#x60;  --- This route expires daily at 11:05

    :param item_id: item_id integer
    :type item_id: int
    :param type_id: type_id integer
    :type type_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_dogma_effects(request: web.Request, datasource=None, if_none_match=None) -> web.Response:
    """Get effects

    Get a list of dogma effect ids  --- Alternate route: &#x60;/dev/dogma/effects/&#x60;  Alternate route: &#x60;/legacy/dogma/effects/&#x60;  Alternate route: &#x60;/v1/dogma/effects/&#x60;  --- This route expires daily at 11:05

    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_dogma_effects_effect_id(request: web.Request, effect_id, datasource=None, if_none_match=None) -> web.Response:
    """Get effect information

    Get information on a dogma effect  --- Alternate route: &#x60;/dev/dogma/effects/{effect_id}/&#x60;  Alternate route: &#x60;/v2/dogma/effects/{effect_id}/&#x60;  --- This route expires daily at 11:05

    :param effect_id: A dogma effect ID
    :type effect_id: int
    :param datasource: The server name you would like data from
    :type datasource: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)
