from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_response import AccountResponse
from openapi_server.models.link_application403_response import LinkApplication403Response
from openapi_server.models.link_application409_response import LinkApplication409Response
from openapi_server.models.link_application_request import LinkApplicationRequest
from openapi_server.models.model401_response import Model401Response
from openapi_server.models.unli_without_applicationnk_application403_response import UnliWithoutApplicationnkApplication403Response
from openapi_server.models.unli_without_applicationnk_application409_response import UnliWithoutApplicationnkApplication409Response
from openapi_server import util


async def link_application(request: web.Request, provider, external_id, body) -> web.Response:
    """Link application to an account

    

    :param provider: Provider of the account you want to assign an application to
    :type provider: str
    :param external_id: External id of the account you want to assign an application to. This is channel dependent. For Facebook it will be your Facebook Page ID, for Viber your Viber Service Message ID and for WhatsApp your WhatsApp number.
    :type external_id: str
    :param body: Request body can contain any of the following. Please note, the only one application can be linked to the account.
    :type body: dict | bytes

    """
    body = LinkApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def unli_without_applicationnk_application(request: web.Request, provider, external_id, application_id) -> web.Response:
    """Unlink application from an account

    

    :param provider: Provider of the account you want to unlink an application from
    :type provider: str
    :param external_id: External id of the account you want to unlink an application from
    :type external_id: str
    :param application_id: Id of the application you want to unlink
    :type application_id: str

    """
    return web.Response(status=200)
