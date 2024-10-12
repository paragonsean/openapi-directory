# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aadhar_otp_generate_request_pay_load import AadharOtpGenerateRequestPayLoad
from openapi_server.models.create_account_jwt_response import CreateAccountJwtResponse
from openapi_server.models.create_account_with_pre_verified_aadhaar import CreateAccountWithPreVerifiedAadhaar
from openapi_server.models.health_facility_authentication_request import HealthFacilityAuthenticationRequest
from openapi_server.models.health_facility_changed_password_request import HealthFacilityChangedPasswordRequest
from openapi_server.models.health_facility_password_request import HealthFacilityPasswordRequest
from openapi_server.models.txn_response import TxnResponse


pytestmark = pytest.mark.asyncio

async def test_authenticate_health_facility_using_post(client):
    """Test case for authenticate_health_facility_using_post

    Generate token for heath facility id.
    """
    health_facility_authentication_request = {"password":"password","hfrUid":"hfrUid"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/health/facility/authenticate',
        headers=headers,
        json=health_facility_authentication_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_password_using_post(client):
    """Test case for change_password_using_post

    Change password for heath facility id.
    """
    health_facility_password_request = {"hfrUid":"hfrUid","oldPassword":"oldPassword","newPassword":"newPassword"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/health/facility/change/password',
        headers=headers,
        json=health_facility_password_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_aadhaar_account_using_post1(client):
    """Test case for create_aadhaar_account_using_post1

    Generate Health ID card SVG
    """
    account_request = {"firstName":"firstName","lastName":"lastName","password":"password","profilePhoto":"profilePhoto","healthId":"healthId","middleName":"middleName","email":"email","txnId":"txnId"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/health/facility/createHealthIdWithPreVerified',
        headers=headers,
        json=account_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_facility_otp_using_post(client):
    """Test case for generate_facility_otp_using_post

    Generate health hacility OTP on registrered mobile number
    """
    generate_otp_request = {"aadhaar":"aadhaar"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'x_token': 'Bearer XToken',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/health/facility/generateOtp',
        headers=headers,
        json=generate_otp_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_password_using_post(client):
    """Test case for generate_password_using_post

    Generates password for heath facility id.
    """
    health_facility_password_request = {"hfrUid":"hfrUid"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/health/facility/generate/password',
        headers=headers,
        json=health_facility_password_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_svg_card_using_get1(client):
    """Test case for generate_svg_card_using_get1

    generateSvgCard
    """
    headers = { 
        'Accept': '*/*',
        'accept_language': 'en-US',
        'health_id': 'demo@ndhm',
        'x_token': 'Bearer X-Token',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/health/facility/getSvgCard',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_password_using_post(client):
    """Test case for reset_password_using_post

    Reset password for heath facility id.
    """
    health_facility_password_request = {"hfrUid":"hfrUid"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/health/facility/reset/password',
        headers=headers,
        json=health_facility_password_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

