from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_webhook_request_body import AddWebhookRequestBody
from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.update_webhook_request_body import UpdateWebhookRequestBody
from openapi_server.models.webhook_collection_response import WebhookCollectionResponse
from openapi_server.models.webhook_response import WebhookResponse
from openapi_server import util


async def add_webhook(request: web.Request, ev_api_key, ev_access_token, body=None) -> web.Response:
    """Add A New Webhook

    Create a new Webhook on your account. Creating a Webhook will require an endpoint URL, a path, what events should trigger a webhook, and what request version to use. 

    :param ev_api_key: API key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddWebhookRequestBody.from_dict(body)
    return web.Response(status=200)


async def delete_webhook(request: web.Request, id, ev_api_key, ev_access_token) -> web.Response:
    """Delete a webhook

    Deleted the specified webhook. This will not affect logs or any resources the webhook is connected to. 

    :param id: Webhook endpoint ID
    :type id: int
    :param ev_api_key: API key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str

    """
    return web.Response(status=200)


async def get_webhook_by_id(request: web.Request, id, ev_api_key, ev_access_token, include=None) -> web.Response:
    """Get info for a webhook

    Returns the metadata for a specific webhook. Webhook IDs can be retrieve from GET /webhooks

    :param id: Webhook endpoint ID
    :type id: int
    :param ev_api_key: API key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param include:  Include metadata for related items; &#x60;ownerAccount&#x60; and/or &#x60;resource&#x60; 
    :type include: str

    """
    return web.Response(status=200)


async def get_wehooks_list(request: web.Request, ev_api_key, ev_access_token, include=None, offset=None, limit=None) -> web.Response:
    """Get Webhooks List

    Returns a list of Webhooks. By default, this will return metadata on all Webhooks within the account. 

    :param ev_api_key: API key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param include: List of related record types to include. Valid options are &#x60;owningAccount&#x60; and &#x60;resource&#x60;
    :type include: str
    :param offset: Records to skip before returning results.
    :type offset: int
    :param limit: Limit of the records list
    :type limit: int

    """
    return web.Response(status=200)


async def regenerate_webhook_token(request: web.Request, id, ev_api_key, ev_access_token) -> web.Response:
    """Regenerate security token

    This endpoint will allow you to regenerate the security token for a webhook if you believe it’s been compromised in any way. 

    :param id: Webhook ID
    :type id: str
    :param ev_api_key: API key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str

    """
    return web.Response(status=200)


async def resend_webhook_activity_entry(request: web.Request, activity_id, ev_api_key, ev_access_token) -> web.Response:
    """Resend a webhook message

    This endpoint will allow you to resend a webhook that was previously sent. Resent webhooks will send exactly the same as the original webhook with the exception of the “sent” timestamp. Activity IDs can be retrieve from the webhook logs in your account or via GET /activity/webhooks

    :param activity_id: Webhooks activity entry ID
    :type activity_id: str
    :param ev_api_key: API key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str

    """
    return web.Response(status=200)


async def update_webhook(request: web.Request, id, ev_api_key, ev_access_token, body=None) -> web.Response:
    """Update a webhook

    Update the specified webhook. Updated webhooks will take effect immediately and could impact active workflows. Please be certain the webhook is not currently in use prior to updating.   You only need to send the portions of the webhook configuration you wish to change, rather than the entire webhook object.

    :param id: Webhook endpoint ID
    :type id: int
    :param ev_api_key: API key required to make the API call.
    :type ev_api_key: str
    :param ev_access_token: Access token required to make the API call.
    :type ev_access_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateWebhookRequestBody.from_dict(body)
    return web.Response(status=200)
