# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_account_by_verified_mobile_request import CreateAccountByVerifiedMobileRequest
from openapi_server.models.create_account_jwt_response import CreateAccountJwtResponse
from openapi_server.models.generate_mobile_otp_request import GenerateMobileOTPRequest
from openapi_server.models.mobile_verification_token import MobileVerificationToken
from openapi_server.models.resend_otp_request import ResendOTPRequest
from openapi_server.models.txn_response import TxnResponse
from openapi_server.models.verify_mobile_request import VerifyMobileRequest


pytestmark = pytest.mark.asyncio

async def test_generate_mobile_otp_using_post1(client):
    """Test case for generate_mobile_otp_using_post1

    Generate Mobile OTP to start registration
    """
    generate_otp_request = {"mobile":"mobile"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/registration/mobile/generateOtp',
        headers=headers,
        json=generate_otp_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resent_otp_using_post(client):
    """Test case for resent_otp_using_post

    Resend Mobile OTP for Health ID registration
    """
    resend_request = {"txnId":"txnId"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/registration/mobile/resendOtp',
        headers=headers,
        json=resend_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_mobile_otp_using_post(client):
    """Test case for verify_mobile_otp_using_post

    Verify Mobile OTP sent as part of registration transaction.
    """
    verify_otp_request = {"otp":"otp","txnId":"txnId"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/registration/mobile/verifyOtp',
        headers=headers,
        json=verify_otp_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_user_via_mobile_using_post(client):
    """Test case for verify_user_via_mobile_using_post

    Create Health ID with verified mobile token
    """
    create_account_request = {"lastName":"lastName","pincode":0,"address":"address","districtCode":"districtCode","gender":"gender","townCode":"townCode","restrictions":"restrictions","healthId":"healthId","monthOfBirth":"monthOfBirth","token":"token","villageCode":"villageCode","firstName":"firstName","password":"password","profilePhoto":"profilePhoto","subdistrictCode":"subdistrictCode","dayOfBirth":"dayOfBirth","name":"name","middleName":"middleName","stateCode":"stateCode","wardCode":"wardCode","email":"email","txnId":"txnId","yearOfBirth":"yearOfBirth"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/registration/mobile/createHealthId',
        headers=headers,
        json=create_account_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

