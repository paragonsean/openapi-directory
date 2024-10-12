# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.offers import Offers


pytestmark = pytest.mark.asyncio

async def test_books_promooffer_accept(client):
    """Test case for books_promooffer_accept

    
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
                    ('androidId', 'android_id_example'),
                    ('device', 'device_example'),
                    ('manufacturer', 'manufacturer_example'),
                    ('model', 'model_example'),
                    ('offerId', 'offer_id_example'),
                    ('product', 'product_example'),
                    ('serial', 'serial_example'),
                    ('volumeId', 'volume_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/books/v1/promooffer/accept',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_promooffer_dismiss(client):
    """Test case for books_promooffer_dismiss

    
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
                    ('androidId', 'android_id_example'),
                    ('device', 'device_example'),
                    ('manufacturer', 'manufacturer_example'),
                    ('model', 'model_example'),
                    ('offerId', 'offer_id_example'),
                    ('product', 'product_example'),
                    ('serial', 'serial_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/books/v1/promooffer/dismiss',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_books_promooffer_get(client):
    """Test case for books_promooffer_get

    
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
                    ('androidId', 'android_id_example'),
                    ('device', 'device_example'),
                    ('manufacturer', 'manufacturer_example'),
                    ('model', 'model_example'),
                    ('product', 'product_example'),
                    ('serial', 'serial_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/books/v1/promooffer/get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

