# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_meta import APIMeta


pytestmark = pytest.mark.asyncio

async def test_delete_api(client):
    """Test case for delete_api

    Deletes the specified API
    """
    headers = { 
        'Accept': 'application/json',
        'AuthToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/apis/{owner}/{api}'.format(owner='owner_example', api='api_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_api_version(client):
    """Test case for delete_api_version

    Deletes a particular version of the specified API
    """
    headers = { 
        'Accept': 'application/json',
        'AuthToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/apis/{owner}/{api}/{version}'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_api_versions(client):
    """Test case for get_api_versions

    Retrieves an API meta listing for all API versions for this owner and API
    """
    headers = { 
        'Accept': 'application/json',
        'AuthToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/apis/{owner}/{api}'.format(owner='owner_example', api='api_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_json_definition(client):
    """Test case for get_json_definition

    Retrieves the Swagger definition for the specified API and version in JSON format
    """
    headers = { 
        'Accept': 'application/json',
        'AuthToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/apis/{owner}/{api}/{version}/swagger.json'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_owner_apis(client):
    """Test case for get_owner_apis

    Retrieves an API meta listing of all APIs defined for this owner
    """
    params = [('sort', NAME),
                    ('order', ASC)]
    headers = { 
        'Accept': 'application/json',
        'AuthToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/apis/{owner}'.format(owner='owner_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_yaml_definition(client):
    """Test case for get_yaml_definition

    Retrieves the Swagger definition for the specified API and version in YAML format
    """
    headers = { 
        'Accept': 'text/vnd.yaml',
        'AuthToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/apis/{owner}/{api}/{version}/swagger.yaml'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publish_api_version(client):
    """Test case for publish_api_version

    Publish a particular version of the specified API
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/api/v1/apis/{owner}/{api}/{version}'.format(owner='owner_example', api='api_example', version='version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_definition(client):
    """Test case for save_definition

    Saves the provided Swagger definition
    """
    definition = None
    params = [('private', False),
                    ('force', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'AuthToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/apis/{owner}/{api}'.format(owner='owner_example', api='api_example'),
        headers=headers,
        json=definition,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_apis(client):
    """Test case for search_apis

    Retrieves a list of currently defined APIs in API meta list format.
    """
    params = [('query', 'query_example'),
                    ('limit', 10),
                    ('offset', 0),
                    ('sort', NAME),
                    ('order', ASC)]
    headers = { 
        'Accept': 'application/json',
        'AuthToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/apis',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

