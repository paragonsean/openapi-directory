from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.vendor_product_price_files_get200_response import VendorProductPriceFilesGet200Response
from openapi_server.models.vendor_product_price_files_vendor_product_price_file_id_get200_response import VendorProductPriceFilesVendorProductPriceFileIdGet200Response
from openapi_server import util


async def vendor_product_price_files_get(request: web.Request, file_name=None, vendor_name=None, vendor_ids=None, status=None) -> web.Response:
    """Get a list of price files

    

    :param file_name: 
    :type file_name: str
    :param vendor_name: 
    :type vendor_name: str
    :param vendor_ids: 
    :type vendor_ids: List[str]
    :param status: 
    :type status: str

    """
    return web.Response(status=200)


async def vendor_product_price_files_post(request: web.Request, companies_vendor_id, file) -> web.Response:
    """Upload a vendor price file

    

    :param companies_vendor_id: 
    :type companies_vendor_id: str
    :param file: 
    :type file: str

    """
    return web.Response(status=200)


async def vendor_product_price_files_vendor_product_price_file_id_get(request: web.Request, vendor_product_price_file_id) -> web.Response:
    """Get a single price file

    

    :param vendor_product_price_file_id: Automatically added
    :type vendor_product_price_file_id: str

    """
    return web.Response(status=200)
