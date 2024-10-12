from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_config_update200_response import AccountConfigUpdate200Response
from openapi_server.models.attribute_delete200_response import AttributeDelete200Response
from openapi_server.models.bridge_delete200_response import BridgeDelete200Response
from openapi_server.models.cart_config_update200_response import CartConfigUpdate200Response
from openapi_server.models.category_add200_response import CategoryAdd200Response
from openapi_server.models.category_count200_response import CategoryCount200Response
from openapi_server.models.category_find200_response import CategoryFind200Response
from openapi_server.models.category_image_add200_response import CategoryImageAdd200Response
from openapi_server.models.category_info200_response import CategoryInfo200Response
from openapi_server.models.model_response_category_list import ModelResponseCategoryList
from openapi_server import util


async def category_add(request: web.Request, name, parent_id=None, stores_ids=None, store_id=None, lang_id=None, avail=None, sort_order=None, created_time=None, modified_time=None, description=None, meta_title=None, meta_description=None, meta_keywords=None, seo_url=None) -> web.Response:
    """category_add

    Add new category in store

    :param name: Defines category&#39;s name that has to be added
    :type name: str
    :param parent_id: Adds categories specified by parent id
    :type parent_id: str
    :param stores_ids: Create category in the stores that is specified by comma-separated stores&#39; id
    :type stores_ids: str
    :param store_id: Store Id
    :type store_id: str
    :param lang_id: Language id
    :type lang_id: str
    :param avail: Defines category&#39;s visibility status
    :type avail: bool
    :param sort_order: Sort number in the list
    :type sort_order: int
    :param created_time: Entity&#39;s date creation
    :type created_time: str
    :param modified_time: Entity&#39;s date modification
    :type modified_time: str
    :param description: Defines category&#39;s description
    :type description: str
    :param meta_title: Defines unique meta title for each entity
    :type meta_title: str
    :param meta_description: Defines unique meta description of a entity
    :type meta_description: str
    :param meta_keywords: Defines unique meta keywords for each entity
    :type meta_keywords: str
    :param seo_url: Defines unique category&#39;s URL for SEO
    :type seo_url: str

    """
    return web.Response(status=200)


async def category_assign(request: web.Request, product_id, category_id, store_id=None) -> web.Response:
    """category_assign

    Assign category to product

    :param product_id: Defines category assign to the product, specified by product id
    :type product_id: str
    :param category_id: Defines category assign, specified by category id
    :type category_id: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def category_count(request: web.Request, parent_id=None, store_id=None, lang_id=None, created_from=None, created_to=None, modified_from=None, modified_to=None, avail=None) -> web.Response:
    """category_count

    Count categories in store.

    :param parent_id: Counts categories specified by parent id
    :type parent_id: str
    :param store_id: Counts category specified by store id
    :type store_id: str
    :param lang_id: Counts category specified by language id
    :type lang_id: str
    :param created_from: Retrieve entities from their creation date
    :type created_from: str
    :param created_to: Retrieve entities to their creation date
    :type created_to: str
    :param modified_from: Retrieve entities from their modification date
    :type modified_from: str
    :param modified_to: Retrieve entities to their modification date
    :type modified_to: str
    :param avail: Defines category&#39;s visibility status
    :type avail: bool

    """
    return web.Response(status=200)


async def category_delete(request: web.Request, id) -> web.Response:
    """category_delete

    Delete category in store

    :param id: Defines category removal, specified by category id
    :type id: str

    """
    return web.Response(status=200)


async def category_find(request: web.Request, find_value, find_where=None, find_params=None, store_id=None, lang_id=None) -> web.Response:
    """category_find

    Search category in store. \&quot;Laptop\&quot; is specified here by default.

    :param find_value: Entity search that is specified by some value
    :type find_value: str
    :param find_where: Entity search that is specified by the comma-separated unique fields
    :type find_where: str
    :param find_params: Entity search that is specified by comma-separated parameters
    :type find_params: str
    :param store_id: Store Id
    :type store_id: str
    :param lang_id: Language id
    :type lang_id: str

    """
    return web.Response(status=200)


async def category_image_add(request: web.Request, category_id, image_name, url, type, label=None, mime=None, position=None, store_id=None) -> web.Response:
    """category_image_add

    Add image to category

    :param category_id: Defines category id where the image should be added
    :type category_id: str
    :param image_name: Defines image&#39;s name
    :type image_name: str
    :param url: Defines URL of the image that has to be added
    :type url: str
    :param type: Defines image&#39;s types that are specified by comma-separated list
    :type type: str
    :param label: Defines alternative text that has to be attached to the picture
    :type label: str
    :param mime: Mime type of image http://en.wikipedia.org/wiki/Internet_media_type.
    :type mime: str
    :param position: Defines image’s position in the list
    :type position: int
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def category_image_delete(request: web.Request, category_id, image_id, store_id=None) -> web.Response:
    """category_image_delete

    Delete image

    :param category_id: Defines category id where the image should be deleted
    :type category_id: str
    :param image_id: Define image id
    :type image_id: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def category_info(request: web.Request, id, params=None, response_fields=None, exclude=None, store_id=None, lang_id=None) -> web.Response:
    """category_info

    Get category info about category ID*** or specify other category ID.

    :param id: Retrieves category&#39;s info specified by category id
    :type id: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param store_id: Retrieves category info  specified by store id
    :type store_id: str
    :param lang_id: Retrieves category info  specified by language id
    :type lang_id: str

    """
    return web.Response(status=200)


async def category_list(request: web.Request, start=None, count=None, page_cursor=None, parent_id=None, params=None, response_fields=None, exclude=None, store_id=None, lang_id=None, created_from=None, created_to=None, modified_from=None, modified_to=None, avail=None) -> web.Response:
    """category_list

    Get list of categories from store.

    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param page_cursor: Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param parent_id: Retrieves categories specified by parent id
    :type parent_id: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param store_id: Retrieves categories specified by store id
    :type store_id: str
    :param lang_id: Retrieves categorys specified by language id
    :type lang_id: str
    :param created_from: Retrieve entities from their creation date
    :type created_from: str
    :param created_to: Retrieve entities to their creation date
    :type created_to: str
    :param modified_from: Retrieve entities from their modification date
    :type modified_from: str
    :param modified_to: Retrieve entities to their modification date
    :type modified_to: str
    :param avail: Defines category&#39;s visibility status
    :type avail: bool

    """
    return web.Response(status=200)


async def category_unassign(request: web.Request, category_id, product_id, store_id=None) -> web.Response:
    """category_unassign

    Unassign category to product

    :param category_id: Defines category unassign, specified by category id
    :type category_id: str
    :param product_id: Defines category unassign to the product, specified by product id
    :type product_id: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def category_update(request: web.Request, id, name=None, parent_id=None, stores_ids=None, avail=None, sort_order=None, modified_time=None, description=None, meta_title=None, meta_description=None, meta_keywords=None, seo_url=None, lang_id=None, store_id=None) -> web.Response:
    """category_update

    Update category in store

    :param id: Defines category update specified by category id
    :type id: str
    :param name: Defines new category’s name
    :type name: str
    :param parent_id: Defines new parent category id
    :type parent_id: str
    :param stores_ids: Update category in the stores that is specified by comma-separated stores&#39; id
    :type stores_ids: str
    :param avail: Defines category&#39;s visibility status
    :type avail: bool
    :param sort_order: Sort number in the list
    :type sort_order: int
    :param modified_time: Entity&#39;s date modification
    :type modified_time: str
    :param description: Defines new category&#39;s description
    :type description: str
    :param meta_title: Defines unique meta title for each entity
    :type meta_title: str
    :param meta_description: Defines unique meta description of a entity
    :type meta_description: str
    :param meta_keywords: Defines unique meta keywords for each entity
    :type meta_keywords: str
    :param seo_url: Defines unique category&#39;s URL for SEO
    :type seo_url: str
    :param lang_id: Language id
    :type lang_id: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)
