# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aadhar_number_request_payload import AadharNumberRequestPayload
from openapi_server.models.aadhar_otp_generate_request_pay_load import AadharOtpGenerateRequestPayLoad
from openapi_server.models.create_account_jwt_response import CreateAccountJwtResponse
from openapi_server.models.create_account_with_aadhaar_otp import CreateAccountWithAadhaarOtp
from openapi_server.models.create_account_with_pre_verified_aadhaar import CreateAccountWithPreVerifiedAadhaar
from openapi_server.models.generate_mobile_otp_for_txn_request import GenerateMobileOTPForTxnRequest
from openapi_server.models.resend_otp_request import ResendOTPRequest
from openapi_server.models.txn_response import TxnResponse
from openapi_server.models.verify_aadhaar_otp import VerifyAadhaarOtp
from openapi_server.models.verify_aadhaar_with_bio import VerifyAadhaarWithBio
from openapi_server.models.verify_mobile_request import VerifyMobileRequest


pytestmark = pytest.mark.asyncio

async def test_create_aadhaar_account_using_post(client):
    """Test case for create_aadhaar_account_using_post

    Create Health ID using pre-verified Aadhaar & Mobile.
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
        path='/api/v1/registration/aadhaar/createHealthIdWithPreVerified',
        headers=headers,
        json=account_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_aadhar_otp_using_post(client):
    """Test case for generate_aadhar_otp_using_post

    Generate Aadhaar OTP on registrered mobile number
    """
    generate_otp_request = {"aadhaar":"aadhaar"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/registration/aadhaar/generateOtp',
        headers=headers,
        json=generate_otp_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_mobile_otp_for_txn_using_post(client):
    """Test case for generate_mobile_otp_for_txn_using_post

    Generate Mobile OTP for verification.
    """
    request = {"mobile":"mobile","txnId":"txnId"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/registration/aadhaar/generateMobileOTP',
        headers=headers,
        json=request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_health_id_numbers_by_aadhar_using_post(client):
    """Test case for get_health_id_numbers_by_aadhar_using_post

    Search health id number using aadhar.
    """
    aadhar_number_request_payload = {"aadhaar":"aadhaar"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/registration/aadhaar/search/aadhar',
        headers=headers,
        json=aadhar_number_request_payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resend_aadhar_otp_using_post(client):
    """Test case for resend_aadhar_otp_using_post

    Resend Aadhaar OTP on registrered mobile number to create Health ID.
    """
    request = {"txnId":"txnId"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/registration/aadhaar/resendAadhaarOtp',
        headers=headers,
        json=request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_aadhar_bio_using_post(client):
    """Test case for verify_aadhar_bio_using_post

    Verify Aadhaar using biometrics.
    """
    verify_aadhar_otp_request = {"bioType":"bioType","restrictions":"restrictions","aadhaar":"aadhaar","pid":"pid"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/registration/aadhaar/verifyBio',
        headers=headers,
        json=verify_aadhar_otp_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_aadhar_otp_only_using_post(client):
    """Test case for verify_aadhar_otp_only_using_post

    Verify Aadhaar OTP and continue for mobile verification.
    """
    verify_aadhaar_otp = {"restrictions":"restrictions","otp":"otp","txnId":"txnId"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/registration/aadhaar/verifyOTP',
        headers=headers,
        json=verify_aadhaar_otp,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_aadhar_otp_using_post_0(client):
    """Test case for verify_aadhar_otp_using_post_0

    Verify Aadhaar OTP on registrered mobile number to create Health ID.
    """
    verify_aadhar_otp_request = {"firstName":"firstName","lastName":"lastName","password":"password","profilePhoto":"profilePhoto","mobile":"mobile","restrictions":"restrictions","middleName":"middleName","otp":"otp","email":"email","txnId":"txnId","username":"username"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/registration/aadhaar/createHealthIdWithAadhaarOtp',
        headers=headers,
        json=verify_aadhar_otp_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_verify_mobile_otp_for_txn_using_post(client):
    """Test case for verify_mobile_otp_for_txn_using_post

    Verify Mobile OTP in an existing transaction.
    """
    request = {"otp":"otp","txnId":"txnId"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/registration/aadhaar/verifyMobileOTP',
        headers=headers,
        json=request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

