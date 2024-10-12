from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_setting_values_model import ConfigSettingValuesModel
from openapi_server.models.json_patch import JsonPatch
from openapi_server.models.setting_value_model import SettingValueModel
from openapi_server.models.setting_value_model_haljson import SettingValueModelHaljson
from openapi_server.models.update_setting_value_model import UpdateSettingValueModel
from openapi_server.models.update_setting_values_with_id_model import UpdateSettingValuesWithIdModel
from openapi_server import util


async def get_setting_value(request: web.Request, environment_id, setting_id) -> web.Response:
    """Get value

    This endpoint returns the value of a Feature Flag or Setting  in a specified Environment identified by the &#x60;environmentId&#x60; parameter.  The most important attributes in the response are the &#x60;value&#x60;, &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60;. The &#x60;value&#x60; represents what the clients will get when the evaluation requests of our SDKs  are not matching to any of the defined Targeting or Percentage Rules, or when there are no additional rules to evaluate.  The &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60; attributes are representing the current  Targeting and Percentage Rules configuration of the actual Feature Flag or Setting  in an **ordered** collection, which means the order of the returned rules is matching to the evaluation order. You can read more about these rules [here](https://configcat.com/docs/advanced/targeting/).

    :param environment_id: The identifier of the Environment.
    :type environment_id: str
    :type environment_id: str
    :param setting_id: The id of the Setting.
    :type setting_id: int

    """
    return web.Response(status=200)


async def get_setting_values(request: web.Request, config_id, environment_id) -> web.Response:
    """Get values

    This endpoint returns the value of a specified Config&#39;s Feature Flags or Settings identified by the &#x60;configId&#x60; parameter in a specified Environment identified by the &#x60;environmentId&#x60; parameter.  The most important attributes in the response are the &#x60;value&#x60;, &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60;. The &#x60;value&#x60; represents what the clients will get when the evaluation requests of our SDKs  are not matching to any of the defined Targeting or Percentage Rules, or when there are no additional rules to evaluate.  The &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60; attributes are representing the current  Targeting and Percentage Rules configuration of the actual Feature Flag or Setting  in an **ordered** collection, which means the order of the returned rules is matching to the evaluation order. You can read more about these rules [here](https://configcat.com/docs/advanced/targeting/).

    :param config_id: The identifier of the Config.
    :type config_id: str
    :type config_id: str
    :param environment_id: The identifier of the Environment.
    :type environment_id: str
    :type environment_id: str

    """
    return web.Response(status=200)


async def post_setting_values(request: web.Request, config_id, environment_id, body, reason=None) -> web.Response:
    """Post values

    This endpoint replaces the values of a specified Config&#39;s Feature Flags or Settings identified by the &#x60;configId&#x60; parameter in a specified Environment identified by the &#x60;environmentId&#x60; parameter.  Only the &#x60;value&#x60;, &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60; attributes are modifiable by this endpoint.  **Important:** As this endpoint is doing a complete replace, it&#39;s important to set every other attribute that you don&#39;t  want to change in its original state. Not listing one means that it will reset.  For example: We have the following resource. &#x60;&#x60;&#x60; {     \&quot;settingValues\&quot;: [   {    \&quot;rolloutPercentageItems\&quot;: [     {      \&quot;percentage\&quot;: 30,      \&quot;value\&quot;: true     },     {      \&quot;percentage\&quot;: 70,      \&quot;value\&quot;: false     }    ],    \&quot;rolloutRules\&quot;: [],    \&quot;value\&quot;: false,    \&quot;settingId\&quot;: 1   }  ] } &#x60;&#x60;&#x60; If we send a replace request body as below: &#x60;&#x60;&#x60; {   \&quot;settingValues\&quot;: [   {    \&quot;value\&quot;: true,    \&quot;settingId\&quot;: 1   }  ] } &#x60;&#x60;&#x60; Then besides that the default value is set to &#x60;true&#x60;, all the Percentage Rules are deleted.  So we get a response like this: &#x60;&#x60;&#x60; {  \&quot;settingValues\&quot;: [   {    \&quot;rolloutPercentageItems\&quot;: [],    \&quot;rolloutRules\&quot;: [],    \&quot;value\&quot;: true,    \&quot;setting\&quot;:     {     \&quot;settingId\&quot;: 1    }   }  ] } &#x60;&#x60;&#x60;  The &#x60;rolloutRules&#x60; property describes two types of rules:  - **Targeting rules**: When you want to add or update a targenting rule, the &#x60;comparator&#x60;, &#x60;comparisonAttribute&#x60;, and &#x60;comparisonValue&#x60; members are required. - **Segment rules**: When you want to add add or update a segment rule, the &#x60;segmentId&#x60; which identifies the desired segment and the &#x60;segmentComparator&#x60; members are required.

    :param config_id: The identifier of the Config.
    :type config_id: str
    :type config_id: str
    :param environment_id: The identifier of the Environment.
    :type environment_id: str
    :type environment_id: str
    :param body: 
    :type body: dict | bytes
    :param reason: The reason note for the Audit Log if the Product&#39;s \&quot;Config changes require a reason\&quot; preference is turned on.
    :type reason: str

    """
    body = UpdateSettingValuesWithIdModel.from_dict(body)
    return web.Response(status=200)


async def replace_setting_value(request: web.Request, environment_id, setting_id, body, reason=None) -> web.Response:
    """Replace value

    This endpoint replaces the whole value of a Feature Flag or Setting in a specified Environment.  Only the &#x60;value&#x60;, &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60; attributes are modifiable by this endpoint.  **Important:** As this endpoint is doing a complete replace, it&#39;s important to set every other attribute that you don&#39;t  want to change in its original state. Not listing one means that it will reset.  For example: We have the following resource. &#x60;&#x60;&#x60; {  \&quot;rolloutPercentageItems\&quot;: [   {    \&quot;percentage\&quot;: 30,    \&quot;value\&quot;: true   },   {    \&quot;percentage\&quot;: 70,    \&quot;value\&quot;: false   }  ],  \&quot;rolloutRules\&quot;: [],  \&quot;value\&quot;: false } &#x60;&#x60;&#x60; If we send a replace request body as below: &#x60;&#x60;&#x60; {  \&quot;value\&quot;: true } &#x60;&#x60;&#x60; Then besides that the default value is set to &#x60;true&#x60;, all the Percentage Rules are deleted.  So we get a response like this: &#x60;&#x60;&#x60; {  \&quot;rolloutPercentageItems\&quot;: [],  \&quot;rolloutRules\&quot;: [],  \&quot;value\&quot;: true } &#x60;&#x60;&#x60;  The &#x60;rolloutRules&#x60; property describes two types of rules:  - **Targeting rules**: When you want to add or update a targenting rule, the &#x60;comparator&#x60;, &#x60;comparisonAttribute&#x60;, and &#x60;comparisonValue&#x60; members are required. - **Segment rules**: When you want to add add or update a segment rule, the &#x60;segmentId&#x60; which identifies the desired segment and the &#x60;segmentComparator&#x60; members are required.

    :param environment_id: The identifier of the Environment.
    :type environment_id: str
    :type environment_id: str
    :param setting_id: The id of the Setting.
    :type setting_id: int
    :param body: 
    :type body: dict | bytes
    :param reason: The reason note for the Audit Log if the Product&#39;s \&quot;Config changes require a reason\&quot; preference is turned on.
    :type reason: str

    """
    body = UpdateSettingValueModel.from_dict(body)
    return web.Response(status=200)


async def update_setting_value(request: web.Request, environment_id, setting_id, body, reason=None) -> web.Response:
    """Update value

    This endpoint updates the value of a Feature Flag or Setting  with a collection of [JSON Patch](http://jsonpatch.com) operations in a specified Environment.  Only the &#x60;value&#x60;, &#x60;rolloutRules&#x60; and &#x60;percentageRules&#x60; attributes are modifiable by this endpoint.  The advantage of using JSON Patch is that you can describe individual update operations on a resource without touching attributes that you don&#39;t want to change. It supports collection reordering, so it also  can be used for reordering the targeting rules of a Feature Flag or Setting.  For example: We have the following resource. &#x60;&#x60;&#x60; {  \&quot;rolloutPercentageItems\&quot;: [   {    \&quot;percentage\&quot;: 30,    \&quot;value\&quot;: true   },   {    \&quot;percentage\&quot;: 70,    \&quot;value\&quot;: false   }  ],  \&quot;rolloutRules\&quot;: [],  \&quot;value\&quot;: false } &#x60;&#x60;&#x60; If we send an update request body as below: &#x60;&#x60;&#x60; [  {   \&quot;op\&quot;: \&quot;replace\&quot;,   \&quot;path\&quot;: \&quot;/value\&quot;,   \&quot;value\&quot;: true  } ] &#x60;&#x60;&#x60; Only the default value is going to be set to &#x60;true&#x60; and all the Percentage Rules are remaining unchanged. So we get a response like this: &#x60;&#x60;&#x60; {  \&quot;rolloutPercentageItems\&quot;: [   {    \&quot;percentage\&quot;: 30,    \&quot;value\&quot;: true   },   {    \&quot;percentage\&quot;: 70,    \&quot;value\&quot;: false   }  ],  \&quot;rolloutRules\&quot;: [],  \&quot;value\&quot;: true } &#x60;&#x60;&#x60;  The &#x60;rolloutRules&#x60; property describes two types of rules:  - **Targeting rules**: When you want to add or update a targenting rule, the &#x60;comparator&#x60;, &#x60;comparisonAttribute&#x60;, and &#x60;comparisonValue&#x60; members are required. - **Segment rules**: When you want to add add or update a segment rule, the &#x60;segmentId&#x60; which identifies the desired segment and the &#x60;segmentComparator&#x60; members are required.

    :param environment_id: The identifier of the Environment.
    :type environment_id: str
    :type environment_id: str
    :param setting_id: The id of the Setting.
    :type setting_id: int
    :param body: 
    :type body: dict | bytes
    :param reason: The reason note for the Audit Log if the Product&#39;s \&quot;Config changes require a reason\&quot; preference is turned on.
    :type reason: str

    """
    body = JsonPatch.from_dict(body)
    return web.Response(status=200)
