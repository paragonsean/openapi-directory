from typing import List, Dict
from aiohttp import web

from openapi_server.models.repowerreversal11_wrapper import Repowerreversal11Wrapper
from openapi_server.models.repowerreversalrequest10_wrapper import Repowerreversalrequest10Wrapper
from openapi_server import util


async def repower_reversal_post2(request: web.Request, repower_reversal_request=None) -> web.Response:
    """repower_reversal_post2

    A Transfer Reversal is a request to reverse a previously submitted Mastercard rePower Transfer, and is only available in extremely limited circumstances.  Reversal Processing : A rePower transaction reversal may be submitted in the event of a documented clerical error. The rePower transaction reversal must be submitted within 15 minutes of the time the original rePower transaction was authorized.  Use this resource to reverse a previously submitted rePower Transfer. 

    :param repower_reversal_request: Contains the details of the repower reversal request message.
    :type repower_reversal_request: dict | bytes

    """
    repower_reversal_request = Repowerreversalrequest10Wrapper.from_dict(repower_reversal_request)
    return web.Response(status=200)
