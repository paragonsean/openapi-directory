from typing import List, Dict
from aiohttp import web

from openapi_server.models.show_resources_for_all_accounts200_response_inner import ShowResourcesForAllAccounts200ResponseInner
from openapi_server import util


async def show_resource(request: web.Request, account, kind, identifier, x_request_id=None, permitted_roles=None, privilege=None, check=None, role=None) -> web.Response:
    """Shows a description of a single resource.

    Details about a single resource.  If &#x60;permitted_roles&#x60; and &#x60;privilege&#x60; are given, Conjur lists the roles with the specified privilege on the resource.  If &#x60;check&#x60;, &#x60;privilege&#x60; and &#x60;role&#x60; are given, Conjur checks if the specified role has the privilege on the resource.  If &#x60;permitted_roles&#x60; and &#x60;check&#x60; are both given, Conjur responds to the &#x60;check&#x60; call ONLY.  ##### Permissions Required 

    :param account: Organization account name
    :type account: str
    :param kind: Type of resource
    :type kind: str
    :param identifier: ID of the resource for which to get the information about
    :type identifier: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param permitted_roles: Lists the roles which have the named privilege on a resource.
    :type permitted_roles: bool
    :param privilege: Level of privilege to filter on. Can only be used in combination with &#x60;permitted_roles&#x60; or &#x60;check&#x60; parameter.
    :type privilege: str
    :param check: Check whether a role has a privilege on a resource.
    :type check: bool
    :param role: Role to check privilege on. Can only be used in combination with &#x60;check&#x60; parameter.
    :type role: str

    """
    return web.Response(status=200)


async def show_resources_for_account(request: web.Request, account, x_request_id=None, kind=None, search=None, offset=None, limit=None, count=None, role=None, acting_as=None) -> web.Response:
    """Lists resources within an organization account.

    Lists resources within an organization account.  If a &#x60;kind&#x60; query parameter is given, narrows results to only resources of that kind.  If a &#x60;limit&#x60; is given, returns no more than that number of results. Providing an &#x60;offset&#x60; skips a number of resources before returning the rest. In addition, providing an &#x60;offset&#x60; will give &#x60;limit&#x60; a default value of 10 if none other is provided. These two parameters can be combined to page through results.  If the parameter &#x60;count&#x60; is &#x60;true&#x60;, returns only the number of items in the list.  ##### Text search  If the &#x60;search&#x60; parameter is provided, narrows results to those pertaining to the search query. Search works across resource IDs and the values of annotations. It weighs results so that those with matching id or a matching value of an annotation called &#x60;name&#x60; appear first, then those with another matching annotation value, and finally those with a matching  &#x60;kind&#x60;. 

    :param account: Organization account name
    :type account: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param kind: Type of resource
    :type kind: str
    :param search: Filter resources based on this value by name
    :type search: dict | bytes
    :param offset: When listing resources, start at this item number.
    :type offset: int
    :param limit: When listing resources, return up to this many results.
    :type limit: int
    :param count: When listing resources, if &#x60;true&#x60;, return only the count of the results.
    :type count: bool
    :param role: Retrieves the resources list for a different role if the authenticated role has access
    :type role: str
    :param acting_as: Retrieves the resources list for a different role if the authenticated role has access
    :type acting_as: str

    """
    search = .from_dict(search)
    return web.Response(status=200)


async def show_resources_for_all_accounts(request: web.Request, x_request_id=None, account=None, kind=None, search=None, offset=None, limit=None, count=None, role=None, acting_as=None) -> web.Response:
    """Lists resources within an organization account.

    Lists resources within an organization account.  In the absence of an &#x60;account&#x60; query parameter, shows results for the account of the authorization token user.  If an &#x60;account&#x60; query parameter is given, shows results for the specified account.  If a &#x60;kind&#x60; query parameter is given, narrows results to only resources of that kind.  If a &#x60;limit&#x60; is given, returns no more than that number of results. Providing an &#x60;offset&#x60; skips a number of resources before returning the rest. In addition, providing an &#x60;offset&#x60; will give &#x60;limit&#x60; a default value of 10 if none other is provided. These two parameters can be combined to page through results.  If the parameter &#x60;count&#x60; is &#x60;true&#x60;, returns only the number of items in the list.  ##### Text search  If the &#x60;search&#x60; parameter is provided, narrows results to those pertaining to the search query. Search works across resource IDs and the values of annotations. It weighs results so that those with matching id or a matching value of an annotation called &#x60;name&#x60; appear first, then those with another matching annotation value, and finally those with a matching  &#x60;kind&#x60;.\&quot; 

    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param account: Organization account name
    :type account: str
    :param kind: Type of resource
    :type kind: str
    :param search: Filter resources based on this value by name
    :type search: str
    :param offset: When listing resources, start at this item number.
    :type offset: int
    :param limit: When listing resources, return up to this many results.
    :type limit: int
    :param count: When listing resources, if &#x60;true&#x60;, return only the count of the results.
    :type count: bool
    :param role: Retrieves the resources list for a different role if the authenticated role has access
    :type role: str
    :param acting_as: Retrieves the resources list for a different role if the authenticated role has access
    :type acting_as: str

    """
    return web.Response(status=200)


async def show_resources_for_kind(request: web.Request, account, kind, x_request_id=None, search=None, offset=None, limit=None, count=None, role=None, acting_as=None) -> web.Response:
    """Lists resources of the same kind within an organization account.

    Lists resources of the same kind within an organization account.  Kinds of resources include: policy, user, host, group, layer, or variable  If a &#x60;limit&#x60; is given, returns no more than that number of results. Providing an &#x60;offset&#x60; skips a number of resources before returning the rest. In addition, providing an &#x60;offset&#x60; will give &#x60;limit&#x60; a default value of 10 if none other is provided. These two parameters can be combined to page through results.  If the parameter &#x60;count&#x60; is &#x60;true&#x60;, returns only the number of items in the list.  ##### Text search  If the &#x60;search&#x60; parameter is provided, narrows results to those pertaining to the search query. Search works across resource IDs and the values of annotations. It weighs results so that those with matching id or a matching value of an annotation called &#x60;name&#x60; appear first, then those with another matching annotation value, and finally those with a matching  &#x60;kind&#x60;. 

    :param account: Organization account name
    :type account: str
    :param kind: Type of resource
    :type kind: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param search: Filter resources based on this value by name
    :type search: dict | bytes
    :param offset: When listing resources, start at this item number.
    :type offset: int
    :param limit: When listing resources, return up to this many results.
    :type limit: int
    :param count: When listing resources, if &#x60;true&#x60;, return only the count of the results.
    :type count: bool
    :param role: Retrieves the resources list for a different role if the authenticated role has access
    :type role: str
    :param acting_as: Retrieves the resources list for a different role if the authenticated role has access
    :type acting_as: str

    """
    search = .from_dict(search)
    return web.Response(status=200)
