from typing import List, Dict
from aiohttp import web

from openapi_server.models.tenancy_tenant_groups_list200_response import TenancyTenantGroupsList200Response
from openapi_server.models.tenancy_tenants_list200_response import TenancyTenantsList200Response
from openapi_server.models.tenant import Tenant
from openapi_server.models.tenant_group import TenantGroup
from openapi_server.models.writable_tenant import WritableTenant
from openapi_server.models.writable_tenant_group import WritableTenantGroup
from openapi_server import util


async def tenancy_tenant_groups_create(request: web.Request, body) -> web.Response:
    """tenancy_tenant_groups_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableTenantGroup.from_dict(body)
    return web.Response(status=200)


async def tenancy_tenant_groups_delete(request: web.Request, id) -> web.Response:
    """tenancy_tenant_groups_delete

    

    :param id: A unique integer value identifying this tenant group.
    :type id: int

    """
    return web.Response(status=200)


async def tenancy_tenant_groups_list(request: web.Request, id=None, name=None, slug=None, description=None, q=None, parent_id=None, parent=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, parent_id__n=None, parent__n=None, limit=None, offset=None) -> web.Response:
    """tenancy_tenant_groups_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param parent_id: 
    :type parent_id: str
    :param parent: 
    :type parent: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
    :param description__n: 
    :type description__n: str
    :param description__ic: 
    :type description__ic: str
    :param description__nic: 
    :type description__nic: str
    :param description__iew: 
    :type description__iew: str
    :param description__niew: 
    :type description__niew: str
    :param description__isw: 
    :type description__isw: str
    :param description__nisw: 
    :type description__nisw: str
    :param description__ie: 
    :type description__ie: str
    :param description__nie: 
    :type description__nie: str
    :param parent_id__n: 
    :type parent_id__n: str
    :param parent__n: 
    :type parent__n: str
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
    body = WritableTenantGroup.from_dict(body)
    return web.Response(status=200)


async def tenancy_tenant_groups_read(request: web.Request, id) -> web.Response:
    """tenancy_tenant_groups_read

    Call to super to allow for caching

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
    body = WritableTenantGroup.from_dict(body)
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


async def tenancy_tenants_list(request: web.Request, id=None, name=None, slug=None, created=None, created__gte=None, created__lte=None, last_updated=None, last_updated__gte=None, last_updated__lte=None, q=None, group_id=None, group=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, group_id__n=None, group__n=None, tag__n=None, limit=None, offset=None) -> web.Response:
    """tenancy_tenants_list

    Call to super to allow for caching

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param created: 
    :type created: str
    :param created__gte: 
    :type created__gte: str
    :param created__lte: 
    :type created__lte: str
    :param last_updated: 
    :type last_updated: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param q: 
    :type q: str
    :param group_id: 
    :type group_id: str
    :param group: 
    :type group: str
    :param tag: 
    :type tag: str
    :param id__n: 
    :type id__n: str
    :param id__lte: 
    :type id__lte: str
    :param id__lt: 
    :type id__lt: str
    :param id__gte: 
    :type id__gte: str
    :param id__gt: 
    :type id__gt: str
    :param name__n: 
    :type name__n: str
    :param name__ic: 
    :type name__ic: str
    :param name__nic: 
    :type name__nic: str
    :param name__iew: 
    :type name__iew: str
    :param name__niew: 
    :type name__niew: str
    :param name__isw: 
    :type name__isw: str
    :param name__nisw: 
    :type name__nisw: str
    :param name__ie: 
    :type name__ie: str
    :param name__nie: 
    :type name__nie: str
    :param slug__n: 
    :type slug__n: str
    :param slug__ic: 
    :type slug__ic: str
    :param slug__nic: 
    :type slug__nic: str
    :param slug__iew: 
    :type slug__iew: str
    :param slug__niew: 
    :type slug__niew: str
    :param slug__isw: 
    :type slug__isw: str
    :param slug__nisw: 
    :type slug__nisw: str
    :param slug__ie: 
    :type slug__ie: str
    :param slug__nie: 
    :type slug__nie: str
    :param group_id__n: 
    :type group_id__n: str
    :param group__n: 
    :type group__n: str
    :param tag__n: 
    :type tag__n: str
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

    Call to super to allow for caching

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
