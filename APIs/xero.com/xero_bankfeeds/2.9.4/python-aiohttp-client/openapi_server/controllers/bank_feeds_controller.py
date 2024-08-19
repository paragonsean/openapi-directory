from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.feed_connection import FeedConnection
from openapi_server.models.feed_connections import FeedConnections
from openapi_server.models.statement import Statement
from openapi_server.models.statements import Statements
from openapi_server import util


async def create_feed_connections(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Create one or more new feed connection

    By passing in the FeedConnections array object in the body, you can create one or more new feed connections

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: Feed Connection(s) array object in the body
    :type body: dict | bytes

    """
    body = FeedConnections.from_dict(body)
    return web.Response(status=200)


async def create_statements(request: web.Request, xero_tenant_id, body=None) -> web.Response:
    """Creates one or more new statements

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: Statements array of objects in the body
    :type body: dict | bytes

    """
    body = Statements.from_dict(body)
    return web.Response(status=200)


async def delete_feed_connections(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Delete an existing feed connection

    By passing in FeedConnections array object in the body, you can delete a feed connection.

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: Feed Connections array object in the body
    :type body: dict | bytes

    """
    body = FeedConnections.from_dict(body)
    return web.Response(status=200)


async def get_feed_connection(request: web.Request, xero_tenant_id, id) -> web.Response:
    """Retrieve single feed connection based on a unique id provided

    By passing in a FeedConnection Id options, you can search for matching feed connections

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param id: Unique identifier for retrieving single object
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def get_feed_connections(request: web.Request, xero_tenant_id, page=None, page_size=None) -> web.Response:
    """Searches for feed connections

    By passing in the appropriate options, you can search for available feed connections in the system.

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param page: Page number which specifies the set of records to retrieve. By default the number of the records per set is 10. Example - https://api.xero.com/bankfeeds.xro/1.0/FeedConnections?page&#x3D;1 to get the second set of the records. When page value is not a number or a negative number, by default, the first set of records is returned.
    :type page: int
    :param page_size: Page size which specifies how many records per page will be returned (default 10). Example - https://api.xero.com/bankfeeds.xro/1.0/FeedConnections?pageSize&#x3D;100 to specify page size of 100.
    :type page_size: int

    """
    return web.Response(status=200)


async def get_statement(request: web.Request, xero_tenant_id, statement_id, statement_id2) -> web.Response:
    """Retrieve single statement based on unique id provided

    By passing in a statement id, you can search for matching statements

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param statement_id: statement id for single object
    :type statement_id: str
    :type statement_id: str
    :param statement_id2: 
    :type statement_id2: str

    """
    return web.Response(status=200)


async def get_statements(request: web.Request, xero_tenant_id, page=None, page_size=None, xero_application_id=None, xero_user_id=None) -> web.Response:
    """Retrieve all statements

    By passing in parameters, you can search for matching statements

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param page: unique id for single object
    :type page: int
    :param page_size: Page size which specifies how many records per page will be returned (default 10). Example - https://api.xero.com/bankfeeds.xro/1.0/Statements?pageSize&#x3D;100 to specify page size of 100.
    :type page_size: int
    :param xero_application_id: 
    :type xero_application_id: str
    :param xero_user_id: 
    :type xero_user_id: str

    """
    return web.Response(status=200)
