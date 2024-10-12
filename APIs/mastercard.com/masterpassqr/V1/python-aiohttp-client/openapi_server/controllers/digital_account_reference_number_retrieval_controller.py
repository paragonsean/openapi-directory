from typing import List, Dict
from aiohttp import web

from openapi_server.models.digital_account89_wrapper import DigitalAccount89Wrapper
from openapi_server.models.digital_account90_wrapper import DigitalAccount90Wrapper
from openapi_server import util


async def retrieve_digital_accnt_ref_num_list(request: web.Request, partner_id, digital_account=None) -> web.Response:
    """Used to retreive a digital account reference list from Incontrol 

    Used to retreive a digital account reference list from Incontrol 

    :param partner_id: Path Param - Provider assigned partner id. Details - string, 32
    :type partner_id: str
    :param digital_account: Contains the details of the request message.
    :type digital_account: dict | bytes

    """
    digital_account = DigitalAccount89Wrapper.from_dict(digital_account)
    return web.Response(status=200)
