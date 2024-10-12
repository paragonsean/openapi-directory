from typing import List, Dict
from aiohttp import web

from openapi_server.models.example17 import Example17
from openapi_server.models.night_modesettings_request import NightModesettingsRequest
from openapi_server.models.rebootand_factory_reset_request import RebootandFactoryResetRequest
from openapi_server.models.set_eureka_info_request import SetEurekaInfoRequest
from openapi_server import util


async def night_modesettings(request: web.Request, body) -> web.Response:
    """Night Mode settings

    This sets night mode options.   To view currently set values, use /setup/eureka_info.   If &#x60;enabled&#x60; is set to false, night mode is disabled and the other values do not matter.   &#x60;led_brightness&#x60; and &#x60;volume&#x60; refer to the maximum LED Brightness and Volume that is set during night mode.   &#x60;demo_to_user&#x60; is always set to &#x60;true&#x60; so change in values will be visible in realtime (like brightness).   &#x60;windows&#x60;: A combination of &#x60;length_hours&#x60; and &#x60;start_hour&#x60; is used to define start and end times for night mode. In this example, night mode starts at 10 PM (22) and ends at 6 AM (8 hours later). &#x60;windows.days&#x60; is an array of days of week when night mode will be enabled. Example: 0-&gt;Sunday, 1-&gt; Monday, ..., 6-&gt;Saturday.

    :param body: 
    :type body: dict | bytes

    """
    body = NightModesettingsRequest.from_dict(body)
    return web.Response(status=200)


async def rebootand_factory_reset(request: web.Request, body) -> web.Response:
    """Reboot and Factory Reset

    This can simply reboot the device (&#x60;params: \&quot;now\&quot;&#x60;) or factory reset the device (&#x60;params: \&quot;fdr\&quot;&#x60;).

    :param body: 
    :type body: dict | bytes

    """
    body = RebootandFactoryResetRequest.from_dict(body)
    return web.Response(status=200)


async def set_eureka_info(request: web.Request, body) -> web.Response:
    """Set Eureka Info

    This can set custom values to some options.  Only fields to be modified need to be sent, not all. The example has some modifiable fields.  TODO: List all modifiable fields.  Sending non-existant fields will still return a 200 OK, but they are not saved.

    :param body: 
    :type body: dict | bytes

    """
    body = SetEurekaInfoRequest.from_dict(body)
    return web.Response(status=200)
