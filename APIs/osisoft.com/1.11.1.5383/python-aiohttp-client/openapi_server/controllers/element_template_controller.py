from typing import List, Dict
from aiohttp import web

from openapi_server.models.attribute_template import AttributeTemplate
from openapi_server.models.element_template import ElementTemplate
from openapi_server.models.errors import Errors
from openapi_server.models.items_analysis_template import ItemsAnalysisTemplate
from openapi_server.models.items_attribute_template import ItemsAttributeTemplate
from openapi_server.models.items_element_category import ItemsElementCategory
from openapi_server.models.items_element_template import ItemsElementTemplate
from openapi_server.models.items_notification_rule_template import ItemsNotificationRuleTemplate
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.notification_rule_template import NotificationRuleTemplate
from openapi_server.models.security_entry import SecurityEntry
from openapi_server import util


async def element_template_create_attribute_template(request: web.Request, web_id, template, web_id_type=None) -> web.Response:
    """Create an attribute template.

    

    :param web_id: The ID of the element template on which to create the attribute template.
    :type web_id: str
    :param template: The attribute template definition.
    :type template: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    template = AttributeTemplate.from_dict(template)
    return web.Response(status=200)


async def element_template_create_notification_rule_template(request: web.Request, web_id, notification_rule_template, web_id_type=None) -> web.Response:
    """Create a notification rule template.

    

    :param web_id: The ID of the element on which to create the notification rule template.
    :type web_id: str
    :param notification_rule_template: The new notification rule template.
    :type notification_rule_template: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    notification_rule_template = NotificationRuleTemplate.from_dict(notification_rule_template)
    return web.Response(status=200)


async def element_template_create_security_entry(request: web.Request, web_id, security_entry, apply_to_children=None, web_id_type=None) -> web.Response:
    """Create a security entry owned by the element template.

    

    :param web_id: The ID of the element template where the security entry will be created.
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


async def element_template_delete(request: web.Request, web_id) -> web.Response:
    """Delete an element template.

    Deleting an element template will delete all associated templated data from elements which were created from it.

    :param web_id: The ID of the element template to update.
    :type web_id: str

    """
    return web.Response(status=200)


async def element_template_delete_security_entry(request: web.Request, name, web_id, apply_to_children=None) -> web.Response:
    """Delete a security entry owned by the element template.

    

    :param name: The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    :type name: str
    :param web_id: The ID of the element template where the security entry will be deleted.
    :type web_id: str
    :param apply_to_children: If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    :type apply_to_children: bool

    """
    return web.Response(status=200)


async def element_template_get(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an element template.

    

    :param web_id: The ID of the element template.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_template_get_analysis_templates(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Get analysis templates for an element template.

    

    :param web_id: The ID of the element template.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_template_get_attribute_templates(request: web.Request, web_id, depth_first_traverse=None, max_count=None, selected_fields=None, show_descendants=None, show_inherited=None, start_index=None, web_id_type=None) -> web.Response:
    """Get child attribute templates for an element template.

    If &#39;showInherited&#39; and &#39;showDescendants&#39; are &#39;true&#39;, it returns all the attribute templates from current element template and the base template.  If &#39;showInherited&#39; is &#39;false&#39;, it returns all the attribute templates from the current element template.

    :param web_id: The ID of the element template.
    :type web_id: str
    :param depth_first_traverse: When &#39;true&#39;, a Depth First traversal will be performed; this starts at the root and explores as far as possible along each branch before backtracking. When &#39;false&#39;, a Breadth First traversal will be performed; this starts at the tree root and explores the neighbor nodes first, then moves onto the next level of neighbors. The default is &#39;false&#39; (Breadth First).
    :type depth_first_traverse: bool
    :param max_count: The maximum number of objects to be returned. The default is 1000.
    :type max_count: int
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param show_descendants: Specifies if the result should include all descendant attribute templates from the current element template, even indirect ones. The default is &#39;false&#39;.
    :type show_descendants: bool
    :param show_inherited: Specifies if the result should include attribute templates inherited from base element templates. The default is &#39;false&#39;.
    :type show_inherited: bool
    :param start_index: The starting index (zero based) of the items to be returned. The default is 0.
    :type start_index: int
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_template_get_base_element_templates(request: web.Request, web_id, max_count=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Get base element templates for an element template.

    The root template will be returned first, followed by successive templates in the inheritance chain.

    :param web_id: The ID of the element template.
    :type web_id: str
    :param max_count: The maximum number of objects to be returned. The default is 1000.
    :type max_count: int
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_template_get_by_path(request: web.Request, path, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an element template by path.

    This method returns an element template based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

    :param path: The path to the element template.
    :type path: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_template_get_categories(request: web.Request, web_id, selected_fields=None, show_inherited=None, web_id_type=None) -> web.Response:
    """Get an element template&#39;s categories.

    

    :param web_id: The ID of the element template.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param show_inherited: Specifies if the result should include categories inherited from base element templates. The default is &#39;false&#39;.
    :type show_inherited: bool
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_template_get_derived_element_templates(request: web.Request, web_id, max_count=None, selected_fields=None, show_descendants=None, web_id_type=None) -> web.Response:
    """Get derived element templates for an element template.

    

    :param web_id: The ID of the element template.
    :type web_id: str
    :param max_count: The maximum number of objects to be returned. The default is 1000.
    :type max_count: int
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param show_descendants: Specifies if the result should include all descendant element templates from the current element template, even indirect ones. The default is &#39;false&#39;.
    :type show_descendants: bool
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_template_get_notification_rule_templates(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Get notification rule templates for an element template

    

    :param web_id: The ID of the element template.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_template_get_security(request: web.Request, web_id, user_identity, force_refresh=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Get the security information of the specified security item associated with the element template for a specified user.

    

    :param web_id: The ID of the element template for the security to be checked.
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


async def element_template_get_security_entries(request: web.Request, web_id, name_filter=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the security entries associated with the element template based on the specified criteria. By default, all security entries for this element template are returned.

    

    :param web_id: The ID of the element template.
    :type web_id: str
    :param name_filter: The name query string used for filtering security entries. The default is no filter.
    :type name_filter: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_template_get_security_entry_by_name(request: web.Request, name, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the security entry associated with the element template with the specified name.

    

    :param name: The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    :type name: str
    :param web_id: The ID of the element template.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_template_update(request: web.Request, web_id, template) -> web.Response:
    """Update an element template by replacing items in its definition.

    Updating the InstanceType property of an element template will not affect any elements that have already been created from this template; it will only affect any future elements created from this template. All other changes will be propagated to elements based on this template.

    :param web_id: The ID of the element template to update.
    :type web_id: str
    :param template: A partial element template containing the desired changes.
    :type template: dict | bytes

    """
    template = ElementTemplate.from_dict(template)
    return web.Response(status=200)


async def element_template_update_security_entry(request: web.Request, name, web_id, security_entry, apply_to_children=None) -> web.Response:
    """Update a security entry owned by the element template.

    

    :param name: The name of the security entry.
    :type name: str
    :param web_id: The ID of the element template where the security entry will be updated.
    :type web_id: str
    :param security_entry: The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
    :type security_entry: dict | bytes
    :param apply_to_children: If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    :type apply_to_children: bool

    """
    security_entry = SecurityEntry.from_dict(security_entry)
    return web.Response(status=200)
