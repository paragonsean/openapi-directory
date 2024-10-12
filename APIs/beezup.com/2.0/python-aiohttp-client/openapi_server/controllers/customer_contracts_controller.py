from typing import List, Dict
from aiohttp import web

from openapi_server.models.beez_up_common_error_response_message import BeezUPCommonErrorResponseMessage
from openapi_server.models.billing_period_list import BillingPeriodList
from openapi_server.models.contracts import Contracts
from openapi_server.models.create_contract import CreateContract
from openapi_server.models.create_contract_response import CreateContractResponse
from openapi_server.models.offer import Offer
from openapi_server.models.offer_request import OfferRequest
from openapi_server.models.standard_offers import StandardOffers
from openapi_server.models.terminate_contract import TerminateContract
from openapi_server import util


async def create_contract(request: web.Request, body) -> web.Response:
    """Create a new contract

    Now you are ready to create your contract. Before that, please ensure that you check the offer with the same request parameterts. /offers 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateContract.from_dict(body)
    return web.Response(status=200)


async def delete_next_contract(request: web.Request, ) -> web.Response:
    """Delete your next contract

    


    """
    return web.Response(status=200)


async def get_billing_periods(request: web.Request, if_none_match=None) -> web.Response:
    """Get billing periods conditions

    

    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_contracts(request: web.Request, if_none_match=None) -> web.Response:
    """Get contract list

    

    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def get_offer(request: web.Request, body) -> web.Response:
    """Get offer pricing

    Get the offer pricing then you can create your contract with the same request parameters. /v2/user/customer/contracts 

    :param body: 
    :type body: dict | bytes

    """
    body = OfferRequest.from_dict(body)
    return web.Response(status=200)


async def get_standard_offers(request: web.Request, if_none_match=None) -> web.Response:
    """Get all standard offers

    

    :param if_none_match: ETag value to identify the last known version of requested resource.\\ To avoid useless exchange, we recommend you to indicate the ETag you previously got from this operation.\\ If the ETag value does not match the response will be 200 to give you a new content, otherwise the response will be: 304 Not Modified, without any content.\\ For more details go to this link: http://tools.ietf.org/html/rfc7232#section-2.3 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def reactivate_current_contract(request: web.Request, ) -> web.Response:
    """Reactivate your terminated contract.

    By calling this operation you can re-enable the auto renewal.


    """
    return web.Response(status=200)


async def terminate_current_contract(request: web.Request, body) -> web.Response:
    """Schedule termination of your current contract at the end of the commitment.

    By default your contract are automatically renew. By calling this operation you can disable the auto renewal.

    :param body: Indicate the termination reason
    :type body: dict | bytes

    """
    body = TerminateContract.from_dict(body)
    return web.Response(status=200)
