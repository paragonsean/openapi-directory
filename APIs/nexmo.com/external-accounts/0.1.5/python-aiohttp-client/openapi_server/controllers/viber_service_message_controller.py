from typing import List, Dict
from aiohttp import web

from openapi_server.models.model401_response import Model401Response
from openapi_server.models.vsm_account_response import VSMAccountResponse
from openapi_server import util


async def get_vsm_account(request: web.Request, external_id) -> web.Response:
    """Retrieve a Viber Service Message account

    

    :param external_id: External id of the account you want to retrieve. In this case it will be your Viber Service Message ID.
    :type external_id: str

    """
    return web.Response(status=200)
