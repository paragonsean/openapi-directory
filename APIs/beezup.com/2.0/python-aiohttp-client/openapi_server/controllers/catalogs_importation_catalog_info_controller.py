from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.change_custom_column_request import ChangeCustomColumnRequest
from openapi_server.models.configure_catalog_column_catalog_request import ConfigureCatalogColumnCatalogRequest
from openapi_server.models.detected_catalog_column_list import DetectedCatalogColumnList
from openapi_server.models.importation_custom_column_list import ImportationCustomColumnList
from openapi_server.models.map_beez_up_column_request import MapBeezUPColumnRequest
from openapi_server.models.product_sample import ProductSample
from openapi_server import util


async def importation_configure_catalog_column(request: web.Request, store_id, execution_id, column_id, body) -> web.Response:
    """Configure catalog column

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str
    :param column_id: The custom column identifier
    :type column_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConfigureCatalogColumnCatalogRequest.from_dict(body)
    return web.Response(status=200)


async def importation_delete_custom_column(request: web.Request, store_id, execution_id, column_id) -> web.Response:
    """Delete Custom Column

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str
    :param column_id: The custom column identifier
    :type column_id: str

    """
    return web.Response(status=200)


async def importation_get_custom_column_expression(request: web.Request, store_id, execution_id, column_id) -> web.Response:
    """Get the encrypted custom column expression in this importation

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str
    :param column_id: The custom column identifier
    :type column_id: str

    """
    return web.Response(status=200)


async def importation_get_custom_columns(request: web.Request, store_id, execution_id) -> web.Response:
    """Get custom columns currently place in this importation

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str

    """
    return web.Response(status=200)


async def importation_get_detected_catalog_columns(request: web.Request, store_id, execution_id) -> web.Response:
    """Get detected catalog columns during this importation.

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str

    """
    return web.Response(status=200)


async def importation_get_product_sample(request: web.Request, store_id, execution_id, product_sample_index) -> web.Response:
    """Get the product sample related to this importation with all columns (catalog and custom)

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str
    :param product_sample_index: Index of the product sample. Starting from 0 to 99.
    :type product_sample_index: int

    """
    return web.Response(status=200)


async def importation_get_product_sample_custom_column_value(request: web.Request, store_id, execution_id, product_sample_index, column_id) -> web.Response:
    """Get product sample custom column value related to this importation.

    /!\\ Use this operation only when you just changed the custom column expression and you want to get a precise the property value. Otherwise use the operation Importation_GetProductSample which will give you all property values

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str
    :param product_sample_index: Index of the product sample. Starting from 0 to 99.
    :type product_sample_index: int
    :param column_id: The custom column identifier
    :type column_id: str

    """
    return web.Response(status=200)


async def importation_ignore_column(request: web.Request, store_id, execution_id, column_id) -> web.Response:
    """Ignore Column

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str
    :param column_id: The custom column identifier
    :type column_id: str

    """
    return web.Response(status=200)


async def importation_map_catalog_column(request: web.Request, store_id, execution_id, column_id, body) -> web.Response:
    """Map catalog column to a BeezUP column

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str
    :param column_id: The catalog column identifier
    :type column_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MapBeezUPColumnRequest.from_dict(body)
    return web.Response(status=200)


async def importation_map_custom_column(request: web.Request, store_id, execution_id, column_id, body) -> web.Response:
    """Map custom column to a BeezUP column

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str
    :param column_id: The custom column identifier
    :type column_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MapBeezUPColumnRequest.from_dict(body)
    return web.Response(status=200)


async def importation_reattend_column(request: web.Request, store_id, execution_id, column_id) -> web.Response:
    """Reattend Column

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str
    :param column_id: The custom column identifier
    :type column_id: str

    """
    return web.Response(status=200)


async def importation_save_custom_column(request: web.Request, store_id, execution_id, column_id, body) -> web.Response:
    """Create or replace a custom column

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str
    :param column_id: The custom column identifier
    :type column_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ChangeCustomColumnRequest.from_dict(body)
    return web.Response(status=200)


async def importation_unmap_catalog_column(request: web.Request, store_id, execution_id, column_id) -> web.Response:
    """Unmap catalog column

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str
    :param column_id: The catalog column identifier
    :type column_id: str

    """
    return web.Response(status=200)


async def importation_unmap_custom_column(request: web.Request, store_id, execution_id, column_id) -> web.Response:
    """Unmap custom column

    

    :param store_id: Your store identifier
    :type store_id: str
    :param execution_id: The execution identifier of you catalog importation
    :type execution_id: str
    :param column_id: The custom column identifier
    :type column_id: str

    """
    return web.Response(status=200)
