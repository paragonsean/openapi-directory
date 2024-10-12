from typing import List, Dict
from aiohttp import web

from openapi_server.models.digital_account86_wrapper import DigitalAccount86Wrapper
from openapi_server.models.digital_account87_wrapper import DigitalAccount87Wrapper
from openapi_server import util


async def create_digital_accnt_ref_num(request: web.Request, partner_id, digital_account=None) -> web.Response:
    """Used to create a digital account reference number from Incontrol 

    Used to create a digital account reference number from Incontrol 

    :param partner_id: Path Param - Provider assigned partner id.   Type: Alphanumeric Special  [a-zA-Z0-9_-], Length: 32
    :type partner_id: str
    :param digital_account: Contains the details of the request message.
    :type digital_account: dict | bytes

    """
    digital_account = DigitalAccount86Wrapper.from_dict(digital_account)
    return web.Response(status=200)
