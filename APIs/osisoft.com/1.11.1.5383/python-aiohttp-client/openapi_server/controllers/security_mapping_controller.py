from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.security_entry import SecurityEntry
from openapi_server.models.security_mapping import SecurityMapping
from openapi_server import util


async def security_mapping_delete(request: web.Request, web_id) -> web.Response:
    """Delete a security mapping.

    

    :param web_id: The ID of the security mapping.
    :type web_id: str

    """
    return web.Response(status=200)


async def security_mapping_get(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a security mapping.

    

    :param web_id: The ID of the security mapping.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def security_mapping_get_by_path(request: web.Request, path, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a security mapping by path.

    This method returns a security mapping based on the path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

    :param path: The path to the security mapping.
    :type path: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def security_mapping_get_security(request: web.Request, web_id, user_identity, force_refresh=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Get the security information of the specified security item associated with the security mapping for a specified user.

    

    :param web_id: The ID of the security mapping for the security to be checked.
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


async def security_mapping_get_security_entries(request: web.Request, web_id, name_filter=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the security entries associated with the security mapping based on the specified criteria. By default, all security entries for this security mapping are returned.

    

    :param web_id: The ID of the security mapping.
    :type web_id: str
    :param name_filter: The name query string used for filtering security entries. The default is no filter.
    :type name_filter: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def security_mapping_get_security_entry_by_name(request: web.Request, name, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the security entry associated with the security mapping with the specified name.

    

    :param name: The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    :type name: str
    :param web_id: The ID of the security mapping.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def security_mapping_update(request: web.Request, web_id, security_mapping) -> web.Response:
    """Update a security mapping by replacing items in its definition.

    

    :param web_id: The ID of the security mapping.
    :type web_id: str
    :param security_mapping: A partial security mapping containing the desired changes.
    :type security_mapping: dict | bytes

    """
    security_mapping = SecurityMapping.from_dict(security_mapping)
    return web.Response(status=200)
