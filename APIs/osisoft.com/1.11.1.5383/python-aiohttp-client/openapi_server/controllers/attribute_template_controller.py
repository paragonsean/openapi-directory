from typing import List, Dict
from aiohttp import web

from openapi_server.models.attribute_template import AttributeTemplate
from openapi_server.models.items_attribute_category import ItemsAttributeCategory
from openapi_server.models.items_attribute_template import ItemsAttributeTemplate
from openapi_server import util


async def attribute_template_create_attribute_template(request: web.Request, web_id, template, web_id_type=None) -> web.Response:
    """Create an attribute template as a child of another attribute template.

    

    :param web_id: The ID of the parent attribute template on which to create the attribute template.
    :type web_id: str
    :param template: The attribute template definition.
    :type template: dict | bytes
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    template = AttributeTemplate.from_dict(template)
    return web.Response(status=200)


async def attribute_template_delete(request: web.Request, web_id) -> web.Response:
    """Delete an attribute template.

    Deleting an attribute template will delete the attributes that were created based on the template

    :param web_id: The ID of the attribute template.
    :type web_id: str

    """
    return web.Response(status=200)


async def attribute_template_get(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an attribute template.

    

    :param web_id: The ID of the attribute template.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def attribute_template_get_attribute_templates(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an attribute template&#39;s child attribute templates.

    

    :param web_id: The ID of the attribute template.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def attribute_template_get_by_path(request: web.Request, path, selected_fields=None, web_id_type=None) -> web.Response:
    """Retrieve an attribute template by path.

    This method returns an attribute template based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

    :param path: The path to the attribute template.
    :type path: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def attribute_template_get_categories(request: web.Request, web_id, selected_fields=None, web_id_type=None) -> web.Response:
    """Get an attribute template&#39;s categories.

    

    :param web_id: The ID of the attribute template.
    :type web_id: str
    :param selected_fields: List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
    :type selected_fields: str
    :param web_id_type: Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;.
    :type web_id_type: str

    """
    return web.Response(status=200)


async def attribute_template_update(request: web.Request, web_id, template) -> web.Response:
    """Update an existing attribute template by replacing items in its definition.

    Updating an attribute template will propagate changes to the attributes that were created based on the template

    :param web_id: The ID of the attribute template.
    :type web_id: str
    :param template: A partial attribute template containing the desired changes.
    :type template: dict | bytes

    """
    template = AttributeTemplate.from_dict(template)
    return web.Response(status=200)
