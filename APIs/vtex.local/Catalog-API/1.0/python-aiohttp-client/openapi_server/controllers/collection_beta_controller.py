from typing import List, Dict
from aiohttp import web

from openapi_server.models.request_body import RequestBody
from openapi_server import util


async def g_et_all_collections(request: web.Request, content_type, accept, page, page_size, order_by_asc) -> web.Response:
    """Get All Collections

    Retrieves a list of all collections matching a filter.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param page: Page number.
    :type page: int
    :param page_size: Number of the items of the page.
    :type page_size: int
    :param order_by_asc: Defines if the items of the page are in ascending order.
    :type order_by_asc: bool

    """
    return web.Response(status=200)


async def g_et_all_inactive_collections(request: web.Request, content_type, accept) -> web.Response:
    """Get All Inactive Collections

    Retrieves a list of Collection IDs of the inactive Collections.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def g_et_collectionsbyseachterms(request: web.Request, content_type, accept, search_terms, page=None, page_size=None, order_by_asc=None) -> web.Response:
    """Get Collections by search terms

    Retrieves a list of collections matching a filter.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param search_terms: String that will search for a collection related to it.
    :type search_terms: str
    :param page: Page number.
    :type page: int
    :param page_size: Number of the items of the page.
    :type page_size: int
    :param order_by_asc: Defines if the items of the page are in ascending order.
    :type order_by_asc: bool

    """
    return web.Response(status=200)


async def g_et_importfileexample(request: web.Request, content_type, accept) -> web.Response:
    """Import Collection file example

    Imports a sample of the imported XLS file. You need to save the response file to your device.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def g_et_productsfromacollection(request: web.Request, content_type, accept, collection_id, page=None, page_size=None, filter=None, active=None, visible=None, category_id=None, brand_id=None, supplier_id=None, sales_channel_id=None, release_from=None, release_to=None, specification_product=None, specification_field_id=None) -> web.Response:
    """Get products from a collection

    Retrieves information about the products from a collection.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param collection_id: Collection&#39;s unique identifier.
    :type collection_id: int
    :param page: Page number.
    :type page: int
    :param page_size: Number of the items of the page.
    :type page_size: int
    :param filter: Filter used to refine the Collection&#39;s products.
    :type filter: str
    :param active: Defines if the status of the product is active or not.
    :type active: bool
    :param visible: Defines if the product is visible on the store or not.
    :type visible: bool
    :param category_id: Product&#39;s Category unique identifier.
    :type category_id: int
    :param brand_id: Product&#39;s Brand unique identifier.
    :type brand_id: int
    :param supplier_id: Product&#39;s Supplier unique identifier.
    :type supplier_id: int
    :param sales_channel_id: Product&#39;s Trade Policy unique identifier.
    :type sales_channel_id: int
    :param release_from: Product past release date.
    :type release_from: str
    :param release_to: Product future release date.
    :type release_to: str
    :param specification_product: Product Specification Field Value. You must also fill in &#x60;SpecificationFieldId&#x60; to use this parameter.
    :type specification_product: str
    :param specification_field_id: Product Specification Field unique identifier.
    :type specification_field_id: int

    """
    return web.Response(status=200)


async def p_ost_addproductsbyimportfile(request: web.Request, content_type, accept, collection_id, file=None) -> web.Response:
    """Add products to Collection by imported file

    Adds products to a collection from the request body file. The file must be an imported template.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param collection_id: Collection&#39;s unique identifier.
    :type collection_id: int
    :param file: XLS file with information about products to be added to a Collection. The file must be an imported template from [Import Collection file example](https://developers.vtex.com/vtex-developer-docs/reference/get-importfileexample) endpoint.
    :type file: dict | bytes

    """
    file = object.from_dict(file)
    return web.Response(status=200)


async def p_ost_create_collection(request: web.Request, content_type, accept, body) -> web.Response:
    """Create Collection

    Creates a new collection.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = RequestBody.from_dict(body)
    return web.Response(status=200)


async def p_ost_removeproductsbyimportfile(request: web.Request, content_type, accept, collection_id, file=None) -> web.Response:
    """Remove products from Collection by imported file

    Removes products from a collection from the request body file. The file must be an imported template.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param collection_id: Collection&#39;s unique identifier.
    :type collection_id: int
    :param file: XLS file with information about products to be added to a Collection. The file must be an imported template from [Import Collection file example](https://developers.vtex.com/vtex-developer-docs/reference/get-importfileexample) endpoint.
    :type file: dict | bytes

    """
    file = object.from_dict(file)
    return web.Response(status=200)
