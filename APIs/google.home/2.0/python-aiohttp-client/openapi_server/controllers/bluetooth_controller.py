from typing import List, Dict
from aiohttp import web

from openapi_server.models.change_discoverability_request import ChangeDiscoverabilityRequest
from openapi_server.models.example110 import Example110
from openapi_server.models.example111 import Example111
from openapi_server.models.example112 import Example112
from openapi_server.models.forgetpaireddevice_request import ForgetpaireddeviceRequest
from openapi_server.models.pairwith_speaker_request import PairwithSpeakerRequest
from openapi_server.models.scanfordevices_request import ScanfordevicesRequest
from openapi_server import util


async def change_discoverability(request: web.Request, body) -> web.Response:
    """Change Discoverability

    *See note for Bluetooth under &#x60;/setup/bluetooth/status&#x60;*  **For Part 1 only**  This enables/disables Home&#39;s bluetooth discovery and other devices can pair with Home (where Home acts as a speaker).

    :param body: 
    :type body: dict | bytes

    """
    body = ChangeDiscoverabilityRequest.from_dict(body)
    return web.Response(status=200)


async def forgetpaireddevice(request: web.Request, body) -> web.Response:
    """Forget paired device

    *See note for Bluetooth under &#x60;/setup/bluetooth/status&#x60;*  **For both parts**  This is to forget paired devices by mac address. Works for both kinds of devices (Part 1 and Part 2).

    :param body: 
    :type body: dict | bytes

    """
    body = ForgetpaireddeviceRequest.from_dict(body)
    return web.Response(status=200)


async def get_paired_devices(request: web.Request, ) -> web.Response:
    """Get Paired Devices

    *See note for Bluetooth under &#x60;/setup/bluetooth/status&#x60;*  **For both parts**  This gives a list of all paired or &#39;bonded&#39; devices. The response field names are self-descriptive.


    """
    return web.Response(status=200)


async def get_scan_results(request: web.Request, ) -> web.Response:
    """Get Scan Results

    *See note for Bluetooth under &#x60;/setup/bluetooth/status&#x60;*  **For Part 2 only**  This returns a list of all nearby bluetooth devices. While the Home app only shows speakers, this list contains all devices including TVs, mobiles, etc.  &#x60;rssi&#x60; is signal strength, &#x60;name&#x60; is name, &#x60;mac_address&#x60; is mac address.   &#x60;device_class&#x60; and &#x60;device_type&#x60; are bluetooth codes.    The Home app only lists those devices with &#x60;expected_profiles&#x60; &gt; 0. Basically, the device should function as a speaker.


    """
    return web.Response(status=200)


async def pairwith_speaker(request: web.Request, body) -> web.Response:
    """Pair with Speaker

    *See note for Bluetooth under &#x60;/setup/bluetooth/status&#x60;*  **For Part 2 only**  This pairs with other bluetooth speakers by mac address.

    :param body: 
    :type body: dict | bytes

    """
    body = PairwithSpeakerRequest.from_dict(body)
    return web.Response(status=200)


async def scanfordevices(request: web.Request, body) -> web.Response:
    """Scan for devices

    *See note for Bluetooth under &#x60;/setup/bluetooth/status&#x60;*  **For Part 2 only**  This initiates scan for other bluetooth speakers/devices. Scan results will be updated continuously for &#x60;timeout&#x60; seconds.   To get the scan results, see /setup/bluetooth/scan_results.

    :param body: 
    :type body: dict | bytes

    """
    body = ScanfordevicesRequest.from_dict(body)
    return web.Response(status=200)


async def status(request: web.Request, ) -> web.Response:
    """Status

    &gt; **There are 2 parts of Bluetooth.** &gt; &gt; *Part 1*: Devices like phones connect to Home and play audio through Home.   &gt; For this, /setup/bluetooth/discovery is used to make Home discoverable. Then devices can connect to it as if Home is just another bluetooth speaker. &gt; &gt; *Part 2*: Bluetooth speakers connect to Home and Home plays audio through the speakers. &gt; For this, /setup/bluetooth/scan and /setup/bluetooth/scan_results are used to connect to other speakers. &gt; &gt; The other endpoints are common for both parts.   **For both parts**  This gives the status of all bluetooth things. - Not sure what &#x60;audio_mode&#x60; is. - &#x60;discovery_enabled&#x60; states whether Home is discoverable. (**Part 1**) - &#x60;connecting_devices&#x60; is a list of all media sources (like phones) connected to Home. (**Part 1**) - &#x60;scanning_enabled&#x60; states whether Home scanning for other bluetooth speakers/devices. (**Part 2**) - &#x60;connected_devices&#x60; is a list of all speakers connected to Home. (**Part 2**)


    """
    return web.Response(status=200)
