# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.aadhar_otp_generate_request_pay_load import AadharOtpGenerateRequestPayLoad
from openapi_server.models.auth_account_aadhaar_otp_request import AuthAccountAadhaarOTPRequest
from openapi_server.models.generate_mobile_otp_request import GenerateMobileOTPRequest
from openapi_server.models.retrieve_health_id_payload_response import RetrieveHealthIdPayloadResponse
from openapi_server.models.retrive_health_id_mobile_pay_load import RetriveHealthIdMobilePayLoad
from openapi_server.models.txn_response import TxnResponse


pytestmark = pytest.mark.asyncio

async def test_generate_aadhar_otp_using_post1(client):
    """Test case for generate_aadhar_otp_using_post1

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
        path='/api/v1/forgot/healthId/aadhaar/generateOtp',
        headers=headers,
        json=generate_otp_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_mobile_otp_using_post(client):
    """Test case for generate_mobile_otp_using_post

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
        path='/api/v1/forgot/healthId/mobile/generateOtp',
        headers=headers,
        json=generate_otp_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieval_health_id_by_aadhar_using_post(client):
    """Test case for retrieval_health_id_by_aadhar_using_post

    Verify aadhar OTP sent as part of forgetHealth id.
    """
    auth_account_aadhaar_otp_request = {"otp":"otp","txnId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/forgot/healthId/aadhaar',
        headers=headers,
        json=auth_account_aadhaar_otp_request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieval_health_id_by_mobile_using_post(client):
    """Test case for retrieval_health_id_by_mobile_using_post

    Verify Mobile OTP sent as  part of forgetHealth id.
    """
    retrive_health_id_mobile_pay_load = {"firstName":"firstName","lastName":"lastName","gender":"gender","dayOfBirth":"dayOfBirth","name":"name","middleName":"middleName","otp":"otp","monthOfBirth":"monthOfBirth","txnId":"txnId","yearOfBirth":"yearOfBirth"}
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'accept_language': 'en-US',
        'Authorization': 'special-key',
        'X-HIP-ID': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/forgot/healthId/mobile',
        headers=headers,
        json=retrive_health_id_mobile_pay_load,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

