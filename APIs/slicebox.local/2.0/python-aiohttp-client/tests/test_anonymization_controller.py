# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.anonymization_data import AnonymizationData
from openapi_server.models.anonymization_key import AnonymizationKey
from openapi_server.models.anonymization_key_query import AnonymizationKeyQuery
from openapi_server.models.anonymization_key_value import AnonymizationKeyValue
from openapi_server.models.confidentiality_option import ConfidentialityOption
from openapi_server.models.image import Image
from openapi_server.models.image_tag_values import ImageTagValues


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_anonymization_anonymize_post(client):
    """Test case for anonymization_anonymize_post

    
    """
    query = [openapi_server.ImageTagValues()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/anonymization/anonymize',
        headers=headers,
        json=query,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_anonymization_keys_export_csv_get(client):
    """Test case for anonymization_keys_export_csv_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/anonymization/keys/export/csv',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_anonymization_keys_get(client):
    """Test case for anonymization_keys_get

    
    """
    params = [('startindex', 0),
                    ('count', 20),
                    ('orderby', 'orderby_example'),
                    ('orderascending', True),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/anonymization/keys',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_anonymization_keys_id_delete(client):
    """Test case for anonymization_keys_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/anonymization/keys/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_anonymization_keys_id_get(client):
    """Test case for anonymization_keys_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/anonymization/keys/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_anonymization_keys_id_keyvalues_get(client):
    """Test case for anonymization_keys_id_keyvalues_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/anonymization/keys/{id}/keyvalues'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_anonymization_keys_query_post(client):
    """Test case for anonymization_keys_query_post

    
    """
    query = openapi_server.AnonymizationKeyQuery()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/anonymization/keys/query',
        headers=headers,
        json=query,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_anonymization_options_get(client):
    """Test case for anonymization_options_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/anonymization/options',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_images_id_anonymize_put(client):
    """Test case for images_id_anonymize_put

    
    """
    tag_values = openapi_server.AnonymizationData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/images/{id}/anonymize'.format(id=56),
        headers=headers,
        json=tag_values,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_images_id_anonymized_post(client):
    """Test case for images_id_anonymized_post

    
    """
    tag_values = openapi_server.AnonymizationData()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/images/{id}/anonymized'.format(id=56),
        headers=headers,
        json=tag_values,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

