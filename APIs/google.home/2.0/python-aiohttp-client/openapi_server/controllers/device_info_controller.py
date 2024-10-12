from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_device_id_request import AppDeviceIDRequest
from openapi_server.models.check_ready_status_request import CheckReadyStatusRequest
from openapi_server.models.example1 import Example1
from openapi_server.models.example11 import Example11
from openapi_server.models.example12 import Example12
from openapi_server.models.example13 import Example13
from openapi_server.models.example14 import Example14
from openapi_server.models.example15 import Example15
from openapi_server.models.example16 import Example16
from openapi_server.models.test_internet_download_speed_request import TestInternetDownloadSpeedRequest
from openapi_server import util


async def app_device_id(request: web.Request, body) -> web.Response:
    """App Device ID

    This gives \&quot;app device id\&quot;, \&quot;certificate\&quot; and \&quot;signed data\&quot;.   The &#x60;app_id&#x60; in the request is mandatory and refers to Chromecast backdrop/screensaver app. It has to be set to &#x60;E8C28D3C&#x60;.    The certificate is valid and issued by &#x60;Chromecast ICA 6 (Audio Assist), Google Inc&#x60;.  Not sure what the other two are.

    :param body: 
    :type body: dict | bytes

    """
    body = AppDeviceIDRequest.from_dict(body)
    return web.Response(status=200)


async def check_ready_status(request: web.Request, body) -> web.Response:
    """Check Ready Status

    **Update:** This seems to have changed now and is no longer possible. The error is also new.  Setting &#x60;play_ready_message&#x60; to true plays a welcome message on the device saying \&quot;Hi, I&#39;m your Google Assistant. I&#39;m here to help. To learn a few things you can do, continue in the Google Home app.\&quot;

    :param body: 
    :type body: dict | bytes

    """
    body = CheckReadyStatusRequest.from_dict(body)
    return web.Response(status=200)


async def eureka_info(request: web.Request, params, options, nonce) -> web.Response:
    """Eureka Info

    This gives most of the device info. The GET parameter &#x60;param&#x60; is a comma separated list of json keys to fetch. Currently, these params are known: &#x60;version,audio,name,build_info,detail,device_info,net,wifi,setup,settings,opt_in,opencast,multizone,proxy,night_mode_params,user_eq,room_equalizer,sign,aogh,ultrasound,mesh&#x60;  Nested items can also be filtered using the dot notation. Example: &#x60;audio.digital&#x60;  The &#x60;options&#x60; GET parameter is always set to &#x60;detail&#x60; or &#x60;detail,sign&#x60;. &#x60;sign&#x60; signs the &#x60;nonce&#x60; and returns some value.  The &#x60;nonce&#x60; GET parameter is an integer value signed with needed (see &#x60;option&#x60; parameter above).

    :param params: 
    :type params: str
    :param options: 
    :type options: str
    :param nonce: 
    :type nonce: int

    """
    return web.Response(status=200)


async def locales(request: web.Request, ) -> web.Response:
    """Locales

    Simply returns a list of all supported locales.


    """
    return web.Response(status=200)


async def offer(request: web.Request, ) -> web.Response:
    """Offer

    This gives a token which is used by the Home app to get offers. The offers themselves are not stored on the device.   A new token is generated for every request.


    """
    return web.Response(status=200)


async def test_internet_download_speed(request: web.Request, body) -> web.Response:
    """Test Internet Download Speed

    **Update:** This seems to have been removed. Returns 404 Not Found.  This endpoint tests internet download speed. Any sample file URL can be provided.

    :param body: 
    :type body: dict | bytes

    """
    body = TestInternetDownloadSpeedRequest.from_dict(body)
    return web.Response(status=200)


async def timezones(request: web.Request, ) -> web.Response:
    """Timezones

    Simply returns a list of all supported timezones.


    """
    return web.Response(status=200)
