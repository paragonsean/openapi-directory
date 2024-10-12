# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_capabilities(client):
    """Test case for get_capabilities

    GetCapabilities
    """
    params = [('service', 'service_example'),
                    ('request', 'request_example'),
                    ('version', 'version_example')]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/map/{version_number}/wms'.format(version_number=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_map_version_number_wmts_key_wmts_version_wmts_capabilities_xml_get(client):
    """Test case for map_version_number_wmts_key_wmts_version_wmts_capabilities_xml_get

    WMTS
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/map/{version_number}/wmts/{key}/{wmts_version}/WMTSCapabilities.xml'.format(version_number=56, key='key_example', wmts_version='wmts_version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

