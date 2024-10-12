from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_funding_account_request_v2 import CreateFundingAccountRequestV2
from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.inline_response409 import InlineResponse409
from openapi_server import util


async def create_funding_account_v2(request: web.Request, body=None) -> web.Response:
    """Create Funding Account

    Create Funding Account

    :param body: 
    :type body: dict | bytes

    """
    body = CreateFundingAccountRequestV2.from_dict(body)
    return web.Response(status=200)


async def delete_source_account_v3(request: web.Request, source_account_id) -> web.Response:
    """Delete a source account by ID

    Mark a source account as deleted by ID

    :param source_account_id: Source account id
    :type source_account_id: str
    :type source_account_id: str

    """
    return web.Response(status=200)
