from typing import List, Dict
from aiohttp import web

from openapi_server.models.webhook_test_entity import WebhookTestEntity
from openapi_server import util


async def post_webhook_tests(request: web.Request, url, action=None, body=None, encoding=None, file_as_body=None, file_form_field=None, headers=None, method=None, raw_body=None) -> web.Response:
    """Create Webhook Test

    Create Webhook Test

    :param url: URL for testing the webhook.
    :type url: str
    :param action: action for test body
    :type action: str
    :param body: Additional body parameters.
    :type body: dict | bytes
    :param encoding: HTTP encoding method.  Can be JSON, XML, or RAW (form data).
    :type encoding: str
    :param file_as_body: Send the file data as the request body?
    :type file_as_body: bool
    :param file_form_field: Send the file data as a named parameter in the request POST body
    :type file_form_field: str
    :param headers: Additional request headers.
    :type headers: dict | bytes
    :param method: HTTP method(GET or POST).
    :type method: str
    :param raw_body: raw body text
    :type raw_body: str

    """
    body = object.from_dict(body)
    headers = object.from_dict(headers)
    return web.Response(status=200)
