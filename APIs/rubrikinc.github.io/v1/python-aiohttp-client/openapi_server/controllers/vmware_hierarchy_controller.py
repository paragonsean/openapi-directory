from typing import List, Dict
from aiohttp import web

from openapi_server.models.vmware_hierarchy_info import VmwareHierarchyInfo
from openapi_server.models.vmware_hierarchy_info_list_response import VmwareHierarchyInfoListResponse
from openapi_server import util


async def get_vmware_hierarchy_export(request: web.Request, root_id=None) -> web.Response:
    """Get Available VMware Hierarchy Objects for Export Operations

    Get VMware Clusters, Hosts, and Resource Pool hierarchy objects that are available as the target for Virtual Machine Export operations.

    :param root_id: Get child objects of given root ID.
    :type root_id: str

    """
    return web.Response(status=200)


async def get_vmware_hierarchy_object(request: web.Request, id) -> web.Response:
    """Get VMware Hierarchy Object Information

    Get VMware Clusters, Hosts, and Resource Pool hierarchy object detail information by object ID.

    :param id: Get VMware hierarchy objects of given ID.
    :type id: str

    """
    return web.Response(status=200)
