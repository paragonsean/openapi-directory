# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.complete_verification_request import CompleteVerificationRequest
from openapi_server.models.complete_verification_response import CompleteVerificationResponse
from openapi_server.models.fetch_verification_options_request import FetchVerificationOptionsRequest
from openapi_server.models.fetch_verification_options_response import FetchVerificationOptionsResponse
from openapi_server.models.list_verifications_response import ListVerificationsResponse
from openapi_server.models.verify_location_request import VerifyLocationRequest
from openapi_server.models.verify_location_response import VerifyLocationResponse
from openapi_server.models.voice_of_merchant_state import VoiceOfMerchantState


pytestmark = pytest.mark.asyncio

async def test_mybusinessverifications_locations_fetch_verification_options(client):
    """Test case for mybusinessverifications_locations_fetch_verification_options

    
    """
    body = {"context":{"address":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":0}},"languageCode":"languageCode"}
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
    }
    response = await client.request(
        method='POST',
        path='/v1/{locationfetch_verification_option}'.format(location='location_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusinessverifications_locations_get_voice_of_merchant_state(client):
    """Test case for mybusinessverifications_locations_get_voice_of_merchant_state

    
    """
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
    }
    response = await client.request(
        method='GET',
        path='/v1/{name}/VoiceOfMerchantState'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusinessverifications_locations_verifications_complete(client):
    """Test case for mybusinessverifications_locations_verifications_complete

    
    """
    body = {"pin":"pin"}
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
    }
    response = await client.request(
        method='POST',
        path='/v1/{namecomplet}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusinessverifications_locations_verifications_list(client):
    """Test case for mybusinessverifications_locations_verifications_list

    
    """
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
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/{parent}/verifications'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mybusinessverifications_locations_verify(client):
    """Test case for mybusinessverifications_locations_verify

    
    """
    body = {"emailAddress":"emailAddress","phoneNumber":"phoneNumber","method":"VERIFICATION_METHOD_UNSPECIFIED","context":{"address":{"regionCode":"regionCode","sortingCode":"sortingCode","recipients":["recipients","recipients"],"organization":"organization","postalCode":"postalCode","locality":"locality","sublocality":"sublocality","addressLines":["addressLines","addressLines"],"administrativeArea":"administrativeArea","languageCode":"languageCode","revision":0}},"mailerContact":"mailerContact","languageCode":"languageCode","token":{"tokenString":"tokenString"}}
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
    }
    response = await client.request(
        method='POST',
        path='/v1/{nameverif}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

