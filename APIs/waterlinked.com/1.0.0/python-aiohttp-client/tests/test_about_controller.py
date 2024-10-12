# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.waterlinked_about import WaterlinkedAbout
from openapi_server.models.waterlinked_operation_response import WaterlinkedOperationResponse
from openapi_server.models.waterlinked_status import WaterlinkedStatus
from openapi_server.models.waterlinked_temperature import WaterlinkedTemperature
from openapi_server.models.wupdater_apiversion import WupdaterApiversion


pytestmark = pytest.mark.asyncio

async def test_about_api_version(client):
    """Test case for about_api_version

    ApiVersion about
    """
    headers = { 
        'Accept': 'application/vnd.wupdater.apiversion',
    }
    response = await client.request(
        method='GET',
        path='/api/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_about_factory_reset(client):
    """Test case for about_factory_reset

    FactoryReset about
    """
    headers = { 
        'Accept': 'application/vnd.waterlinked.operation_response+json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/about/factoryreset',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_about_get(client):
    """Test case for about_get

    Get about
    """
    headers = { 
        'Accept': 'application/vnd.waterlinked.about+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/about',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_about_led(client):
    """Test case for about_led

    LED about
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/about/led',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_about_status(client):
    """Test case for about_status

    Status about
    """
    headers = { 
        'Accept': 'application/vnd.waterlinked.status+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/about/status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_about_temperature(client):
    """Test case for about_temperature

    Temperature about
    """
    headers = { 
        'Accept': 'application/vnd.waterlinked.temperature+json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/about/temperature',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

