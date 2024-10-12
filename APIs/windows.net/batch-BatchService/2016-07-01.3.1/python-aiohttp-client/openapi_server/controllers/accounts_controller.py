from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_list_node_agent_skus_result import AccountListNodeAgentSkusResult
from openapi_server.models.batch_error import BatchError
from openapi_server import util


async def account_list_node_agent_skus(request: web.Request, api_version, filter=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Lists all node agent SKUs supported by the Azure Batch service.

    

    :param api_version: Client API Version.
    :type api_version: str
    :param filter: An OData $filter clause.
    :type filter: str
    :param maxresults: The maximum number of items to return in the response. A maximum of 1000 results will be returned.
    :type maxresults: int
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)
