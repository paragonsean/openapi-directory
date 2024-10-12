from typing import List, Dict
from aiohttp import web

from openapi_server.models.tenancy_tenant_groups_list200_response import TenancyTenantGroupsList200Response
from openapi_server.models.tenancy_tenants_list200_response import TenancyTenantsList200Response
from openapi_server.models.tenant import Tenant
from openapi_server.models.tenant_group import TenantGroup
from openapi_server.models.writable_tenant import WritableTenant
from openapi_server import util


async def tenancy_choices_list(request: web.Request, ) -> web.Response:
    """tenancy_choices_list

    


    """
    return web.Response(status=200)


async def tenancy_choices_read(request: web.Request, id) -> web.Response:
    """tenancy_choices_read

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def tenancy_tenant_groups_create(request: web.Request, body) -> web.Response:
    """tenancy_tenant_groups_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = TenantGroup.from_dict(body)
    return web.Response(status=200)


async def tenancy_tenant_groups_delete(request: web.Request, id) -> web.Response:
    """tenancy_tenant_groups_delete

    

    :param id: A unique integer value identifying this tenant group.
    :type id: int

    """
    return web.Response(status=200)


async def tenancy_tenant_groups_list(request: web.Request, name=None, slug=None, limit=None, offset=None) -> web.Response:
    """tenancy_tenant_groups_list

    

    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def tenancy_tenant_groups_partial_update(request: web.Request, id, body) -> web.Response:
    """tenancy_tenant_groups_partial_update

    

    :param id: A unique integer value identifying this tenant group.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = TenantGroup.from_dict(body)
    return web.Response(status=200)


async def tenancy_tenant_groups_read(request: web.Request, id) -> web.Response:
    """tenancy_tenant_groups_read

    

    :param id: A unique integer value identifying this tenant group.
    :type id: int

    """
    return web.Response(status=200)


async def tenancy_tenant_groups_update(request: web.Request, id, body) -> web.Response:
    """tenancy_tenant_groups_update

    

    :param id: A unique integer value identifying this tenant group.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = TenantGroup.from_dict(body)
    return web.Response(status=200)


async def tenancy_tenants_create(request: web.Request, body) -> web.Response:
    """tenancy_tenants_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableTenant.from_dict(body)
    return web.Response(status=200)


async def tenancy_tenants_delete(request: web.Request, id) -> web.Response:
    """tenancy_tenants_delete

    

    :param id: A unique integer value identifying this tenant.
    :type id: int

    """
    return web.Response(status=200)


async def tenancy_tenants_list(request: web.Request, name=None, id__in=None, q=None, group_id=None, group=None, tag=None, limit=None, offset=None) -> web.Response:
    """tenancy_tenants_list

    

    :param name: 
    :type name: str
    :param id__in: Multiple values may be separated by commas.
    :type id__in: str
    :param q: 
    :type q: str
    :param group_id: 
    :type group_id: str
    :param group: 
    :type group: str
    :param tag: 
    :type tag: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def tenancy_tenants_partial_update(request: web.Request, id, body) -> web.Response:
    """tenancy_tenants_partial_update

    

    :param id: A unique integer value identifying this tenant.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableTenant.from_dict(body)
    return web.Response(status=200)


async def tenancy_tenants_read(request: web.Request, id) -> web.Response:
    """tenancy_tenants_read

    

    :param id: A unique integer value identifying this tenant.
    :type id: int

    """
    return web.Response(status=200)


async def tenancy_tenants_update(request: web.Request, id, body) -> web.Response:
    """tenancy_tenants_update

    

    :param id: A unique integer value identifying this tenant.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableTenant.from_dict(body)
    return web.Response(status=200)
