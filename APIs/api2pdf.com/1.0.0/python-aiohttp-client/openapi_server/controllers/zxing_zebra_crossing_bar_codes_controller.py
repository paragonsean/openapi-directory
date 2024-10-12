from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def zebra_get(request: web.Request, format, value, showlabel=None, height=None, width=None) -> web.Response:
    """Generate bar codes and QR codes with ZXING.

    See full list of options and documentation [here](https://www.api2pdf.com/documentation/advanced-options-zxing-zebra-crossing-barcodes/) ### Authorize via Query String Parameter **apikey&#x3D;YOUR-API-KEY** ### Example &#x60;&#x60;&#x60; https://v2018.api2pdf.com/zebra?format&#x3D;{format}&amp;apikey&#x3D;{YourApiKey}&amp;value&#x3D;{YourText} &#x60;&#x60;&#x60; 

    :param format: Most common is CODE_39 or QR_CODE
    :type format: str
    :param value: Specify the text value you want to convert
    :type value: str
    :param showlabel: Show label of text below barcode
    :type showlabel: bool
    :param height: Height of the barcode generated image
    :type height: int
    :param width: Width of the barcode generated image
    :type width: int

    """
    return web.Response(status=200)
