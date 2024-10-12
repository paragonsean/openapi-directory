from typing import List, Dict
from aiohttp import web

from openapi_server.models.shipping_quote import ShippingQuote
from openapi_server.models.shipping_quote_request import ShippingQuoteRequest
from openapi_server import util


async def create_shipping_quote(request: web.Request, x_ebay_c_marketplace_id, body) -> web.Response:
    """create_shipping_quote

    The &lt;b&gt;createShippingQuote&lt;/b&gt; method returns a &lt;i&gt;shipping quote &lt;/i&gt; that contains a list of live \&quot;rates.\&quot;  &lt;br&gt;&lt;br&gt;Each rate represents an offer made by a shipping carrier for a specific service and each offer has a live quote for the base service cost. Rates have a time window in which they are \&quot;live,\&quot; and rates expire when their purchase window ends. If offered by the carrier, rates can include shipping options (and their associated prices), and users can add any offered shipping option to the base service should they desire.  Also, depending on the services required, rates can also include pickup and delivery windows.  &lt;br&gt;&lt;br&gt;Each rate is for a single package and is based on the following information: &lt;ul&gt;&lt;li&gt;The shipping origin&lt;/li&gt; &lt;li&gt;The shipping destination&lt;/li&gt; &lt;li&gt;The package size (weight and dimensions)&lt;/li&gt;&lt;/ul&gt;  Rates are identified by a unique eBay-assigned &lt;b&gt;rateId&lt;/b&gt; and rates are based on price points, pickup and delivery time frames, and other user requirements. Because each rate offered must be compliant with the eBay shipping program, all rates reflect eBay-negotiated prices.  &lt;br&gt;&lt;br&gt;The various rates returned in a shipping quote offer the user a choice from which they can choose a shipping service that best fits their needs. Select the rate for your shipment and using the associated &lt;b&gt;rateId&lt;/b&gt;, call &lt;b&gt;createFromShippingQuote&lt;/b&gt; to create a shipment and generate a shipping label that you can use to ship the package.

    :param x_ebay_c_marketplace_id: This header parameter specifies the eBay marketplace for the shipping quote that is being created. For a list of valid values, refer to the section &lt;a href&#x3D;\&quot;/api-docs/static/rest-request-components.html#marketpl\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Marketplace ID Values&lt;/a&gt; in the &lt;b&gt;Using eBay RESTful APIs&lt;/b&gt; guide.
    :type x_ebay_c_marketplace_id: str
    :param body: The request object for &lt;b&gt;createShippingQuote&lt;/b&gt;.
    :type body: dict | bytes

    """
    body = ShippingQuoteRequest.from_dict(body)
    return web.Response(status=200)


async def get_shipping_quote(request: web.Request, shipping_quote_id) -> web.Response:
    """get_shipping_quote

    This method retrieves the complete details of the shipping quote associated with the specified &lt;b&gt;shippingQuoteId&lt;/b&gt; value.  &lt;br&gt;&lt;br&gt;A \&quot;shipping quote\&quot; pertains to a single specific package and contains a set of shipping \&quot;rates\&quot; that quote the cost to ship the package by different shipping carriers and services. The quotes are based on the package&#39;s origin, destination, and size.  &lt;br&gt;&lt;br&gt;Call &lt;b&gt;createShippingQuote&lt;/b&gt; to create a &lt;b&gt;shippingQuoteId&lt;/b&gt;.

    :param shipping_quote_id: This path parameter specifies the unique eBay-assigned ID of the shipping quote you want to retrieve. The &lt;b&gt;shippingQuoteId&lt;/b&gt; value is generated and returned by a call to &lt;b&gt;createShippingQuote&lt;/b&gt;.
    :type shipping_quote_id: str

    """
    return web.Response(status=200)
