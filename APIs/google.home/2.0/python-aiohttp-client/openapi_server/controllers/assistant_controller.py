from typing import List, Dict
from aiohttp import web

from openapi_server.models.accessibility_request import AccessibilityRequest
from openapi_server.models.alarm_volume_request import AlarmVolumeRequest
from openapi_server.models.delete_alarmsand_timers_request import DeleteAlarmsandTimersRequest
from openapi_server.models.example18 import Example18
from openapi_server.models.example19 import Example19
from openapi_server.models.getcurrentstate import Getcurrentstate
from openapi_server.models.getcurrentvalues import Getcurrentvalues
from openapi_server.models.getvolume import Getvolume
from openapi_server.models.set_equalizer_values_request import SetEqualizerValuesRequest
from openapi_server import util


async def accessibility(request: web.Request, body) -> web.Response:
    """Accessibility

    This controls Accessibility sounds. &#x60;hotword_enabled&#x60; is for &#39;Play start sound&#39; and &#x60;endpoint_enabled&#x60; is for &#39;Play end sound&#39;.   Sending an empty-body POST request returns the current values.   Either of the fields or both can be sent and new values will be saved.

    :param body: 
    :type body: dict | bytes

    """
    body = AccessibilityRequest.from_dict(body)
    return web.Response(status=200)


async def alarm_volume(request: web.Request, body) -> web.Response:
    """Alarm Volume

    This gets and sets alarms and timers volume.   **Note:** This is not the same as normal volume.  Volume is a float number in [0, 1] where 0 is minimum and 1 is maximum.   Sending an empty body gets the volume. Sending &#x60;volume&#x60; sets the volume.

    :param body: 
    :type body: dict | bytes

    """
    body = AlarmVolumeRequest.from_dict(body)
    return web.Response(status=200)


async def delete_alarmsand_timers(request: web.Request, body) -> web.Response:
    """Delete Alarms and Timers

    This deletes alarms and timers by their id.  &#x60;ids&#x60; is a list of ids to be deleted. Sending invalid id still returns a 200 OK. The &#x60;/&#x60; in the ids have to be escaped like &#x60;/&#x60;.

    :param body: 
    :type body: dict | bytes

    """
    body = DeleteAlarmsandTimersRequest.from_dict(body)
    return web.Response(status=200)


async def do_not_disturb(request: web.Request, content_type) -> web.Response:
    """Do Not Disturb

    This is for the Do Not Disturb option. Sending an empty-body POST returns the current value. Sending a new value changes it.

    :param content_type: 
    :type content_type: str

    """
    return web.Response(status=200)


async def get_alarmsand_timers(request: web.Request, ) -> web.Response:
    """Get Alarms and Timers

    This gives a list of all active alarms and timers.  Both alarms and timers have &#x60;id&#x60;s which can be used to delete them. (There is no known way of creating/deleting yet). The value of &#x60;status&#x60; have different meanings for alarms and timers (given below).  Alarms have &#x60;date_pattern&#x60; and &#x60;time_pattern&#x60; with day, month, year, hour, minute, second. &#x60;fire_time&#x60; is the same in unix time (milliseconds, not seconds).   &#x60;status&#x60; is 1 for set up and 2 for ringing.  Timers have &#x60;original_duration&#x60; is the original duration.   &#x60;status&#x60; is 1 for set up and 3 for ringing.


    """
    return web.Response(status=200)


async def set_equalizer_values(request: web.Request, body) -> web.Response:
    """Set Equalizer Values

    This can only set new equalizer values. To get already set values, use /setup/eureka_info.  The body is mandatory. It can either contain &#x60;low_shelf&#x60; or &#x60;high_shelf&#x60; or both.  &#x60;low_shelf.gain_db&#x60; and &#x60;high_shelf.gain_db&#x60; refer to **bass** and **treble** respectively.  Default values are 0 for both.   While the slider in the Home app only ranges from -6 to +6, they can be set to any integer like 50 or -100. These changes persist.

    :param body: 
    :type body: dict | bytes

    """
    body = SetEqualizerValuesRequest.from_dict(body)
    return web.Response(status=200)
