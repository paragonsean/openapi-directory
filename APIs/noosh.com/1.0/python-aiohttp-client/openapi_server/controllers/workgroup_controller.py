from typing import List, Dict
from aiohttp import web

from openapi_server.models.client_workgroup_expand_vo import ClientWorkgroupExpandVO
from openapi_server.models.client_workgroup_list_vo import ClientWorkgroupListVO
from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.supplier_workgroup_expand_vo import SupplierWorkgroupExpandVO
from openapi_server.models.supplier_workgroup_list_vo import SupplierWorkgroupListVO
from openapi_server.models.workgroup_expand_vo import WorkgroupExpandVO
from openapi_server.models.workgroup_http_status_vo import WorkgroupHTTPStatusVO
from openapi_server.models.workgroup_list_vo import WorkgroupListVO
from openapi_server.models.workgroup_upd_persist_vo import WorkgroupUpdPersistVO
from openapi_server import util


async def get_client_workgroup_list(request: web.Request, workgroup_id) -> web.Response:
    """List client workgroups

    List client workgroups

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def get_specific_client_workgroup(request: web.Request, workgroup_id, client_workgroup_id) -> web.Response:
    """Get a specific client workgroups

    Get a specific client workgroups

    :param workgroup_id: 
    :type workgroup_id: str
    :param client_workgroup_id: 
    :type client_workgroup_id: str

    """
    return web.Response(status=200)


async def get_supplier_workgroup_detail(request: web.Request, workgroup_id, bu_supplier_workgroup_id) -> web.Response:
    """Get the specific supplier of My Group

    Get the specific supplier of My Group

    :param workgroup_id: 
    :type workgroup_id: str
    :param bu_supplier_workgroup_id: 
    :type bu_supplier_workgroup_id: str

    """
    return web.Response(status=200)


async def get_supplier_workgroup_list(request: web.Request, workgroup_id) -> web.Response:
    """List supplier workgroups

    List supplier workgroups

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def get_workgroup_detail(request: web.Request, workgroup_id) -> web.Response:
    """Detail workgroup info

    Detail workgroup info

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def get_workgroup_list(request: web.Request, workgroup_name=None, workgroup_types=None) -> web.Response:
    """List the workgroups

    List the workgroups

    :param workgroup_name: Workgroup Name
    :type workgroup_name: str
    :param workgroup_types: 1000001 for Buyer, 1000002 for supplier, 1000003 for agent, 1000004 for Broker/Outsourcer and 1000005 for Partner
    :type workgroup_types: List[str]

    """
    return web.Response(status=200)


async def put_workgroup(request: web.Request, workgroup_id, body=None) -> web.Response:
    """Update a specific Workgroup

    Update a specific Workgroup

    :param workgroup_id: 
    :type workgroup_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = WorkgroupUpdPersistVO.from_dict(body)
    return web.Response(status=200)
