from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_error import BatchError
from openapi_server.models.compute_node import ComputeNode
from openapi_server.models.compute_node_list_result import ComputeNodeListResult
from openapi_server.models.compute_node_user import ComputeNodeUser
from openapi_server.models.node_disable_scheduling_parameter import NodeDisableSchedulingParameter
from openapi_server.models.node_reboot_parameter import NodeRebootParameter
from openapi_server.models.node_reimage_parameter import NodeReimageParameter
from openapi_server.models.node_remove_parameter import NodeRemoveParameter
from openapi_server.models.node_update_user_parameter import NodeUpdateUserParameter
from openapi_server import util


async def compute_node_add_user(request: web.Request, pool_id, node_id, api_version, body, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """compute_node_add_user

    Adds a user account to the specified compute node.

    :param pool_id: The id of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The id of the machine on which you want to create a user account.
    :type node_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param body: Specifies the user account to be created.
    :type body: dict | bytes
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    body = ComputeNodeUser.from_dict(body)
    return web.Response(status=200)


async def compute_node_delete_user(request: web.Request, pool_id, node_id, user_name, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """compute_node_delete_user

    Deletes a user account from the specified compute node.

    :param pool_id: The id of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The id of the machine on which you want to delete a user account.
    :type node_id: str
    :param user_name: The name of the user account to delete.
    :type user_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def compute_node_disable_scheduling(request: web.Request, pool_id, node_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, body=None) -> web.Response:
    """compute_node_disable_scheduling

    Disable task scheduling of the specified compute node.

    :param pool_id: The id of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The id of the compute node that you want to disable task scheduling.
    :type node_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param body: The parameters for the request.
    :type body: dict | bytes

    """
    body = NodeDisableSchedulingParameter.from_dict(body)
    return web.Response(status=200)


async def compute_node_enable_scheduling(request: web.Request, pool_id, node_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """compute_node_enable_scheduling

    Enable task scheduling of the specified compute node.

    :param pool_id: The id of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The id of the compute node that you want to enable task scheduling.
    :type node_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def compute_node_get(request: web.Request, pool_id, node_id, api_version, select=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """compute_node_get

    Gets information about the specified compute node.

    :param pool_id: The id of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The id of the compute node that you want to get information about.
    :type node_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param select: Sets an OData $select clause.
    :type select: str
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def compute_node_get_remote_desktop(request: web.Request, pool_id, node_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """compute_node_get_remote_desktop

    Gets the Remote Desktop Protocol file for the specified compute node.

    :param pool_id: The id of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The id of the compute node for which you want to get the Remote Desktop Protocol file.
    :type node_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def compute_node_list(request: web.Request, pool_id, api_version, filter=None, select=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """compute_node_list

    Lists the compute nodes in the specified pool.

    :param pool_id: The id of the pool from which you want to list nodes.
    :type pool_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: Sets an OData $filter clause.
    :type filter: str
    :param select: Sets an OData $select clause.
    :type select: str
    :param maxresults: Sets the maximum number of items to return in the response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def compute_node_reboot(request: web.Request, pool_id, node_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, body=None) -> web.Response:
    """compute_node_reboot

    Restarts the specified compute node.

    :param pool_id: The id of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The id of the compute node that you want to restart.
    :type node_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param body: The parameters for the request.
    :type body: dict | bytes

    """
    body = NodeRebootParameter.from_dict(body)
    return web.Response(status=200)


async def compute_node_reimage(request: web.Request, pool_id, node_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, body=None) -> web.Response:
    """compute_node_reimage

    Reinstalls the operating system on the specified compute node.

    :param pool_id: The id of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The id of the compute node that you want to restart.
    :type node_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param body: The parameters for the request.
    :type body: dict | bytes

    """
    body = NodeReimageParameter.from_dict(body)
    return web.Response(status=200)


async def compute_node_update_user(request: web.Request, pool_id, node_id, user_name, api_version, body, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """compute_node_update_user

    Updates the password or expiration time of a user account on the specified compute node.

    :param pool_id: The id of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The id of the machine on which you want to update a user account.
    :type node_id: str
    :param user_name: The name of the user account to update.
    :type user_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param body: The parameters for the request.
    :type body: dict | bytes
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    body = NodeUpdateUserParameter.from_dict(body)
    return web.Response(status=200)


async def pool_remove_nodes(request: web.Request, pool_id, api_version, body, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """pool_remove_nodes

    Removes compute nodes from the specified pool.

    :param pool_id: The id of the pool from which you want to remove nodes.
    :type pool_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param body: The parameters for the request.
    :type body: dict | bytes
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param if_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified.
    :type if_match: str
    :param if_none_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag.
    :type if_none_match: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str

    """
    body = NodeRemoveParameter.from_dict(body)
    return web.Response(status=200)
