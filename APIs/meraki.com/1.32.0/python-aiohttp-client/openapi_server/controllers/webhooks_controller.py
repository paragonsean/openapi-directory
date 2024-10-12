from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_webhooks_http_server_request import CreateNetworkWebhooksHttpServerRequest
from openapi_server.models.create_network_webhooks_payload_template_request import CreateNetworkWebhooksPayloadTemplateRequest
from openapi_server.models.create_network_webhooks_webhook_test201_response import CreateNetworkWebhooksWebhookTest201Response
from openapi_server.models.create_network_webhooks_webhook_test_request import CreateNetworkWebhooksWebhookTestRequest
from openapi_server.models.get_network_webhooks_http_servers200_response_inner import GetNetworkWebhooksHttpServers200ResponseInner
from openapi_server.models.get_network_webhooks_payload_templates200_response_inner import GetNetworkWebhooksPayloadTemplates200ResponseInner
from openapi_server.models.get_organization_webhooks_logs200_response_inner import GetOrganizationWebhooksLogs200ResponseInner
from openapi_server.models.update_network_webhooks_http_server_request import UpdateNetworkWebhooksHttpServerRequest
from openapi_server.models.update_network_webhooks_payload_template_request import UpdateNetworkWebhooksPayloadTemplateRequest
from openapi_server import util


async def create_network_webhooks_http_server_1(request: web.Request, network_id, body) -> web.Response:
    """Add an HTTP server to a network

    Add an HTTP server to a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkWebhooksHttpServerRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_webhooks_payload_template_1(request: web.Request, network_id, body) -> web.Response:
    """Create a webhook payload template for a network

    Create a webhook payload template for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkWebhooksPayloadTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def create_network_webhooks_webhook_test_1(request: web.Request, network_id, body) -> web.Response:
    """Send a test webhook for a network

    Send a test webhook for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkWebhooksWebhookTestRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_webhooks_http_server_1(request: web.Request, network_id, http_server_id) -> web.Response:
    """Delete an HTTP server from a network

    Delete an HTTP server from a network

    :param network_id: 
    :type network_id: str
    :param http_server_id: 
    :type http_server_id: str

    """
    return web.Response(status=200)


async def delete_network_webhooks_payload_template_1(request: web.Request, network_id, payload_template_id) -> web.Response:
    """Destroy a webhook payload template for a network

    Destroy a webhook payload template for a network. Does not work for included templates (&#39;wpt_00001&#39;, &#39;wpt_00002&#39;, &#39;wpt_00003&#39;, &#39;wpt_00004&#39;, &#39;wpt_00005&#39; or &#39;wpt_00006&#39;)

    :param network_id: 
    :type network_id: str
    :param payload_template_id: 
    :type payload_template_id: str

    """
    return web.Response(status=200)


async def get_network_webhooks_http_server_1(request: web.Request, network_id, http_server_id) -> web.Response:
    """Return an HTTP server for a network

    Return an HTTP server for a network

    :param network_id: 
    :type network_id: str
    :param http_server_id: 
    :type http_server_id: str

    """
    return web.Response(status=200)


async def get_network_webhooks_http_servers_1(request: web.Request, network_id) -> web.Response:
    """List the HTTP servers for a network

    List the HTTP servers for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_webhooks_payload_template_1(request: web.Request, network_id, payload_template_id) -> web.Response:
    """Get the webhook payload template for a network

    Get the webhook payload template for a network

    :param network_id: 
    :type network_id: str
    :param payload_template_id: 
    :type payload_template_id: str

    """
    return web.Response(status=200)


async def get_network_webhooks_payload_templates_1(request: web.Request, network_id) -> web.Response:
    """List the webhook payload templates for a network

    List the webhook payload templates for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_webhooks_webhook_test_1(request: web.Request, network_id, webhook_test_id) -> web.Response:
    """Return the status of a webhook test for a network

    Return the status of a webhook test for a network

    :param network_id: 
    :type network_id: str
    :param webhook_test_id: 
    :type webhook_test_id: str

    """
    return web.Response(status=200)


async def get_organization_webhooks_alert_types_1(request: web.Request, organization_id, product_type=None) -> web.Response:
    """Return a list of alert types to be used with managing webhook alerts

    Return a list of alert types to be used with managing webhook alerts

    :param organization_id: 
    :type organization_id: str
    :param product_type: Filter sample alerts to a specific product type
    :type product_type: str

    """
    return web.Response(status=200)


async def get_organization_webhooks_logs_1(request: web.Request, organization_id, t0=None, t1=None, timespan=None, per_page=None, starting_after=None, ending_before=None, url=None) -> web.Response:
    """Return the log of webhook POSTs sent

    Return the log of webhook POSTs sent

    :param organization_id: 
    :type organization_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 90 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param url: The URL the webhook was sent to
    :type url: str

    """
    return web.Response(status=200)


async def update_network_webhooks_http_server_1(request: web.Request, network_id, http_server_id, body=None) -> web.Response:
    """Update an HTTP server

    Update an HTTP server. To change a URL, create a new HTTP server.

    :param network_id: 
    :type network_id: str
    :param http_server_id: 
    :type http_server_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWebhooksHttpServerRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_webhooks_payload_template_1(request: web.Request, network_id, payload_template_id, body=None) -> web.Response:
    """Update a webhook payload template for a network

    Update a webhook payload template for a network

    :param network_id: 
    :type network_id: str
    :param payload_template_id: 
    :type payload_template_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWebhooksPayloadTemplateRequest.from_dict(body)
    return web.Response(status=200)
