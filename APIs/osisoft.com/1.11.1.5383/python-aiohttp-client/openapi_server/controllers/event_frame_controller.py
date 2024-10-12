from typing import List, Dict
from aiohttp import web

from openapi_server.models.annotation import Annotation
from openapi_server.models.attribute import Attribute
from openapi_server.models.errors import Errors
from openapi_server.models.event_frame import EventFrame
from openapi_server.models.items_annotation import ItemsAnnotation
from openapi_server.models.items_attribute import ItemsAttribute
from openapi_server.models.items_element import ItemsElement
from openapi_server.models.items_element_category import ItemsElementCategory
from openapi_server.models.items_event_frame import ItemsEventFrame
from openapi_server.models.items_item_event_frame import ItemsItemEventFrame
from openapi_server.models.items_security_entry import ItemsSecurityEntry
from openapi_server.models.items_security_rights import ItemsSecurityRights
from openapi_server.models.media_metadata import MediaMetadata
from openapi_server.models.search_by_attribute import SearchByAttribute
from openapi_server.models.security_entry import SecurityEntry
from openapi_server import util


async def event_frame_acknowledge(request: web.Request, web_id) -> web.Response:
    """Calls the EventFrame&#39;s Acknowledge method.

    

    :param web_id: The ID of the event frame.
    :type web_id: str

    """
    return web.Response(status=200)


async def event_frame_capture_values(request: web.Request, web_id) -> web.Response:
    """Calls the EventFrame&#39;s CaptureValues method.

    

    :param web_id: The ID of the event frame.
    :type web_id: str

    """
    return web.Response(status=200)


async def event_frame_create_annotation(request: web.Request, web_id, annotation, web_id_type=None) -> web.Response:
    """Create an annotation on an event frame.

    

    :param web_id: The ID of the owner event frame on which to create the annotation.
    :type web_id: str
    :param annotation: The new annotation definition.
    :type annotation: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    annotation = Annotation.from_dict(annotation)
    return web.Response(status=200)


async def event_frame_create_attribute(request: web.Request, web_id, attribute, web_id_type=None) -> web.Response:
    """Create a new attribute of the specified event frame.

    

    :param web_id: The ID of the event frame on which to create the attribute.
    :type web_id: str
    :param attribute: The definition of the new attribute.
    :type attribute: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    attribute = Attribute.from_dict(attribute)
    return web.Response(status=200)


async def event_frame_create_config(request: web.Request, web_id, include_child_elements=None) -> web.Response:
    """Executes the create configuration function of the data references found within the attributes of the event frame, and optionally, its children.

    

    :param web_id: The ID of the event frame.
    :type web_id: str
    :param include_child_elements: If true, includes the child event frames of the specified event frame.
    :type include_child_elements: bool

    """
    return web.Response(status=200)


async def event_frame_create_event_frame(request: web.Request, web_id, event_frame, web_id_type=None) -> web.Response:
    """Create an event frame as a child of the specified event frame.

    

    :param web_id: The ID of the parent event frame on which to create the event frame.
    :type web_id: str
    :param event_frame: The new event frame definition.
    :type event_frame: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    event_frame = EventFrame.from_dict(event_frame)
    return web.Response(status=200)


async def event_frame_create_search_by_attribute(request: web.Request, query, no_results=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Create a link for a \&quot;Search EventFrames By Attribute Value\&quot; operation, whose queries are specified in the request content. The SearchRoot is specified by the Web Id of the root EventFrame. If the SearchRoot is not specified, then the search starts at the Asset Database. ElementTemplate must be provided as the Web ID of the ElementTemplate, which are used to create the EventFrames. All the attributes in the queries must be defined as AttributeTemplates on the ElementTemplate. An array of attribute value queries are ANDed together to find the desired Element objects. At least one value query must be specified. There are limitations on SearchOperators.

    

    :param query: The query of search by attribute.
    :type query: dict | bytes
    :param no_results: If false, the response content will contain the first page of the search results. If true, the response content will be empty. The default is false.
    :type no_results: bool
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    query = SearchByAttribute.from_dict(query)
    return web.Response(status=200)


async def event_frame_create_security_entry(request: web.Request, web_id, security_entry, apply_to_children=None, web_id_type=None) -> web.Response:
    """Create a security entry owned by the event frame.

    

    :param web_id: The ID of the event frame where the security entry will be created.
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


async def event_frame_delete(request: web.Request, web_id) -> web.Response:
    """Delete an event frame.

    

    :param web_id: The ID of the event frame to delete.
    :type web_id: str

    """
    return web.Response(status=200)


async def event_frame_delete_annotation(request: web.Request, id, web_id) -> web.Response:
    """Delete an annotation on an event frame. If the annotation has attached media, the attached media will also be deleted.

    

    :param id: The Annotation identifier of the annotation to be deleted.
    :type id: str
    :param web_id: The ID of the owner event frame of the annotation to delete.
    :type web_id: str

    """
    return web.Response(status=200)


async def event_frame_delete_annotation_attachment_media_by_id(request: web.Request, id, web_id) -> web.Response:
    """Delete attached media from an annotation on an event frame.

    

    :param id: The Annotation identifier of the annotation to delete the attached media of.
    :type id: str
    :param web_id: The ID of the owner event frame of the annotation to delete the attached media of.
    :type web_id: str

    """
    return web.Response(status=200)


async def event_frame_delete_security_entry(request: web.Request, name, web_id, apply_to_children=None) -> web.Response:
    """Delete a security entry owned by the event frame.

    

    :param name: The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    :type name: str
    :param web_id: The ID of the event frame where the security entry will be deleted.
    :type web_id: str
    :param apply_to_children: If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    :type apply_to_children: bool

    """
    return web.Response(status=200)


async def event_frame_execute_search_by_attribute(request: web.Request, search_id, can_be_acknowledged=None, end_time=None, is_acknowledged=None, max_count=None, name_filter=None, referenced_element_name_filter=None, search_full_hierarchy=None, search_mode=None, selected_fields=None, severity=None, sort_field=None, sort_order=None, start_index=None, start_time=None, web_id_type=None) -> web.Response:
    """Execute a \&quot;Search EventFrames By Attribute Value\&quot; operation.

    

    :param search_id: The encoded search Id of the \&quot;Search EventFrames By Attribute Value\&quot; operation.
    :type search_id: str
    :param can_be_acknowledged: Specify the returned event frames&#39; canBeAcknowledged property. The default is no canBeAcknowledged filter.
    :type can_be_acknowledged: bool
    :param end_time: The ending time for the search. endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*&#39;.
    :type end_time: str
    :param is_acknowledged: Specify the returned event frames&#39; isAcknowledged property. The default no isAcknowledged filter.
    :type is_acknowledged: bool
    :param max_count: The maximum number of objects to be returned per call (page size). The default is 1000.
    :type max_count: int
    :param name_filter: The name query string used for finding event frames. The default is no filter.
    :type name_filter: str
    :param referenced_element_name_filter: The name query string which must match the name of a referenced element. The default is no filter.
    :type referenced_element_name_filter: str
    :param search_full_hierarchy: Specifies whether the search should include objects nested further than the immediate children of the search root. The default is &#39;false&#39;.
    :type search_full_hierarchy: bool
    :param search_mode: Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. The default is &#39;Overlapped&#39;.
    :type search_mode: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param severity: Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter.
    :type severity: List[str]
    :param sort_field: The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;.
    :type sort_field: str
    :param sort_order: The order that the returned collection is sorted. The default is &#39;Ascending&#39;.
    :type sort_order: str
    :param start_index: The starting index (zero based) of the items to be returned. The default is 0.
    :type start_index: int
    :param start_time: The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*-8h&#39;.
    :type start_time: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def event_frame_find_event_frame_attributes(request: web.Request, web_id, associations=None, attribute_category=None, attribute_description_filter=None, attribute_name_filter=None, attribute_type=None, end_time=None, event_frame_category=None, event_frame_description_filter=None, event_frame_name_filter=None, event_frame_template=None, max_count=None, referenced_element_name_filter=None, search_full_hierarchy=None, search_mode=None, selected_fields=None, sort_field=None, sort_order=None, start_index=None, start_time=None, web_id_type=None) -> web.Response:
    """Retrieves a list of event frame attributes matching the specified filters from the specified event frame.

    

    :param web_id: The ID of the event frame to use as the root of the search.
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


async def event_frame_get(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an event frame.

    

    :param web_id: The ID of the event frame.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def event_frame_get_annotation_attachment_media_metadata_by_id(request: web.Request, id, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Gets the metadata of the media attached to the specified annotation.

    

    :param id: The Annotation identifier of the specific annotation.
    :type id: str
    :param web_id: The ID of the owner event frame.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def event_frame_get_annotation_by_id(request: web.Request, id, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Get a specific annotation on an event frame.

    

    :param id: The Annotation identifier of the specific annotation.
    :type id: str
    :param web_id: The ID of the owner event frame.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def event_frame_get_annotations(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Get an event frame&#39;s annotations.

    

    :param web_id: The ID of the owner event frame.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def event_frame_get_attributes(request: web.Request, web_id, associations=None, category_name=None, max_count=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, start_index=None, template_name=None, trait=None, trait_category=None, value_type=None, web_id_type=None) -> web.Response:
    """Get the attributes of the specified event frame.

    

    :param web_id: The ID of the event frame.
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


async def event_frame_get_by_path(request: web.Request, path, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an event frame by path.

    This method returns an event frame based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

    :param path: The path to the event frame.
    :type path: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def event_frame_get_categories(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Get an event frame&#39;s categories.

    

    :param web_id: The ID of the event frame.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def event_frame_get_event_frames(request: web.Request, web_id, can_be_acknowledged=None, category_name=None, end_time=None, is_acknowledged=None, max_count=None, name_filter=None, referenced_element_name_filter=None, referenced_element_template_name=None, search_full_hierarchy=None, search_mode=None, selected_fields=None, severity=None, sort_field=None, sort_order=None, start_index=None, start_time=None, template_name=None, web_id_type=None) -> web.Response:
    """Retrieve event frames based on the specified conditions. By default, returns all children of the specified root event frame that have been active in the past 8 hours.

    

    :param web_id: The ID of the event frame to use as the root of the search.
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


async def event_frame_get_event_frames_query(request: web.Request, database_web_id=None, max_count=None, query=None, selected_fields=None, start_index=None, web_id_type=None) -> web.Response:
    """Retrieve event frames based on the specified conditions. Returns event frames using the specified search query string.

    

    :param database_web_id: The ID of the asset database to use as the root of the query.
    :type database_web_id: str
    :param max_count: The maximum number of objects to be returned per call (page size). The default is 1000.
    :type max_count: int
    :param query: The query string is a list of filters used to perform an AFSearch for the eventframes in the asset database. An example would be: \&quot;query&#x3D;Name:&#x3D;MyEventFrame* Category:&#x3D;MyCategory Template:&#x3D;EFTemplate\&quot;.
    :type query: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param start_index: The starting index (zero based) of the items to be returned. The default is 0.
    :type start_index: int
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def event_frame_get_multiple(request: web.Request, as_parallel=None, include_mode=None, path=None, selected_fields=None, web_id=None, web_id_type=None) -> web.Response:
    """Retrieve multiple event frames by web ids or paths.

    

    :param as_parallel: Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested attributes. The default is &#39;false&#39;.
    :type as_parallel: bool
    :param include_mode: The include mode for the return list. The default is &#39;All&#39;.
    :type include_mode: str
    :param path: The path of an event frame. Multiple event frames may be specified with multiple instances of the parameter.
    :type path: List[str]
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id: The ID of an event frame. Multiple event frames may be specified with multiple instances of the parameter.
    :type web_id: List[str]
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def event_frame_get_referenced_elements(request: web.Request, web_id, associations=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the event frame&#39;s referenced elements.

    

    :param web_id: The ID of the event frame whose referenced elements should be retrieved.
    :type web_id: str
    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned.
    :type associations: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def event_frame_get_security(request: web.Request, web_id, user_identity, force_refresh=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Get the security information of the specified security item associated with the event frame for a specified user.

    

    :param web_id: The ID of the event frame for the security to be checked.
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


async def event_frame_get_security_entries(request: web.Request, web_id, name_filter=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the security entries associated with the event frame based on the specified criteria. By default, all security entries for this event frame are returned.

    

    :param web_id: The ID of the event frame.
    :type web_id: str
    :param name_filter: The name query string used for filtering security entries. The default is no filter.
    :type name_filter: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def event_frame_get_security_entry_by_name(request: web.Request, name, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve the security entry associated with the event frame with the specified name.

    

    :param name: The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
    :type name: str
    :param web_id: The ID of the event frame.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def event_frame_update(request: web.Request, web_id, event_frame) -> web.Response:
    """Update an event frame by replacing items in its definition.

    

    :param web_id: The ID of the event frame to update.
    :type web_id: str
    :param event_frame: A partial event frame containing the desired changes.
    :type event_frame: dict | bytes

    """
    event_frame = EventFrame.from_dict(event_frame)
    return web.Response(status=200)


async def event_frame_update_annotation(request: web.Request, id, web_id, annotation) -> web.Response:
    """Update an annotation on an event frame by replacing items in its definition.

    

    :param id: The Annotation identifier of the annotation to be updated.
    :type id: str
    :param web_id: The ID of the owner event frame of the annotation to update.
    :type web_id: str
    :param annotation: A partial annotation containing the desired changes.
    :type annotation: dict | bytes

    """
    annotation = Annotation.from_dict(annotation)
    return web.Response(status=200)


async def event_frame_update_security_entry(request: web.Request, name, web_id, security_entry, apply_to_children=None) -> web.Response:
    """Update a security entry owned by the event frame.

    

    :param name: The name of the security entry.
    :type name: str
    :param web_id: The ID of the event frame where the security entry will be updated.
    :type web_id: str
    :param security_entry: The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
    :type security_entry: dict | bytes
    :param apply_to_children: If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
    :type apply_to_children: bool

    """
    security_entry = SecurityEntry.from_dict(security_entry)
    return web.Response(status=200)
