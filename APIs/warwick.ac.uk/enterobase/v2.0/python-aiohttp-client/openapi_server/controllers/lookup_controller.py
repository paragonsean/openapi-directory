from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v20_lookup_barcode_post_request import ApiV20LookupBarcodePostRequest
from openapi_server import util


async def api_v20_lookup_barcode_get(request: web.Request, barcode) -> web.Response:
    """api_v20_lookup_barcode_get

    Generic endpoint for lookup of barcodes

    :param barcode: Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_&lt;Table code&gt; e.g. SAL_AA0001AA_ST
    :type barcode: str

    """
    return web.Response(status=200)


async def api_v20_lookup_barcode_post(request: web.Request, barcode, body=None) -> web.Response:
    """api_v20_lookup_barcode_post

    Generic endpoint for lookup of barcodes

    :param barcode: Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_&lt;Table code&gt; e.g. SAL_AA0001AA_ST
    :type barcode: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApiV20LookupBarcodePostRequest.from_dict(body)
    return web.Response(status=200)


async def api_v20_lookup_get(request: web.Request, barcode=None) -> web.Response:
    """api_v20_lookup_get

    Generic endpoint for lookup list of barcodes

    :param barcode: Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_&lt;Table code&gt; e.g. SAL_AA0001AA_ST
    :type barcode: str

    """
    return web.Response(status=200)
