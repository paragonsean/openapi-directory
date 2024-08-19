from typing import List, Dict
from aiohttp import web

from openapi_server.models.analysis_rule import AnalysisRule
from openapi_server.models.items_analysis_rule import ItemsAnalysisRule
from openapi_server import util


async def analysis_rule_create_analysis_rule(request: web.Request, web_id, analysis_rule, web_id_type=None) -> web.Response:
    """Create a new Analysis Rule as a child of an existing Analysis Rule.

    

    :param web_id: The ID of the parent Analysis Rule, on which to create the child Analysis Rule.
    :type web_id: str
    :param analysis_rule: The definition of the new Analysis Rule.
    :type analysis_rule: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    analysis_rule = AnalysisRule.from_dict(analysis_rule)
    return web.Response(status=200)


async def analysis_rule_delete(request: web.Request, web_id) -> web.Response:
    """Delete an Analysis Rule.

    

    :param web_id: The ID of the Analysis Rule.
    :type web_id: str

    """
    return web.Response(status=200)


async def analysis_rule_get(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an Analysis Rule.

    

    :param web_id: The ID of the Analysis Rule.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def analysis_rule_get_analysis_rules(request: web.Request, web_id, max_count=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, web_id_type=None) -> web.Response:
    """Get the child Analysis Rules of the Analysis Rule.

    

    :param web_id: The ID of the parent Analysis Rule.
    :type web_id: str
    :param max_count: The maximum number of objects to be returned per call (page size). The default is 1000.
    :type max_count: int
    :param name_filter: The name query string used for finding Analysis Rules. The default is no filter.
    :type name_filter: str
    :param search_full_hierarchy: Specifies if the search should include Analysis Rules nested further than the immediate children of the searchRoot. The default is &#39;false&#39;.
    :type search_full_hierarchy: bool
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param sort_field: The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;.
    :type sort_order: str
    :param start_index: The starting index (zero based) of the items to be returned. The default is 0.
    :type start_index: int
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def analysis_rule_get_by_path(request: web.Request, path, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an Analysis Rule by path.

    This method returns an Analysis Rule based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

    :param path: The path to the Analysis Rule.
    :type path: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def analysis_rule_update(request: web.Request, web_id, analysis_rule) -> web.Response:
    """Update an Analysis Rule by replacing items in its definition.

    

    :param web_id: The ID of the Analysis Rule.
    :type web_id: str
    :param analysis_rule: A partial Analysis Rule containing the desired changes.
    :type analysis_rule: dict | bytes

    """
    analysis_rule = AnalysisRule.from_dict(analysis_rule)
    return web.Response(status=200)
