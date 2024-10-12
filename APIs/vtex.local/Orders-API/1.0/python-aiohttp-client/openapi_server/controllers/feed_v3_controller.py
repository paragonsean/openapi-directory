from typing import List, Dict
from aiohttp import web

from openapi_server.models.commititemfeedorderstatus_request import CommititemfeedorderstatusRequest
from openapi_server.models.feed_configuration_request import FeedConfigurationRequest
from openapi_server.models.get_feed_configuration200_response import GetFeedConfiguration200Response
from openapi_server.models.getfeedorderstatus import Getfeedorderstatus
from openapi_server.models.test_jso_nata_expression import TestJSONataExpression
from openapi_server import util


async def commititemfeedorderstatus(request: web.Request, content_type, accept, body) -> web.Response:
    """Commit feed items

    Commit items in the [feed](https://developers.vtex.com/docs/guides/orders-feed) queue.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = CommititemfeedorderstatusRequest.from_dict(body)
    return web.Response(status=200)


async def feed_configuration(request: web.Request, accept, content_type, body) -> web.Response:
    """Create or update feed configuration

    The Orders Feed v3 is the best way to create order integrations. Below you can find details on the configuration API specification, and to know more see our [Feed v3 guide](https://developers.vtex.com/vtex-rest-api/docs/orders-feed) and our [order integration guide](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-order-integration)    There are two types of filtering that can be used. The &#x60;FromWorkflow&#x60; type filters orders by status, whereas the &#x60;FromOrders&#x60; type uses JSONata expressions to filter orders according to any property in the orders JSON document. This enables stores to filter delivered orders and orders in which products have been added or removed, for example. To learn more, access the [JSONata documentation](https://docs.jsonata.org/overview.html) and test filtering JSONata expressions with our [Test JSONata expression](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/expressions/jsonata) endpoint.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = FeedConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def feed_configuration_delete(request: web.Request, accept, content_type) -> web.Response:
    """Delete feed configuration

    Deletes the configuration set up in [Feed v3](https://developers.vtex.com/docs/guides/orders-feed).

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str

    """
    return web.Response(status=200)


async def get_feed_configuration(request: web.Request, content_type, accept) -> web.Response:
    """Get feed configuration

    The Orders Feed v3 is the best way to create order integrations. Below you can find details on the configuration API specification, and to know more see our [Feed v3 guide](https://developers.vtex.com/vtex-rest-api/docs/orders-feed) and our [order integration guide](https://developers.vtex.com/vtex-rest-api/docs/erp-integration-set-up-order-integration).   &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Orders onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/orders-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Orders and is organized by focusing on the developer&#39;s journey.    

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str

    """
    return web.Response(status=200)


async def getfeedorderstatus1(request: web.Request, maxlot, accept, content_type) -> web.Response:
    """Retrieve feed items

    Retrieve items from [feed](https://developers.vtex.com/docs/guides/orders-feed) queue.    The event will be removed if the message &#x60;send retry&#x60; is equal to, or greater than the maximum retention period.    &gt; This API will return &#x60;404 Not Found&#x60; if there is no [Feed Configuration](https://developers.vtex.com/docs/guides/orders-feed) available for the given X-VTEX-API-AppKey.

    :param maxlot: Lot quantity to retrieve. Maximum accepted value is 10.
    :type maxlot: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param content_type: Type of the content being sent
    :type content_type: str

    """
    return web.Response(status=200)


async def test_jso_nata_expression(request: web.Request, accept, content_type, body=None) -> web.Response:
    """Test JSONata expression

    This endpoint allows you to test a JSON document with a JSONata expression, returning &#x60;true&#x60; if the document meets the criteria posed in the expression, or &#x60;false&#x60; if it does not.    Since JSONata expressions can be used to filter order updates in the [Orders API feed and hook](https://developers.vtex.com/docs/guides/orders-feed), this endpoint can be used to test an expression&#39;s results before configuring the [feed or hook](https://developers.vtex.com/docs/guides/orders-feed).    Learn more about how to use JSONata expressions, in the [JSONata documentation](https://docs.jsonata.org/overview.html).

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param content_type: Type of the content being sent
    :type content_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = TestJSONataExpression.from_dict(body)
    return web.Response(status=200)
