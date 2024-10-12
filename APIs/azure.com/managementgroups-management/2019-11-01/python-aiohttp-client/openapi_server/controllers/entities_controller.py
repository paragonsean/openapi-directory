from typing import List, Dict
from aiohttp import web

from openapi_server.models.entity_list_result import EntityListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def entities_list(request: web.Request, api_version, skiptoken=None, skip=None, top=None, select=None, search=None, filter=None, view=None, group_name=None, cache_control=None) -> web.Response:
    """entities_list

    List all entities (Management Groups, Subscriptions, etc.) for the authenticated user.

    :param api_version: Version of the API to be used with the client request. The current version is 2018-01-01-preview.
    :type api_version: str
    :param skiptoken: Page continuation token is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a token parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str
    :param skip: Number of entities to skip over when retrieving results. Passing this in will override $skipToken.
    :type skip: int
    :param top: Number of elements to return when retrieving results. Passing this in will override $skipToken.
    :type top: int
    :param select: This parameter specifies the fields to include in the response. Can include any combination of Name,DisplayName,Type,ParentDisplayNameChain,ParentChain, e.g. &#39;$select&#x3D;Name,DisplayName,Type,ParentDisplayNameChain,ParentNameChain&#39;. When specified the $select parameter can override select in $skipToken.
    :type select: str
    :param search: The $search parameter is used in conjunction with the $filter parameter to return three different outputs depending on the parameter passed in. With $search&#x3D;AllowedParents the API will return the entity info of all groups that the requested entity will be able to reparent to as determined by the user&#39;s permissions.With $search&#x3D;AllowedChildren the API will return the entity info of all entities that can be added as children of the requested entity.With $search&#x3D;ParentAndFirstLevelChildren the API will return the parent and  first level of children that the user has either direct access to or indirect access via one of their descendants.With $search&#x3D;ParentOnly the API will return only the group if the user has access to at least one of the descendants of the group.With $search&#x3D;ChildrenOnly the API will return only the first level of children of the group entity info specified in $filter.  The user must have direct access to the children entities or one of it&#39;s descendants for it to show up in the results.
    :type search: str
    :param filter: The filter parameter allows you to filter on the the name or display name fields. You can check for equality on the name field (e.g. name eq &#39;{entityName}&#39;)  and you can check for substrings on either the name or display name fields(e.g. contains(name, &#39;{substringToSearch}&#39;), contains(displayName, &#39;{substringToSearch&#39;)). Note that the &#39;{entityName}&#39; and &#39;{substringToSearch}&#39; fields are checked case insensitively.
    :type filter: str
    :param view: The view parameter allows clients to filter the type of data that is returned by the getEntities call.
    :type view: str
    :param group_name: A filter which allows the get entities call to focus on a particular group (i.e. \&quot;$filter&#x3D;name eq &#39;groupName&#39;\&quot;)
    :type group_name: str
    :param cache_control: Indicates that the request shouldn&#39;t utilize any caches.
    :type cache_control: str

    """
    return web.Response(status=200)
