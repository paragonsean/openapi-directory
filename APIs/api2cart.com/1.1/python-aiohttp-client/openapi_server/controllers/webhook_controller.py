from typing import List, Dict
from aiohttp import web

from openapi_server.models.attribute_add200_response import AttributeAdd200Response
from openapi_server.models.attribute_delete200_response import AttributeDelete200Response
from openapi_server.models.product_image_update200_response import ProductImageUpdate200Response
from openapi_server.models.webhook_count200_response import WebhookCount200Response
from openapi_server.models.webhook_events200_response import WebhookEvents200Response
from openapi_server.models.webhook_list200_response import WebhookList200Response
from openapi_server import util


async def webhook_count(request: web.Request, entity=None, action=None, active=None) -> web.Response:
    """webhook_count

    Count registered webhooks on the store.

    :param entity: The entity you want to filter webhooks by (e.g. order or product)
    :type entity: str
    :param action: The action you want to filter webhooks by (e.g. order or product)
    :type action: str
    :param active: The webhook status you want to filter webhooks by
    :type active: bool

    """
    return web.Response(status=200)


async def webhook_create(request: web.Request, entity, action, param_callback=None, label=None, fields=None, active=None, store_id=None) -> web.Response:
    """webhook_create

    Create webhook on the store and subscribe to it.

    :param entity: Specify the entity that you want to enable webhooks for (e.g product, order, customer, category)
    :type entity: str
    :param action: Specify what action (event) will trigger the webhook (e.g add, delete, or update)
    :type action: str
    :param param_callback: Callback url that returns shipping rates. It should be able to accept POST requests with json data.
    :type param_callback: str
    :param label: The name you give to the webhook
    :type label: str
    :param fields: Fields the webhook should send
    :type fields: str
    :param active: Webhook status
    :type active: bool
    :param store_id: Defines store id where the webhook should be assigned
    :type store_id: str

    """
    return web.Response(status=200)


async def webhook_delete(request: web.Request, id) -> web.Response:
    """webhook_delete

    Delete registered webhook on the store.

    :param id: Webhook id
    :type id: str

    """
    return web.Response(status=200)


async def webhook_events(request: web.Request, ) -> web.Response:
    """webhook_events

    List all Webhooks that are available on this store.


    """
    return web.Response(status=200)


async def webhook_list(request: web.Request, params=None, start=None, count=None, entity=None, action=None, active=None, ids=None) -> web.Response:
    """webhook_list

    List registered webhook on the store.

    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param entity: The entity you want to filter webhooks by (e.g. order or product)
    :type entity: str
    :param action: The action you want to filter webhooks by (e.g. add, update, or delete)
    :type action: str
    :param active: The webhook status you want to filter webhooks by
    :type active: bool
    :param ids: List of сomma-separated webhook ids
    :type ids: str

    """
    return web.Response(status=200)


async def webhook_update(request: web.Request, id, param_callback=None, label=None, fields=None, active=None) -> web.Response:
    """webhook_update

    Update Webhooks parameters.

    :param id: Webhook id
    :type id: str
    :param param_callback: Callback url that returns shipping rates. It should be able to accept POST requests with json data.
    :type param_callback: str
    :param label: The name you give to the webhook
    :type label: str
    :param fields: Fields the webhook should send
    :type fields: str
    :param active: Webhook status
    :type active: bool

    """
    return web.Response(status=200)
