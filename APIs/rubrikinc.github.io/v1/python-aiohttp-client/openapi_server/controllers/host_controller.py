from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server.models.discovered_nas_share import DiscoveredNasShare
from openapi_server.models.host_detail import HostDetail
from openapi_server.models.host_make_primary_request import HostMakePrimaryRequest
from openapi_server.models.host_register import HostRegister
from openapi_server.models.host_summary_list_response import HostSummaryListResponse
from openapi_server.models.host_update import HostUpdate
from openapi_server.models.host_volume_summary_list_response import HostVolumeSummaryListResponse
from openapi_server.models.rbs_host_operation_request import RbsHostOperationRequest
from openapi_server.models.rbs_host_operation_response import RbsHostOperationResponse
from openapi_server.models.rbs_host_summary import RbsHostSummary
from openapi_server.models.search_response_list_response import SearchResponseListResponse
from openapi_server import util


async def bulk_register_host_async(request: web.Request, body) -> web.Response:
    """Register hosts

    Register multiple hosts and perform discovery for databases and Microsoft SQL Server instances. When called, this API returns a success message, but completes the host registration in the background. Monitor the status of the background host discovery with the \&quot;status\&quot; field in GET API on /hosts. The POST API on /hosts can take longer for discovery, depending on the number of hosts on the system. POST on this API can be used instead to perform the discovery in the background and quickly register the host. Doing this requires that you install RBS for Linux and Windows hosts, similar to regular register using POST on /hosts.

    :param body: Registration definition for each host.
    :type body: list | bytes

    """
    body = [HostRegister.from_dict(d) for d in body]
    return web.Response(status=200)


async def delete_host(request: web.Request, id) -> web.Response:
    """Delete a registered host

    Delete host by specifying the host ID.

    :param id: ID of the host to delete.
    :type id: str

    """
    return web.Response(status=200)


async def discover_nas_shares(request: web.Request, id) -> web.Response:
    """Discover and return all shares on a NAS host

    Discover and return all shares on the identified NAS host.

    :param id: The discoverable NAS host ID.
    :type id: str

    """
    return web.Response(status=200)


async def get_host(request: web.Request, id) -> web.Response:
    """Get summary information for a host

    Retrieve summary information for a registered host.

    :param id: ID of the registered host.
    :type id: str

    """
    return web.Response(status=200)


async def get_rbs_host_info(request: web.Request, name, username, password, operation_timeout=None) -> web.Response:
    """Get the Rubrik Backup Service details for a host

    Get the details of the Rubrik Backup Service (RBS) installed on a specific host. Specify the details of the host to check whether RBS is installed on the host or not. If RBS is installed, the response will include the RBS details.

    :param name: IP address or hostname of the host.
    :type name: str
    :param username: Name of the user account that has sudo/admin privileges on the RBS host. This is required to install/uninstall/upgrade RBS packages on the RBS host.
    :type username: str
    :param password: Password associated with the username that has access to the host.
    :type password: str
    :param operation_timeout: Number of seconds after which the operation is terminated if it has not completed execution. Default value is 600 seconds.
    :type operation_timeout: int

    """
    return web.Response(status=200)


async def host_make_primary(request: web.Request, body) -> web.Response:
    """Make this cluster the primary for agents on a set of hosts

    Migrate the primary cluster with which the agent is able to perform regular operations (backup, restore etc). This can be done on a specified set of hosts or for all hosts that currently have a specified primary cluster for disaster recovery. Specify exactly one of &#x60;ids&#x60; or &#x60;oldPrimaryClusterUuid&#x60;.

    :param body: Description of hosts to migrate.
    :type body: dict | bytes

    """
    body = HostMakePrimaryRequest.from_dict(body)
    return web.Response(status=200)


async def query_host(request: web.Request, operating_system_type=None, operating_system=None, primary_cluster_id=None, name=None, hostname=None, sort_by=None, sort_order=None, snappable_status=None) -> web.Response:
    """Get summary information for hosts

    Retrieve summary information for all hosts that are registered with a Rubrik cluster.

    :param operating_system_type: Filter the summary information based on the operating system type. Accepted values are &#39;Windows&#39;, &#39;UnixLike&#39;, &#39;ANY&#39;, &#39;NONE&#39;. Use **_NONE_** to only return information for hosts templates that do not have operating system type set. Use **_ANY_** to only return information for hosts that have operating system type set.
    :type operating_system_type: str
    :param operating_system: Filter the summary information based on the operating system. Use **_AIX_**, **_Linux_** or **_Solaris_** to restrict the returned information to hosts with operating systems within the specified operating system family. Use a specific operating system release version to restrict the returned information to hosts with operating systems that match the specified version.
    :type operating_system: str
    :param primary_cluster_id: Filters the summary information based on the Rubrik cluster specified by the value of primary_cluster_id. Use &#39;local&#39; for the Rubrik cluster that is hosting the current REST API session.
    :type primary_cluster_id: str
    :param name: Retrieve hosts with a host name matching the provided name. The search type is infix.
    :type name: str
    :param hostname: (Deprecated) Retrieve hosts with a host name matching the provided name. The search type is infix.
    :type hostname: str
    :param sort_by: Specifies the host attribute to use in sorting the host summary information. Performs an ASCII sort of the summary information using the specified attribute, in the order specified. Valid attributes are &#39;hostname&#39;.
    :type sort_by: str
    :param sort_order: Sort order, either ascending or descending.
    :type sort_order: str
    :param snappable_status: Determines whether to fetch hosts with additional privilege checks.
    :type snappable_status: str

    """
    return web.Response(status=200)


async def query_host_volume(request: web.Request, id) -> web.Response:
    """Get list of Volume Group volumes

    Retrieve summary information for each volume on a specified Volume Group host.

    :param id: The ID of the host.
    :type id: str

    """
    return web.Response(status=200)


async def rbs_install(request: web.Request, body) -> web.Response:
    """Install Rubrik Backup Service on a host

    Install Rubrik Backup Service on a host.

    :param body: Configuration parameters to install RBS on a host.
    :type body: dict | bytes

    """
    body = RbsHostOperationRequest.from_dict(body)
    return web.Response(status=200)


async def rbs_uninstall(request: web.Request, body) -> web.Response:
    """Uninstall Rubrik Backup Service from a host

    Uninstall Rubrik Backup Service from a host.

    :param body: Configuration parameters to uninstall RBS from a host.
    :type body: dict | bytes

    """
    body = RbsHostOperationRequest.from_dict(body)
    return web.Response(status=200)


async def rbs_upgrade(request: web.Request, body) -> web.Response:
    """Upgrade Rubrik Backup Service on a host

    Upgrade Rubrik Backup Service on a host.

    :param body: Configuration parameters to upgrade RBS on a host.
    :type body: dict | bytes

    """
    body = RbsHostOperationRequest.from_dict(body)
    return web.Response(status=200)


async def refresh_host(request: web.Request, id) -> web.Response:
    """Refresh a host

    Refresh the properties of a host object when changes on the host are not seen in the Rubrik web UI.

    :param id: ID assigned to a host object.
    :type id: str

    """
    return web.Response(status=200)


async def register_host(request: web.Request, body) -> web.Response:
    """Register a host

    Register a host.

    :param body: Registration definition for a host.
    :type body: dict | bytes

    """
    body = HostRegister.from_dict(body)
    return web.Response(status=200)


async def register_host_async(request: web.Request, body) -> web.Response:
    """Register a host

    Register a host and perform discovery for databases and Microsoft SQL Server instances. When called, this API returns a success message, but completes the host registration in the background. Monitor the status of the background host discovery with the \&quot;status\&quot; field in GET API on /hosts. The POST API on /hosts can take longer for discovery, depending on the number of hosts on the system. POST on this API can be used instead to perform the discovery in the background and quickly register the host. Doing this requires that you install RBS for Linux and Windows hosts, similar to regular register using POST on /hosts.

    :param body: Registration definition for a host.
    :type body: dict | bytes

    """
    body = HostRegister.from_dict(body)
    return web.Response(status=200)


async def search_host(request: web.Request, id, path) -> web.Response:
    """Search for a file within the host

    Search for a file within the host. Search via full path prefix or filename prefix.

    :param id: ID of the host to search.
    :type id: str
    :param path: The path query. Either path prefix or filename prefix.
    :type path: str

    """
    return web.Response(status=200)


async def update_certificate_host(request: web.Request, id) -> web.Response:
    """Update certificate

    Provide an updated certificate for a specified host.

    :param id: ID of the host.
    :type id: str

    """
    return web.Response(status=200)


async def update_host(request: web.Request, id, body) -> web.Response:
    """Modify information for a registered host

    Change the FQDN and IPv4 address that is assigned to a host object. Enable or disable pre-transfer data compression. Enable or disable change block tracking (CBT) for backups of SQL Server databases on Windows hosts. Enable or disable volume filter driver (VFD) for volume backups on Windows hosts. Set an Oracle user with sysdba privileges to permit Oracle discovery queries.

    :param id: ID of the registered host.
    :type id: str
    :param body: Properties of host to update.
    :type body: dict | bytes

    """
    body = HostUpdate.from_dict(body)
    return web.Response(status=200)
