from typing import List, Dict
from aiohttp import web

from openapi_server.models.device_authorization_code import DeviceAuthorizationCode
from openapi_server.models.device_authorization_code_response import DeviceAuthorizationCodeResponse
from openapi_server.models.get_device_code_id400_response import GetDeviceCodeId400Response
from openapi_server.models.get_device_code_id401_response import GetDeviceCodeId401Response
from openapi_server.models.get_device_code_id500_response import GetDeviceCodeId500Response
from openapi_server import util


async def get_device_code_id(request: web.Request, body=None) -> web.Response:
    """Get Device Code

    The client device calls the DigiLocker API to get the device code by providing the client_id issued to the device OEM and either the username or the mobile number of the user. DigiLocker responds with a device code and then sends an OTP on the mobile number and email address associated with the user’s account. The masked mobile number and email address is also sent in response. The device should use these values to notify the users about the mobile and email address on which the OTP has been sent.

    :param body: 
    :type body: dict | bytes

    """
    body = DeviceAuthorizationCode.from_dict(body)
    return web.Response(status=200)
