from typing import List, Dict
from aiohttp import web

from openapi_server.models.analysis import Analysis
from openapi_server.models.errors import Errors
from openapi_server.models.items_analysis import ItemsAnalysis
from openapi_server.models.items_analysis_category import ItemsAnalysisCategory
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.security_entry import SecurityEntry
from openapi_server import util


async def analysis_create_security_entry(request: web.Request, web_id, security_entry, apply_to_children=None, web_id_type=None) -> web.Response:
    """Create a security entry owned by the analysis.

    

    :param web_id: The ID of the analysis, where the security entry will be created.
    :type web_id: str
    :param security_entry: The new security entry definition. The full list of allow and deny rights must be supplied.
    :type security_entry: dict | bytes
    :param apply_to_children: If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    :type apply_to_children: bool
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    security_entry = SecurityEntry.from_dict(security_entry)
    return web.Response(status=200)


async def analysis_delete(request: web.Request, web_id) -> web.Response:
    """Delete an Analysis.

    

    :param web_id: The ID of the Analysis to delete.
    :type web_id: str

    """
    return web.Response(status=200)


async def analysis_delete_security_entry(request: web.Request, name, web_id, apply_to_children=None) -> web.Response:
    """Delete a security entry owned by the analysis.

    

    :param name: The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    :type name: str
    :param web_id: The ID of the analysis, where the security entry will be deleted.
    :type web_id: str
    :param apply_to_children: If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    :type apply_to_children: bool

    """
    return web.Response(status=200)


async def analysis_get(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an Analysis.

    

    :param web_id: The ID of the Analysis.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def analysis_get_analyses_query(request: web.Request, database_web_id=None, max_count=None, query=None, selected_fields=None, start_index=None, web_id_type=None) -> web.Response:
    """Retrieve analyses based on the specified conditions. By default, returns all analyses.

    

    :param database_web_id: The ID of the asset database to use as the root of the query.
    :type database_web_id: str
    :param max_count: The maximum number of objects to be returned per call (page size). The default is 1000.
    :type max_count: int
    :param query: The query string is a list of filters used to perform an AFSearch for the analyses in the asset database. An example would be: \&quot;query&#x3D; Name:&#x3D;MyAnalysis1* Template:&#x3D;AnalysisTemplate\&quot;.
    :type query: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param start_index: The starting index (zero based) of the items to be returned. The default is 0.
    :type start_index: int
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def analysis_get_by_path(request: web.Request, path, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an Analysis by path.

    This method returns an Analysis based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

    :param path: The path to the Analysis.
    :type path: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def analysis_get_categories(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Get an Analysis&#39; categories.

    

    :param web_id: The ID of the Analysis.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def analysis_get_security(request: web.Request, web_id, user_identity, force_refresh=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Get the security information of the specified security item associated with the Analysis for a specified user.

    

    :param web_id: The ID of the Analysis for the security to be checked.
    :type web_id: str
    :param user_identity: The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user&#39;s security rights will be returned.
    :type user_identity: List[str]
    :param force_refresh: Indicates if the security cache should be refreshed before getting security information. The default is &#39;false&#39;.
    :type force_refresh: bool
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def analysis_get_security_entries(request: web.Request, web_id, name_filter=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the security entries associated with the analysis based on the specified criteria. By default, all security entries for this analysis are returned.

    

    :param web_id: The ID of the analysis.
    :type web_id: str
    :param name_filter: The name query string used for filtering security entries. The default is no filter.
    :type name_filter: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def analysis_get_security_entry_by_name(request: web.Request, name, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the security entry associated with the analysis with the specified name.

    

    :param name: The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    :type name: str
    :param web_id: The ID of the analysis.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def analysis_update(request: web.Request, web_id, analysis) -> web.Response:
    """Update an Analysis.

    

    :param web_id: The ID of the Analysis to update.
    :type web_id: str
    :param analysis: A partial Analysis containing the desired changes.
    :type analysis: dict | bytes

    """
    analysis = Analysis.from_dict(analysis)
    return web.Response(status=200)


async def analysis_update_security_entry(request: web.Request, name, web_id, security_entry, apply_to_children=None) -> web.Response:
    """Update a security entry owned by the analysis.

    

    :param name: The name of the security entry.
    :type name: str
    :param web_id: The ID of the analysis, where the security entry will be updated.
    :type web_id: str
    :param security_entry: The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
    :type security_entry: dict | bytes
    :param apply_to_children: If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    :type apply_to_children: bool

    """
    security_entry = SecurityEntry.from_dict(security_entry)
    return web.Response(status=200)
