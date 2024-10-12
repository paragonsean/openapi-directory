from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_subscription import CreateSubscription
from openapi_server.models.subscribe_result import SubscribeResult
from openapi_server.models.webhook_list import WebhookList
from openapi_server import util


async def webhook_delete(request: web.Request, id) -> web.Response:
    """Delete Webhook Subscription by ID

    

    :param id: Subscription id to be deleted
    :type id: int

    """
    return web.Response(status=200)


async def webhook_delete_by_url(request: web.Request, target_url) -> web.Response:
    """Delete webhook subscription by URL

    

    :param target_url: Target URL that should be used to delete subscriptions
    :type target_url: str

    """
    return web.Response(status=200)


async def webhook_get(request: web.Request, ) -> web.Response:
    """Get list of Webhook Subscriptions

    


    """
    return web.Response(status=200)


async def webhook_get_by_id(request: web.Request, id) -> web.Response:
    """Get Webhook Subscription by SubscriptionID

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def webhook_post(request: web.Request, model) -> web.Response:
    """Subscribe to Webhook. On success, returns ID of webhook subscription.

    When you receive a webhook, you should respond with Http 200 OK Status Code, otherwise we will retry. To create a webhook, you need both the webhook_notifications scope, as well as the scope for the required entity being monitored.  Event values are: \&quot;company_created\&quot;, \&quot;company_deleted\&quot;, \&quot;company_updated\&quot;, \&quot;contact_created\&quot;, \&quot;contact_deleted\&quot;, \&quot;contact_updated\&quot;, \&quot;invoice_created\&quot;, \&quot;invoice_sent\&quot;,\&quot;invoice_updated\&quot;,\&quot;invoice_deleted\&quot;, \&quot;project_created\&quot;, \&quot;project_deleted\&quot;, \&quot;project_updated\&quot;, \&quot;task_created\&quot;, \&quot;task_updated\&quot;,\&quot;task_deleted\&quot;, \&quot;timesheet_created\&quot;, \&quot;timesheet_deleted\&quot;, \&quot;timesheet_updated, \&quot;bill_created\&quot;, \&quot;bill_updated\&quot;.  You can subscribe to any webhook, but you will only receive notifications for data appropriate to the roles of your user account. There is an optional  Secret parameter (string 255 char max). This allows for webhook authentication. If provided, the Secret will be BASE 64 encoded and passed with notications as a basic authentication http header. i.e. Authorization Basic [BASE64 of Secret]\&quot;

    :param model: 
    :type model: dict | bytes

    """
    model = CreateSubscription.from_dict(model)
    return web.Response(status=200)
