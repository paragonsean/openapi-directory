from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_shipment_from_quote_request import CreateShipmentFromQuoteRequest
from openapi_server.models.shipment import Shipment
from openapi_server import util


async def cancel_shipment(request: web.Request, shipment_id) -> web.Response:
    """cancel_shipment

    This method cancels the shipment associated with the specified shipment ID and the associated shipping label is deleted. When you cancel a shipment, the &lt;b&gt;totalShippingCost&lt;/b&gt; of the canceled shipment is refunded to the account established by the user&#39;s billing agreement.  &lt;br&gt;&lt;br&gt;Note that you cannot cancel a shipment if you have used the associated shipping label.

    :param shipment_id: This path parameter specifies the unique eBay-assigned ID of the shipment to be canceled. The &lt;b&gt;shipmentId&lt;/b&gt; value is generated and returned by a call to &lt;b&gt;createFromShippingQuote&lt;/b&gt;.
    :type shipment_id: str

    """
    return web.Response(status=200)


async def create_from_shipping_quote(request: web.Request, body) -> web.Response:
    """create_from_shipping_quote

    This method creates a \&quot;shipment\&quot; based on the &lt;b&gt;shippingQuoteId&lt;/b&gt; and &lt;b&gt;rateId&lt;/b&gt; values supplied in the request. The rate identified by the &lt;b&gt;rateId&lt;/b&gt; value specifies the carrier and service for the package shipment, and the rate ID must be contained in the shipping quote identified by the &lt;b&gt;shippingQuoteId&lt;/b&gt; value. Call &lt;b&gt;createShippingQuote&lt;/b&gt; to retrieve a set of live shipping rates.  &lt;br&gt;&lt;br&gt;When you create a shipment, eBay generates a shipping label that you can download and use to ship your package.  &lt;br&gt;&lt;br&gt;In a &lt;b&gt;createFromShippingQuote&lt;/b&gt; request, sellers can include a list of shipping options they want to add to the base service quoted in the selected rate. The list of available shipping options is specific to each quoted rate and if available, the options are listed in the rate container of the of the shipping quote.  &lt;br&gt;&lt;br&gt;In addition to a configurable return-to location and other details about the shipment, the response to this method includes:  &lt;ul&gt;&lt;li&gt;The shipping carrier and service to be used for the package shipment&lt;/li&gt; &lt;li&gt;A list of selected shipping options, if any&lt;/li&gt; &lt;li&gt;The shipment tracking number&lt;/li&gt; &lt;li&gt;The total shipping cost (the sum cost of the base shipping service and any added options)&lt;/li&gt;&lt;/ul&gt; When you create a shipment, your billing agreement account is charged the sum of the &lt;b&gt;baseShippingCost&lt;/b&gt; and the total cost of any additional shipping options you might have selected. Use the URL returned in &lt;b&gt;labelDownloadUrl&lt;/b&gt; field, or call &lt;b&gt;downloadLabelFile&lt;/b&gt; with the &lt;b&gt;shipmentId&lt;/b&gt; value from the response, to download a shipping label for your package. &lt;p class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Important!&lt;/b&gt; Sellers must set up their payment method with eBay before they can use this method to create a shipment and the associated shipping label.&lt;/p&gt;

    :param body: The create shipment from quote request.
    :type body: dict | bytes

    """
    body = CreateShipmentFromQuoteRequest.from_dict(body)
    return web.Response(status=200)


async def download_label_file(request: web.Request, shipment_id) -> web.Response:
    """download_label_file

    This method returns the shipping label file that was generated for the &lt;b&gt;shipmentId&lt;/b&gt; value specified in the request. Call &lt;b&gt;createFromShippingQuote&lt;/b&gt; to generate a shipment ID.  &lt;br&gt;&lt;br&gt;Use the &lt;code&gt;Accept&lt;/code&gt; HTTP header to specify the format of the returned file. The default file format is a PDF file. &lt;!-- Are other options available? --&gt;

    :param shipment_id: This path parameter specifies the unique eBay-assigned ID of the shipment associated with the shipping label you want to download. The &lt;b&gt;shipmentId&lt;/b&gt; value is generated and returned by a call to &lt;b&gt;createFromShippingQuote&lt;/b&gt;.
    :type shipment_id: str

    """
    return web.Response(status=200)


async def get_shipment(request: web.Request, shipment_id) -> web.Response:
    """get_shipment

    This method retrieves the shipment details for the specified shipment ID. Call &lt;b&gt;createFromShippingQuote&lt;/b&gt; to generate a shipment ID.

    :param shipment_id: This path parameter specifies the unique eBay-assigned ID of the shipment you want to retrieve. The &lt;b&gt;shipmentId&lt;/b&gt; value is generated and returned by a call to &lt;b&gt;createFromShippingQuote&lt;/b&gt;.
    :type shipment_id: str

    """
    return web.Response(status=200)
