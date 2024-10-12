from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.catalog_column_list import CatalogColumnList
from openapi_server.models.catalog_store_index import CatalogStoreIndex
from openapi_server.models.category_list import CategoryList
from openapi_server.models.change_custom_column_expression_request import ChangeCustomColumnExpressionRequest
from openapi_server.models.change_user_column_name_request import ChangeUserColumnNameRequest
from openapi_server.models.compute_expression_request import ComputeExpressionRequest
from openapi_server.models.create_custom_column_request import CreateCustomColumnRequest
from openapi_server.models.custom_column_list import CustomColumnList
from openapi_server.models.get_products_request import GetProductsRequest
from openapi_server.models.import_already_in_progress_response import ImportAlreadyInProgressResponse
from openapi_server.models.last_manual_import_input_configuration import LastManualImportInputConfiguration
from openapi_server.models.product import Product
from openapi_server.models.product_list import ProductList
from openapi_server.models.random_product_list import RandomProductList
from openapi_server import util


async def catalog_change_catalog_column_user_name(request: web.Request, store_id, column_id, body) -> web.Response:
    """Change Catalog Column User Name

    

    :param store_id: Your store identifier
    :type store_id: str
    :param column_id: The catalog column identifier
    :type column_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangeUserColumnNameRequest.from_dict(body)
    return web.Response(status=200)


async def catalog_change_custom_column_expression(request: web.Request, store_id, column_id, body) -> web.Response:
    """Change custom column expression

    

    :param store_id: Your store identifier
    :type store_id: str
    :param column_id: The custom column identifier
    :type column_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangeCustomColumnExpressionRequest.from_dict(body)
    return web.Response(status=200)


async def catalog_change_custom_column_user_name(request: web.Request, store_id, column_id, body) -> web.Response:
    """Change Custom Column User Name

    

    :param store_id: Your store identifier
    :type store_id: str
    :param column_id: The custom column identifier
    :type column_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangeUserColumnNameRequest.from_dict(body)
    return web.Response(status=200)


async def catalog_compute_expression(request: web.Request, store_id, body) -> web.Response:
    """Compute the expression for this catalog.

    

    :param store_id: Your store identifier
    :type store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ComputeExpressionRequest.from_dict(body)
    return web.Response(status=200)


async def catalog_delete_custom_column(request: web.Request, store_id, column_id) -> web.Response:
    """Delete custom column

    

    :param store_id: Your store identifier
    :type store_id: str
    :param column_id: The custom column identifier
    :type column_id: str

    """
    return web.Response(status=200)


async def catalog_get_catalog_columns(request: web.Request, store_id) -> web.Response:
    """Get catalog column list

    

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)


async def catalog_get_categories(request: web.Request, store_id, accept_encoding) -> web.Response:
    """Get category list

    

    :param store_id: Your store identifier
    :type store_id: str
    :param accept_encoding: Indicates that the client accepts that the response will be compressed to reduce traffic size.
    :type accept_encoding: List[str]

    """
    return web.Response(status=200)


async def catalog_get_custom_column_expression(request: web.Request, store_id, column_id) -> web.Response:
    """Get the encrypted custom column expression

    

    :param store_id: Your store identifier
    :type store_id: str
    :param column_id: The custom column identifier
    :type column_id: str

    """
    return web.Response(status=200)


async def catalog_get_custom_columns(request: web.Request, store_id) -> web.Response:
    """Get custom column list

    

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)


async def catalog_get_product_by_product_id(request: web.Request, store_id, product_id) -> web.Response:
    """Get product by ProductId

    

    :param store_id: Your store identifier
    :type store_id: str
    :param product_id: The product identifier you want to get
    :type product_id: str

    """
    return web.Response(status=200)


async def catalog_get_product_by_sku(request: web.Request, store_id, sku) -> web.Response:
    """Get product by Sku

    

    :param store_id: Your store identifier
    :type store_id: str
    :param sku: The product sku you want to get
    :type sku: str

    """
    return web.Response(status=200)


async def catalog_get_products(request: web.Request, store_id, body) -> web.Response:
    """Get product list

    

    :param store_id: Your store identifier
    :type store_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetProductsRequest.from_dict(body)
    return web.Response(status=200)


async def catalog_get_random_products(request: web.Request, store_id) -> web.Response:
    """Get random product list

    We will return 10 products randomly selected with all product values

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)


async def catalog_save_custom_column(request: web.Request, store_id, column_id, body) -> web.Response:
    """Create or replace a custom column

    

    :param store_id: Your store identifier
    :type store_id: str
    :param column_id: The custom column identifier
    :type column_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateCustomColumnRequest.from_dict(body)
    return web.Response(status=200)


async def catalog_store_index(request: web.Request, store_id) -> web.Response:
    """Get the index of the catalog API for this store

    The operation will give you all the operations you will be able to do on this store for this API.

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)


async def importation_get_manual_update_last_input_config(request: web.Request, store_id) -> web.Response:
    """Get the last input configuration

    

    :param store_id: Your store identifier
    :type store_id: str

    """
    return web.Response(status=200)
