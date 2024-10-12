# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_media_processor_response import ListMediaProcessorResponse
from openapi_server.models.media_processor_enum_order import MediaProcessorEnumOrder
from openapi_server.models.media_processor_enum_status import MediaProcessorEnumStatus
from openapi_server.models.media_processor_enum_update_status import MediaProcessorEnumUpdateStatus
from openapi_server.models.media_v1_media_processor import MediaV1MediaProcessor


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_media_processor(client):
    """Test case for create_media_processor

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'extension': 'extension_example',
        'extension_context': 'extension_context_example',
        'extension_environment': None,
        'max_duration': 56,
        'status_callback': 'status_callback_example',
        'status_callback_method': 'status_callback_method_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/MediaProcessors',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_media_processor(client):
    """Test case for fetch_media_processor

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/MediaProcessors/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_media_processor(client):
    """Test case for list_media_processor

    
    """
    params = [('Order', openapi_server.MediaProcessorEnumOrder()),
                    ('Status', openapi_server.MediaProcessorEnumStatus()),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/MediaProcessors',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_media_processor(client):
    """Test case for update_media_processor

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'status': openapi_server.MediaProcessorEnumUpdateStatus()
        }
    response = await client.request(
        method='POST',
        path='/v1/MediaProcessors/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

