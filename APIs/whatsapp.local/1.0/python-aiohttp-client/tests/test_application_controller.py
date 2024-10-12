# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_settings import ApplicationSettings
from openapi_server.models.get_media_providers_response import GetMediaProvidersResponse
from openapi_server.models.media_provider import MediaProvider
from openapi_server.models.response import Response
from openapi_server.models.set_shards_request_body import SetShardsRequestBody


pytestmark = pytest.mark.asyncio

async def test_delete_media_providers(client):
    """Test case for delete_media_providers

    Delete-Media-Providers
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/settings/application/media/providers/{provider_name}'.format(provider_name='provider_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_application_settings(client):
    """Test case for get_application_settings

    Get-Application-Settings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/settings/application',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_media_providers(client):
    """Test case for get_media_providers

    Get-Media-Providers
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/settings/application/media/providers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_application_settings(client):
    """Test case for reset_application_settings

    Reset-Application-Settings
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/settings/application',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_shards(client):
    """Test case for set_shards

    Set-Shards
    """
    body = {"cc":"<Country Code>","phone_number":"<Phone Number>","pin":"<Two-Step PIN>","shards":32}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/account/shards',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_application_settings(client):
    """Test case for update_application_settings

    Update-Application-Settings
    """
    body = {"webhooks":{"url":"<Webhook URL, https>"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/settings/application',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_media_providers(client):
    """Test case for update_media_providers

    Update-Media-Providers
    """
    body = [{"config":{"bearer":"<Bearer Auth Token>"},"name":"<Provider Name>","type":"www"}]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/settings/application/media/providers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

