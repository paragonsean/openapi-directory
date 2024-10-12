from typing import List, Dict
from aiohttp import web

from openapi_server.models.standard_postmark_response import StandardPostmarkResponse
from openapi_server.models.templates_push_model import TemplatesPushModel
from openapi_server.models.templates_push_response import TemplatesPushResponse
from openapi_server import util


async def push_templates(request: web.Request, x_postmark_account_token, body) -> web.Response:
    """Push templates from one server to another

    

    :param x_postmark_account_token: The token associated with the Account on which this request will operate.
    :type x_postmark_account_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = TemplatesPushModel.from_dict(body)
    return web.Response(status=200)
