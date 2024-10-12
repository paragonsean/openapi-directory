from typing import List, Dict
from aiohttp import web

from openapi_server.models.analysis_category import AnalysisCategory
from openapi_server.models.analysis_template import AnalysisTemplate
from openapi_server.models.asset_database import AssetDatabase
from openapi_server.models.attribute_category import AttributeCategory
from openapi_server.models.element import Element
from openapi_server.models.element_category import ElementCategory
from openapi_server.models.element_template import ElementTemplate
from openapi_server.models.enumeration_set import EnumerationSet
from openapi_server.models.errors import Errors
from openapi_server.models.event_frame import EventFrame
from openapi_server.models.items_analysis import ItemsAnalysis
from openapi_server.models.items_analysis_category import ItemsAnalysisCategory
from openapi_server.models.items_analysis_template import ItemsAnalysisTemplate
from openapi_server.models.items_attribute import ItemsAttribute
from openapi_server.models.items_attribute_category import ItemsAttributeCategory
from openapi_server.models.items_element import ItemsElement
from openapi_server.models.items_element_category import ItemsElementCategory
from openapi_server.models.items_element_template import ItemsElementTemplate
from openapi_server.models.items_enumeration_set import ItemsEnumerationSet
from openapi_server.models.items_event_frame import ItemsEventFrame
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.items_table import ItemsTable
from openapi_server.models.items_table_category import ItemsTableCategory
from openapi_server.models.security_entry import SecurityEntry
from openapi_server.models.table import Table
from openapi_server.models.table_category import TableCategory
from openapi_server import util


async def asset_database_add_referenced_element(request: web.Request, web_id, referenced_element_web_id, reference_type=None) -> web.Response:
    """Add a reference to an existing element to the specified database.

    

    :param web_id: The ID of the database which the referenced element will be added to.
    :type web_id: str
    :param referenced_element_web_id: The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter.
    :type referenced_element_web_id: List[str]
    :param reference_type: The name of the reference type between the parent and the referenced element. This must be a \&quot;strong\&quot; reference type. The default is \&quot;parent-child\&quot;.
    :type reference_type: str

    """
    return web.Response(status=200)


async def asset_database_create_analysis_category(request: web.Request, web_id, analysis_category, web_id_type=None) -> web.Response:
    """Create an analysis category at the Asset Database root.

    

    :param web_id: The ID of the database in which to create the analysis category.
    :type web_id: str
    :param analysis_category: The new analysis category definition.
    :type analysis_category: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    analysis_category = AnalysisCategory.from_dict(analysis_category)
    return web.Response(status=200)


async def asset_database_create_analysis_template(request: web.Request, web_id, template, web_id_type=None) -> web.Response:
    """Create an analysis template at the Asset Database root.

    Analyses that are based on an analysis template will inherit characteristics defined in the template.

    :param web_id: The ID of the database in which to create the analysis template.
    :type web_id: str
    :param template: The new analysis template definition.
    :type template: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    template = AnalysisTemplate.from_dict(template)
    return web.Response(status=200)


async def asset_database_create_attribute_category(request: web.Request, web_id, attribute_category, web_id_type=None) -> web.Response:
    """Create an attribute category at the Asset Database root.

    

    :param web_id: The ID of the database in which to create the attribute category.
    :type web_id: str
    :param attribute_category: The new attribute category definition.
    :type attribute_category: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    attribute_category = AttributeCategory.from_dict(attribute_category)
    return web.Response(status=200)


async def asset_database_create_element(request: web.Request, web_id, element, web_id_type=None) -> web.Response:
    """Create a child element.

    

    :param web_id: The ID of the asset database on which to create the element.
    :type web_id: str
    :param element: The new element definition.
    :type element: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    element = Element.from_dict(element)
    return web.Response(status=200)


async def asset_database_create_element_category(request: web.Request, web_id, element_category, web_id_type=None) -> web.Response:
    """Create an element category at the Asset Database root.

    

    :param web_id: The ID of the database in which to create the element category.
    :type web_id: str
    :param element_category: The new element category definition.
    :type element_category: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    element_category = ElementCategory.from_dict(element_category)
    return web.Response(status=200)


async def asset_database_create_element_template(request: web.Request, web_id, template, web_id_type=None) -> web.Response:
    """Create a template at the Asset Database root. Specify InstanceType of \&quot;Element\&quot; or \&quot;EventFrame\&quot; to create element or event frame template respectively. Only these two types of templates can be created.

    Elements and event frames that are based on an element template will inherit characteristics defined in the template.

    :param web_id: The ID of the database in which to create the element template.
    :type web_id: str
    :param template: The new element template definition.
    :type template: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    template = ElementTemplate.from_dict(template)
    return web.Response(status=200)


async def asset_database_create_enumeration_set(request: web.Request, web_id, enumeration_set, web_id_type=None) -> web.Response:
    """Create an enumeration set at the Asset Database.

    

    :param web_id: The ID of the database in which to create the enumeration set.
    :type web_id: str
    :param enumeration_set: The new enumeration set definition.
    :type enumeration_set: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    enumeration_set = EnumerationSet.from_dict(enumeration_set)
    return web.Response(status=200)


async def asset_database_create_event_frame(request: web.Request, web_id, event_frame, web_id_type=None) -> web.Response:
    """Create an event frame.

    

    :param web_id: The ID of the database on which to create the event frame.
    :type web_id: str
    :param event_frame: The new event frame definition.
    :type event_frame: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    event_frame = EventFrame.from_dict(event_frame)
    return web.Response(status=200)


async def asset_database_create_security_entry(request: web.Request, web_id, security_entry, apply_to_children=None, security_item=None, web_id_type=None) -> web.Response:
    """Create a security entry owned by the asset database.

    

    :param web_id: The ID of the asset database where the security entry will be created.
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


async def asset_database_create_table(request: web.Request, web_id, table, web_id_type=None) -> web.Response:
    """Create a table on the Asset Database.

    

    :param web_id: The ID of the database in which to create the table.
    :type web_id: str
    :param table: The new table definition.
    :type table: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    table = Table.from_dict(table)
    return web.Response(status=200)


async def asset_database_create_table_category(request: web.Request, web_id, table_category, web_id_type=None) -> web.Response:
    """Create a table category on the Asset Database.

    

    :param web_id: The ID of the database in which to create the table category.
    :type web_id: str
    :param table_category: The new table category definition.
    :type table_category: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    table_category = TableCategory.from_dict(table_category)
    return web.Response(status=200)


async def asset_database_delete(request: web.Request, web_id) -> web.Response:
    """Delete an asset database.

    

    :param web_id: The ID of the database.
    :type web_id: str

    """
    return web.Response(status=200)


async def asset_database_delete_security_entry(request: web.Request, name, web_id, apply_to_children=None, security_item=None) -> web.Response:
    """Delete a security entry owned by the asset database.

    

    :param name: The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    :type name: str
    :param web_id: The ID of the asset database where the security entry will be deleted.
    :type web_id: str
    :param apply_to_children: If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    :type apply_to_children: bool
    :param security_item: The security item of the desired security entries to be deleted. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be deleted.
    :type security_item: str

    """
    return web.Response(status=200)


async def asset_database_export(request: web.Request, web_id, end_time=None, export_mode=None, start_time=None) -> web.Response:
    """Export the asset database.

    

    :param web_id: The ID of the database.
    :type web_id: str
    :param end_time: The latest ending time for AFEventFrame, AFTransfer, and AFCase objects that may be part of the export. The default is &#39;*&#39;.
    :type end_time: str
    :param export_mode: Indicates the type of export to perform. The default is &#39;StrongReferences&#39;. Multiple export modes may be specified by using multiple instances of exportMode.
    :type export_mode: List[str]
    :param start_time: The earliest starting time for AFEventFrame, AFTransfer, and AFCase objects that may be part of the export. The default is &#39;*-30d&#39;.
    :type start_time: str

    """
    return web.Response(status=200)


async def asset_database_find_analyses(request: web.Request, web_id, _field, max_count=None, query=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, web_id_type=None) -> web.Response:
    """Retrieve analyses based on the specified conditions.

    Users can search for the analyses based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the analyses that match the default search.

    :param web_id: The ID of the database to search for the analyses.
    :type web_id: str
    :param _field: Specifies which of the object&#39;s properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is &#39;Name&#39;.
    :type _field: List[str]
    :param max_count: The maximum number of objects to be returned per call (page size). The default is 1000.
    :type max_count: int
    :param query: The query string used for finding analyses. The default is null.
    :type query: str
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


async def asset_database_find_element_attributes(request: web.Request, web_id, associations=None, attribute_category=None, attribute_description_filter=None, attribute_name_filter=None, attribute_type=None, element_category=None, element_description_filter=None, element_name_filter=None, element_template=None, element_type=None, max_count=None, search_full_hierarchy=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, web_id_type=None) -> web.Response:
    """Retrieves a list of element attributes matching the specified filters from the specified asset database.

    

    :param web_id: The ID of the asset database to use as the root of the search.
    :type web_id: str
    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
    :type associations: str
    :param attribute_category: Specify that returned attributes must have this category. The default is no filter.
    :type attribute_category: str
    :param attribute_description_filter: The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.
    :type attribute_description_filter: str
    :param attribute_name_filter: The attribute name filter string used for finding objects. The default is no filter.
    :type attribute_name_filter: str
    :param attribute_type: Specify that returned attributes&#39; value type must be this value type. The default is no filter.
    :type attribute_type: str
    :param element_category: Specify that the owner of the returned attributes must have this category. The default is no filter.
    :type element_category: str
    :param element_description_filter: The element description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.
    :type element_description_filter: str
    :param element_name_filter: The element name filter string used for finding objects. The default is no filter.
    :type element_name_filter: str
    :param element_template: Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter.
    :type element_template: str
    :param element_type: Specify that the element of the returned attributes must have this AFElementType. The default is no filter.
    :type element_type: str
    :param max_count: The maximum number of objects to be returned (the page size). The default is 1000.
    :type max_count: int
    :param search_full_hierarchy: Specifies if the search should include objects nested further than immediate children of the given resource. The default is &#39;false&#39;.
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


async def asset_database_find_event_frame_attributes(request: web.Request, web_id, associations=None, attribute_category=None, attribute_description_filter=None, attribute_name_filter=None, attribute_type=None, end_time=None, event_frame_category=None, event_frame_description_filter=None, event_frame_name_filter=None, event_frame_template=None, max_count=None, referenced_element_name_filter=None, search_full_hierarchy=None, search_mode=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, start_time=None, web_id_type=None) -> web.Response:
    """Retrieves a list of event frame attributes matching the specified filters from the specified asset database.

    

    :param web_id: The ID of the asset database to use as the root of the search.
    :type web_id: str
    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
    :type associations: str
    :param attribute_category: Specify that returned attributes must have this category. The default is no filter.
    :type attribute_category: str
    :param attribute_description_filter: The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.
    :type attribute_description_filter: str
    :param attribute_name_filter: The attribute name filter string used for finding objects. The default is no filter.
    :type attribute_name_filter: str
    :param attribute_type: Specify that returned attributes&#39; value type must be this value type. The default is no filter.
    :type attribute_type: str
    :param end_time: A string representing the latest ending time for the event frames to be matched. The endTime must be greater than or equal to the startTime. The default is &#39;*&#39;.
    :type end_time: str
    :param event_frame_category: Specify that the owner of the returned attributes must have this category. The default is no filter.
    :type event_frame_category: str
    :param event_frame_description_filter: The event frame description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.
    :type event_frame_description_filter: str
    :param event_frame_name_filter: The event frame name filter string used for finding objects. The default is no filter.
    :type event_frame_name_filter: str
    :param event_frame_template: Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter.
    :type event_frame_template: str
    :param max_count: The maximum number of objects to be returned (the page size). The default is 1000.
    :type max_count: int
    :param referenced_element_name_filter: The name query string which must match the name of a referenced element. The default is no filter.
    :type referenced_element_name_filter: str
    :param search_full_hierarchy: Specifies if the search should include objects nested further than immediate children of the given resource. The default is &#39;false&#39;.
    :type search_full_hierarchy: bool
    :param search_mode: Determines how the startTime and endTime parameters are treated when searching for event frames. The default is &#39;Overlapped&#39;.
    :type search_mode: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param sort_field: The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;.
    :type sort_order: str
    :param start_index: The starting index (zero based) of the items to be returned. The default is 0.
    :type start_index: int
    :param start_time: A string representing the earliest starting time for the event frames to be matched. startTime must be less than or equal to the endTime. The default is &#39;*-8h&#39;.
    :type start_time: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_database_get(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an Asset Database.

    

    :param web_id: The ID of the database.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_database_get_analysis_categories(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve analysis categories for a given Asset Database.

    

    :param web_id: The ID of the database.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_database_get_analysis_templates(request: web.Request, web_id, _field, max_count=None, query=None, selected_fields=None, sort_field=None, sort_order=None, web_id_type=None) -> web.Response:
    """Retrieve analysis templates based on the specified criteria. By default, all analysis templates in the specified Asset Database are returned.

    Users can search for the analysis templates based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the templates that match the default search.

    :param web_id: The ID of the database to search.
    :type web_id: str
    :param _field: Specifies which of the object&#39;s properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is &#39;Name&#39;.
    :type _field: List[str]
    :param max_count: The maximum number of objects to be returned per call (page size). The default is 1000.
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


async def asset_database_get_attribute_categories(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve attribute categories for a given Asset Database.

    

    :param web_id: The ID of the database.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_database_get_by_path(request: web.Request, path, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an Asset Database by path.

    This method returns an asset database based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

    :param path: The path to the database.
    :type path: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_database_get_element_categories(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve element categories for a given Asset Database.

    

    :param web_id: The ID of the database.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_database_get_element_templates(request: web.Request, web_id, _field, max_count=None, query=None, selected_fields=None, sort_field=None, sort_order=None, web_id_type=None) -> web.Response:
    """Retrieve element templates based on the specified criteria. Only templates of instance type \&quot;Element\&quot; and \&quot;EventFrame\&quot; are returned. By default, all element and event frame templates in the specified Asset Database are returned.

    Users can search for the element and event frame template based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the templates that match the default search.

    :param web_id: The ID of the database to search.
    :type web_id: str
    :param _field: Specifies which of the object&#39;s properties are searched. Multiple search fields may be specified with multiple instances of the parameter. The default is &#39;Name&#39;.
    :type _field: List[str]
    :param max_count: The maximum number of objects to be returned per call (page size). The default is 1000.
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


async def asset_database_get_elements(request: web.Request, web_id, associations=None, category_name=None, description_filter=None, element_type=None, max_count=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, template_name=None, web_id_type=None) -> web.Response:
    """Retrieve elements based on the specified conditions. By default, this method selects immediate children of the specified asset database.

    Users can search for the elements based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the elements that match the default search.

    :param web_id: The ID of the database to use as the root of the search.
    :type web_id: str
    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned.
    :type associations: str
    :param category_name: Specify that returned elements must have this category. The default is no category filter.
    :type category_name: str
    :param description_filter: Specify that returned elements must have this description. The default is no description filter.
    :type description_filter: str
    :param element_type: Specify that returned elements must have this type. The default type is &#39;Any&#39;.
    :type element_type: str
    :param max_count: The maximum number of objects to be returned per call (page size). The default is 1000.
    :type max_count: int
    :param name_filter: The name query string used for finding objects. The default is no filter.
    :type name_filter: str
    :param search_full_hierarchy: Specifies if the search should include objects nested further than the immediate children of the searchRoot. The default is &#39;false&#39;.
    :type search_full_hierarchy: bool
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param sort_field: The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;.
    :type sort_order: str
    :param start_index: The starting index (zero based) of the items to be returned. The default is 0.
    :type start_index: int
    :param template_name: Specify that returned elements must have this template or a template derived from this template. The default is no template filter.
    :type template_name: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_database_get_enumeration_sets(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve enumeration sets for given asset database.

    

    :param web_id: The ID of the database.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_database_get_event_frames(request: web.Request, web_id, can_be_acknowledged=None, category_name=None, end_time=None, is_acknowledged=None, max_count=None, name_filter=None, referenced_element_name_filter=None, referenced_element_template_name=None, search_full_hierarchy=None, search_mode=None, selected_fields=None, severity=None, sort_field=None, sort_order=None, start_index=None, start_time=None, template_name=None, web_id_type=None) -> web.Response:
    """Retrieve event frames based on the specified conditions. By default, returns all children of the specified root resource that have been active in the past 8 hours.

    

    :param web_id: The ID of the asset database to use as the root of the search.
    :type web_id: str
    :param can_be_acknowledged: Specify the returned event frames&#39; canBeAcknowledged property. The default is no canBeAcknowledged filter.
    :type can_be_acknowledged: bool
    :param category_name: Specify that returned event frames must have this category. The default is no category filter.
    :type category_name: str
    :param end_time: The ending time for the search. The endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*&#39; if searchMode is not one of the &#39;Backward*&#39; or &#39;Forward*&#39; values.
    :type end_time: str
    :param is_acknowledged: Specify the returned event frames&#39; isAcknowledged property. The default no isAcknowledged filter.
    :type is_acknowledged: bool
    :param max_count: The maximum number of objects to be returned per call (page size). The default is 1000.
    :type max_count: int
    :param name_filter: The name query string used for finding event frames. The default is no filter.
    :type name_filter: str
    :param referenced_element_name_filter: The name query string which must match the name of a referenced element. The default is no filter.
    :type referenced_element_name_filter: str
    :param referenced_element_template_name: Specify that returned event frames must have an element in the event frame&#39;s referenced elements collection that derives from the template. Specify this parameter by name.
    :type referenced_element_template_name: str
    :param search_full_hierarchy: Specifies whether the search should include objects nested further than the immediate children of the search root. The default is &#39;false&#39;.
    :type search_full_hierarchy: bool
    :param search_mode: Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. If this parameter is one of the &#39;Backward*&#39; or &#39;Forward*&#39; values, none of endTime, sortField, or sortOrder may be specified. The default is &#39;Overlapped&#39;.
    :type search_mode: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param severity: Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter.
    :type severity: List[str]
    :param sort_field: The field or property of the object used to sort the returned collection. The default is &#39;Name&#39; if searchMode is not one of the &#39;Backward*&#39; or &#39;Forward*&#39; values.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39; if searchMode is not one of the &#39;Backward*&#39; or &#39;Forward*&#39; values.
    :type sort_order: str
    :param start_index: The starting index (zero based) of the items to be returned. The default is 0.
    :type start_index: int
    :param start_time: The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*-8h&#39;.
    :type start_time: str
    :param template_name: Specify that returned event frames must have this template or a template derived from this template. The default is no template filter. Specify this parameter by name.
    :type template_name: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_database_get_referenced_elements(request: web.Request, web_id, associations=None, category_name=None, description_filter=None, element_type=None, max_count=None, name_filter=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, template_name=None, web_id_type=None) -> web.Response:
    """Retrieve referenced elements based on the specified conditions. By default, this method selects all referenced elements at the root level of the asset database.

    Users can search for the referenced elements based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the elements that match the default search.

    :param web_id: The ID of the resource to use as the root of the search.
    :type web_id: str
    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned.
    :type associations: str
    :param category_name: Specify that returned elements must have this category. The default is no category filter.
    :type category_name: str
    :param description_filter: Specify that returned elements must have this description. The default is no description filter.
    :type description_filter: str
    :param element_type: Specify that returned elements must have this type. The default type is &#39;Any&#39;.
    :type element_type: str
    :param max_count: The maximum number of objects to be returned per call (page size). The default is 1000.
    :type max_count: int
    :param name_filter: The name query string used for finding objects. The default is no filter.
    :type name_filter: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param sort_field: The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;.
    :type sort_order: str
    :param start_index: The starting index (zero based) of the items to be returned. The default is 0.
    :type start_index: int
    :param template_name: Specify that returned elements must have this template or a template derived from this template. The default is no template filter.
    :type template_name: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_database_get_security(request: web.Request, web_id, security_item, user_identity, force_refresh=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Get the security information of the specified security item associated with the asset database for a specified user.

    

    :param web_id: The ID of the asset database for the security to be checked.
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


async def asset_database_get_security_entries(request: web.Request, web_id, name_filter=None, security_item=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the security entries of the specified security item associated with the asset database based on the specified criteria. By default, all security entries for this asset database are returned.

    

    :param web_id: The ID of the asset database.
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


async def asset_database_get_security_entry_by_name(request: web.Request, name, web_id, security_item=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the security entry of the specified security item associated with the asset database with the specified name.

    

    :param name: The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    :type name: str
    :param web_id: The ID of the asset database.
    :type web_id: str
    :param security_item: The security item of the desired security entries information to be returned. If the parameter is not specified, security entries of the &#39;Default&#39; security item will be returned.
    :type security_item: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_database_get_table_categories(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve table categories for a given Asset Database.

    

    :param web_id: The ID of the database.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_database_get_tables(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve tables for given Asset Database.

    

    :param web_id: The ID of the database.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def asset_database_import(request: web.Request, web_id, import_mode=None) -> web.Response:
    """Import an asset database.

    

    :param web_id: The ID of the asset database.
    :type web_id: str
    :param import_mode: Indicates the type of import to perform. The default is &#39;AllowCreate | AllowUpdate | AutoCheckIn&#39;. Multiple import modes may be specified by using multiple instances of importMode.
    :type import_mode: List[str]

    """
    return web.Response(status=200)


async def asset_database_remove_referenced_element(request: web.Request, web_id, referenced_element_web_id) -> web.Response:
    """Remove a reference to an existing element from the specified database.

    

    :param web_id: The ID of the database which the referenced element will be removed from.
    :type web_id: str
    :param referenced_element_web_id: The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter.
    :type referenced_element_web_id: List[str]

    """
    return web.Response(status=200)


async def asset_database_update(request: web.Request, web_id, database) -> web.Response:
    """Update an asset database by replacing items in its definition.

    

    :param web_id: The ID of the database.
    :type web_id: str
    :param database: A partial database containing the desired changes.
    :type database: dict | bytes

    """
    database = AssetDatabase.from_dict(database)
    return web.Response(status=200)


async def asset_database_update_security_entry(request: web.Request, name, web_id, security_entry, apply_to_children=None, security_item=None) -> web.Response:
    """Update a security entry owned by the asset database.

    

    :param name: The name of the security entry.
    :type name: str
    :param web_id: The ID of the asset database where the security entry will be updated.
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
