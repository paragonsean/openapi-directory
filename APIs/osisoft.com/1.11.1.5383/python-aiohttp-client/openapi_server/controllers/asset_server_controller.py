from typing import List, Dict
from aiohttp import web

from openapi_server.models.asset_database import AssetDatabase
from openapi_server.models.asset_server import AssetServer
from openapi_server.models.errors import Errors
from openapi_server.models.items_analysis_rule_plug_in import ItemsAnalysisRulePlugIn
from openapi_server.models.items_asset_database import ItemsAssetDatabase
from openapi_server.models.items_asset_server import ItemsAssetServer
from openapi_server.models.items_notification_contact_template import ItemsNotificationContactTemplate
from openapi_server.models.items_notification_plug_in import ItemsNotificationPlugIn
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_identity import ItemsSecurityIdentity
from openapi_server.models.items_security_mapping import ItemsSecurityMapping
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.items_time_rule_plug_in import ItemsTimeRulePlugIn
from openapi_server.models.items_unit_class import ItemsUnitClass
from openapi_server.models.notification_contact_template import NotificationContactTemplate
from openapi_server.models.security_entry import SecurityEntry
from openapi_server.models.security_identity import SecurityIdentity
from openapi_server.models.security_mapping import SecurityMapping
from openapi_server.models.unit_class import UnitClass
from openapi_server import util


async def asset_server_create_asset_database(request: web.Request, web_id, database, web_id_type=None) -> web.Response:
    """Create an asset database.

    

    :param web_id: The ID of the asset server on which to create the database.
    :type web_id: str
    :param database: The new database definition.
    :type database: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    database = AssetDatabase.from_dict(database)
    return web.Response(status=200)


async def asset_server_create_notification_contact_template(request: web.Request, web_id, notification_contact_template, web_id_type=None) -> web.Response:
    """Create a notification contact template.

    

    :param web_id: The ID of the asset server on which to create the notification contact template.
    :type web_id: str
    :param notification_contact_template: The new notification contact template definition.
    :type notification_contact_template: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    notification_contact_template = NotificationContactTemplate.from_dict(notification_contact_template)
    return web.Response(status=200)


async def asset_server_create_security_entry(request: web.Request, web_id, security_entry, apply_to_children=None, security_item=None, web_id_type=None) -> web.Response:
    """Create a security entry owned by the asset server.

    

    :param web_id: The ID of the asset server where the security entry will be created.
    :type web_id: str
    :param security_entry: The new security entry definition. The full list of allow and deny rights must be supplied.
    :type security_entry: dict | bytes
    :param apply_to_children: If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    :type apply_to_children: bool
    :param security_item: The security item of the desired security entries to be created. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be created.
    :type security_item: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    security_entry = SecurityEntry.from_dict(security_entry)
    return web.Response(status=200)


async def asset_server_create_security_identity(request: web.Request, web_id, security_identity, web_id_type=None) -> web.Response:
    """Create a security identity.

    

    :param web_id: The ID of the asset server on which to create the security identity.
    :type web_id: str
    :param security_identity: The new security identity definition.
    :type security_identity: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    security_identity = SecurityIdentity.from_dict(security_identity)
    return web.Response(status=200)


async def asset_server_create_security_mapping(request: web.Request, web_id, security_mapping, web_id_type=None) -> web.Response:
    """Create a security mapping.

    

    :param web_id: The ID of the asset server on which to create the security mapping.
    :type web_id: str
    :param security_mapping: The new security mapping definition.
    :type security_mapping: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    security_mapping = SecurityMapping.from_dict(security_mapping)
    return web.Response(status=200)


async def asset_server_create_unit_class(request: web.Request, web_id, unit_class, web_id_type=None) -> web.Response:
    """Create a unit class in the specified Asset Server.

    

    :param web_id: The ID of the server.
    :type web_id: str
    :param unit_class: The new unit class definition.
    :type unit_class: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    unit_class = UnitClass.from_dict(unit_class)
    return web.Response(status=200)


async def asset_server_delete_security_entry(request: web.Request, name, web_id, apply_to_children=None, security_item=None) -> web.Response:
    """Delete a security entry owned by the asset server.

    

    :param name: The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    :type name: str
    :param web_id: The ID of the asset server where the security entry will be deleted.
    :type web_id: str
    :param apply_to_children: If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    :type apply_to_children: bool
    :param security_item: The security item of the desired security entries to be deleted. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be deleted.
    :type security_item: str

    """
    return web.Response(status=200)


async def asset_server_get(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an Asset Server.

    

    :param web_id: The ID of the server.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_server_get_analysis_rule_plug_ins(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a list of all Analysis Rule Plug-in&#39;s.

    

    :param web_id: The ID of the asset server, where the Analysis Rule Plug-in&#39;s are installed.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_server_get_by_name(request: web.Request, name, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an Asset Server by name.

    This method returns an asset server based on the name associated with it. Users should primarily search with the WebID when available.

    :param name: The name of the server.
    :type name: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_server_get_by_path(request: web.Request, path, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an Asset Server by path.

    This method returns an asset server based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

    :param path: The path to the server.
    :type path: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_server_get_databases(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a list of all Asset Databases on the specified Asset Server.

    

    :param web_id: The ID of the server.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_server_get_notification_contact_templates(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a list of all notification contact templates on the specified Asset Server.

    

    :param web_id: The ID of the server.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_server_get_notification_plug_ins(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a list of all notification plugins on the specified Asset Server.

    

    :param web_id: The ID of the server.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_server_get_security(request: web.Request, web_id, security_item, user_identity, force_refresh=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Get the security information of the specified security item associated with the asset server for a specified user.

    

    :param web_id: The ID of the asset server for the security to be checked.
    :type web_id: str
    :param security_item: The security item of the desired security information to be returned. Multiple security items may be specified with multiple instances of the parameter. If the parameter is not specified, only &#39;Default&#39; security item of the security information will be returned.
    :type security_item: List[str]
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


async def asset_server_get_security_entries(request: web.Request, web_id, name_filter=None, security_item=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the security entries of the specified security item associated with the asset server based on the specified criteria. By default, all security entries for this asset server are returned.

    

    :param web_id: The ID of the asset server.
    :type web_id: str
    :param name_filter: The name query string used for filtering security entries. The default is no filter.
    :type name_filter: str
    :param security_item: The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be returned.
    :type security_item: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_server_get_security_entry_by_name(request: web.Request, name, web_id, security_item=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the security entry of the specified security item associated with the asset server with the specified name.

    

    :param name: The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    :type name: str
    :param web_id: The ID of the asset server.
    :type web_id: str
    :param security_item: The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be returned.
    :type security_item: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_server_get_security_identities(request: web.Request, web_id, _field=None, max_count=None, query=None, selected_fields=None, sort_field=None, sort_order=None, web_id_type=None) -> web.Response:
    """Retrieve security identities based on the specified criteria. By default, all security identities in the specified Asset Server are returned.

    

    :param web_id: The ID of the asset server to search.
    :type web_id: str
    :param _field: Specifies which of the object&#39;s properties are searched. The default is &#39;Name&#39;.
    :type _field: str
    :param max_count: The maximum number of objects to be returned. The default is 1000.
    :type max_count: int
    :param query: The query string used for finding objects. The default is no query string.
    :type query: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param sort_field: The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;.
    :type sort_order: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_server_get_security_identities_for_user(request: web.Request, web_id, user_identity, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve security identities for a specific user.

    

    :param web_id: The ID of the server.
    :type web_id: str
    :param user_identity: The user identity to search for.
    :type user_identity: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_server_get_security_mappings(request: web.Request, web_id, _field=None, max_count=None, query=None, selected_fields=None, sort_field=None, sort_order=None, web_id_type=None) -> web.Response:
    """Retrieve security mappings based on the specified criteria. By default, all security mappings in the specified Asset Server are returned.

    

    :param web_id: The ID of the asset server to search.
    :type web_id: str
    :param _field: Specifies which of the object&#39;s properties are searched. The default is &#39;Name&#39;.
    :type _field: str
    :param max_count: The maximum number of objects to be returned. The default is 1000.
    :type max_count: int
    :param query: The query string used for finding objects. The default is no query string.
    :type query: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param sort_field: The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;.
    :type sort_order: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_server_get_time_rule_plug_ins(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a list of all Time Rule Plug-in&#39;s.

    

    :param web_id: The ID of the asset server, where the Time Rule Plug-in&#39;s are installed.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_server_get_unit_classes(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a list of all unit classes on the specified Asset Server.

    

    :param web_id: The ID of the server.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_server_list(request: web.Request, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve a list of all Asset Servers known to this service.

    

    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_server_update_security_entry(request: web.Request, name, web_id, security_entry, apply_to_children=None, security_item=None) -> web.Response:
    """Update a security entry owned by the asset server.

    

    :param name: The name of the security entry.
    :type name: str
    :param web_id: The ID of the asset server where the security entry will be updated.
    :type web_id: str
    :param security_entry: The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
    :type security_entry: dict | bytes
    :param apply_to_children: If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    :type apply_to_children: bool
    :param security_item: The security item of the desired security entries to be updated. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be updated.
    :type security_item: str

    """
    security_entry = SecurityEntry.from_dict(security_entry)
    return web.Response(status=200)
