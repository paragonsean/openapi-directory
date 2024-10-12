from typing import List, Dict
from aiohttp import web

from openapi_server.models.vendor_products_get200_response import VendorProductsGet200Response
from openapi_server.models.vendor_products_vendor_product_id_get200_response import VendorProductsVendorProductIdGet200Response
from openapi_server import util


async def vendor_products_get(request: web.Request, name=None, product_number=None, barcode=None, vendor_id=None) -> web.Response:
    """List vendor products

    

    :param name: Used to filter on the &#x60;name&#x60; of the vendor products
    :type name: str
    :param product_number: Used to filter on the &#x60;product_number&#x60; of the vendor products
    :type product_number: str
    :type product_number: str
    :param barcode: Used to filter on the &#x60;barcode&#x60; of the vendor products
    :type barcode: str
    :param vendor_id: Used to filter on the &#x60;vendor_id&#x60; of the vendor products
    :type vendor_id: str

    """
    return web.Response(status=200)


async def vendor_products_vendor_product_id_get(request: web.Request, vendor_product_id) -> web.Response:
    """View single vendor product

    

    :param vendor_product_id: 
    :type vendor_product_id: str

    """
    return web.Response(status=200)
