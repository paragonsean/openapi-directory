from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.paginated_change_descriptions import PaginatedChangeDescriptions
from openapi_server import util


async def changelog_adhoc_get(request: web.Request, filter=None) -> web.Response:
    """Allows an arbitrary filter to be specified and applied to the org\\&#39;s change log.

    Perform an adhoc query against the change log for your org. The filter is a JSON encoded FilterSum as defined in this file.

    :param filter: Encoded FilterSums representing the query you would like to execute. See object definition for details.
    :type filter: str

    """
    return web.Response(status=200)


async def changelog_cluster_graph_cluster_key_get(request: web.Request, cluster_key, start=None, end=None, max_results=None, ref_id=None, direction=None) -> web.Response:
    """get changes related to the indicated cluster

    Gets all changes to a cluster. 

    :param cluster_key: the cluster key to see an audit log for
    :type cluster_key: str
    :param start: The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    :type start: 
    :param end: The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    :type end: 
    :param max_results: Determines how many ChangeDescription object should be returned to the calling code. 
    :type max_results: 
    :param ref_id: When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
    :type ref_id: str
    :param direction: If set to \&quot;before\&quot; then changes will be returned that occurred before reference ID. If \&quot;after\&quot; then changes will be returned that have occurred since the reference ID. 
    :type direction: str

    """
    return web.Response(status=200)


async def changelog_domain_graph_domain_key_get(request: web.Request, domain_key, start=None, end=None, max_results=None, ref_id=None, direction=None) -> web.Response:
    """get changes related to the indicated domain

    Gets all changes to a domain, the proxies that front the specified domain, routes within that domain, the shared rules of each route, the clusters connected via route or shared rules. 

    :param domain_key: the domain key to see an audit log for
    :type domain_key: str
    :param start: The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    :type start: 
    :param end: The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    :type end: 
    :param max_results: Determines how many ChangeDescription object should be returned to the calling code. 
    :type max_results: 
    :param ref_id: When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
    :type ref_id: str
    :param direction: If set to \&quot;before\&quot; then changes will be returned that occurred before reference ID. If \&quot;after\&quot; then changes will be returned that have occurred since the reference ID. 
    :type direction: str

    """
    return web.Response(status=200)


async def changelog_route_graph_route_key_get(request: web.Request, route_key, start=None, end=None, max_results=None, ref_id=None, direction=None) -> web.Response:
    """get changes related to the indicated route

    Gets all changes to a route, the domains associated with it, the shared rules it references, and the clusters connected to it. 

    :param route_key: the route key to see an audit log for
    :type route_key: str
    :param start: The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    :type start: 
    :param end: The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    :type end: 
    :param max_results: Determines how many ChangeDescription object should be returned to the calling code. 
    :type max_results: 
    :param ref_id: When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
    :type ref_id: str
    :param direction: If set to \&quot;before\&quot; then changes will be returned that occurred before reference ID. If \&quot;after\&quot; then changes will be returned that have occurred since the reference ID. 
    :type direction: str

    """
    return web.Response(status=200)


async def changelog_shared_rules_graph_shared_rules_key_get(request: web.Request, shared_rules_key, start=None, end=None, max_results=None, ref_id=None, direction=None) -> web.Response:
    """get changes related to the indicated SharedRules

    Gets all changes associated with set of Shared Rules; the domains using it and the clusters referenced by it. 

    :param shared_rules_key: the shared rules key to see an audit log for
    :type shared_rules_key: str
    :param start: The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    :type start: 
    :param end: The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    :type end: 
    :param max_results: Determines how many ChangeDescription object should be returned to the calling code. 
    :type max_results: 
    :param ref_id: When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
    :type ref_id: str
    :param direction: If set to \&quot;before\&quot; then changes will be returned that occurred before reference ID. If \&quot;after\&quot; then changes will be returned that have occurred since the reference ID. 
    :type direction: str

    """
    return web.Response(status=200)


async def changelog_zone_zone_key_get(request: web.Request, zone_key, start=None, end=None, max_results=None, ref_id=None, direction=None) -> web.Response:
    """get changes in a specified zone

    Retrieve all changes in the specified zone.

    :param zone_key: the zone key to see an audit log for
    :type zone_key: str
    :param start: The beginning of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    :type start: 
    :param end: The end of the window we want to see changes for; measured in microseconds since Unix Epoch. 
    :type end: 
    :param max_results: Determines how many ChangeDescription object should be returned to the calling code. 
    :type max_results: 
    :param ref_id: When paginating a Changelog request start on the entry that comes immediately before or after this ID (as determined by the direction argument). 
    :type ref_id: str
    :param direction: If set to \&quot;before\&quot; then changes will be returned that occurred before reference ID. If \&quot;after\&quot; then changes will be returned that have occurred since the reference ID. 
    :type direction: str

    """
    return web.Response(status=200)
