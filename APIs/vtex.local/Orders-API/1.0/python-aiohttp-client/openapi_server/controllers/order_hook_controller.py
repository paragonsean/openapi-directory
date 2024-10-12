from typing import List, Dict
from aiohttp import web

from openapi_server.models.hook_configuration import HookConfiguration
from openapi_server.models.hook_configuration_request import HookConfigurationRequest
from openapi_server import util


async def delete_hook_configuration(request: web.Request, accept, content_type) -> web.Response:
    """Delete hook configuration

    Deletes a given hook configuration.    Learn more with the [orders hook guide](https://developers.vtex.com/vtex-rest-api/docs/orders-feed#hook).

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str

    """
    return web.Response(status=200)


async def get_hook_configuration(request: web.Request, content_type, accept, client_email=None, page=None, per_page=None) -> web.Response:
    """Get hook configuration

    Retrieves a given hook&#39;s configuration details. Learn more with the [orders hook guide](https://developers.vtex.com/vtex-rest-api/docs/orders-feed#hook).     &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Orders onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/orders-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Orders and is organized by focusing on the developer&#39;s journey.    

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param client_email: Customer email.
    :type client_email: str
    :param page: Page number for result pagination.
    :type page: str
    :param per_page: Page quantity for result pagination.
    :type per_page: str

    """
    return web.Response(status=200)


async def hook_configuration(request: web.Request, content_type, accept, body) -> web.Response:
    """Create or update hook configuration

    Configures filtering rules applied to orders hook. Learn more with the [orders hook guide](https://developers.vtex.com/vtex-rest-api/docs/orders-feed#hook).    There are two types of filtering that can be used:      - &#x60;FromWorkflow&#x60;: filters orders by status.     - &#x60;FromOrders&#x60;: uses JSONata expressions to filter orders according to any property in the orders JSON document.     This enables stores to filter delivered orders and orders in which products have been added or removed, for example.    To learn more, access the [JSONata documentation](https://docs.jsonata.org/overview.html) and test filtering JSONata expressions with our [expressions API](https://developers.vtex.com/docs/api-reference/orders-api#post-/api/orders/expressions/jsonata).

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = HookConfigurationRequest.from_dict(body)
    return web.Response(status=200)
