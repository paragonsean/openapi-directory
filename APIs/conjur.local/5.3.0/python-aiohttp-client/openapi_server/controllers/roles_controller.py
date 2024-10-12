from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def add_member_to_role(request: web.Request, account, kind, identifier, members, member, x_request_id=None) -> web.Response:
    """Update or modify an existing role membership

    Updates or modifies an existing role membership.  If a role A is granted to a role B, then role A is said to have role B as a member. These relationships are described in the “members” portion of the returned JSON.  When the &#x60;members&#x60; query parameter is provided, you will get the members of a role.  When the &#x60;members&#x60; and &#x60;member&#x60; query parameters are provided, the role specfified by &#x60;member&#x60; will be added as a member of the role specified in the endpoint URI. 

    :param account: Organization account name
    :type account: str
    :param kind: Type of resource
    :type kind: str
    :param identifier: ID of the role for which to get the information about
    :type identifier: str
    :param members: Returns a list of the Role&#39;s members.
    :type members: str
    :param member: The identifier of the Role to be added as a member.
    :type member: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str

    """
    return web.Response(status=200)


async def remove_member_from_role(request: web.Request, account, kind, identifier, members, member, x_request_id=None) -> web.Response:
    """Deletes an existing role membership

    Deletes an existing role membership.  If a role A is granted to a role B, then role A is said to have role B as a member. These relationships are described in the “members” portion of the returned JSON.  When the &#x60;members&#x60; query parameter is provided, you will get the members of a role.  When the &#x60;members&#x60; and &#x60;member&#x60; query parameters are provided, the role specfified by &#x60;member&#x60; will be removed as a member of the role specified in the endpoint URI. 

    :param account: Organization account name
    :type account: str
    :param kind: Type of resource
    :type kind: str
    :param identifier: ID of the role for which to get the information about
    :type identifier: str
    :param members: Returns a list of the Role&#39;s members.
    :type members: str
    :param member: The identifier of the Role to be added as a member.
    :type member: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str

    """
    return web.Response(status=200)


async def show_role(request: web.Request, account, kind, identifier, x_request_id=None, all=None, memberships=None, members=None, offset=None, limit=None, count=None, search=None, graph=None) -> web.Response:
    """Get role information

    Gets detailed information about a specific role, including the role members.  If a role A is granted to a role B, then role A is said to have role B as a member. These relationships are described in the “members” portion of the returned JSON.  ##### Listing members  If &#x60;members&#x60; is provided, you will get the members of a role.  If a &#x60;kind&#x60; query parameter is given, narrows results to only resources of that kind.  If a &#x60;limit&#x60; is given, returns no more than that number of results. Providing an &#x60;offset&#x60; skips a number of resources before returning the rest. In addition, providing an &#x60;offset&#x60; will give limit a default value of 10 if none other is provided. These two parameters can be combined to page through results.  If the parameter &#x60;count&#x60; is true, returns only the number of items in the list.  ##### Text search  If the search parameter is provided, narrows results to those pertaining to the search query. Search works across resource IDs and the values of annotations. It weights results so that those with matching id or a matching value of an annotation called name appear first, then those with another matching annotation value, and finally those with a matching kind.  ##### Parameter Priority  If Conjur is given any combination of optional parameters, it responds with ONLY results for the parameter of the highest priority.  1. &#x60;graph&#x60; 2. &#x60;all&#x60; 3. &#x60;memberships&#x60; 4. &#x60;members&#x60; 

    :param account: Organization account name
    :type account: str
    :param kind: Type of resource
    :type kind: str
    :param identifier: ID of the role for which to get the information about
    :type identifier: str
    :param x_request_id: Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    :type x_request_id: str
    :param all: Returns an array of Role IDs representing all role memberships, expanded recursively.
    :type all: str
    :param memberships: Returns all direct role memberships (members not expanded recursively).
    :type memberships: str
    :param members: Returns a list of the Role&#39;s members.
    :type members: str
    :param offset: When listing members, start at this item number.
    :type offset: int
    :param limit: When listing members, return up to this many results.
    :type limit: int
    :param count: When listing members, if &#x60;true&#x60;, return only the count of members.
    :type count: bool
    :param search: When listing members, the results will be narrowed to only those matching the provided string
    :type search: str
    :param graph: If included in the query returns a graph view of the role
    :type graph: str

    """
    return web.Response(status=200)
