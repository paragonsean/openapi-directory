# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api import API
from openapi_server.models.get_providers200_response import GetProviders200Response
from openapi_server.models.get_services200_response import GetServices200Response
from openapi_server.models.metrics import Metrics


pytestmark = pytest.mark.asyncio

async def test_get_api(client):
    """Test case for get_api

    Retrieve one version of a particular API
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/specs/{provider}/{api_jso}'.format(provider='apis.guru', api='2.1.0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_metrics(client):
    """Test case for get_metrics

    Get basic metrics
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/metrics.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_provider(client):
    """Test case for get_provider

    List all APIs for a particular provider
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/{provider_jso}'.format(provider='apis.guru'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_providers(client):
    """Test case for get_providers

    List all providers
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/providers.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_service_api(client):
    """Test case for get_service_api

    Retrieve one version of a particular API with a serviceName.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/specs/{provider}/{service}/{api_jso}'.format(provider='apis.guru', service='graph', api='2.1.0'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_services(client):
    """Test case for get_services

    List all serviceNames for a particular provider
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/{provider}/services.json'.format(provider='apis.guru'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_apis(client):
    """Test case for list_apis

    List all APIs
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/list.json',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

