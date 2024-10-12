from typing import List, Dict
from aiohttp import web

from openapi_server.models.attribute_add200_response import AttributeAdd200Response
from openapi_server.models.attribute_assign_group200_response import AttributeAssignGroup200Response
from openapi_server.models.attribute_attributeset_list200_response import AttributeAttributesetList200Response
from openapi_server.models.attribute_count200_response import AttributeCount200Response
from openapi_server.models.attribute_delete200_response import AttributeDelete200Response
from openapi_server.models.attribute_info200_response import AttributeInfo200Response
from openapi_server.models.attribute_type_list200_response import AttributeTypeList200Response
from openapi_server.models.attribute_unassign_group200_response import AttributeUnassignGroup200Response
from openapi_server.models.attribute_update200_response import AttributeUpdate200Response
from openapi_server.models.model_response_attribute_list import ModelResponseAttributeList
from openapi_server import util


async def attribute_add(request: web.Request, type, name, code=None, store_id=None, lang_id=None, visible=None, required=None, position=None, attribute_group_id=None, is_global=None, is_searchable=None, is_filterable=None, is_comparable=None, is_html_allowed_on_front=None, is_filterable_in_search=None, is_configurable=None, is_visible_in_advanced_search=None, is_used_for_promo_rules=None, used_in_product_listing=None, used_for_sort_by=None, apply_to=None) -> web.Response:
    """attribute_add

    Add new attribute

    :param type: Defines attribute&#39;s type
    :type type: str
    :param name: Defines attributes&#39;s name
    :type name: str
    :param code: Entity code
    :type code: str
    :param store_id: Store Id
    :type store_id: str
    :param lang_id: Language id
    :type lang_id: str
    :param visible: Set visibility status
    :type visible: bool
    :param required: Defines if the option is required
    :type required: bool
    :param position: Attribute&#x60;s position
    :type position: int
    :param attribute_group_id: Filter by attribute_group_id
    :type attribute_group_id: str
    :param is_global: Attribute saving scope
    :type is_global: str
    :param is_searchable: Use attribute in Quick Search
    :type is_searchable: bool
    :param is_filterable: Use In Layered Navigation
    :type is_filterable: str
    :param is_comparable: Comparable on Front-end
    :type is_comparable: bool
    :param is_html_allowed_on_front: Allow HTML Tags on Frontend
    :type is_html_allowed_on_front: bool
    :param is_filterable_in_search: Use In Search Results Layered Navigation
    :type is_filterable_in_search: bool
    :param is_configurable: Use To Create Configurable Product
    :type is_configurable: bool
    :param is_visible_in_advanced_search: Use in Advanced Search
    :type is_visible_in_advanced_search: bool
    :param is_used_for_promo_rules: Use for Promo Rule Conditions
    :type is_used_for_promo_rules: bool
    :param used_in_product_listing: Used in Product Listing
    :type used_in_product_listing: bool
    :param used_for_sort_by: Used for Sorting in Product Listing
    :type used_for_sort_by: bool
    :param apply_to: Types of products which can have this attribute
    :type apply_to: str

    """
    return web.Response(status=200)


async def attribute_assign_group(request: web.Request, id, group_id, attribute_set_id=None) -> web.Response:
    """attribute_assign_group

    Assign attribute to the group

    :param id: Entity id
    :type id: str
    :param group_id: Attribute group_id
    :type group_id: str
    :param attribute_set_id: Attribute set id
    :type attribute_set_id: str

    """
    return web.Response(status=200)


async def attribute_assign_set(request: web.Request, id, attribute_set_id, group_id=None) -> web.Response:
    """attribute_assign_set

    Assign attribute to the attribute set

    :param id: Entity id
    :type id: str
    :param attribute_set_id: Attribute set id
    :type attribute_set_id: str
    :param group_id: Attribute group_id
    :type group_id: str

    """
    return web.Response(status=200)


async def attribute_attributeset_list(request: web.Request, start=None, count=None, params=None, exclude=None, response_fields=None) -> web.Response:
    """attribute_attributeset_list

    Get attribute_set list

    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str

    """
    return web.Response(status=200)


async def attribute_count(request: web.Request, type=None, store_id=None, lang_id=None, visible=None, required=None, system=None) -> web.Response:
    """attribute_count

    Get attributes count

    :param type: Defines attribute&#39;s type
    :type type: str
    :param store_id: Store Id
    :type store_id: str
    :param lang_id: Language id
    :type lang_id: str
    :param visible: Filter items by visibility status
    :type visible: bool
    :param required: Defines if the option is required
    :type required: bool
    :param system: True if attribute is system
    :type system: bool

    """
    return web.Response(status=200)


async def attribute_delete(request: web.Request, id, store_id=None) -> web.Response:
    """attribute_delete

    Delete attribute from store

    :param id: Entity id
    :type id: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def attribute_group_list(request: web.Request, start=None, count=None, lang_id=None, params=None, exclude=None, response_fields=None, attribute_set_id=None) -> web.Response:
    """attribute_group_list

    Get attribute group list

    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param lang_id: Language id
    :type lang_id: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param attribute_set_id: Attribute set id
    :type attribute_set_id: str

    """
    return web.Response(status=200)


async def attribute_info(request: web.Request, id, store_id=None, lang_id=None, params=None, exclude=None, response_fields=None) -> web.Response:
    """attribute_info

    Get attribute info

    :param id: Entity id
    :type id: str
    :param store_id: Store Id
    :type store_id: str
    :param lang_id: Language id
    :type lang_id: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str

    """
    return web.Response(status=200)


async def attribute_list(request: web.Request, start=None, count=None, type=None, attribute_ids=None, store_id=None, lang_id=None, params=None, exclude=None, response_fields=None, visible=None, required=None, system=None) -> web.Response:
    """attribute_list

    Get attributes list

    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param type: Defines attribute&#39;s type
    :type type: str
    :param attribute_ids: Filter attributes by ids
    :type attribute_ids: str
    :param store_id: Store Id
    :type store_id: str
    :param lang_id: Retrieves attributes on specified language id
    :type lang_id: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param visible: Filter items by visibility status
    :type visible: bool
    :param required: Defines if the option is required
    :type required: bool
    :param system: True if attribute is system
    :type system: bool

    """
    return web.Response(status=200)


async def attribute_type_list(request: web.Request, ) -> web.Response:
    """attribute_type_list

    Get list of supported attributes types


    """
    return web.Response(status=200)


async def attribute_unassign_group(request: web.Request, id, group_id) -> web.Response:
    """attribute_unassign_group

    Unassign attribute from group

    :param id: Entity id
    :type id: str
    :param group_id: Customer group_id
    :type group_id: str

    """
    return web.Response(status=200)


async def attribute_unassign_set(request: web.Request, id, attribute_set_id) -> web.Response:
    """attribute_unassign_set

    Unassign attribute from attribute set

    :param id: Entity id
    :type id: str
    :param attribute_set_id: Attribute set id
    :type attribute_set_id: str

    """
    return web.Response(status=200)


async def attribute_update(request: web.Request, id, name, store_id=None, lang_id=None) -> web.Response:
    """attribute_update

    Update attribute data

    :param id: Entity id
    :type id: str
    :param name: Defines new attributes&#39;s name
    :type name: str
    :param store_id: Store Id
    :type store_id: str
    :param lang_id: Language id
    :type lang_id: str

    """
    return web.Response(status=200)
