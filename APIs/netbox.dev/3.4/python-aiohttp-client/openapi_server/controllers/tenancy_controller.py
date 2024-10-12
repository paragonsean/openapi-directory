from typing import List, Dict
from aiohttp import web

from openapi_server.models.contact import Contact
from openapi_server.models.contact_assignment import ContactAssignment
from openapi_server.models.contact_group import ContactGroup
from openapi_server.models.contact_role import ContactRole
from openapi_server.models.tenancy_contact_assignments_list200_response import TenancyContactAssignmentsList200Response
from openapi_server.models.tenancy_contact_groups_list200_response import TenancyContactGroupsList200Response
from openapi_server.models.tenancy_contact_roles_list200_response import TenancyContactRolesList200Response
from openapi_server.models.tenancy_contacts_list200_response import TenancyContactsList200Response
from openapi_server.models.tenancy_tenant_groups_list200_response import TenancyTenantGroupsList200Response
from openapi_server.models.tenancy_tenants_list200_response import TenancyTenantsList200Response
from openapi_server.models.tenant import Tenant
from openapi_server.models.tenant_group import TenantGroup
from openapi_server.models.writable_contact import WritableContact
from openapi_server.models.writable_contact_assignment import WritableContactAssignment
from openapi_server.models.writable_contact_group import WritableContactGroup
from openapi_server.models.writable_tenant import WritableTenant
from openapi_server.models.writable_tenant_group import WritableTenantGroup
from openapi_server import util


async def tenancy_contact_assignments_bulk_delete(request: web.Request, ) -> web.Response:
    """tenancy_contact_assignments_bulk_delete

    


    """
    return web.Response(status=200)


async def tenancy_contact_assignments_bulk_partial_update(request: web.Request, body) -> web.Response:
    """tenancy_contact_assignments_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableContactAssignment.from_dict(body)
    return web.Response(status=200)


async def tenancy_contact_assignments_bulk_update(request: web.Request, body) -> web.Response:
    """tenancy_contact_assignments_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableContactAssignment.from_dict(body)
    return web.Response(status=200)


async def tenancy_contact_assignments_create(request: web.Request, body) -> web.Response:
    """tenancy_contact_assignments_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableContactAssignment.from_dict(body)
    return web.Response(status=200)


async def tenancy_contact_assignments_delete(request: web.Request, id) -> web.Response:
    """tenancy_contact_assignments_delete

    

    :param id: A unique integer value identifying this contact assignment.
    :type id: int

    """
    return web.Response(status=200)


async def tenancy_contact_assignments_list(request: web.Request, id=None, content_type_id=None, object_id=None, priority=None, created=None, last_updated=None, content_type=None, contact_id=None, role_id=None, role=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, content_type_id__n=None, object_id__n=None, object_id__lte=None, object_id__lt=None, object_id__gte=None, object_id__gt=None, priority__n=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, content_type__n=None, contact_id__n=None, role_id__n=None, role__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """tenancy_contact_assignments_list

    

    :param id: 
    :type id: str
    :param content_type_id: 
    :type content_type_id: str
    :param object_id: 
    :type object_id: str
    :param priority: 
    :type priority: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param content_type: 
    :type content_type: str
    :param contact_id: 
    :type contact_id: str
    :param role_id: 
    :type role_id: str
    :param role: 
    :type role: str
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
    :param content_type_id__n: 
    :type content_type_id__n: str
    :param object_id__n: 
    :type object_id__n: str
    :param object_id__lte: 
    :type object_id__lte: str
    :param object_id__lt: 
    :type object_id__lt: str
    :param object_id__gte: 
    :type object_id__gte: str
    :param object_id__gt: 
    :type object_id__gt: str
    :param priority__n: 
    :type priority__n: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param content_type__n: 
    :type content_type__n: str
    :param contact_id__n: 
    :type contact_id__n: str
    :param role_id__n: 
    :type role_id__n: str
    :param role__n: 
    :type role__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def tenancy_contact_assignments_partial_update(request: web.Request, id, body) -> web.Response:
    """tenancy_contact_assignments_partial_update

    

    :param id: A unique integer value identifying this contact assignment.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableContactAssignment.from_dict(body)
    return web.Response(status=200)


async def tenancy_contact_assignments_read(request: web.Request, id) -> web.Response:
    """tenancy_contact_assignments_read

    

    :param id: A unique integer value identifying this contact assignment.
    :type id: int

    """
    return web.Response(status=200)


async def tenancy_contact_assignments_update(request: web.Request, id, body) -> web.Response:
    """tenancy_contact_assignments_update

    

    :param id: A unique integer value identifying this contact assignment.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableContactAssignment.from_dict(body)
    return web.Response(status=200)


async def tenancy_contact_groups_bulk_delete(request: web.Request, ) -> web.Response:
    """tenancy_contact_groups_bulk_delete

    


    """
    return web.Response(status=200)


async def tenancy_contact_groups_bulk_partial_update(request: web.Request, body) -> web.Response:
    """tenancy_contact_groups_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableContactGroup.from_dict(body)
    return web.Response(status=200)


async def tenancy_contact_groups_bulk_update(request: web.Request, body) -> web.Response:
    """tenancy_contact_groups_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableContactGroup.from_dict(body)
    return web.Response(status=200)


async def tenancy_contact_groups_create(request: web.Request, body) -> web.Response:
    """tenancy_contact_groups_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableContactGroup.from_dict(body)
    return web.Response(status=200)


async def tenancy_contact_groups_delete(request: web.Request, id) -> web.Response:
    """tenancy_contact_groups_delete

    

    :param id: A unique integer value identifying this contact group.
    :type id: int

    """
    return web.Response(status=200)


async def tenancy_contact_groups_list(request: web.Request, id=None, name=None, slug=None, description=None, created=None, last_updated=None, q=None, tag=None, parent_id=None, parent=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, parent_id__n=None, parent__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """tenancy_contact_groups_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
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
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param parent_id__n: 
    :type parent_id__n: str
    :param parent__n: 
    :type parent__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def tenancy_contact_groups_partial_update(request: web.Request, id, body) -> web.Response:
    """tenancy_contact_groups_partial_update

    

    :param id: A unique integer value identifying this contact group.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableContactGroup.from_dict(body)
    return web.Response(status=200)


async def tenancy_contact_groups_read(request: web.Request, id) -> web.Response:
    """tenancy_contact_groups_read

    

    :param id: A unique integer value identifying this contact group.
    :type id: int

    """
    return web.Response(status=200)


async def tenancy_contact_groups_update(request: web.Request, id, body) -> web.Response:
    """tenancy_contact_groups_update

    

    :param id: A unique integer value identifying this contact group.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableContactGroup.from_dict(body)
    return web.Response(status=200)


async def tenancy_contact_roles_bulk_delete(request: web.Request, ) -> web.Response:
    """tenancy_contact_roles_bulk_delete

    


    """
    return web.Response(status=200)


async def tenancy_contact_roles_bulk_partial_update(request: web.Request, body) -> web.Response:
    """tenancy_contact_roles_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = ContactRole.from_dict(body)
    return web.Response(status=200)


async def tenancy_contact_roles_bulk_update(request: web.Request, body) -> web.Response:
    """tenancy_contact_roles_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = ContactRole.from_dict(body)
    return web.Response(status=200)


async def tenancy_contact_roles_create(request: web.Request, body) -> web.Response:
    """tenancy_contact_roles_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = ContactRole.from_dict(body)
    return web.Response(status=200)


async def tenancy_contact_roles_delete(request: web.Request, id) -> web.Response:
    """tenancy_contact_roles_delete

    

    :param id: A unique integer value identifying this contact role.
    :type id: int

    """
    return web.Response(status=200)


async def tenancy_contact_roles_list(request: web.Request, id=None, name=None, slug=None, description=None, created=None, last_updated=None, q=None, tag=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """tenancy_contact_roles_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
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
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def tenancy_contact_roles_partial_update(request: web.Request, id, body) -> web.Response:
    """tenancy_contact_roles_partial_update

    

    :param id: A unique integer value identifying this contact role.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ContactRole.from_dict(body)
    return web.Response(status=200)


async def tenancy_contact_roles_read(request: web.Request, id) -> web.Response:
    """tenancy_contact_roles_read

    

    :param id: A unique integer value identifying this contact role.
    :type id: int

    """
    return web.Response(status=200)


async def tenancy_contact_roles_update(request: web.Request, id, body) -> web.Response:
    """tenancy_contact_roles_update

    

    :param id: A unique integer value identifying this contact role.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ContactRole.from_dict(body)
    return web.Response(status=200)


async def tenancy_contacts_bulk_delete(request: web.Request, ) -> web.Response:
    """tenancy_contacts_bulk_delete

    


    """
    return web.Response(status=200)


async def tenancy_contacts_bulk_partial_update(request: web.Request, body) -> web.Response:
    """tenancy_contacts_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableContact.from_dict(body)
    return web.Response(status=200)


async def tenancy_contacts_bulk_update(request: web.Request, body) -> web.Response:
    """tenancy_contacts_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableContact.from_dict(body)
    return web.Response(status=200)


async def tenancy_contacts_create(request: web.Request, body) -> web.Response:
    """tenancy_contacts_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableContact.from_dict(body)
    return web.Response(status=200)


async def tenancy_contacts_delete(request: web.Request, id) -> web.Response:
    """tenancy_contacts_delete

    

    :param id: A unique integer value identifying this contact.
    :type id: int

    """
    return web.Response(status=200)


async def tenancy_contacts_list(request: web.Request, id=None, name=None, title=None, phone=None, email=None, address=None, link=None, created=None, last_updated=None, q=None, tag=None, group_id=None, group=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, title__n=None, title__ic=None, title__nic=None, title__iew=None, title__niew=None, title__isw=None, title__nisw=None, title__ie=None, title__nie=None, title__empty=None, phone__n=None, phone__ic=None, phone__nic=None, phone__iew=None, phone__niew=None, phone__isw=None, phone__nisw=None, phone__ie=None, phone__nie=None, phone__empty=None, email__n=None, email__ic=None, email__nic=None, email__iew=None, email__niew=None, email__isw=None, email__nisw=None, email__ie=None, email__nie=None, email__empty=None, address__n=None, address__ic=None, address__nic=None, address__iew=None, address__niew=None, address__isw=None, address__nisw=None, address__ie=None, address__nie=None, address__empty=None, link__n=None, link__ic=None, link__nic=None, link__iew=None, link__niew=None, link__isw=None, link__nisw=None, link__ie=None, link__nie=None, link__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, group_id__n=None, group__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """tenancy_contacts_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param title: 
    :type title: str
    :param phone: 
    :type phone: str
    :param email: 
    :type email: str
    :param address: 
    :type address: str
    :param link: 
    :type link: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param group_id: 
    :type group_id: str
    :param group: 
    :type group: str
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
    :param name__empty: 
    :type name__empty: str
    :param title__n: 
    :type title__n: str
    :param title__ic: 
    :type title__ic: str
    :param title__nic: 
    :type title__nic: str
    :param title__iew: 
    :type title__iew: str
    :param title__niew: 
    :type title__niew: str
    :param title__isw: 
    :type title__isw: str
    :param title__nisw: 
    :type title__nisw: str
    :param title__ie: 
    :type title__ie: str
    :param title__nie: 
    :type title__nie: str
    :param title__empty: 
    :type title__empty: str
    :param phone__n: 
    :type phone__n: str
    :param phone__ic: 
    :type phone__ic: str
    :param phone__nic: 
    :type phone__nic: str
    :param phone__iew: 
    :type phone__iew: str
    :param phone__niew: 
    :type phone__niew: str
    :param phone__isw: 
    :type phone__isw: str
    :param phone__nisw: 
    :type phone__nisw: str
    :param phone__ie: 
    :type phone__ie: str
    :param phone__nie: 
    :type phone__nie: str
    :param phone__empty: 
    :type phone__empty: str
    :param email__n: 
    :type email__n: str
    :param email__ic: 
    :type email__ic: str
    :param email__nic: 
    :type email__nic: str
    :param email__iew: 
    :type email__iew: str
    :param email__niew: 
    :type email__niew: str
    :param email__isw: 
    :type email__isw: str
    :param email__nisw: 
    :type email__nisw: str
    :param email__ie: 
    :type email__ie: str
    :param email__nie: 
    :type email__nie: str
    :param email__empty: 
    :type email__empty: str
    :param address__n: 
    :type address__n: str
    :param address__ic: 
    :type address__ic: str
    :param address__nic: 
    :type address__nic: str
    :param address__iew: 
    :type address__iew: str
    :param address__niew: 
    :type address__niew: str
    :param address__isw: 
    :type address__isw: str
    :param address__nisw: 
    :type address__nisw: str
    :param address__ie: 
    :type address__ie: str
    :param address__nie: 
    :type address__nie: str
    :param address__empty: 
    :type address__empty: str
    :param link__n: 
    :type link__n: str
    :param link__ic: 
    :type link__ic: str
    :param link__nic: 
    :type link__nic: str
    :param link__iew: 
    :type link__iew: str
    :param link__niew: 
    :type link__niew: str
    :param link__isw: 
    :type link__isw: str
    :param link__nisw: 
    :type link__nisw: str
    :param link__ie: 
    :type link__ie: str
    :param link__nie: 
    :type link__nie: str
    :param link__empty: 
    :type link__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param group_id__n: 
    :type group_id__n: str
    :param group__n: 
    :type group__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def tenancy_contacts_partial_update(request: web.Request, id, body) -> web.Response:
    """tenancy_contacts_partial_update

    

    :param id: A unique integer value identifying this contact.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableContact.from_dict(body)
    return web.Response(status=200)


async def tenancy_contacts_read(request: web.Request, id) -> web.Response:
    """tenancy_contacts_read

    

    :param id: A unique integer value identifying this contact.
    :type id: int

    """
    return web.Response(status=200)


async def tenancy_contacts_update(request: web.Request, id, body) -> web.Response:
    """tenancy_contacts_update

    

    :param id: A unique integer value identifying this contact.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableContact.from_dict(body)
    return web.Response(status=200)


async def tenancy_tenant_groups_bulk_delete(request: web.Request, ) -> web.Response:
    """tenancy_tenant_groups_bulk_delete

    


    """
    return web.Response(status=200)


async def tenancy_tenant_groups_bulk_partial_update(request: web.Request, body) -> web.Response:
    """tenancy_tenant_groups_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableTenantGroup.from_dict(body)
    return web.Response(status=200)


async def tenancy_tenant_groups_bulk_update(request: web.Request, body) -> web.Response:
    """tenancy_tenant_groups_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableTenantGroup.from_dict(body)
    return web.Response(status=200)


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


async def tenancy_tenant_groups_list(request: web.Request, id=None, name=None, slug=None, description=None, created=None, last_updated=None, q=None, tag=None, parent_id=None, parent=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, parent_id__n=None, parent__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """tenancy_tenant_groups_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
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
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param parent_id__n: 
    :type parent_id__n: str
    :param parent__n: 
    :type parent__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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


async def tenancy_tenants_bulk_delete(request: web.Request, ) -> web.Response:
    """tenancy_tenants_bulk_delete

    


    """
    return web.Response(status=200)


async def tenancy_tenants_bulk_partial_update(request: web.Request, body) -> web.Response:
    """tenancy_tenants_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableTenant.from_dict(body)
    return web.Response(status=200)


async def tenancy_tenants_bulk_update(request: web.Request, body) -> web.Response:
    """tenancy_tenants_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableTenant.from_dict(body)
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


async def tenancy_tenants_list(request: web.Request, id=None, name=None, slug=None, description=None, created=None, last_updated=None, q=None, tag=None, contact=None, contact_role=None, contact_group=None, group_id=None, group=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, slug__n=None, slug__ic=None, slug__nic=None, slug__iew=None, slug__niew=None, slug__isw=None, slug__nisw=None, slug__ie=None, slug__nie=None, slug__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, created__n=None, created__lte=None, created__lt=None, created__gte=None, created__gt=None, last_updated__n=None, last_updated__lte=None, last_updated__lt=None, last_updated__gte=None, last_updated__gt=None, tag__n=None, contact__n=None, contact_role__n=None, contact_group__n=None, group_id__n=None, group__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """tenancy_tenants_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param slug: 
    :type slug: str
    :param description: 
    :type description: str
    :param created: 
    :type created: str
    :param last_updated: 
    :type last_updated: str
    :param q: 
    :type q: str
    :param tag: 
    :type tag: str
    :param contact: 
    :type contact: str
    :param contact_role: 
    :type contact_role: str
    :param contact_group: 
    :type contact_group: str
    :param group_id: 
    :type group_id: str
    :param group: 
    :type group: str
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
    :param name__empty: 
    :type name__empty: str
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
    :param slug__empty: 
    :type slug__empty: str
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
    :param description__empty: 
    :type description__empty: str
    :param created__n: 
    :type created__n: str
    :param created__lte: 
    :type created__lte: str
    :param created__lt: 
    :type created__lt: str
    :param created__gte: 
    :type created__gte: str
    :param created__gt: 
    :type created__gt: str
    :param last_updated__n: 
    :type last_updated__n: str
    :param last_updated__lte: 
    :type last_updated__lte: str
    :param last_updated__lt: 
    :type last_updated__lt: str
    :param last_updated__gte: 
    :type last_updated__gte: str
    :param last_updated__gt: 
    :type last_updated__gt: str
    :param tag__n: 
    :type tag__n: str
    :param contact__n: 
    :type contact__n: str
    :param contact_role__n: 
    :type contact_role__n: str
    :param contact_group__n: 
    :type contact_group__n: str
    :param group_id__n: 
    :type group_id__n: str
    :param group__n: 
    :type group__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
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
