from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def barcode_decode_post(request: web.Request, barimage) -> web.Response:
    """barcode_decode_post

    Decode a Barcode image and return the cotents if successful

    :param barimage: Barcode image to decode and get the content value
    :type barimage: str

    """
    return web.Response(status=200)


async def barcode_decode_types_get(request: web.Request, ) -> web.Response:
    """barcode_decode_types_get

    Get the supported barcode types for the decoding process.


    """
    return web.Response(status=200)


async def barcode_encode_get(request: web.Request, number, barcodeformat=None, outputformat=None, widthfactor=None, totalheight=None) -> web.Response:
    """barcode_encode_get

    Get a Bar Code image for the given barcode number

    :param number: Barcode number
    :type number: str
    :param barcodeformat: Barcode format default C39. Valid values are the keys to those returned from /barcode/encode/types.
    :type barcodeformat: str
    :param outputformat: Output image format. Must be one of png/html/jpg/svg
    :type outputformat: str
    :param widthfactor: Width factor of the image
    :type widthfactor: int
    :param totalheight: Total height of the image
    :type totalheight: int

    """
    return web.Response(status=200)


async def barcode_encode_types_get(request: web.Request, ) -> web.Response:
    """barcode_encode_types_get

    Get the supported barcode types for encoding / image generation.


    """
    return web.Response(status=200)
