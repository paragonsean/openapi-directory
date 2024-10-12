from typing import List, Dict
from aiohttp import web

from openapi_server.models.json_patch import JsonPatch
from openapi_server.models.setting_value_model import SettingValueModel
from openapi_server.models.setting_value_model_haljson import SettingValueModelHaljson
from openapi_server.models.update_setting_value_model import UpdateSettingValueModel
from openapi_server import util


async def get_setting_value_by_sdkkey(request: web.Request, setting_key_or_id, x_configcat_sdkkey=None) -> web.Response:
    """Get value

    This endpoint returns the value of a Feature Flag or Setting  in a specified Environment identified by the &lt;a target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; href&#x3D;\&quot;https://app.configcat.com/sdkkey\&quot;&gt;SDK key&lt;/a&gt; passed in the &#x60;X-CONFIGCAT-SDKKEY&#x60; header.  The most important attributes in the response are the &#x60;value&#x60;, &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60;. The &#x60;value&#x60; represents what the clients will get when the evaluation requests of our SDKs  are not matching to any of the defined Targeting or Percentage Rules, or when there are no additional rules to evaluate.  The &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60; attributes are representing the current  Targeting and Percentage Rules configuration of the actual Feature Flag or Setting  in an **ordered** collection, which means the order of the returned rules is matching to the evaluation order. You can read more about these rules [here](https://configcat.com/docs/advanced/targeting/).

    :param setting_key_or_id: The key or id of the Setting.
    :type setting_key_or_id: str
    :param x_configcat_sdkkey: The ConfigCat SDK Key. (https://app.configcat.com/sdkkey)
    :type x_configcat_sdkkey: str

    """
    return web.Response(status=200)


async def replace_setting_value_by_sdkkey(request: web.Request, setting_key_or_id, body, reason=None, x_configcat_sdkkey=None) -> web.Response:
    """Replace value

    This endpoint replaces the value of a Feature Flag or Setting  in a specified Environment identified by the &lt;a target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; href&#x3D;\&quot;https://app.configcat.com/sdkkey\&quot;&gt;SDK key&lt;/a&gt; passed in the &#x60;X-CONFIGCAT-SDKKEY&#x60; header.  Only the &#x60;value&#x60;, &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60; attributes are modifiable by this endpoint.  **Important:** As this endpoint is doing a complete replace, it&#39;s important to set every other attribute that you don&#39;t  want to change to its original state. Not listing one means that it will reset.  For example: We have the following resource. &#x60;&#x60;&#x60; {  \&quot;rolloutPercentageItems\&quot;: [   {    \&quot;percentage\&quot;: 30,    \&quot;value\&quot;: true   },   {    \&quot;percentage\&quot;: 70,    \&quot;value\&quot;: false   }  ],  \&quot;rolloutRules\&quot;: [],  \&quot;value\&quot;: false } &#x60;&#x60;&#x60; If we send a replace request body as below: &#x60;&#x60;&#x60; {  \&quot;value\&quot;: true } &#x60;&#x60;&#x60; Then besides that the default served value is set to &#x60;true&#x60;, all the Percentage Rules are deleted.  So we get a response like this: &#x60;&#x60;&#x60; {  \&quot;rolloutPercentageItems\&quot;: [],  \&quot;rolloutRules\&quot;: [],  \&quot;value\&quot;: true } &#x60;&#x60;&#x60;

    :param setting_key_or_id: The key or id of the Setting.
    :type setting_key_or_id: str
    :param body: 
    :type body: dict | bytes
    :param reason: The reason note for the Audit Log if the Product&#39;s \&quot;Config changes require a reason\&quot; preference is turned on.
    :type reason: str
    :param x_configcat_sdkkey: The ConfigCat SDK Key. (https://app.configcat.com/sdkkey)
    :type x_configcat_sdkkey: str

    """
    body = UpdateSettingValueModel.from_dict(body)
    return web.Response(status=200)


async def update_setting_value_by_sdkkey(request: web.Request, setting_key_or_id, body, reason=None, x_configcat_sdkkey=None) -> web.Response:
    """Update value

    This endpoint updates the value of a Feature Flag or Setting  with a collection of [JSON Patch](http://jsonpatch.com) operations in a specified Environment identified by the &lt;a target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot; href&#x3D;\&quot;https://app.configcat.com/sdkkey\&quot;&gt;SDK key&lt;/a&gt; passed in the &#x60;X-CONFIGCAT-SDKKEY&#x60; header.  Only the &#x60;value&#x60;, &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60; attributes are modifiable by this endpoint.  The advantage of using JSON Patch is that you can describe individual update operations on a resource without touching attributes that you don&#39;t want to change. It supports collection reordering, so it also  can be used for reordering the targeting rules of a Feature Flag or Setting.  For example: We have the following resource. &#x60;&#x60;&#x60; {  \&quot;rolloutPercentageItems\&quot;: [   {    \&quot;percentage\&quot;: 30,    \&quot;value\&quot;: true   },   {    \&quot;percentage\&quot;: 70,    \&quot;value\&quot;: false   }  ],  \&quot;rolloutRules\&quot;: [],  \&quot;value\&quot;: false } &#x60;&#x60;&#x60; If we send an update request body as below: &#x60;&#x60;&#x60; [  {   \&quot;op\&quot;: \&quot;replace\&quot;,   \&quot;path\&quot;: \&quot;/value\&quot;,   \&quot;value\&quot;: true  } ] &#x60;&#x60;&#x60; Only the default served value is going to be set to &#x60;true&#x60; and all the Percentage Rules are remaining unchanged. So we get a response like this: &#x60;&#x60;&#x60; {  \&quot;rolloutPercentageItems\&quot;: [   {    \&quot;percentage\&quot;: 30,    \&quot;value\&quot;: true   },   {    \&quot;percentage\&quot;: 70,    \&quot;value\&quot;: false   }  ],  \&quot;rolloutRules\&quot;: [],  \&quot;value\&quot;: true } &#x60;&#x60;&#x60;

    :param setting_key_or_id: The key or id of the Setting.
    :type setting_key_or_id: str
    :param body: 
    :type body: dict | bytes
    :param reason: The reason note for the Audit Log if the Product&#39;s \&quot;Config changes require a reason\&quot; preference is turned on.
    :type reason: str
    :param x_configcat_sdkkey: The ConfigCat SDK Key. (https://app.configcat.com/sdkkey)
    :type x_configcat_sdkkey: str

    """
    body = JsonPatch.from_dict(body)
    return web.Response(status=200)
