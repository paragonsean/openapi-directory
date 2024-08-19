from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors import Errors
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.items_table_category import ItemsTableCategory
from openapi_server.models.security_entry import SecurityEntry
from openapi_server.models.table import Table
from openapi_server.models.table_data import TableData
from openapi_server import util


async def table_create_security_entry(request: web.Request, web_id, security_entry, apply_to_children=None, web_id_type=None) -> web.Response:
    """Create a security entry owned by the table.

    

    :param web_id: The ID of the table where the security entry will be created.
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


async def table_delete(request: web.Request, web_id) -> web.Response:
    """Delete a table.

    

    :param web_id: The ID of the table to delete.
    :type web_id: str

    """
    return web.Response(status=200)


async def table_delete_security_entry(request: web.Request, name, web_id, apply_to_children=None) -> web.Response:
    """Delete a security entry owned by the table.

    

    :param name: The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    :type name: str
    :param web_id: The ID of the table where the security entry will be deleted.
    :type web_id: str
    :param apply_to_children: If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    :type apply_to_children: bool

    """
    return web.Response(status=200)


async def table_get(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a table.

    

    :param web_id: The ID of the table.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def table_get_by_path(request: web.Request, path, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a table by path.

    

    :param path: The path to the table.
    :type path: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def table_get_categories(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Get a table&#39;s categories.

    

    :param web_id: The ID of the table.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def table_get_data(request: web.Request, web_id, selected_fields=None) -> web.Response:
    """Get the table&#39;s data.

    

    :param web_id: The ID of the table.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str

    """
    return web.Response(status=200)


async def table_get_security(request: web.Request, web_id, user_identity, force_refresh=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Get the security information of the specified security item associated with the table for a specified user.

    

    :param web_id: The ID of the table for the security to be checked.
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


async def table_get_security_entries(request: web.Request, web_id, name_filter=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the security entries associated with the table based on the specified criteria. By default, all security entries for this table are returned.

    

    :param web_id: The ID of the table.
    :type web_id: str
    :param name_filter: The name query string used for filtering security entries. The default is no filter.
    :type name_filter: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def table_get_security_entry_by_name(request: web.Request, name, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the security entry associated with the table with the specified name.

    

    :param name: The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    :type name: str
    :param web_id: The ID of the table.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def table_update(request: web.Request, web_id, table) -> web.Response:
    """Update a table by replacing items in its definition.

    

    :param web_id: The ID of the table to update.
    :type web_id: str
    :param table: A partial table containing the desired changes.
    :type table: dict | bytes

    """
    table = Table.from_dict(table)
    return web.Response(status=200)


async def table_update_data(request: web.Request, web_id, data) -> web.Response:
    """Update the table&#39;s data.

    

    :param web_id: The ID of the table on which to update the data.
    :type web_id: str
    :param data: The new table data definition.
    :type data: dict | bytes

    """
    data = TableData.from_dict(data)
    return web.Response(status=200)


async def table_update_security_entry(request: web.Request, name, web_id, security_entry, apply_to_children=None) -> web.Response:
    """Update a security entry owned by the table.

    

    :param name: The name of the security entry.
    :type name: str
    :param web_id: The ID of the table where the security entry will be updated.
    :type web_id: str
    :param security_entry: The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
    :type security_entry: dict | bytes
    :param apply_to_children: If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    :type apply_to_children: bool

    """
    security_entry = SecurityEntry.from_dict(security_entry)
    return web.Response(status=200)
