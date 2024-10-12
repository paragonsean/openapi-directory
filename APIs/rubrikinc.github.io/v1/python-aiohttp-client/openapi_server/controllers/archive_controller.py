from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.reader_refresh_data_sources_request import ReaderRefreshDataSourcesRequest
from openapi_server.models.string_response import StringResponse
from openapi_server import util


async def disable_archival_location(request: web.Request, id) -> web.Response:
    """Disable location for archival and modification operations

    Disables archiving and any changes to the data for the specified archival location. This operation disables snapshot upload, snapshot expiration, consolidation, and garbage collection operations on the archival location. 

    :param id: ID assigned to an archival location object.
    :type id: str

    """
    return web.Response(status=200)


async def enable_archival_location(request: web.Request, id) -> web.Response:
    """Enable archival location for archival and modification operations

    Enable archiving and other operations that were previously disabled on the specified archival location. 

    :param id: ID assigned to an archival location object.
    :type id: str

    """
    return web.Response(status=200)


async def get_aws_account_id(request: web.Request, id) -> web.Response:
    """Get the AWS account ID of an AWS S3 archival location

    Get the AWS account ID of an AWS S3 archival location.

    :param id: ID of an AWS archival location that uses the S3 protocol.
    :type id: str

    """
    return web.Response(status=200)


async def refresh_archival_location_data_sources(request: web.Request, location_id, body) -> web.Response:
    """Refresh archive information for a list of data sources

    Update the current Rubrik CDM cluster with information about the changes made to a list of data sources in an archival location by the Rubrik CDM cluster that owns the archival location. 

    :param location_id: ID assigned to an archival location object.
    :type location_id: str
    :param body: A set of local and archival IDs for data sources to refresh. For a data source, either a local or archival data source ID should be specified. The operation will fail if &#x60;none&#x60; is specified. 
    :type body: dict | bytes

    """
    body = ReaderRefreshDataSourcesRequest.from_dict(body)
    return web.Response(status=200)
