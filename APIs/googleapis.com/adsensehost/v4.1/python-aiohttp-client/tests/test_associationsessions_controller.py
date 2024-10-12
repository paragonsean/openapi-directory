# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.association_session import AssociationSession


pytestmark = pytest.mark.asyncio

async def test_adsensehost_associationsessions_start(client):
    """Test case for adsensehost_associationsessions_start

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('productCode', ['product_code_example']),
                    ('websiteUrl', 'website_url_example'),
                    ('callbackUrl', 'callback_url_example'),
                    ('userLocale', 'user_locale_example'),
                    ('websiteLocale', 'website_locale_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adsensehost/v4.1/associationsessions/start',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_adsensehost_associationsessions_verify(client):
    """Test case for adsensehost_associationsessions_verify

    
    """
    params = [('alt', 'alt_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('userIp', 'user_ip_example'),
                    ('token', 'token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/adsensehost/v4.1/associationsessions/verify',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

