# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.auth_account_aadhaar_bio_request import AuthAccountAadhaarBioRequest
from openapi_server.models.auth_account_aadhaar_otp_request import AuthAccountAadhaarOTPRequest
from openapi_server.models.auth_account_mobile_otp_request import AuthAccountMobileOTPRequest
from openapi_server.models.auth_account_with_demographics_request import AuthAccountWithDemographicsRequest
from openapi_server.models.auth_init_request import AuthInitRequest
from openapi_server.models.auth_mobile_otp_request import AuthMobileOTPRequest
from openapi_server.models.auth_with_mobile_txn_and_user_data import AuthWithMobileTxnAndUserData
from openapi_server.models.auth_with_password_request import AuthWithPasswordRequest
from openapi_server.models.jwt_request import JwtRequest
from openapi_server.models.jwt_response import JwtResponse
from openapi_server.models.resend_otp_request import ResendOTPRequest
from openapi_server.models.txn_response import TxnResponse


pytestmark = pytest.mark.asyncio

async def test_auth_account_password_request_using_post(client):
    """Test case for auth_account_password_request_using_post

    Authentication with PASSWORD based auth transaction.
    """
    authentication_request = {"password":"password","txnId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/confirmWithPassword',
        headers=headers,
        json=authentication_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_with_mobile_token_using_post(client):
    """Test case for auth_with_mobile_token_using_post

    Authenticate using verified Mobile Number and user data
    """
    auth_request = {"gender":"gender","name":"name","healthId":"healthId","token":"token","txnId":"txnId","yearOfBirth":"yearOfBirth"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/authWithMobileToken',
        headers=headers,
        json=auth_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authenticate_user_using_post(client):
    """Test case for authenticate_user_using_post

    Authenticate request to generate Mobile OTP using Health ID number / Health ID
    """
    auth_request = {"healthid":"healthid"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/authWithMobile',
        headers=headers,
        json=auth_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authenticate_with_password_using_post(client):
    """Test case for authenticate_with_password_using_post

    Authenticate using Health ID number / Health ID and password
    """
    authentication_request = {"password":"password","healthId":"healthId"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/authPassword',
        headers=headers,
        json=authentication_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cert_using_get(client):
    """Test case for cert_using_get

    Auth token public key.
    """
    headers = { 
        'Accept': '*/*',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/auth/cert',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_confirm_with_aadhaar_bio_using_post(client):
    """Test case for confirm_with_aadhaar_bio_using_post

    Authentication with Aadhaar Biometric based auth transaction.
    """
    authentication_request = {"bioType":"bioType","pid":"pid","authType":"FINGERSCAN","txnId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/confirmWithAadhaarBio',
        headers=headers,
        json=authentication_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_confirm_with_aadhaar_otp_using_post(client):
    """Test case for confirm_with_aadhaar_otp_using_post

    Authentication with Aadhaar OTP based auth transaction.
    """
    authentication_request = {"otp":"otp","txnId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/confirmWithAadhaarOtp',
        headers=headers,
        json=authentication_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_confirm_with_demographics_using_post(client):
    """Test case for confirm_with_demographics_using_post

    Authenticate using demographic data of user.
    """
    authentication_request = {"gender":"gender","name":"name","txnId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","yearOfBirth":"yearOfBirth"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/confirmWithDemographics',
        headers=headers,
        json=authentication_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_confirm_with_mobile_using_post(client):
    """Test case for confirm_with_mobile_using_post

    Authentication with Mobile OTP based auth transaction.
    """
    authentication_request = {"otp":"otp","txnId":"txnId"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/confirmWithMobileOTP',
        headers=headers,
        json=authentication_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_initiate_auth_using_post(client):
    """Test case for initiate_auth_using_post

    Initiate authentication process for given Health ID
    """
    auth_request = {"healthid":"healthid","authMethod":"AADHAAR_OTP"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/init',
        headers=headers,
        json=auth_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resend_auth_mobile_otp_using_post(client):
    """Test case for resend_auth_mobile_otp_using_post

    Resend Aadhaar/Mobile OTP for Authentication Transaction.
    """
    resend_otp_request = {"txnId":"txnId"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/auth/resendAuthOTP',
        headers=headers,
        json=resend_otp_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

