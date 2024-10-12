from typing import List, Dict
from aiohttp import web

from openapi_server.models.direct_debit import DirectDebit
from openapi_server.models.direct_debits import DirectDebits
from openapi_server.models.mandate import Mandate
from openapi_server.models.mandates import Mandates
from openapi_server import util


async def activate_mandate(request: web.Request, mandate_uuid) -> web.Response:
    """Activate a direct debit mandate

    This endpoint can only be used to activate a direct debit mandate when it is in the status REJECT_REQUESTED (even if the account has direct debits disabled). This action will also enable the account for direct debits if it was previously set to be disabled. The permision needed to access this endpoint is PERM_BUSINESS_POST_MANDATE_ACTIVATE 

    :param mandate_uuid: 
    :type mandate_uuid: str

    """
    return web.Response(status=200)


async def cancel_mandate_by_uuid(request: web.Request, mandate_uuid) -> web.Response:
    """Cancel a direct debit mandate

    This endpoint allows you to cancel a direct debit mandate. The permision needed to access this endpoint is PERM_BUSINESS_POST_MANDATE_CANCEL 

    :param mandate_uuid: 
    :type mandate_uuid: str

    """
    return web.Response(status=200)


async def get_direct_debit_by_uuid(request: web.Request, direct_debit_uuid) -> web.Response:
    """Get the details of a direct debit

    Retrieve all details of a single direct debit collection/payment, whether successful or not. The permision needed to access this endpoint is **PERM_BUSINESS_GET_DIRECT_DEBIT** 

    :param direct_debit_uuid: 
    :type direct_debit_uuid: str

    """
    return web.Response(status=200)


async def get_direct_debit_mandates(request: web.Request, ) -> web.Response:
    """List all direct debit mandates

    The permision needed to access this endpoint is PERM_BUSINESS_GET_MANDATES 


    """
    return web.Response(status=200)


async def get_direct_debits_for_mandate_uuid(request: web.Request, mandate_uuid) -> web.Response:
    """Get all DD payments associated with a direct debit mandate

    Retrieve all direct debit payments associated with a direct debit mandate. The permision needed to access this endpoint is PERM_BUSINESS_GET_DIRECT_DEBITS 

    :param mandate_uuid: The mandate UUID to retrieve
    :type mandate_uuid: str

    """
    return web.Response(status=200)


async def get_mandate(request: web.Request, mandate_uuid) -> web.Response:
    """Get direct debit mandate details

    Retrieve all details for a direct debit mandate. The permision needed to access this endpoint is PERM_BUSINESS_GET_MANDATE 

    :param mandate_uuid: 
    :type mandate_uuid: str

    """
    return web.Response(status=200)


async def reject_direct_debit(request: web.Request, direct_debit_uuid) -> web.Response:
    """Reject a direct debit payment

    This endpoint allows you to reject a direct debit payment where the status is still set to RECEIVED. Permission name PERM_BUSINESS_POST_DIRECT_DEBIT_REJECT 

    :param direct_debit_uuid: 
    :type direct_debit_uuid: str

    """
    return web.Response(status=200)


async def update_mandate_alias(request: web.Request, mandate_uuid) -> web.Response:
    """Update a direct debit mandate alias

    Update Direct Debit Mandate Alias The permision needed to access this endpoint is PERM_BUSINESS_PUT_MANDATE 

    :param mandate_uuid: 
    :type mandate_uuid: str

    """
    return web.Response(status=200)
