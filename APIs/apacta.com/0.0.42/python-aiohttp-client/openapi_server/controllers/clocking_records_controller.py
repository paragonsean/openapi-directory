from typing import List, Dict
from aiohttp import web

from openapi_server.models.clocking_records_checkout_post201_response import ClockingRecordsCheckoutPost201Response
from openapi_server.models.clocking_records_clocking_record_id_delete200_response import ClockingRecordsClockingRecordIdDelete200Response
from openapi_server.models.clocking_records_clocking_record_id_get200_response import ClockingRecordsClockingRecordIdGet200Response
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_get200_response import ClockingRecordsGet200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.clocking_records_post_request import ClockingRecordsPostRequest
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server import util


async def clocking_records_checkout_post(request: web.Request, ) -> web.Response:
    """Checkout active clocking record for authenticated user

    


    """
    return web.Response(status=200)


async def clocking_records_clocking_record_id_delete(request: web.Request, clocking_record_id) -> web.Response:
    """Delete a clocking record

    

    :param clocking_record_id: 
    :type clocking_record_id: str

    """
    return web.Response(status=200)


async def clocking_records_clocking_record_id_get(request: web.Request, clocking_record_id) -> web.Response:
    """Details of 1 clocking_record

    

    :param clocking_record_id: 
    :type clocking_record_id: str

    """
    return web.Response(status=200)


async def clocking_records_clocking_record_id_put(request: web.Request, clocking_record_id) -> web.Response:
    """Edit a clocking record

    

    :param clocking_record_id: 
    :type clocking_record_id: str

    """
    return web.Response(status=200)


async def clocking_records_get(request: web.Request, active=None) -> web.Response:
    """Get a list of clocking records

    

    :param active: Used to search for active clocking records
    :type active: bool

    """
    return web.Response(status=200)


async def clocking_records_post(request: web.Request, body) -> web.Response:
    """Create clocking record for authenticated user

    

    :param body: 
    :type body: dict | bytes

    """
    body = ClockingRecordsPostRequest.from_dict(body)
    return web.Response(status=200)
