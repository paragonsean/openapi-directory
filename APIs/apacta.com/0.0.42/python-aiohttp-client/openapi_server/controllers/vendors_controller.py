from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_vendor_request import AddVendorRequest
from openapi_server.models.clocking_records_clocking_record_id_delete200_response import ClockingRecordsClockingRecordIdDelete200Response
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.get_vendor200_response import GetVendor200Response
from openapi_server.models.get_vendors_list200_response import GetVendorsList200Response
from openapi_server import util


async def add_vendor(request: web.Request, body=None) -> web.Response:
    """Add a new vendor

    

    :param body: 
    :type body: dict | bytes

    """
    body = AddVendorRequest.from_dict(body)
    return web.Response(status=200)


async def edit_vendor(request: web.Request, vendor_id, body=None) -> web.Response:
    """Edit a vendor

    

    :param vendor_id: 
    :type vendor_id: str
    :type vendor_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddVendorRequest.from_dict(body)
    return web.Response(status=200)


async def get_vendor(request: web.Request, vendor_id) -> web.Response:
    """Get a vendor

    

    :param vendor_id: 
    :type vendor_id: str

    """
    return web.Response(status=200)


async def get_vendors_list(request: web.Request, with_custom=None, email=None, name=None, cvr=None) -> web.Response:
    """Get a list of vendors

    

    :param with_custom: 
    :type with_custom: bool
    :param email: 
    :type email: str
    :param name: 
    :type name: str
    :param cvr: 
    :type cvr: str

    """
    return web.Response(status=200)


async def vendors_vendor_id_delete(request: web.Request, vendor_id) -> web.Response:
    """Delete a vendor

    

    :param vendor_id: 
    :type vendor_id: str

    """
    return web.Response(status=200)
