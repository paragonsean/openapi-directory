# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_number_insight_advanced200_response import GetNumberInsightAdvanced200Response
from openapi_server.models.get_number_insight_async200_response import GetNumberInsightAsync200Response
from openapi_server.models.get_number_insight_standard200_response import GetNumberInsightStandard200Response
from openapi_server.models.ni_response_async import NiResponseAsync
from openapi_server.models.ni_response_json_basic import NiResponseJsonBasic
from openapi_server.models.ni_response_xml_advanced import NiResponseXmlAdvanced
from openapi_server.models.ni_response_xml_basic import NiResponseXmlBasic
from openapi_server.models.ni_response_xml_standard import NiResponseXmlStandard


pytestmark = pytest.mark.asyncio

async def test_get_number_insight_advanced(client):
    """Test case for get_number_insight_advanced

    Advanced Number Insight (sync)
    """
    params = [('real_time_data', true),
                    ('number', '447700900000'),
                    ('country', 'GB'),
                    ('cnam', False),
                    ('ip', '123.0.0.255')]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
        'apiSecret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ni/advanced/{format}'.format(format='json'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_number_insight_async(client):
    """Test case for get_number_insight_async

    Advanced Number Insight (async)
    """
    params = [('callback', 'https://example.com/callback'),
                    ('number', '447700900000'),
                    ('country', 'GB'),
                    ('cnam', False),
                    ('ip', '123.0.0.255')]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
        'apiSecret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ni/advanced/async/{format}'.format(format='json'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_number_insight_basic(client):
    """Test case for get_number_insight_basic

    Basic Number Insight
    """
    params = [('number', '447700900000'),
                    ('country', 'GB')]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
        'apiSecret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ni/basic/{format}'.format(format='json'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_number_insight_standard(client):
    """Test case for get_number_insight_standard

    Standard Number Insight
    """
    params = [('number', '447700900000'),
                    ('country', 'GB'),
                    ('cnam', False)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
        'apiSecret': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ni/standard/{format}'.format(format='json'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

