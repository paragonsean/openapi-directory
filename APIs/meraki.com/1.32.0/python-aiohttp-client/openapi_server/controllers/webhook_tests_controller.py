from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_webhooks_webhook_test201_response import CreateNetworkWebhooksWebhookTest201Response
from openapi_server.models.create_network_webhooks_webhook_test_request import CreateNetworkWebhooksWebhookTestRequest
from openapi_server import util


async def create_network_webhooks_webhook_test_2(request: web.Request, network_id, body) -> web.Response:
    """Send a test webhook for a network

    Send a test webhook for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkWebhooksWebhookTestRequest.from_dict(body)
    return web.Response(status=200)


async def get_network_webhooks_webhook_test_2(request: web.Request, network_id, webhook_test_id) -> web.Response:
    """Return the status of a webhook test for a network

    Return the status of a webhook test for a network

    :param network_id: 
    :type network_id: str
    :param webhook_test_id: 
    :type webhook_test_id: str

    """
    return web.Response(status=200)
