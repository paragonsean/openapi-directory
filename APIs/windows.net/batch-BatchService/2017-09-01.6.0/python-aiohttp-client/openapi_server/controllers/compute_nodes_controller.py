from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_error import BatchError
from openapi_server.models.compute_node import ComputeNode
from openapi_server.models.compute_node_get_remote_login_settings_result import ComputeNodeGetRemoteLoginSettingsResult
from openapi_server.models.compute_node_list_result import ComputeNodeListResult
from openapi_server.models.compute_node_user import ComputeNodeUser
from openapi_server.models.node_disable_scheduling_parameter import NodeDisableSchedulingParameter
from openapi_server.models.node_reboot_parameter import NodeRebootParameter
from openapi_server.models.node_reimage_parameter import NodeReimageParameter
from openapi_server.models.node_remove_parameter import NodeRemoveParameter
from openapi_server.models.node_update_user_parameter import NodeUpdateUserParameter
from openapi_server import util


async def compute_node_add_user(request: web.Request, pool_id, node_id, api_version, user, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Adds a user account to the specified compute node.

    You can add a user account to a node only when it is in the idle or running state.

    :param pool_id: The ID of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The ID of the machine on which you want to create a user account.
    :type node_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param user: The user account to be created.
    :type user: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str

    """
    user = ComputeNodeUser.from_dict(user)
    return web.Response(status=200)


async def compute_node_delete_user(request: web.Request, pool_id, node_id, user_name, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Deletes a user account from the specified compute node.

    You can delete a user account to a node only when it is in the idle or running state.

    :param pool_id: The ID of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The ID of the machine on which you want to delete a user account.
    :type node_id: str
    :param user_name: The name of the user account to delete.
    :type user_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def compute_node_disable_scheduling(request: web.Request, pool_id, node_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, node_disable_scheduling_parameter=None) -> web.Response:
    """Disables task scheduling on the specified compute node.

    You can disable task scheduling on a node only if its current scheduling state is enabled.

    :param pool_id: The ID of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The ID of the compute node on which you want to disable task scheduling.
    :type node_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str
    :param node_disable_scheduling_parameter: The parameters for the request.
    :type node_disable_scheduling_parameter: dict | bytes

    """
    node_disable_scheduling_parameter = NodeDisableSchedulingParameter.from_dict(node_disable_scheduling_parameter)
    return web.Response(status=200)


async def compute_node_enable_scheduling(request: web.Request, pool_id, node_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Enables task scheduling on the specified compute node.

    You can enable task scheduling on a node only if its current scheduling state is disabled

    :param pool_id: The ID of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The ID of the compute node on which you want to enable task scheduling.
    :type node_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def compute_node_get(request: web.Request, pool_id, node_id, api_version, select=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Gets information about the specified compute node.

    

    :param pool_id: The ID of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The ID of the compute node that you want to get information about.
    :type node_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param select: An OData $select clause.
    :type select: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def compute_node_get_remote_desktop(request: web.Request, pool_id, node_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Gets the Remote Desktop Protocol file for the specified compute node.

    Before you can access a node by using the RDP file, you must create a user account on the node. This API can only be invoked on pools created with a cloud service configuration. For pools created with a virtual machine configuration, see the GetRemoteLoginSettings API.

    :param pool_id: The ID of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The ID of the compute node for which you want to get the Remote Desktop Protocol file.
    :type node_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def compute_node_get_remote_login_settings(request: web.Request, pool_id, node_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Gets the settings required for remote login to a compute node.

    Before you can remotely login to a node using the remote login settings, you must create a user account on the node. This API can be invoked only on pools created with the virtual machine configuration property. For pools created with a cloud service configuration, see the GetRemoteDesktop API.

    :param pool_id: The ID of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The ID of the compute node for which to obtain the remote login settings.
    :type node_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def compute_node_list(request: web.Request, pool_id, api_version, filter=None, select=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Lists the compute nodes in the specified pool.

    

    :param pool_id: The ID of the pool from which you want to list nodes.
    :type pool_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: An OData $filter clause. For more information on constructing this filter, see https://docs.microsoft.com/en-us/rest/api/batchservice/odata-filters-in-batch#list-nodes-in-a-pool.
    :type filter: str
    :param select: An OData $select clause.
    :type select: str
    :param maxresults: The maximum number of items to return in the response. A maximum of 1000 nodes can be returned.
    :type maxresults: int
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def compute_node_reboot(request: web.Request, pool_id, node_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, node_reboot_parameter=None) -> web.Response:
    """Restarts the specified compute node.

    You can restart a node only if it is in an idle or running state.

    :param pool_id: The ID of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The ID of the compute node that you want to restart.
    :type node_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str
    :param node_reboot_parameter: The parameters for the request.
    :type node_reboot_parameter: dict | bytes

    """
    node_reboot_parameter = NodeRebootParameter.from_dict(node_reboot_parameter)
    return web.Response(status=200)


async def compute_node_reimage(request: web.Request, pool_id, node_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, node_reimage_parameter=None) -> web.Response:
    """Reinstalls the operating system on the specified compute node.

    You can reinstall the operating system on a node only if it is in an idle or running state. This API can be invoked only on pools created with the cloud service configuration property.

    :param pool_id: The ID of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The ID of the compute node that you want to restart.
    :type node_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str
    :param node_reimage_parameter: The parameters for the request.
    :type node_reimage_parameter: dict | bytes

    """
    node_reimage_parameter = NodeReimageParameter.from_dict(node_reimage_parameter)
    return web.Response(status=200)


async def compute_node_update_user(request: web.Request, pool_id, node_id, user_name, api_version, node_update_user_parameter, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Updates the password and expiration time of a user account on the specified compute node.

    This operation replaces of all the updatable properties of the account. For example, if the expiryTime element is not specified, the current value is replaced with the default value, not left unmodified. You can update a user account on a node only when it is in the idle or running state.

    :param pool_id: The ID of the pool that contains the compute node.
    :type pool_id: str
    :param node_id: The ID of the machine on which you want to update a user account.
    :type node_id: str
    :param user_name: The name of the user account to update.
    :type user_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param node_update_user_parameter: The parameters for the request.
    :type node_update_user_parameter: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str

    """
    node_update_user_parameter = NodeUpdateUserParameter.from_dict(node_update_user_parameter)
    return web.Response(status=200)


async def pool_remove_nodes(request: web.Request, pool_id, api_version, node_remove_parameter, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """Removes compute nodes from the specified pool.

    This operation can only run when the allocation state of the pool is steady. When this operation runs, the allocation state changes from steady to resizing.

    :param pool_id: The ID of the pool from which you want to remove nodes.
    :type pool_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param node_remove_parameter: The parameters for the request.
    :type node_remove_parameter: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str
    :param if_match: An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service exactly matches the value specified by the client.
    :type if_match: str
    :param if_none_match: An ETag value associated with the version of the resource known to the client. The operation will be performed only if the resource&#39;s current ETag on the service does not match the value specified by the client.
    :type if_none_match: str
    :param if_modified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has been modified since the specified time.
    :type if_modified_since: str
    :param if_unmodified_since: A timestamp indicating the last modified time of the resource known to the client. The operation will be performed only if the resource on the service has not been modified since the specified time.
    :type if_unmodified_since: str

    """
    node_remove_parameter = NodeRemoveParameter.from_dict(node_remove_parameter)
    return web.Response(status=200)
