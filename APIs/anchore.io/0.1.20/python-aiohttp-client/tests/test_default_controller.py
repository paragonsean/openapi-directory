# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server.models.file_content_search_result import FileContentSearchResult
from openapi_server.models.retrieved_file import RetrievedFile
from openapi_server.models.secret_search_result import SecretSearchResult
from openapi_server.models.service_version import ServiceVersion
from openapi_server.models.token_response import TokenResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_get_oauth_token(client):
    """Test case for get_oauth_token

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'client_id': 'anonymous',
        'grant_type': 'password',
        'password': 'password_example',
        'username': 'username_example'
        }
    response = await client.request(
        method='POST',
        path='/oauth/token',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_health_check(client):
    """Test case for health_check

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/health',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_file_content_search_results(client):
    """Test case for list_file_content_search_results

    Return a list of analyzer artifacts of the specified type
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/images/{image_digest}/artifacts/file_content_search'.format(image_digest='image_digest_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_retrieved_files(client):
    """Test case for list_retrieved_files

    Return a list of analyzer artifacts of the specified type
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/images/{image_digest}/artifacts/retrieved_files'.format(image_digest='image_digest_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_secret_search_results(client):
    """Test case for list_secret_search_results

    Return a list of analyzer artifacts of the specified type
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/images/{image_digest}/artifacts/secret_search'.format(image_digest='image_digest_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ping(client):
    """Test case for ping

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_version_check(client):
    """Test case for version_check

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/version',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

