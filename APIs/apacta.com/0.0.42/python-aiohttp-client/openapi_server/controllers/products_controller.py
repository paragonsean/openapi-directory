from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.clocking_records_clocking_record_id_delete200_response import ClockingRecordsClockingRecordIdDelete200Response
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.products_get200_response import ProductsGet200Response
from openapi_server.models.products_post_request import ProductsPostRequest
from openapi_server.models.products_product_id_get200_response import ProductsProductIdGet200Response
from openapi_server import util


async def bulk_delete_products(request: web.Request, body) -> web.Response:
    """Bulk delete products

    

    :param body: Products ids
    :type body: dict | bytes

    """
    body = BulkActionRequestBody.from_dict(body)
    return web.Response(status=200)


async def products_get(request: web.Request, name=None, product_number=None, barcode=None, modified_gte=None) -> web.Response:
    """List products

    

    :param name: Used to filter on the &#x60;name&#x60; of the products
    :type name: str
    :param product_number: Used to filter on the &#x60;product_number&#x60; of the products
    :type product_number: str
    :type product_number: str
    :param barcode: Used to filter on the &#x60;barcode&#x60; of the products
    :type barcode: str
    :param modified_gte: 
    :type modified_gte: str

    """
    return web.Response(status=200)


async def products_post(request: web.Request, body=None) -> web.Response:
    """Add new product

    

    :param body: 
    :type body: dict | bytes

    """
    body = ProductsPostRequest.from_dict(body)
    return web.Response(status=200)


async def products_product_id_delete(request: web.Request, product_id) -> web.Response:
    """Delete a product

    

    :param product_id: 
    :type product_id: str

    """
    return web.Response(status=200)


async def products_product_id_get(request: web.Request, product_id) -> web.Response:
    """View single product

    

    :param product_id: 
    :type product_id: str

    """
    return web.Response(status=200)


async def products_product_id_put(request: web.Request, product_id) -> web.Response:
    """Edit a product

    

    :param product_id: 
    :type product_id: str

    """
    return web.Response(status=200)


async def products_undelete_product_id_post(request: web.Request, product_id) -> web.Response:
    """Restore a deleted product

    

    :param product_id: 
    :type product_id: str
    :type product_id: str

    """
    return web.Response(status=200)


async def upload_or_delete_product_image(request: web.Request, product_id, image=None) -> web.Response:
    """

    Upload or delete product image

    :param product_id: 
    :type product_id: str
    :param image: 
    :type image: str

    """
    return web.Response(status=200)
