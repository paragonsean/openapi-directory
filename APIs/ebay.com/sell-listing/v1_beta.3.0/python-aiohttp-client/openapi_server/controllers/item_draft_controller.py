from typing import List, Dict
from aiohttp import web

from openapi_server.models.item_draft import ItemDraft
from openapi_server.models.item_draft_response import ItemDraftResponse
from openapi_server import util


async def create_item_draft(request: web.Request, x_ebay_c_marketplace_id, content_language=None, body=None) -> web.Response:
    """create_item_draft

    This call gives Partners the ability to create an eBay draft of a item for their seller using information from their site. This lets the Partner increase the exposure of items on their site and leverage the eBay user listing experience seamlessly. This experience provides guidance on pricing, aspects, etc. and recommendations that help create a listing that is complete and improves the exposure of the listing in search results. After the listing draft is created, the seller logs into their eBay account and uses the listing experience to finish the listing and publish the item on eBay.

    :param x_ebay_c_marketplace_id: Use this header to specify an eBay marketplace ID. For a list of supported sites, see API Restrictions in the Listing API overview.
    :type x_ebay_c_marketplace_id: str
    :param content_language: Use this header to specify the natural language of the seller. For details, see Content-Language in HTTP request headers. Required: For EBAY_CA in French. (Content-Language &#x3D; fr-CA)
    :type content_language: str
    :param body: 
    :type body: dict | bytes

    """
    body = ItemDraft.from_dict(body)
    return web.Response(status=200)
