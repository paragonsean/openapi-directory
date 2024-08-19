from typing import List, Dict
from aiohttp import web

from openapi_server.models.attribute import Attribute
from openapi_server.models.items_attribute import ItemsAttribute
from openapi_server.models.items_attribute_category import ItemsAttributeCategory
from openapi_server.models.items_item_attribute import ItemsItemAttribute
from openapi_server.models.timed_value import TimedValue
from openapi_server import util


async def attribute_create_attribute(request: web.Request, web_id, attribute, web_id_type=None) -> web.Response:
    """Create a new attribute as a child of the specified attribute.

    

    :param web_id: The ID of the parent attribute on which to create the attribute.
    :type web_id: str
    :param attribute: The definition of the new attribute.
    :type attribute: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    attribute = Attribute.from_dict(attribute)
    return web.Response(status=200)


async def attribute_create_config(request: web.Request, web_id, web_id_type=None) -> web.Response:
    """Create or update an attribute&#39;s DataReference configuration (Create/Update PI point for PI Point DataReference).

    

    :param web_id: The ID of the attribute.
    :type web_id: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def attribute_delete(request: web.Request, web_id) -> web.Response:
    """Delete an attribute.

    

    :param web_id: The ID of the attribute.
    :type web_id: str

    """
    return web.Response(status=200)


async def attribute_get(request: web.Request, web_id, associations=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an attribute.

    

    :param web_id: The ID of the attribute.
    :type web_id: str
    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
    :type associations: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def attribute_get_attributes(request: web.Request, web_id, associations=None, category_name=None, max_count=None, name_filter=None, search_full_hierarchy=None, selected_fields=None, show_excluded=None, show_hidden=None, sort_field=None, sort_order=None, start_index=None, template_name=None, trait=None, trait_category=None, value_type=None, web_id_type=None) -> web.Response:
    """Get the child attributes of the specified attribute.

    

    :param web_id: The ID of the parent attribute.
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


async def attribute_get_attributes_query(request: web.Request, associations=None, database_web_id=None, max_count=None, query=None, selected_fields=None, start_index=None, web_id_type=None) -> web.Response:
    """Retrieve attributes based on the specified conditions. Returns attributes using the specified search query string.

    

    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
    :type associations: str
    :param database_web_id: The ID of the asset database to use as the root of the query.
    :type database_web_id: str
    :param max_count: The maximum number of objects to be returned per call (page size). The default is 1000.
    :type max_count: int
    :param query: The query string is a list of filters used to perform an AFSearch for the attributes in the asset database. An example would be: \&quot;query&#x3D;Element:{ Name:&#x3D;&#39;MyElement&#39; } Type:&#x3D;Int32\&quot;.
    :type query: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param start_index: The starting index (zero based) of the items to be returned. The default is 0.
    :type start_index: int
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def attribute_get_by_path(request: web.Request, path, associations=None, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an attribute by path.

    This method returns an attribute based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

    :param path: The path to the attribute.
    :type path: str
    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
    :type associations: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def attribute_get_categories(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Get an attribute&#39;s categories.

    

    :param web_id: The ID of the attribute.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def attribute_get_multiple(request: web.Request, as_parallel=None, associations=None, include_mode=None, path=None, selected_fields=None, web_id=None, web_id_type=None) -> web.Response:
    """Retrieve multiple attributes by web id or path.

    

    :param as_parallel: Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested attributes. The default is &#39;false&#39;.
    :type as_parallel: bool
    :param associations: Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
    :type associations: str
    :param include_mode: The include mode for the return list. The default is &#39;All&#39;.
    :type include_mode: str
    :param path: The path of an attribute. Multiple attributes may be specified with multiple instances of the parameter.
    :type path: List[str]
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id: The ID of an attribute. Multiple attributes may be specified with multiple instances of the parameter.
    :type web_id: List[str]
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def attribute_get_value(request: web.Request, web_id, selected_fields=None) -> web.Response:
    """Get the attribute&#39;s value. This call is intended for use with attributes that have no data reference only. For attributes with a data reference, consult the documentation for Streams.

    

    :param web_id: The ID of the attribute.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str

    """
    return web.Response(status=200)


async def attribute_set_value(request: web.Request, web_id, value) -> web.Response:
    """Set the value of a configuration item attribute. For attributes with a data reference or non-configuration item attributes, consult the documentation for streams.

    Users must be aware of the value type that the attribute takes before changing the value. If a value entered by the user does not match the value type expressed in the attribute, it will not work or it will return an error. Users should also be careful of what the value type means, for instance, if a value type accepts strings and the user enters a number, the attribute will interpret it as a string of characters and not as the integer value that the user may have wanted.

    :param web_id: The ID of the attribute.
    :type web_id: str
    :param value: The value to write.
    :type value: dict | bytes

    """
    value = TimedValue.from_dict(value)
    return web.Response(status=200)


async def attribute_update(request: web.Request, web_id, attribute) -> web.Response:
    """Update an attribute by replacing items in its definition.

    If an attribute is based on a template, the user must make sure to update the attribute appropriately so that it does not conflict with the template&#39;s design. Once a template is applied to an attribute, it can not be changed.

    :param web_id: The ID of the attribute.
    :type web_id: str
    :param attribute: A partial attribute containing the desired changes.
    :type attribute: dict | bytes

    """
    attribute = Attribute.from_dict(attribute)
    return web.Response(status=200)
