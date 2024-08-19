from typing import List, Dict
from aiohttp import web

from openapi_server.models.barcode import Barcode
from openapi_server.models.issuing_country import IssuingCountry
from openapi_server.models.product import Product
from openapi_server.models.verify_checksum import VerifyChecksum
from openapi_server import util


async def barcode_image(request: web.Request, op, ean, width=None, height=None, format=None) -> web.Response:
    """Generate a PNG barcode image

    

    :param op: API operation
    :type op: str
    :param ean: EAN code to search for
    :type ean: int
    :param width: 
    :type width: int
    :param height: 
    :type height: int
    :param format: output format
    :type format: str

    """
    return web.Response(status=200)


async def barcode_lookup(request: web.Request, op, ean, language=None, format=None) -> web.Response:
    """Look up an EAN

    Search by EAN code

    :param op: API operation
    :type op: str
    :param ean: EAN code to search for
    :type ean: int
    :param language: preferred language for the product name
    :type language: int
    :param format: output format
    :type format: str

    """
    return web.Response(status=200)


async def barcode_prefix_search(request: web.Request, op, prefix, language=None, page=None, format=None) -> web.Response:
    """Query the database for all barcodes with the same beginning

    

    :param op: API operation
    :type op: str
    :param prefix: barcode prefix to search for, at least 4 digits
    :type prefix: str
    :param language: preferred language for the product name
    :type language: int
    :param page: result page
    :type page: int
    :param format: output format
    :type format: str

    """
    return web.Response(status=200)


async def category_search(request: web.Request, op, category, name=None, language=None, page=None, format=None) -> web.Response:
    """Search for products form a certain category

    

    :param op: API operation
    :type op: str
    :param category: category number
    :type category: int
    :param name: name or keyords to search for
    :type name: str
    :param language: preferred language for the product name (default any language)
    :type language: int
    :param page: result page
    :type page: int
    :param format: output format
    :type format: str

    """
    return web.Response(status=200)


async def issuing_country(request: web.Request, op, ean, format=None) -> web.Response:
    """Search for a issuing country of a barcode

    Search for a issuing country of a barcode. In contrast to barcode-lookup, this will always give a result, even if we don&#39;t know the product name.

    :param op: API operation
    :type op: str
    :param ean: EAN code to search for
    :type ean: int
    :param format: output format
    :type format: str

    """
    return web.Response(status=200)


async def product_search(request: web.Request, op, name, language=None, page=None, format=None) -> web.Response:
    """Search by product name

    

    :param op: API operation
    :type op: str
    :param name: name or keyords to search for
    :type name: str
    :param language: preferred language for the product name (default any language)
    :type language: int
    :param page: result page
    :type page: int
    :param format: output format
    :type format: str

    """
    return web.Response(status=200)


async def verify_checksum(request: web.Request, op, ean, format=None) -> web.Response:
    """Verify the checksum of an EAN code

    

    :param op: API operation
    :type op: str
    :param ean: EAN code to search for
    :type ean: int
    :param format: output format
    :type format: str

    """
    return web.Response(status=200)
