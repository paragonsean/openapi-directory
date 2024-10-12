# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.hid_change_password_request_payload import HidChangePasswordRequestPayload
from openapi_server.models.hid_otp_request_paylaod import HidOtpRequestPaylaod
from openapi_server.models.txn_response import TxnResponse
from openapi_server.models.update_account_request import UpdateAccountRequest
from openapi_server.models.user_dto import UserDTO
from openapi_server.models.validate_token_request import ValidateTokenRequest
from openapi_server.models.verify_aadhaar_otp import VerifyAadhaarOtp


pytestmark = pytest.mark.asyncio

async def test_change_password_via_aadhar_using_post(client):
    """Test case for change_password_via_aadhar_using_post

    Change password via Aadhar for heath id.
    """
    hid_otp_request_paylaod = {"newPassword":"newPassword","otp":"otp","txnId":"txnId"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'x_token': 'Bearer X-Token',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/account/change/passwd/byAadhaar',
        headers=headers,
        json=hid_otp_request_paylaod,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_password_via_mobile_using_post(client):
    """Test case for change_password_via_mobile_using_post

    Change password via mobile for heath id.
    """
    hid_otp_request_paylaod = {"newPassword":"newPassword","otp":"otp","txnId":"txnId"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'x_token': 'Bearer X-Token',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/account/change/passwd/byMobile',
        headers=headers,
        json=hid_otp_request_paylaod,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_password_via_using_post(client):
    """Test case for change_password_via_using_post

    Change password via password for heath id.
    """
    health_facility_password_request = {"oldPassword":"oldPassword","newPassword":"newPassword"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'x_token': 'Bearer X-Token',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/account/change/password',
        headers=headers,
        json=health_facility_password_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_account_using_delete(client):
    """Test case for delete_account_using_delete

    Delete account
    """
    headers = { 
        'Accept': '*/*',
        'accept_language': 'en-US',
        'x_token': 'Bearer X-Token',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/account/profile',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_aadhar_otp_using_get(client):
    """Test case for generate_aadhar_otp_using_get

    Generate Aadhaar OTP on registrered mobile number.
    """
    headers = { 
        'Accept': '*/*',
        'accept_language': 'en-US',
        'x_token': 'Bearer X-Token',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/account/change/passwd/generateAadhaarOTP',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_card_using_get(client):
    """Test case for generate_card_using_get

    Generate Health ID card in PDF format
    """
    headers = { 
        'Accept': '*/*',
        'accept_language': 'en-US',
        'x_token': 'Bearer X-Token',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/account/getCard',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_mobile_otp_using_get(client):
    """Test case for generate_mobile_otp_using_get

    Generate Mobile OTP to start registration.
    """
    headers = { 
        'Accept': '*/*',
        'accept_language': 'en-US',
        'x_token': 'Bearer X-Token',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/account/change/passwd/generateMobileOTP',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_png_card_using_get(client):
    """Test case for generate_png_card_using_get

    Generate Health ID card PNG
    """
    headers = { 
        'Accept': '*/*',
        'accept_language': 'en-US',
        'x_token': 'Bearer X-Token',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/account/getPngCard',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_svg_card_using_get(client):
    """Test case for generate_svg_card_using_get

    Generate Health ID card SVG
    """
    headers = { 
        'Accept': '*/*',
        'accept_language': 'en-US',
        'x_token': 'Bearer X-Token',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/account/getSvgCard',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generatere_kyc_aadhar_otp_using_post(client):
    """Test case for generatere_kyc_aadhar_otp_using_post

    Generate Aadhaar OTP on registrered for link account with aadhar number
    """
    headers = { 
        'Accept': '*/*',
        'accept_language': 'en-US',
        'x_token': 'Bearer X-Token',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/account/aadhaar/generateOTP',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account_information_using_get(client):
    """Test case for get_account_information_using_get

    Get account information.
    """
    headers = { 
        'Accept': '*/*',
        'accept_language': 'en-US',
        'x_token': 'Bearer XToken',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/account/profile',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_benefits_using_get(client):
    """Test case for get_benefits_using_get

    Get List of Benefits associated with HealthID.
    """
    headers = { 
        'Accept': '*/*',
        'accept_language': 'en-US',
        'x_token': 'Bearer XToken',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/account/benefits',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_qr_code_using_get(client):
    """Test case for get_qr_code_using_get

    Get Quick Response code in PNG format for this account.
    """
    headers = { 
        'Accept': 'image/png',
        'accept_language': 'en-US',
        'x_token': 'Bearer XToken',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/account/qrCode',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_account_information_using_post(client):
    """Test case for update_account_information_using_post

    Update account information
    """
    request = {"lastName":"lastName","pincode":0,"address":"address","districtCode":"districtCode","townCode":"townCode","healthId":"healthId","monthOfBirth":"monthOfBirth","villageCode":"villageCode","firstName":"firstName","password":"password","profilePhoto":"profilePhoto","subdistrictCode":"subdistrictCode","dayOfBirth":"dayOfBirth","middleName":"middleName","stateCode":"stateCode","wardCode":"wardCode","email":"email","yearOfBirth":"yearOfBirth"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'x_token': 'Bearer X-Token',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/account/profile',
        headers=headers,
        json=request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_validate_token_using_post(client):
    """Test case for validate_token_using_post

    Validate auth token
    """
    request = {"authToken":"authToken"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/account/token',
        headers=headers,
        json=request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_aadhar_otp_only_using_post1(client):
    """Test case for verify_aadhar_otp_only_using_post1

    Verify Aadhaar OTP to complete KYC/re-KYC verification.
    """
    verify_aadhaar_otp = {"restrictions":"restrictions","otp":"otp","txnId":"txnId"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'x_token': 'Bearer X-Token',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/account/aadhaar/verifyOTP',
        headers=headers,
        json=verify_aadhaar_otp,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

