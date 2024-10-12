# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.association import Association


pytestmark = pytest.mark.asyncio

async def test_get_activity_collection(client):
    """Test case for get_activity_collection

    Returns list of models
    """
    params = [('title', 'title_example'),
                    ('contributor', 'contributor_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/cam/activity',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_instance_object(client):
    """Test case for get_instance_object

    Returns list of matches
    """
    params = [('title', 'title_example'),
                    ('contributor', 'contributor_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/cam/instance/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_model_collection(client):
    """Test case for get_model_collection

    Returns list of ALL models
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/cam/model',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_model_contributors(client):
    """Test case for get_model_contributors

    Returns list of all contributors across all models
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/cam/model/contributors',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_model_instances(client):
    """Test case for get_model_instances

    Returns list of all instances
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/cam/instances',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_model_object(client):
    """Test case for get_model_object

    Returns a complete model
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/cam/model/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_model_properties(client):
    """Test case for get_model_properties

    Returns list of all properties used across all models
    """
    params = [('title', 'title_example'),
                    ('contributor', 'contributor_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/cam/model/properties',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_model_property_values(client):
    """Test case for get_model_property_values

    Returns list property-values for all models
    """
    params = [('title', 'title_example'),
                    ('contributor', 'contributor_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/cam/model/property_values',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_model_query(client):
    """Test case for get_model_query

    Returns list of models matching query
    """
    params = [('title', 'title_example'),
                    ('contributor', 'contributor_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/cam/model/query',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_physical_interaction(client):
    """Test case for get_physical_interaction

    Returns list of models
    """
    params = [('title', 'title_example'),
                    ('contributor', 'contributor_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/cam/physical_interaction',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

