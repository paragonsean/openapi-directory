from typing import List, Dict
from aiohttp import web

from openapi_server.models.enumeration_set import EnumerationSet
from openapi_server.models.enumeration_value import EnumerationValue
from openapi_server.models.errors import Errors
from openapi_server.models.items_enumeration_value import ItemsEnumerationValue
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.security_entry import SecurityEntry
from openapi_server import util


async def enumeration_set_create_security_entry(request: web.Request, web_id, security_entry, apply_to_children=None, web_id_type=None) -> web.Response:
    """Create a security entry owned by the enumeration set.

    

    :param web_id: The ID of the enumeration set where the security entry will be created.
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


async def enumeration_set_create_value(request: web.Request, web_id, enumeration_value, web_id_type=None) -> web.Response:
    """Create an enumeration value for a enumeration set.

    

    :param web_id: The ID of the enumeration set on which to create the enumeration value.
    :type web_id: str
    :param enumeration_value: The new enumeration value definition.
    :type enumeration_value: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    enumeration_value = EnumerationValue.from_dict(enumeration_value)
    return web.Response(status=200)


async def enumeration_set_delete(request: web.Request, web_id) -> web.Response:
    """Delete an enumeration set.

    

    :param web_id: The ID of the enumeration set to delete.
    :type web_id: str

    """
    return web.Response(status=200)


async def enumeration_set_delete_security_entry(request: web.Request, name, web_id, apply_to_children=None) -> web.Response:
    """Delete a security entry owned by the enumeration set.

    

    :param name: The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    :type name: str
    :param web_id: The ID of the enumeration set where the security entry will be deleted.
    :type web_id: str
    :param apply_to_children: If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    :type apply_to_children: bool

    """
    return web.Response(status=200)


async def enumeration_set_get(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an enumeration set.

    

    :param web_id: The ID of the enumeration set.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def enumeration_set_get_by_path(request: web.Request, path, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an enumeration set by path.

    This method returns an enumeration set based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

    :param path: The path to the target enumeration set.
    :type path: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def enumeration_set_get_security(request: web.Request, web_id, user_identity, force_refresh=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Get the security information of the specified security item associated with the enumeration set for a specified user.

    

    :param web_id: The ID of the enumeration set for the security to be checked.
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


async def enumeration_set_get_security_entries(request: web.Request, web_id, name_filter=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the security entries associated with the enumeration set based on the specified criteria. By default, all security entries for this enumeration set are returned.

    

    :param web_id: The ID of the enumeration set.
    :type web_id: str
    :param name_filter: The name query string used for filtering security entries. The default is no filter.
    :type name_filter: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def enumeration_set_get_security_entry_by_name(request: web.Request, name, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the security entry associated with the enumeration set with the specified name.

    

    :param name: The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    :type name: str
    :param web_id: The ID of the enumeration set.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def enumeration_set_get_values(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an enumeration set&#39;s values.

    

    :param web_id: The ID of the enumeration set.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def enumeration_set_update(request: web.Request, web_id, enumeration_set) -> web.Response:
    """Update an enumeration set by replacing items in its definition.

    

    :param web_id: The ID of the enumeration set to update.
    :type web_id: str
    :param enumeration_set: A partial enumeration set containing the desired changes.
    :type enumeration_set: dict | bytes

    """
    enumeration_set = EnumerationSet.from_dict(enumeration_set)
    return web.Response(status=200)


async def enumeration_set_update_security_entry(request: web.Request, name, web_id, security_entry, apply_to_children=None) -> web.Response:
    """Update a security entry owned by the enumeration set.

    

    :param name: The name of the security entry.
    :type name: str
    :param web_id: The ID of the enumeration set where the security entry will be updated.
    :type web_id: str
    :param security_entry: The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
    :type security_entry: dict | bytes
    :param apply_to_children: If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    :type apply_to_children: bool

    """
    security_entry = SecurityEntry.from_dict(security_entry)
    return web.Response(status=200)
