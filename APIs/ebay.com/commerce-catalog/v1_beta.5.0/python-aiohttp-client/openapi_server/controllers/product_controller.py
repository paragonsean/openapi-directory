from typing import List, Dict
from aiohttp import web

from openapi_server.models.product import Product
from openapi_server import util


async def get_product(request: web.Request, epid, x_ebay_c_marketplace_id=None) -> web.Response:
    """get_product

    This method retrieves details of the catalog product identified by the eBay product identifier (ePID) specified in the request. These details include the product&#39;s title and description, aspects and their values, associated images, applicable category IDs, and any recognized identifiers that apply to the product. &lt;br /&gt;&lt;br /&gt; For a new listing, you can use the &lt;b&gt;search&lt;/b&gt; method to identify candidate products on which to base the listing, then use the &lt;b&gt;getProduct&lt;/b&gt; method to present the full details of those candidate products to the seller to make a a final selection.

    :param epid: The ePID of the product being requested. This value can be discovered by issuing the &lt;b&gt;search&lt;/b&gt; method and examining the value of the &lt;b&gt;productSummaries.epid&lt;/b&gt; field for the desired returned product summary.
    :type epid: str
    :param x_ebay_c_marketplace_id: This method also uses the &lt;code&gt;X-EBAY-C-MARKETPLACE-ID&lt;/code&gt; header to identify the seller&#39;s eBay marketplace. It is required for all marketplaces except EBAY_US, which is the default. &lt;b&gt;Note:&lt;/b&gt; This method is limited to &lt;code&gt;EBAY_US&lt;/code&gt;, &lt;code&gt;EBAY_AU&lt;/code&gt;, &lt;code&gt;EBAY_CA&lt;/code&gt;, and &lt;code&gt;EBAY_GB&lt;/code&gt; values.
    :type x_ebay_c_marketplace_id: str

    """
    return web.Response(status=200)
