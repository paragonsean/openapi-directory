# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.demo_auth_response import DemoAuthResponse
from openapi_server.models.demo_auth_verify_response import DemoAuthVerifyResponse
from openapi_server.models.get_device_code_id401_response import GetDeviceCodeId401Response
from openapi_server.models.signupid400_response import SIGNUPId400Response
from openapi_server.models.verify_account_id500_response import VerifyAccountId500Response
from openapi_server.models.verify_otpid400_response import VerifyOTPId400Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_s_ign_up_id(client):
    """Test case for s_ign_up_id

    SIGN UP
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('clientid', 'clientid_example')
    data.add_field('consent', 'consent_example')
    data.add_field('demoauth', 'demoauth_example')
    data.add_field('dob', 56)
    data.add_field('gender', 'gender_example')
    data.add_field('hmac', '/path/to/file')
    data.add_field('mobile', 56)
    data.add_field('name', 'name_example')
    data.add_field('ts', 'ts_example')
    data.add_field('uid', 56)
    data.add_field('verification', 'verification_example')
    response = await client.request(
        method='POST',
        path='/public/signup/2/demoauth',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_verify_otp_id(client):
    """Test case for verify_otp_id

    Verify OTP
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('clientid', 'clientid_example')
    data.add_field('hmac', '/path/to/file')
    data.add_field('mobile', 56)
    data.add_field('otp', 56)
    data.add_field('ts', 'ts_example')
    response = await client.request(
        method='POST',
        path='/public/signup/1/demoauthverify',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

