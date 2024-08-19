from typing import List, Dict
from aiohttp import web

from openapi_server.models.analysis import Analysis
from openapi_server.models.attribute import Attribute
from openapi_server.models.element import Element
from openapi_server.models.errors import Errors
from openapi_server.models.items_analysis import ItemsAnalysis
from openapi_server.models.items_attribute import ItemsAttribute
from openapi_server.models.items_element import ItemsElement
from openapi_server.models.items_element_category import ItemsElementCategory
from openapi_server.models.items_event_frame import ItemsEventFrame
from openapi_server.models.items_item_element import ItemsItemElement
from openapi_server.models.items_notification_rule import ItemsNotificationRule
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.items_string import ItemsString
from openapi_server.models.notification_rule import NotificationRule
from openapi_server.models.search_by_attribute import SearchByAttribute
from openapi_server.models.security_entry import SecurityEntry
from openapi_server import util


async def element_add_referenced_element(request: web.Request, web_id, referenced_element_web_id, reference_type=None) -> web.Response:
    """Add a reference to an existing element to the child elements collection.

    

    :param web_id: The ID of the element which the referenced element will be added to.
    :type web_id: str
    :param referenced_element_web_id: The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter.
    :type referenced_element_web_id: List[str]
    :param reference_type: The name of the reference type between the parent and the referenced element. The default is \&quot;parent-child\&quot;.
    :type reference_type: str

    """
    return web.Response(status=200)


async def element_create_analysis(request: web.Request, web_id, analysis, web_id_type=None) -> web.Response:
    """Create an Analysis.

    

    :param web_id: The ID of the element on which to create the Analysis.
    :type web_id: str
    :param analysis: The new Analysis definition.
    :type analysis: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    analysis = Analysis.from_dict(analysis)
    return web.Response(status=200)


async def element_create_attribute(request: web.Request, web_id, attribute, web_id_type=None) -> web.Response:
    """Create a new attribute of the specified element.

    

    :param web_id: The ID of the element on which to create the attribute.
    :type web_id: str
    :param attribute: The definition of the new attribute.
    :type attribute: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    attribute = Attribute.from_dict(attribute)
    return web.Response(status=200)


async def element_create_config(request: web.Request, web_id, include_child_elements=None) -> web.Response:
    """Executes the create configuration function of the data references found within the attributes of the element, and optionally, its children.

    

    :param web_id: The ID of the element.
    :type web_id: str
    :param include_child_elements: If true, includes the child elements of the specified element.
    :type include_child_elements: bool

    """
    return web.Response(status=200)


async def element_create_element(request: web.Request, web_id, element, web_id_type=None) -> web.Response:
    """Create a child element.

    

    :param web_id: The ID of the parent element on which to create the element.
    :type web_id: str
    :param element: The new element definition.
    :type element: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    element = Element.from_dict(element)
    return web.Response(status=200)


async def element_create_notification_rule(request: web.Request, web_id, notification_rule, web_id_type=None) -> web.Response:
    """Create a notification rule.

    

    :param web_id: The ID of the element on which to create the notification rule.
    :type web_id: str
    :param notification_rule: The new notification rule.
    :type notification_rule: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    notification_rule = NotificationRule.from_dict(notification_rule)
    return web.Response(status=200)


async def element_create_search_by_attribute(request: web.Request, query, associations=None, no_results=None, web_id_type=None) -> web.Response:
    """Create a link for a \&quot;Search Elements By Attribute Value\&quot; operation, whose queries are specified in the request content. The SearchRoot is specified by the Web Id of the root Element. If the SearchRoot is not specified, then the search starts at the Asset Database. ElementTemplate must be provided as the Web ID of the ElementTemplate, which are used to create the Elements. All the attributes in the queries must be defined as AttributeTemplates on the ElementTemplate. An array of attribute value queries are ANDed together to find the desired Element objects. At least one value query must be specified. There are limitations on SearchOperators.

    

    :param query: The query of search by attribute.
    :type query: dict | bytes
    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned.
    :type associations: str
    :param no_results: If false, the response content will contain the first page of the search results. If true, the response content will be empty. The default is false.
    :type no_results: bool
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    query = SearchByAttribute.from_dict(query)
    return web.Response(status=200)


async def element_create_security_entry(request: web.Request, web_id, security_entry, apply_to_children=None, web_id_type=None) -> web.Response:
    """Create a security entry owned by the element.

    

    :param web_id: The ID of the element where the security entry will be created.
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


async def element_delete(request: web.Request, web_id) -> web.Response:
    """Delete an element.

    

    :param web_id: The ID of the element.
    :type web_id: str

    """
    return web.Response(status=200)


async def element_delete_security_entry(request: web.Request, name, web_id, apply_to_children=None) -> web.Response:
    """Delete a security entry owned by the element.

    

    :param name: The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    :type name: str
    :param web_id: The ID of the element where the security entry will be deleted.
    :type web_id: str
    :param apply_to_children: If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    :type apply_to_children: bool

    """
    return web.Response(status=200)


async def element_execute_search_by_attribute(request: web.Request, search_id, associations=None, category_name=None, description_filter=None, max_count=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, web_id_type=None) -> web.Response:
    """Execute a \&quot;Search Elements By Attribute Value\&quot; operation.

    

    :param search_id: The encoded search Id of the \&quot;Search Elements By Attribute Value\&quot; operation.
    :type search_id: str
    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned.
    :type associations: str
    :param category_name: Specify that the owner of the returned attributes must have this category. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.
    :type category_name: str
    :param description_filter: The element description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.
    :type description_filter: str
    :param max_count: The maximum number of objects to be returned. The default is 1000.
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
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_find_element_attributes(request: web.Request, web_id, associations=None, attribute_category=None, attribute_description_filter=None, attribute_name_filter=None, attribute_type=None, element_category=None, element_description_filter=None, element_name_filter=None, element_template=None, element_type=None, max_count=None, search_full_hierarchy=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, web_id_type=None) -> web.Response:
    """Retrieves a list of element attributes matching the specified filters from the specified element.

    

    :param web_id: The ID of the element to use as the root of the search.
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


async def element_get(request: web.Request, web_id, associations=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an element.

    

    :param web_id: The ID of the element.
    :type web_id: str
    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned.
    :type associations: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_get_analyses(request: web.Request, web_id, max_count=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, web_id_type=None) -> web.Response:
    """Retrieve analyses based on the specified conditions.

    Users can search for the analyses based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the analyses that match the default search.

    :param web_id: The ID of the element, which is the Target of the analyses.
    :type web_id: str
    :param max_count: The maximum number of objects to be returned per call (page size). The default is 1000.
    :type max_count: int
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


async def element_get_attributes(request: web.Request, web_id, associations=None, category_name=None, max_count=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, start_index=None, template_name=None, trait=None, trait_category=None, value_type=None, web_id_type=None) -> web.Response:
    """Get the attributes of the specified element.

    

    :param web_id: The ID of the element.
    :type web_id: str
    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
    :type associations: str
    :param category_name: Specify that returned attributes must have this category. The default is no category filter.
    :type category_name: str
    :param max_count: The maximum number of objects to be returned per call (page size). The default is 1000.
    :type max_count: int
    :param name_filter: The name query string used for finding attributes. The default is no filter.
    :type name_filter: str
    :param search_full_hierarchy: Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;.
    :type search_full_hierarchy: bool
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param show_excluded: Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;.
    :type show_excluded: bool
    :param show_hidden: Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;.
    :type show_hidden: bool
    :param sort_field: The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;.
    :type sort_order: str
    :param start_index: The starting index (zero based) of the items to be returned. The default is 0.
    :type start_index: int
    :param template_name: Specify that returned attributes must be members of this template. The default is no template filter.
    :type template_name: str
    :param trait: The name of the attribute trait. Multiple traits may be specified with multiple instances of the parameter.
    :type trait: List[str]
    :param trait_category: The category of the attribute traits. Multiple categories may be specified with multiple instances of the parameter. If the parameter is not specified, or if its value is \&quot;all\&quot;, then all attribute traits of all categories will be returned.
    :type trait_category: List[str]
    :param value_type: Specify that returned attributes&#39; value type must be the given value type. The default is no value type filter.
    :type value_type: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_get_by_path(request: web.Request, path, associations=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an element by path.

    This method returns an element based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

    :param path: The path to the element.
    :type path: str
    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned.
    :type associations: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_get_categories(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Get an element&#39;s categories.

    

    :param web_id: The ID of the element.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_get_elements(request: web.Request, web_id, associations=None, category_name=None, description_filter=None, element_type=None, max_count=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, template_name=None, web_id_type=None) -> web.Response:
    """Retrieve elements based on the specified conditions. By default, this method selects immediate children of the specified element.

    Users can search for the elements based on specific search parameters. If no parameters are specified in the search, the default values for each parameter will be used and will return the elements that match the default search.

    :param web_id: The ID of the element to use as the root of the search.
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


async def element_get_elements_query(request: web.Request, associations=None, database_web_id=None, max_count=None, query=None, query_date=None, selected_fields=None, start_index=None, web_id_type=None) -> web.Response:
    """Retrieve elements based on the specified conditions. By default, returns all the elements.

    

    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned.
    :type associations: str
    :param database_web_id: The ID of the asset database to use as the root of the query.
    :type database_web_id: str
    :param max_count: The maximum number of objects to be returned per call (page size). The default is 1000.
    :type max_count: int
    :param query: The query string is a list of filters used to perform an AFSearch for the elements in the asset database. An example would be: \&quot;query&#x3D;Name:&#x3D;MyElement* Template:&#x3D;ElementTemplate\&quot;.
    :type query: str
    :param query_date: Optional parameter. Used to retrieve the relative the version of an object. A value of null or AFTime.MaxValue initializes the query date so the latest versions of sub-objects are retrieved. The value may be an AFTime, DateTime, PITime, String, or numeric. An integer numeric represents the number of ticks (100-nanosecond intervals) since January 1, 0001. A floating point numeric represents the number of seconds since January 1, 1970 UTC. A String is interpreted as local time, unless it contains a time zone indicator such as a trailing \&quot;Z\&quot; or \&quot;GMT\&quot;.
    :type query_date: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param start_index: The starting index (zero based) of the items to be returned. The default is 0.
    :type start_index: int
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_get_event_frames(request: web.Request, web_id, can_be_acknowledged=None, category_name=None, end_time=None, is_acknowledged=None, max_count=None, name_filter=None, search_mode=None, selected_fields=None, severity=None, sort_field=None, sort_order=None, start_index=None, start_time=None, template_name=None, web_id_type=None) -> web.Response:
    """Retrieve event frames that reference this element based on the specified conditions. By default, returns all event frames that reference this element that have been active in the past 8 hours.

    

    :param web_id: The ID of the element whose related event frames are sought.
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


async def element_get_multiple(request: web.Request, as_parallel=None, associations=None, include_mode=None, path=None, selected_fields=None, web_id=None, web_id_type=None) -> web.Response:
    """Retrieve multiple elements by web id or path.

    

    :param as_parallel: Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested attributes. The default is &#39;false&#39;.
    :type as_parallel: bool
    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned.
    :type associations: str
    :param include_mode: The include mode for the return list. The default is &#39;All&#39;.
    :type include_mode: str
    :param path: The path of an element. Multiple elements may be specified with multiple instances of the parameter.
    :type path: List[str]
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id: The ID of an element. Multiple elements may be specified with multiple instances of the parameter.
    :type web_id: List[str]
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_get_notification_rules(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve notification rules for an element

    

    :param web_id: The ID of the resource to use as the root of the search.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_get_paths(request: web.Request, web_id, relative_path=None) -> web.Response:
    """Get a list of the full or relative paths to this element.

    This method will return paths with the primary path at the first index. If there is no primary path, then null will be at the first index. If relative path is specified but does not exist, null will be returned at the first index.

    :param web_id: The ID of the element.
    :type web_id: str
    :param relative_path: The full path in ShortName format to the parent object that the returned paths should be relative. For example, \&quot;\\\\Server1\\Database2\&quot; would return all the paths to the element relative to the database. A path of \&quot;\\\\Server1\\Database2\\RootElement\&quot; would return all paths to the element relative to \&quot;RootElement\&quot;. If null, then all the full paths to the element will be returned.
    :type relative_path: str

    """
    return web.Response(status=200)


async def element_get_referenced_elements(request: web.Request, web_id, associations=None, category_name=None, description_filter=None, element_type=None, max_count=None, name_filter=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, template_name=None, web_id_type=None) -> web.Response:
    """Retrieve referenced elements based on the specified conditions. By default, this method selects all referenced elements of the current resource.

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


async def element_get_security(request: web.Request, web_id, user_identity, force_refresh=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Get the security information of the specified security item associated with the element for a specified user.

    

    :param web_id: The ID of the element for the security to be checked.
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


async def element_get_security_entries(request: web.Request, web_id, name_filter=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the security entries associated with the element based on the specified criteria. By default, all security entries for this element are returned.

    

    :param web_id: The ID of the element.
    :type web_id: str
    :param name_filter: The name query string used for filtering security entries. The default is no filter.
    :type name_filter: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_get_security_entry_by_name(request: web.Request, name, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the security entry associated with the element with the specified name.

    

    :param name: The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    :type name: str
    :param web_id: The ID of the element.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def element_remove_referenced_element(request: web.Request, web_id, referenced_element_web_id) -> web.Response:
    """Remove a reference to an existing element from the child elements collection.

    

    :param web_id: The ID of the element which the referenced element will be removed from.
    :type web_id: str
    :param referenced_element_web_id: The ID of the referenced element. Multiple referenced elements may be specified with multiple instances of the parameter.
    :type referenced_element_web_id: List[str]

    """
    return web.Response(status=200)


async def element_update(request: web.Request, web_id, element) -> web.Response:
    """Update an element by replacing items in its definition.

    

    :param web_id: The ID of the element.
    :type web_id: str
    :param element: A partial element containing the desired changes.
    :type element: dict | bytes

    """
    element = Element.from_dict(element)
    return web.Response(status=200)


async def element_update_security_entry(request: web.Request, name, web_id, security_entry, apply_to_children=None) -> web.Response:
    """Update a security entry owned by the element.

    

    :param name: The name of the security entry.
    :type name: str
    :param web_id: The ID of the element where the security entry will be updated.
    :type web_id: str
    :param security_entry: The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
    :type security_entry: dict | bytes
    :param apply_to_children: If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    :type apply_to_children: bool

    """
    security_entry = SecurityEntry.from_dict(security_entry)
    return web.Response(status=200)
