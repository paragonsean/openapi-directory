from typing import List, Dict
from aiohttp import web

from openapi_server.models.container_for_registered_webhooks import ContainerForRegisteredWebhooks
from openapi_server.models.container_for_webhook_ids import ContainerForWebhookIDs
from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.failed_webhooks import FailedWebhooks
from openapi_server.models.page_bean_webhook import PageBeanWebhook
from openapi_server.models.webhook_registration_details import WebhookRegistrationDetails
from openapi_server.models.webhooks_expiration_date import WebhooksExpirationDate
from openapi_server import util


async def delete_webhook_by_id(request: web.Request, body) -> web.Response:
    """Delete webhooks by ID

    Removes webhooks by ID. Only webhooks registered by the calling app are removed. If webhooks created by other apps are specified, they are ignored.  **[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.

    :param body: 
    :type body: dict | bytes

    """
    body = ContainerForWebhookIDs.from_dict(body)
    return web.Response(status=200)


async def get_dynamic_webhooks_for_app(request: web.Request, start_at=None, max_results=None) -> web.Response:
    """Get dynamic webhooks for app

    Returns a [paginated](#pagination) list of the webhooks registered by the calling app.  **[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.

    :param start_at: The index of the first item to return in a page of results (page offset).
    :type start_at: int
    :param max_results: The maximum number of items to return per page.
    :type max_results: int

    """
    return web.Response(status=200)


async def get_failed_webhooks(request: web.Request, max_results=None, after=None) -> web.Response:
    """Get failed webhooks

    Returns webhooks that have recently failed to be delivered to the requesting app after the maximum number of retries.  After 72 hours the failure may no longer be returned by this operation.  The oldest failure is returned first.  This method uses a cursor-based pagination. To request the next page use the failure time of the last webhook on the list as the &#x60;failedAfter&#x60; value or use the URL provided in &#x60;next&#x60;.  **[Permissions](#permissions) required:** Only [Connect apps](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) can use this operation.

    :param max_results: The maximum number of webhooks to return per page. If obeying the maxResults directive would result in records with the same failure time being split across pages, the directive is ignored and all records with the same failure time included on the page.
    :type max_results: int
    :param after: The time after which any webhook failure must have occurred for the record to be returned, expressed as milliseconds since the UNIX epoch.
    :type after: int

    """
    return web.Response(status=200)


async def refresh_webhooks(request: web.Request, body) -> web.Response:
    """Extend webhook life

    Extends the life of webhook. Webhooks registered through the REST API expire after 30 days. Call this operation to keep them alive.  Unrecognized webhook IDs (those that are not found or belong to other apps) are ignored.  **[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.

    :param body: 
    :type body: dict | bytes

    """
    body = ContainerForWebhookIDs.from_dict(body)
    return web.Response(status=200)


async def register_dynamic_webhooks(request: web.Request, body) -> web.Response:
    """Register dynamic webhooks

    Registers webhooks.  **NOTE:** for non-public OAuth apps, webhooks are delivered only if there is a match between the app owner and the user who registered a dynamic webhook.  **[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.

    :param body: 
    :type body: dict | bytes

    """
    body = WebhookRegistrationDetails.from_dict(body)
    return web.Response(status=200)
