from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_to_batch_request_body import AddToBatchRequestBody
from openapi_server.models.batch_status import BatchStatus
from openapi_server.models.batches_sort_by import BatchesSortBy
from openapi_server.models.create_batch_request_body import CreateBatchRequestBody
from openapi_server.models.create_batch_response_body import CreateBatchResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_batch_by_external_id_response_body import GetBatchByExternalIdResponseBody
from openapi_server.models.get_batch_by_id_response_body import GetBatchByIdResponseBody
from openapi_server.models.list_batch_errors_response_body import ListBatchErrorsResponseBody
from openapi_server.models.list_batches_response_body import ListBatchesResponseBody
from openapi_server.models.process_batch_request_body import ProcessBatchRequestBody
from openapi_server.models.remove_from_batch_request_body import RemoveFromBatchRequestBody
from openapi_server.models.sort_dir import SortDir
from openapi_server import util


async def add_to_batch(request: web.Request, batch_id, body) -> web.Response:
    """Add to a Batch

    Add a Shipment or Rate to a Batch

    :param batch_id: Batch ID
    :type batch_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddToBatchRequestBody.from_dict(body)
    return web.Response(status=200)


async def create_batch(request: web.Request, body) -> web.Response:
    """Create A Batch

    Create a Batch

    :param body: 
    :type body: dict | bytes

    """
    body = CreateBatchRequestBody.from_dict(body)
    return web.Response(status=200)


async def delete_batch(request: web.Request, batch_id) -> web.Response:
    """Delete Batch By Id

    Delete Batch By Id

    :param batch_id: Batch ID
    :type batch_id: str

    """
    return web.Response(status=200)


async def get_batch_by_external_id(request: web.Request, external_batch_id) -> web.Response:
    """Get Batch By External ID

    Get Batch By External ID

    :param external_batch_id: 
    :type external_batch_id: str

    """
    return web.Response(status=200)


async def get_batch_by_id(request: web.Request, batch_id) -> web.Response:
    """Get Batch By ID

    Get Batch By ID

    :param batch_id: Batch ID
    :type batch_id: str

    """
    return web.Response(status=200)


async def list_batch_errors(request: web.Request, batch_id, page=None, pagesize=None) -> web.Response:
    """Get Batch Errors

    Error handling in batches are handled differently than in a single synchronous request. You must retrieve the status of your batch by [getting a batch](https://www.shipengine.com/docs/reference/get-batch-by-id/) and getting an overview of the statuses or you can list errors directly here below to get detailed information about the errors. 

    :param batch_id: Batch ID
    :type batch_id: str
    :param page: Return a specific page of results. Defaults to the first page. If set to a number that&#39;s greater than the number of pages of results, an empty page is returned. 
    :type page: int
    :param pagesize: 
    :type pagesize: int

    """
    return web.Response(status=200)


async def list_batches(request: web.Request, status=None, page=None, page_size=None, sort_dir=None, batch_number=None, sort_by=None) -> web.Response:
    """List Batches

    List Batches associated with your Shipengine account

    :param status: 
    :type status: dict | bytes
    :param page: Return a specific page of results. Defaults to the first page. If set to a number that&#39;s greater than the number of pages of results, an empty page is returned. 
    :type page: int
    :param page_size: The number of results to return per response.
    :type page_size: int
    :param sort_dir: Controls the sort order of the query.
    :type sort_dir: dict | bytes
    :param batch_number: Batch Number
    :type batch_number: str
    :param sort_by: 
    :type sort_by: dict | bytes

    """
    status = .from_dict(status)
    sort_dir = .from_dict(sort_dir)
    sort_by = .from_dict(sort_by)
    return web.Response(status=200)


async def process_batch(request: web.Request, batch_id, body) -> web.Response:
    """Process Batch ID Labels

    Process Batch ID Labels

    :param batch_id: Batch ID
    :type batch_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ProcessBatchRequestBody.from_dict(body)
    return web.Response(status=200)


async def remove_from_batch(request: web.Request, batch_id, body) -> web.Response:
    """Remove From Batch

    Remove a shipment or rate from a batch

    :param batch_id: Batch ID
    :type batch_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveFromBatchRequestBody.from_dict(body)
    return web.Response(status=200)


async def update_batch(request: web.Request, batch_id) -> web.Response:
    """Update Batch By Id

    Update Batch By Id

    :param batch_id: Batch ID
    :type batch_id: str

    """
    return web.Response(status=200)
