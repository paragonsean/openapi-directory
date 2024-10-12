from typing import List, Dict
from aiohttp import web

from openapi_server.models.entity_property import EntityProperty
from openapi_server.models.operation_message import OperationMessage
from openapi_server.models.property_keys import PropertyKeys
from openapi_server import util


async def addon_properties_resource_delete_addon_property_delete(request: web.Request, addon_key, property_key) -> web.Response:
    """Delete app property

    Deletes an app&#39;s property.  **[Permissions](#permissions) required:** Only a Connect app whose key matches &#x60;addonKey&#x60; can make this request.

    :param addon_key: The key of the app, as defined in its descriptor.
    :type addon_key: str
    :param property_key: The key of the property.
    :type property_key: str

    """
    return web.Response(status=200)


async def addon_properties_resource_get_addon_properties_get(request: web.Request, addon_key) -> web.Response:
    """Get app properties

    Gets all the properties of an app.  **[Permissions](#permissions) required:** Only a Connect app whose key matches &#x60;addonKey&#x60; can make this request. Additionally, Forge apps published on the Marketplace can access properties of Connect apps they were [migrated from](https://developer.atlassian.com/platform/forge/build-a-connect-on-forge-app/).

    :param addon_key: The key of the app, as defined in its descriptor.
    :type addon_key: str

    """
    return web.Response(status=200)


async def addon_properties_resource_get_addon_property_get(request: web.Request, addon_key, property_key) -> web.Response:
    """Get app property

    Returns the key and value of an app&#39;s property.  **[Permissions](#permissions) required:** Only a Connect app whose key matches &#x60;addonKey&#x60; can make this request. Additionally, Forge apps published on the Marketplace can access properties of Connect apps they were [migrated from](https://developer.atlassian.com/platform/forge/build-a-connect-on-forge-app/).

    :param addon_key: The key of the app, as defined in its descriptor.
    :type addon_key: str
    :param property_key: The key of the property.
    :type property_key: str

    """
    return web.Response(status=200)


async def addon_properties_resource_put_addon_property_put(request: web.Request, addon_key, property_key, body) -> web.Response:
    """Set app property

    Sets the value of an app&#39;s property. Use this resource to store custom data for your app.  The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters.  **[Permissions](#permissions) required:** Only a Connect app whose key matches &#x60;addonKey&#x60; can make this request.

    :param addon_key: The key of the app, as defined in its descriptor.
    :type addon_key: str
    :param property_key: The key of the property.
    :type property_key: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)
