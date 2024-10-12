# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.newsletter_settings import NewsletterSettings
from openapi_server.models.newsletter_settings_input import NewsletterSettingsInput
from openapi_server.models.newslettersettingresponse import Newslettersettingresponse


pytestmark = pytest.mark.asyncio

async def test_find_newsletter_settings(client):
    """Test case for find_newsletter_settings

    
    """
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/newsletter_settings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_newsletter_settings_by_id(client):
    """Test case for find_newsletter_settings_by_id

    
    """
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/newsletter_settings/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_newsletter_settings_by_id(client):
    """Test case for update_newsletter_settings_by_id

    
    """
    newsletter_setting = openapi_server.NewsletterSettingsInput()
    params = [('vestorly_auth', 'vestorly_auth_example'),
                    ('access_token', 'access_token_example')]
    headers = { 
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/newsletter_settings/{id}'.format(id='id_example'),
        headers=headers,
        json=newsletter_setting,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

