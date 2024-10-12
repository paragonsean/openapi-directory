# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.google_cloud_identitytoolkit_v2_finalize_mfa_enrollment_request import GoogleCloudIdentitytoolkitV2FinalizeMfaEnrollmentRequest
from openapi_server.models.google_cloud_identitytoolkit_v2_finalize_mfa_enrollment_response import GoogleCloudIdentitytoolkitV2FinalizeMfaEnrollmentResponse
from openapi_server.models.google_cloud_identitytoolkit_v2_finalize_mfa_sign_in_request import GoogleCloudIdentitytoolkitV2FinalizeMfaSignInRequest
from openapi_server.models.google_cloud_identitytoolkit_v2_finalize_mfa_sign_in_response import GoogleCloudIdentitytoolkitV2FinalizeMfaSignInResponse
from openapi_server.models.google_cloud_identitytoolkit_v2_revoke_token_request import GoogleCloudIdentitytoolkitV2RevokeTokenRequest
from openapi_server.models.google_cloud_identitytoolkit_v2_start_mfa_enrollment_request import GoogleCloudIdentitytoolkitV2StartMfaEnrollmentRequest
from openapi_server.models.google_cloud_identitytoolkit_v2_start_mfa_enrollment_response import GoogleCloudIdentitytoolkitV2StartMfaEnrollmentResponse
from openapi_server.models.google_cloud_identitytoolkit_v2_start_mfa_sign_in_request import GoogleCloudIdentitytoolkitV2StartMfaSignInRequest
from openapi_server.models.google_cloud_identitytoolkit_v2_start_mfa_sign_in_response import GoogleCloudIdentitytoolkitV2StartMfaSignInResponse
from openapi_server.models.google_cloud_identitytoolkit_v2_withdraw_mfa_request import GoogleCloudIdentitytoolkitV2WithdrawMfaRequest
from openapi_server.models.google_cloud_identitytoolkit_v2_withdraw_mfa_response import GoogleCloudIdentitytoolkitV2WithdrawMfaResponse


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_accounts_mfa_enrollment_finalize(client):
    """Test case for identitytoolkit_accounts_mfa_enrollment_finalize

    
    """
    body = {"displayName":"displayName","idToken":"idToken","tenantId":"tenantId","phoneVerificationInfo":{"sessionInfo":"sessionInfo","code":"code","phoneNumber":"phoneNumber","androidVerificationProof":"androidVerificationProof"},"totpVerificationInfo":{"sessionInfo":"sessionInfo","verificationCode":"verificationCode"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/accounts/mfaEnrollment:finalize',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_accounts_mfa_enrollment_start(client):
    """Test case for identitytoolkit_accounts_mfa_enrollment_start

    
    """
    body = {"totpEnrollmentInfo":"{}","idToken":"idToken","phoneEnrollmentInfo":{"phoneNumber":"phoneNumber","iosReceipt":"iosReceipt","autoRetrievalInfo":{"appSignatureHash":"appSignatureHash"},"recaptchaToken":"recaptchaToken","iosSecret":"iosSecret","playIntegrityToken":"playIntegrityToken","safetyNetToken":"safetyNetToken"},"tenantId":"tenantId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/accounts/mfaEnrollment:start',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_accounts_mfa_enrollment_withdraw(client):
    """Test case for identitytoolkit_accounts_mfa_enrollment_withdraw

    
    """
    body = {"idToken":"idToken","tenantId":"tenantId","mfaEnrollmentId":"mfaEnrollmentId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/accounts/mfaEnrollment:withdraw',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_accounts_mfa_sign_in_finalize(client):
    """Test case for identitytoolkit_accounts_mfa_sign_in_finalize

    
    """
    body = {"tenantId":"tenantId","phoneVerificationInfo":{"sessionInfo":"sessionInfo","code":"code","phoneNumber":"phoneNumber","androidVerificationProof":"androidVerificationProof"},"mfaPendingCredential":"mfaPendingCredential","mfaEnrollmentId":"mfaEnrollmentId","totpVerificationInfo":{"verificationCode":"verificationCode"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/accounts/mfaSignIn:finalize',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_accounts_mfa_sign_in_start(client):
    """Test case for identitytoolkit_accounts_mfa_sign_in_start

    
    """
    body = {"tenantId":"tenantId","mfaPendingCredential":"mfaPendingCredential","phoneSignInInfo":{"phoneNumber":"phoneNumber","iosReceipt":"iosReceipt","autoRetrievalInfo":{"appSignatureHash":"appSignatureHash"},"recaptchaToken":"recaptchaToken","iosSecret":"iosSecret","playIntegrityToken":"playIntegrityToken","safetyNetToken":"safetyNetToken"},"mfaEnrollmentId":"mfaEnrollmentId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/accounts/mfaSignIn:start',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_identitytoolkit_accounts_revoke_token(client):
    """Test case for identitytoolkit_accounts_revoke_token

    
    """
    body = {"redirectUri":"redirectUri","providerId":"providerId","idToken":"idToken","tenantId":"tenantId","tokenType":"TOKEN_TYPE_UNSPECIFIED","token":"token"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/accounts:revokeToken',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

