from typing import List, Dict
from aiohttp import web

from openapi_server.models.email_with_template_request import EmailWithTemplateRequest
from openapi_server.models.send_email_request import SendEmailRequest
from openapi_server.models.send_email_response import SendEmailResponse
from openapi_server.models.send_email_templated_batch_request import SendEmailTemplatedBatchRequest
from openapi_server.models.standard_postmark_response import StandardPostmarkResponse
from openapi_server import util


async def send_email(request: web.Request, x_postmark_server_token, body=None) -> web.Response:
    """Send a single email

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = SendEmailRequest.from_dict(body)
    return web.Response(status=200)


async def send_email_batch(request: web.Request, x_postmark_server_token, body=None) -> web.Response:
    """Send a batch of emails

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param body: 
    :type body: list | bytes

    """
    body = [SendEmailRequest.from_dict(d) for d in body]
    return web.Response(status=200)


async def send_email_batch_with_templates(request: web.Request, x_postmark_server_token, body) -> web.Response:
    """Send a batch of email using templates.

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = SendEmailTemplatedBatchRequest.from_dict(body)
    return web.Response(status=200)


async def send_email_with_template(request: web.Request, x_postmark_server_token, body) -> web.Response:
    """Send an email using a Template

    

    :param x_postmark_server_token: The token associated with the Server on which this request will operate.
    :type x_postmark_server_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = EmailWithTemplateRequest.from_dict(body)
    return web.Response(status=200)
