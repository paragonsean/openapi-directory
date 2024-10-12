# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.endpoint_get_messages_id import EndpointGetMessagesID
from openapi_server.models.endpoint_get_messages_id_metadata import EndpointGetMessagesIDMetadata
from openapi_server.models.endpoint_get_messages_id_metadata_collections import EndpointGetMessagesIDMetadataCollections
from openapi_server.models.endpoint_post_messages_id_metadata import EndpointPostMessagesIDMetadata
from openapi_server.models.endpoint_post_messages_metadata_filters import EndpointPostMessagesMetadataFilters


pytestmark = pytest.mark.asyncio

async def test_messages_id_metadata_collections_get(client):
    """Test case for messages_id_metadata_collections_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/messages/{id}/metadata/collections'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_id_metadata_get(client):
    """Test case for messages_id_metadata_get

    
    """
    params = [('offset', 0),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/messages/{id}/metadata'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_messages_id_metadata_post(client):
    """Test case for messages_id_metadata_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('metadata_0_key', 'metadata_0_key_example')
    data.add_field('metadata_0_privacy', 'metadata_0_privacy_example')
    data.add_field('metadata_0_values', ['metadata_0_values_example'])
    data.add_field('metadata_1_key', 'metadata_1_key_example')
    data.add_field('metadata_1_privacy', 'metadata_1_privacy_example')
    data.add_field('metadata_1_values', ['metadata_1_values_example'])
    data.add_field('metadata_2_key', 'metadata_2_key_example')
    data.add_field('metadata_2_privacy', 'metadata_2_privacy_example')
    data.add_field('metadata_2_values', ['metadata_2_values_example'])
    response = await client.request(
        method='POST',
        path='/connect/api/v4/messages/{id}/metadata'.format(id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_messages_idget(client):
    """Test case for messages_idget

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/connect/api/v4/messages/{id}'.format(id=[56]),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_messages_metadata_filters_post(client):
    """Test case for messages_metadata_filters_post

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('limit', 50)
    data.add_field('metadata_0_key', 'metadata_0_key_example')
    data.add_field('metadata_0_values', ['metadata_0_values_example'])
    data.add_field('metadata_1_key', 'metadata_1_key_example')
    data.add_field('metadata_1_values', ['metadata_1_values_example'])
    data.add_field('metadata_2_key', 'metadata_2_key_example')
    data.add_field('metadata_2_values', ['metadata_2_values_example'])
    data.add_field('offset', 0)
    response = await client.request(
        method='POST',
        path='/connect/api/v4/messages/metadata/filters',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

