from typing import List, Dict
from aiohttp import web

from openapi_server.models.webhooks import Webhooks
from openapi_server.models.webhooks_active import WebhooksActive
from openapi_server.models.webhooks_callback_url import WebhooksCallbackURL
from openapi_server.models.webhooks_description import WebhooksDescription
from openapi_server.models.webhooks_id_model import WebhooksIdModel
from openapi_server import util


async def add_webhooks(request: web.Request, key, token, body) -> web.Response:
    """addWebhooks()

    

    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Webhooks\&quot; to be added.
    :type body: dict | bytes

    """
    body = Webhooks.from_dict(body)
    return web.Response(status=200)


async def delete_webhooks_by_id_webhook(request: web.Request, id_webhook, key, token) -> web.Response:
    """deleteWebhooksByIdWebhook()

    

    :param id_webhook: idWebhook
    :type id_webhook: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_webhooks_by_id_webhook(request: web.Request, id_webhook, key, token) -> web.Response:
    """getWebhooksByIdWebhook()

    

    :param id_webhook: idWebhook
    :type id_webhook: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def get_webhooks_by_id_webhook_by_field(request: web.Request, id_webhook, _field, key, token) -> web.Response:
    """getWebhooksByIdWebhookByField()

    

    :param id_webhook: idWebhook
    :type id_webhook: str
    :param _field: field
    :type _field: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str

    """
    return web.Response(status=200)


async def update_webhooks(request: web.Request, key, token, body) -> web.Response:
    """updateWebhooks()

    

    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Webhooks\&quot; to be updated.
    :type body: dict | bytes

    """
    body = Webhooks.from_dict(body)
    return web.Response(status=200)


async def update_webhooks_active_by_id_webhook(request: web.Request, id_webhook, key, token, body) -> web.Response:
    """updateWebhooksActiveByIdWebhook()

    

    :param id_webhook: idWebhook
    :type id_webhook: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Webhooks Active\&quot; to be updated.
    :type body: dict | bytes

    """
    body = WebhooksActive.from_dict(body)
    return web.Response(status=200)


async def update_webhooks_by_id_webhook(request: web.Request, id_webhook, key, token, body) -> web.Response:
    """updateWebhooksByIdWebhook()

    

    :param id_webhook: idWebhook
    :type id_webhook: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Webhooks\&quot; to be updated.
    :type body: dict | bytes

    """
    body = Webhooks.from_dict(body)
    return web.Response(status=200)


async def update_webhooks_callback_urlby_id_webhook(request: web.Request, id_webhook, key, token, body) -> web.Response:
    """updateWebhooksCallbackURLByIdWebhook()

    

    :param id_webhook: idWebhook
    :type id_webhook: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Webhooks Callback Url\&quot; to be updated.
    :type body: dict | bytes

    """
    body = WebhooksCallbackURL.from_dict(body)
    return web.Response(status=200)


async def update_webhooks_description_by_id_webhook(request: web.Request, id_webhook, key, token, body) -> web.Response:
    """updateWebhooksDescriptionByIdWebhook()

    

    :param id_webhook: idWebhook
    :type id_webhook: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Webhooks Description\&quot; to be updated.
    :type body: dict | bytes

    """
    body = WebhooksDescription.from_dict(body)
    return web.Response(status=200)


async def update_webhooks_id_model_by_id_webhook(request: web.Request, id_webhook, key, token, body) -> web.Response:
    """updateWebhooksIdModelByIdWebhook()

    

    :param id_webhook: idWebhook
    :type id_webhook: str
    :param key: &lt;a href&#x3D;\&quot;https://trello.com/1/appKey/generate\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Generate your application key&lt;/a&gt;
    :type key: str
    :param token: &lt;a href&#x3D;\&quot;https://trello.com/docs/gettingstarted/index.html#getting-a-token-from-a-user\&quot;  target&#x3D;\&quot;_blank\&quot;&gt;Getting a token from a user&lt;/a&gt;
    :type token: str
    :param body: Attributes of \&quot;Webhooks Id Model\&quot; to be updated.
    :type body: dict | bytes

    """
    body = WebhooksIdModel.from_dict(body)
    return web.Response(status=200)
