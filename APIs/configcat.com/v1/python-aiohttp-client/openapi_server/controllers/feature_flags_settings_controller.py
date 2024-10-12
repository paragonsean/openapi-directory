from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_setting_initial_values import CreateSettingInitialValues
from openapi_server.models.json_patch import JsonPatch
from openapi_server.models.setting_model import SettingModel
from openapi_server.models.setting_model_haljson import SettingModelHaljson
from openapi_server import util


async def create_setting(request: web.Request, config_id, body) -> web.Response:
    """Create Flag

    This endpoint creates a new Feature Flag or Setting in a specified Config identified by the &#x60;configId&#x60; parameter.  **Important:** The &#x60;key&#x60; attribute must be unique within the given Config.

    :param config_id: The identifier of the Config.
    :type config_id: str
    :type config_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateSettingInitialValues.from_dict(body)
    return web.Response(status=200)


async def delete_setting(request: web.Request, setting_id) -> web.Response:
    """Delete Flag

    This endpoint removes a Feature Flag or Setting from a specified Config,  identified by the &#x60;configId&#x60; parameter.

    :param setting_id: The identifier of the Setting.
    :type setting_id: int

    """
    return web.Response(status=200)


async def get_setting(request: web.Request, setting_id) -> web.Response:
    """Get Flag

    This endpoint returns the metadata attributes of a Feature Flag or Setting  identified by the &#x60;settingId&#x60; parameter.

    :param setting_id: The identifier of the Setting.
    :type setting_id: int

    """
    return web.Response(status=200)


async def get_settings(request: web.Request, config_id) -> web.Response:
    """List Flags

    This endpoint returns the list of the Feature Flags and Settings defined in a  specified Config, identified by the &#x60;configId&#x60; parameter.

    :param config_id: The identifier of the Config.
    :type config_id: str
    :type config_id: str

    """
    return web.Response(status=200)


async def update_setting(request: web.Request, setting_id, body) -> web.Response:
    """Update Flag

    This endpoint updates the metadata of a Feature Flag or Setting  with a collection of [JSON Patch](http://jsonpatch.com) operations in a specified Config.  Only the &#x60;name&#x60;, &#x60;hint&#x60; and &#x60;tags&#x60; attributes are modifiable by this endpoint. The &#x60;tags&#x60; attribute is a simple collection of the [tag IDs](#operation/get-tags) attached to the given setting.  The advantage of using JSON Patch is that you can describe individual update operations on a resource without touching attributes that you don&#39;t want to change.  For example: We have the following resource. &#x60;&#x60;&#x60; {  \&quot;settingId\&quot;: 5345,  \&quot;key\&quot;: \&quot;myGrandFeature\&quot;,  \&quot;name\&quot;: \&quot;Tihs is a naem with soem typos.\&quot;,  \&quot;hint\&quot;: \&quot;This flag controls my grandioso feature.\&quot;,  \&quot;settingType\&quot;: \&quot;boolean\&quot;,  \&quot;tags\&quot;: [   {    \&quot;tagId\&quot;: 0,    \&quot;name\&quot;: \&quot;sample tag\&quot;,    \&quot;color\&quot;: \&quot;whale\&quot;   }  ] } &#x60;&#x60;&#x60; If we send an update request body as below (it changes the name and adds the already existing tag with the id 2): &#x60;&#x60;&#x60; [  {   \&quot;op\&quot;: \&quot;replace\&quot;,   \&quot;path\&quot;: \&quot;/name\&quot;,   \&quot;value\&quot;: \&quot;This is the name without typos.\&quot;  },  {   \&quot;op\&quot;: \&quot;add\&quot;,   \&quot;path\&quot;: \&quot;/tags/-\&quot;,   \&quot;value\&quot;: 2  } ] &#x60;&#x60;&#x60; Only the &#x60;name&#x60; and &#x60;tags&#x60; are going to be updated and all the other attributes are remaining unchanged. So we get a response like this: &#x60;&#x60;&#x60; {  \&quot;settingId\&quot;: 5345,  \&quot;key\&quot;: \&quot;myGrandFeature\&quot;,  \&quot;name\&quot;: \&quot;This is the name without typos.\&quot;,  \&quot;hint\&quot;: \&quot;This flag controls my grandioso feature.\&quot;,  \&quot;settingType\&quot;: \&quot;boolean\&quot;,  \&quot;tags\&quot;: [   {    \&quot;tagId\&quot;: 0,    \&quot;name\&quot;: \&quot;sample tag\&quot;,    \&quot;color\&quot;: \&quot;whale\&quot;   },   {    \&quot;tagId\&quot;: 2,    \&quot;name\&quot;: \&quot;another tag\&quot;,    \&quot;color\&quot;: \&quot;koala\&quot;   }  ] } &#x60;&#x60;&#x60;

    :param setting_id: The identifier of the Setting.
    :type setting_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = JsonPatch.from_dict(body)
    return web.Response(status=200)
