from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def action_organization_activity_list_get(request: web.Request, id=None) -> web.Response:
    """Get the activity stream of an organization

    Return an organization&#39;s activity stream

    :param id: The id or name of the organization
    :type id: str

    """
    return web.Response(status=200)


async def action_organization_activity_list_html_get(request: web.Request, id=None) -> web.Response:
    """Get the activity stream of an organization, HTML format

    Return an organization&#39;s activity stream as HTML

    :param id: The id or name of the organization
    :type id: str

    """
    return web.Response(status=200)


async def action_organization_autocomplete_get(request: web.Request, q=None, limit=None) -> web.Response:
    """Get names of organizations that match a query string

    Return a list of organization names that contain a string

    :param q: The string to search for
    :type q: str
    :param limit: The maximum number of organizations to return (optional)
    :type limit: int

    """
    return web.Response(status=200)


async def action_organization_follower_count_get(request: web.Request, id=None) -> web.Response:
    """Get number of followers of an organization

    Return the number of followers of an organization

    :param id: The id or name of the organization
    :type id: str

    """
    return web.Response(status=200)


async def action_organization_follower_list_get(request: web.Request, id=None) -> web.Response:
    """Get users following an organization

    Return a list of users that are following a given organization

    :param id: The id or name of the organization
    :type id: str

    """
    return web.Response(status=200)


async def action_organization_list_for_user_get(request: web.Request, permission=None) -> web.Response:
    """Get organizations that a user has a given permission for

    Return the organizations that the user has a given permission for

    :param permission: The permission the user has against the returned organization
    :type permission: str

    """
    return web.Response(status=200)


async def action_organization_list_get(request: web.Request, offset=None, limit=None) -> web.Response:
    """Get names of all organizations

    Returns the names of all indexed organizations

    :param offset: The offset (index) of the first organizations to return
    :type offset: int
    :param limit: The number of organizations to be returned per page
    :type limit: int

    """
    return web.Response(status=200)


async def action_organization_revision_list_get(request: web.Request, id=None) -> web.Response:
    """Get organization revisions

    Return an organization&#39;s revisions

    :param id: The name or id of the organization
    :type id: str

    """
    return web.Response(status=200)


async def action_organization_show_get(request: web.Request, id=None, include_datasets=None) -> web.Response:
    """Get details of a specific organization

    Return the details of an organization

    :param id: The id or name of the organization
    :type id: str
    :param include_datasets: include a list of the organization&#39;s datasets
    :type include_datasets: bool

    """
    return web.Response(status=200)


async def action_package_activity_list_get(request: web.Request, id=None, offset=None, limit=None) -> web.Response:
    """Get the activity stream of a package (dataset)

    Returns a package&#39;s activity stream

    :param id: The id or name of the package
    :type id: str
    :param offset: Where to start getting activity items from
    :type offset: int
    :param limit: The maximum number of activities to return
    :type limit: int

    """
    return web.Response(status=200)


async def action_package_activity_list_html_get(request: web.Request, id=None, offset=None, limit=None) -> web.Response:
    """Get the activity stream of a package (dataset), HTML format

    The activity stream is rendered as a snippet of HTML meant to be included in an HTML pag, i.e it doesn&#39;t have any header or footer.

    :param id: The id or name of the package
    :type id: str
    :param offset: Where to start getting activity items from
    :type offset: int
    :param limit: The maximum number of activities to return
    :type limit: int

    """
    return web.Response(status=200)


async def action_package_autocomplete_get(request: web.Request, q=None, limit=None) -> web.Response:
    """Find packages (datasets) matching a query

    Return a list of datasets that match a string

    :param q: The string to query
    :type q: str
    :param limit: The maximum number of resource formats to return
    :type limit: int

    """
    return web.Response(status=200)


async def action_package_list_get(request: web.Request, offset=None, limit=None) -> web.Response:
    """Get a list of all packages (datasets)

    Returns the names of all indexed packages (datasets)

    :param offset: The offset (index) of the first package to return
    :type offset: int
    :param limit: The number of packages to be returned per page
    :type limit: int

    """
    return web.Response(status=200)


async def action_package_relationships_list_get(request: web.Request, id=None, id2=None, rel=None) -> web.Response:
    """Get package (dataset) relationships

    Return a dataset&#39;s relationships

    :param id: The id or name of the first package
    :type id: str
    :param id2: The id or name of the second package
    :type id2: str
    :param rel: relationship as string
    :type rel: str

    """
    return web.Response(status=200)


async def action_package_revision_list_get(request: web.Request, id=None) -> web.Response:
    """Get list of revisions for a package (dataset)

    Return a dataset&#39;s revision as a list of dictionaries

    :param id: The id or name of the dataset
    :type id: str

    """
    return web.Response(status=200)


async def action_package_search_get(request: web.Request, q=None) -> web.Response:
    """Find packages (datasets) matching query terms

    Searches for packages (datasets) matching the specified query terms

    :param q: A query string
    :type q: str

    """
    return web.Response(status=200)


async def action_package_show_get(request: web.Request, id=None) -> web.Response:
    """Get metadata about one specific package (dataset)

    Returns metadata about the package (dataset) corresponding to the specified unique name

    :param id: The package name
    :type id: str

    """
    return web.Response(status=200)


async def action_related_list_get(request: web.Request, id=None, dataset=None, type_filter=None, sort=None, featured=None) -> web.Response:
    """Gets items related to a package (dataset)

    Returns a dataset&#39;s related items.

    :param id: id or name of the dataset (optional)
    :type id: str
    :param dataset: Dataset dictionary of the dataset (optional)
    :type dataset: str
    :param type_filter: The type of related item to show (optional)
    :type type_filter: str
    :param sort: The order to sort the related items in
    :type sort: str
    :param featured: whether or not to restrict the results to only featured items
    :type featured: str

    """
    return web.Response(status=200)


async def action_resource_search_get(request: web.Request, query=None, fields=None, order_by=None, offset=None, limit=None) -> web.Response:
    """Find resources

    Returns a dictionary with two fields &#x60;&#x60;count&#x60;&#x60; and &#x60;&#x60;results&#x60;&#x60;.             The &#x60;&#x60;count&#x60;&#x60; field contains the total number of Resources                found without the limit or query parameters having an effect.             The &#x60;&#x60;results&#x60;&#x60; field is a list of dictized Resource objects.             The query parameter is a required field. It is a string in                the form &#x60;&#x60;{field}:{term}&#x60;&#x60; or a list of strings, each of the             same form. Within each string, &#x60;&#x60;{field}&#x60;&#x60; is a field or extra             field on the Resource domain object.

    :param query: The search criteria string or list of strings of the form &#x60;&#x60;{field}:{term1}&#x60;&#x60;
    :type query: str
    :param fields: Depreciated
    :type fields: str
    :param order_by: A field on the resource model that orders the results
    :type order_by: str
    :param offset: Apply an offset to the query
    :type offset: int
    :param limit: Apply a limit to the query
    :type limit: int

    """
    return web.Response(status=200)


async def action_resource_show_get(request: web.Request, id=None, include_tracking=None) -> web.Response:
    """Get metadata for a specific resource

    Return the metadata of a resource

    :param id: The id of the resource
    :type id: str
    :param include_tracking: Add tracking information to dataset
    :type include_tracking: bool

    """
    return web.Response(status=200)


async def action_status_show_get(request: web.Request, ) -> web.Response:
    """Get the site status

    Returns the site status


    """
    return web.Response(status=200)


async def action_tag_list_get(request: web.Request, offset=None, limit=None) -> web.Response:
    """Get a list of tags

    Returns the names of all indexed tags

    :param offset: The offset (index) of the first tag to return
    :type offset: int
    :param limit: The number of tags to be returned per page
    :type limit: int

    """
    return web.Response(status=200)
