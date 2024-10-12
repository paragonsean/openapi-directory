from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_companies_vendor_request import AddCompaniesVendorRequest
from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.clocking_records_clocking_record_id_delete200_response import ClockingRecordsClockingRecordIdDelete200Response
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.get_compaies_vendors_list200_response import GetCompaiesVendorsList200Response
from openapi_server.models.get_companies_vendor200_response import GetCompaniesVendor200Response
from openapi_server.models.get_companies_vendors_expense_statistics200_response import GetCompaniesVendorsExpenseStatistics200Response
from openapi_server import util


async def add_companies_vendor(request: web.Request, body=None) -> web.Response:
    """Add a new companies vendor

    

    :param body: 
    :type body: dict | bytes

    """
    body = AddCompaniesVendorRequest.from_dict(body)
    return web.Response(status=200)


async def bulk_companies_vendors(request: web.Request, body) -> web.Response:
    """Bulk delete companies vendors

    

    :param body: Companies vendors ids
    :type body: dict | bytes

    """
    body = BulkActionRequestBody.from_dict(body)
    return web.Response(status=200)


async def companies_vendors_companies_vendor_id_delete(request: web.Request, companies_vendor_id) -> web.Response:
    """Delete a companies vendor

    

    :param companies_vendor_id: 
    :type companies_vendor_id: str

    """
    return web.Response(status=200)


async def edit_companies_vendor(request: web.Request, companies_vendor_id, body=None) -> web.Response:
    """Edit a companies vendor

    

    :param companies_vendor_id: 
    :type companies_vendor_id: str
    :type companies_vendor_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddCompaniesVendorRequest.from_dict(body)
    return web.Response(status=200)


async def get_compaies_vendors_list(request: web.Request, ) -> web.Response:
    """Get a list of companies vendors

    


    """
    return web.Response(status=200)


async def get_companies_vendor(request: web.Request, companies_vendor_id) -> web.Response:
    """Get a companies vendor

    

    :param companies_vendor_id: 
    :type companies_vendor_id: str

    """
    return web.Response(status=200)


async def get_companies_vendors_expense_statistics(request: web.Request, companies_vendor_id) -> web.Response:
    """Get companies vendor expense statistics

    

    :param companies_vendor_id: 
    :type companies_vendor_id: str
    :type companies_vendor_id: str

    """
    return web.Response(status=200)
