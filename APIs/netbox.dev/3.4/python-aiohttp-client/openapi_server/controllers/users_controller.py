from typing import List, Dict
from aiohttp import web

from openapi_server.models.group import Group
from openapi_server.models.object_permission import ObjectPermission
from openapi_server.models.token import Token
from openapi_server.models.user import User
from openapi_server.models.users_groups_list200_response import UsersGroupsList200Response
from openapi_server.models.users_permissions_list200_response import UsersPermissionsList200Response
from openapi_server.models.users_tokens_list200_response import UsersTokensList200Response
from openapi_server.models.users_users_list200_response import UsersUsersList200Response
from openapi_server.models.writable_object_permission import WritableObjectPermission
from openapi_server.models.writable_token import WritableToken
from openapi_server.models.writable_user import WritableUser
from openapi_server import util


async def users_config_list(request: web.Request, ) -> web.Response:
    """users_config_list

    Return the UserConfig for the currently authenticated User.


    """
    return web.Response(status=200)


async def users_groups_bulk_delete(request: web.Request, ) -> web.Response:
    """users_groups_bulk_delete

    


    """
    return web.Response(status=200)


async def users_groups_bulk_partial_update(request: web.Request, body) -> web.Response:
    """users_groups_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = Group.from_dict(body)
    return web.Response(status=200)


async def users_groups_bulk_update(request: web.Request, body) -> web.Response:
    """users_groups_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = Group.from_dict(body)
    return web.Response(status=200)


async def users_groups_create(request: web.Request, body) -> web.Response:
    """users_groups_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = Group.from_dict(body)
    return web.Response(status=200)


async def users_groups_delete(request: web.Request, id) -> web.Response:
    """users_groups_delete

    

    :param id: A unique integer value identifying this group.
    :type id: int

    """
    return web.Response(status=200)


async def users_groups_list(request: web.Request, id=None, name=None, q=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, ordering=None, limit=None, offset=None) -> web.Response:
    """users_groups_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param q: 
    :type q: str
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
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def users_groups_partial_update(request: web.Request, id, body) -> web.Response:
    """users_groups_partial_update

    

    :param id: A unique integer value identifying this group.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Group.from_dict(body)
    return web.Response(status=200)


async def users_groups_read(request: web.Request, id) -> web.Response:
    """users_groups_read

    

    :param id: A unique integer value identifying this group.
    :type id: int

    """
    return web.Response(status=200)


async def users_groups_update(request: web.Request, id, body) -> web.Response:
    """users_groups_update

    

    :param id: A unique integer value identifying this group.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Group.from_dict(body)
    return web.Response(status=200)


async def users_permissions_bulk_delete(request: web.Request, ) -> web.Response:
    """users_permissions_bulk_delete

    


    """
    return web.Response(status=200)


async def users_permissions_bulk_partial_update(request: web.Request, body) -> web.Response:
    """users_permissions_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableObjectPermission.from_dict(body)
    return web.Response(status=200)


async def users_permissions_bulk_update(request: web.Request, body) -> web.Response:
    """users_permissions_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableObjectPermission.from_dict(body)
    return web.Response(status=200)


async def users_permissions_create(request: web.Request, body) -> web.Response:
    """users_permissions_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableObjectPermission.from_dict(body)
    return web.Response(status=200)


async def users_permissions_delete(request: web.Request, id) -> web.Response:
    """users_permissions_delete

    

    :param id: A unique integer value identifying this permission.
    :type id: int

    """
    return web.Response(status=200)


async def users_permissions_list(request: web.Request, id=None, name=None, enabled=None, object_types=None, description=None, q=None, user_id=None, user=None, group_id=None, group=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, name__n=None, name__ic=None, name__nic=None, name__iew=None, name__niew=None, name__isw=None, name__nisw=None, name__ie=None, name__nie=None, name__empty=None, object_types__n=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, user_id__n=None, user__n=None, group_id__n=None, group__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """users_permissions_list

    

    :param id: 
    :type id: str
    :param name: 
    :type name: str
    :param enabled: 
    :type enabled: str
    :param object_types: 
    :type object_types: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param user_id: 
    :type user_id: str
    :param user: 
    :type user: str
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
    :param object_types__n: 
    :type object_types__n: str
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
    :param user_id__n: 
    :type user_id__n: str
    :param user__n: 
    :type user__n: str
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


async def users_permissions_partial_update(request: web.Request, id, body) -> web.Response:
    """users_permissions_partial_update

    

    :param id: A unique integer value identifying this permission.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableObjectPermission.from_dict(body)
    return web.Response(status=200)


async def users_permissions_read(request: web.Request, id) -> web.Response:
    """users_permissions_read

    

    :param id: A unique integer value identifying this permission.
    :type id: int

    """
    return web.Response(status=200)


async def users_permissions_update(request: web.Request, id, body) -> web.Response:
    """users_permissions_update

    

    :param id: A unique integer value identifying this permission.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableObjectPermission.from_dict(body)
    return web.Response(status=200)


async def users_tokens_bulk_delete(request: web.Request, ) -> web.Response:
    """users_tokens_bulk_delete

    


    """
    return web.Response(status=200)


async def users_tokens_bulk_partial_update(request: web.Request, body) -> web.Response:
    """users_tokens_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableToken.from_dict(body)
    return web.Response(status=200)


async def users_tokens_bulk_update(request: web.Request, body) -> web.Response:
    """users_tokens_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableToken.from_dict(body)
    return web.Response(status=200)


async def users_tokens_create(request: web.Request, body) -> web.Response:
    """users_tokens_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableToken.from_dict(body)
    return web.Response(status=200)


async def users_tokens_delete(request: web.Request, id) -> web.Response:
    """users_tokens_delete

    

    :param id: A unique integer value identifying this token.
    :type id: int

    """
    return web.Response(status=200)


async def users_tokens_list(request: web.Request, id=None, key=None, write_enabled=None, description=None, q=None, user_id=None, user=None, created=None, created__gte=None, created__lte=None, expires=None, expires__gte=None, expires__lte=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, key__n=None, key__ic=None, key__nic=None, key__iew=None, key__niew=None, key__isw=None, key__nisw=None, key__ie=None, key__nie=None, key__empty=None, description__n=None, description__ic=None, description__nic=None, description__iew=None, description__niew=None, description__isw=None, description__nisw=None, description__ie=None, description__nie=None, description__empty=None, user_id__n=None, user__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """users_tokens_list

    

    :param id: 
    :type id: str
    :param key: 
    :type key: str
    :param write_enabled: 
    :type write_enabled: str
    :param description: 
    :type description: str
    :param q: 
    :type q: str
    :param user_id: 
    :type user_id: str
    :param user: 
    :type user: str
    :param created: 
    :type created: str
    :param created__gte: 
    :type created__gte: str
    :param created__lte: 
    :type created__lte: str
    :param expires: 
    :type expires: str
    :param expires__gte: 
    :type expires__gte: str
    :param expires__lte: 
    :type expires__lte: str
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
    :param key__n: 
    :type key__n: str
    :param key__ic: 
    :type key__ic: str
    :param key__nic: 
    :type key__nic: str
    :param key__iew: 
    :type key__iew: str
    :param key__niew: 
    :type key__niew: str
    :param key__isw: 
    :type key__isw: str
    :param key__nisw: 
    :type key__nisw: str
    :param key__ie: 
    :type key__ie: str
    :param key__nie: 
    :type key__nie: str
    :param key__empty: 
    :type key__empty: str
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
    :param user_id__n: 
    :type user_id__n: str
    :param user__n: 
    :type user__n: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def users_tokens_partial_update(request: web.Request, id, body) -> web.Response:
    """users_tokens_partial_update

    

    :param id: A unique integer value identifying this token.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableToken.from_dict(body)
    return web.Response(status=200)


async def users_tokens_provision_create(request: web.Request, ) -> web.Response:
    """users_tokens_provision_create

    Non-authenticated REST API endpoint via which a user may create a Token.


    """
    return web.Response(status=200)


async def users_tokens_read(request: web.Request, id) -> web.Response:
    """users_tokens_read

    

    :param id: A unique integer value identifying this token.
    :type id: int

    """
    return web.Response(status=200)


async def users_tokens_update(request: web.Request, id, body) -> web.Response:
    """users_tokens_update

    

    :param id: A unique integer value identifying this token.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableToken.from_dict(body)
    return web.Response(status=200)


async def users_users_bulk_delete(request: web.Request, ) -> web.Response:
    """users_users_bulk_delete

    


    """
    return web.Response(status=200)


async def users_users_bulk_partial_update(request: web.Request, body) -> web.Response:
    """users_users_bulk_partial_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableUser.from_dict(body)
    return web.Response(status=200)


async def users_users_bulk_update(request: web.Request, body) -> web.Response:
    """users_users_bulk_update

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableUser.from_dict(body)
    return web.Response(status=200)


async def users_users_create(request: web.Request, body) -> web.Response:
    """users_users_create

    

    :param body: 
    :type body: dict | bytes

    """
    body = WritableUser.from_dict(body)
    return web.Response(status=200)


async def users_users_delete(request: web.Request, id) -> web.Response:
    """users_users_delete

    

    :param id: A unique integer value identifying this user.
    :type id: int

    """
    return web.Response(status=200)


async def users_users_list(request: web.Request, id=None, username=None, first_name=None, last_name=None, email=None, is_staff=None, is_active=None, q=None, group_id=None, group=None, id__n=None, id__lte=None, id__lt=None, id__gte=None, id__gt=None, username__n=None, username__ic=None, username__nic=None, username__iew=None, username__niew=None, username__isw=None, username__nisw=None, username__ie=None, username__nie=None, username__empty=None, first_name__n=None, first_name__ic=None, first_name__nic=None, first_name__iew=None, first_name__niew=None, first_name__isw=None, first_name__nisw=None, first_name__ie=None, first_name__nie=None, first_name__empty=None, last_name__n=None, last_name__ic=None, last_name__nic=None, last_name__iew=None, last_name__niew=None, last_name__isw=None, last_name__nisw=None, last_name__ie=None, last_name__nie=None, last_name__empty=None, email__n=None, email__ic=None, email__nic=None, email__iew=None, email__niew=None, email__isw=None, email__nisw=None, email__ie=None, email__nie=None, email__empty=None, group_id__n=None, group__n=None, ordering=None, limit=None, offset=None) -> web.Response:
    """users_users_list

    

    :param id: 
    :type id: str
    :param username: 
    :type username: str
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param email: 
    :type email: str
    :param is_staff: 
    :type is_staff: str
    :param is_active: 
    :type is_active: str
    :param q: 
    :type q: str
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
    :param username__n: 
    :type username__n: str
    :param username__ic: 
    :type username__ic: str
    :param username__nic: 
    :type username__nic: str
    :param username__iew: 
    :type username__iew: str
    :param username__niew: 
    :type username__niew: str
    :param username__isw: 
    :type username__isw: str
    :param username__nisw: 
    :type username__nisw: str
    :param username__ie: 
    :type username__ie: str
    :param username__nie: 
    :type username__nie: str
    :param username__empty: 
    :type username__empty: str
    :param first_name__n: 
    :type first_name__n: str
    :param first_name__ic: 
    :type first_name__ic: str
    :param first_name__nic: 
    :type first_name__nic: str
    :param first_name__iew: 
    :type first_name__iew: str
    :param first_name__niew: 
    :type first_name__niew: str
    :param first_name__isw: 
    :type first_name__isw: str
    :param first_name__nisw: 
    :type first_name__nisw: str
    :param first_name__ie: 
    :type first_name__ie: str
    :param first_name__nie: 
    :type first_name__nie: str
    :param first_name__empty: 
    :type first_name__empty: str
    :param last_name__n: 
    :type last_name__n: str
    :param last_name__ic: 
    :type last_name__ic: str
    :param last_name__nic: 
    :type last_name__nic: str
    :param last_name__iew: 
    :type last_name__iew: str
    :param last_name__niew: 
    :type last_name__niew: str
    :param last_name__isw: 
    :type last_name__isw: str
    :param last_name__nisw: 
    :type last_name__nisw: str
    :param last_name__ie: 
    :type last_name__ie: str
    :param last_name__nie: 
    :type last_name__nie: str
    :param last_name__empty: 
    :type last_name__empty: str
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


async def users_users_partial_update(request: web.Request, id, body) -> web.Response:
    """users_users_partial_update

    

    :param id: A unique integer value identifying this user.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableUser.from_dict(body)
    return web.Response(status=200)


async def users_users_read(request: web.Request, id) -> web.Response:
    """users_users_read

    

    :param id: A unique integer value identifying this user.
    :type id: int

    """
    return web.Response(status=200)


async def users_users_update(request: web.Request, id, body) -> web.Response:
    """users_users_update

    

    :param id: A unique integer value identifying this user.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WritableUser.from_dict(body)
    return web.Response(status=200)
