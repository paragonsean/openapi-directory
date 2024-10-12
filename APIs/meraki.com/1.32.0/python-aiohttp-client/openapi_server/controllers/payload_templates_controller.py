from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_webhooks_payload_template_request import CreateNetworkWebhooksPayloadTemplateRequest
from openapi_server.models.get_network_webhooks_payload_templates200_response_inner import GetNetworkWebhooksPayloadTemplates200ResponseInner
from openapi_server.models.update_network_webhooks_payload_template_request import UpdateNetworkWebhooksPayloadTemplateRequest
from openapi_server import util


async def create_network_webhooks_payload_template_2(request: web.Request, network_id, body) -> web.Response:
    """Create a webhook payload template for a network

    Create a webhook payload template for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkWebhooksPayloadTemplateRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_webhooks_payload_template_2(request: web.Request, network_id, payload_template_id) -> web.Response:
    """Destroy a webhook payload template for a network

    Destroy a webhook payload template for a network. Does not work for included templates (&#39;wpt_00001&#39;, &#39;wpt_00002&#39;, &#39;wpt_00003&#39;, &#39;wpt_00004&#39;, &#39;wpt_00005&#39; or &#39;wpt_00006&#39;)

    :param network_id: 
    :type network_id: str
    :param payload_template_id: 
    :type payload_template_id: str

    """
    return web.Response(status=200)


async def get_network_webhooks_payload_template_2(request: web.Request, network_id, payload_template_id) -> web.Response:
    """Get the webhook payload template for a network

    Get the webhook payload template for a network

    :param network_id: 
    :type network_id: str
    :param payload_template_id: 
    :type payload_template_id: str

    """
    return web.Response(status=200)


async def get_network_webhooks_payload_templates_2(request: web.Request, network_id) -> web.Response:
    """List the webhook payload templates for a network

    List the webhook payload templates for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_webhooks_payload_template_2(request: web.Request, network_id, payload_template_id, body=None) -> web.Response:
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
