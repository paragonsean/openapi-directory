# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.device_features import DeviceFeatures
from openapi_server.models.device_info import DeviceInfo
from openapi_server.models.http_validation_error import HTTPValidationError


pytestmark = pytest.mark.asyncio

async def test_detect_device(client):
    """Test case for detect_device

    Detect iot device by service banners and mac address
    """
    body = {"ftp_banner":"AXIS P3346 Fixed Dome Network Camera 5.20 (2017) ready.","hostname":"","http_response":"","https_response":"","nic_mac":"","snmp_sysdescr":"","snmp_sysoid":"","telnet_banner":"","upnp_response":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api-key-header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/device/detect',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

