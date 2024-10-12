# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_all_content_types200_response import GetAllContentTypes200Response
from openapi_server.models.get_cm_spage200_response import GetCMSpage200Response
from openapi_server.models.get_pagesby_content_type200_response import GetPagesbyContentType200Response


pytestmark = pytest.mark.asyncio

async def test_get_all_content_types(client):
    """Test case for get_all_content_types

    Get all Content Types
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/_v/cms/api/{builder_id}'.format(builder_id='faststore'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cm_spage(client):
    """Test case for get_cm_spage

    Get CMS page
    """
    params = [('versionId', 'e7263fc8-bc68-4052-9e25-dd5a2572d3bb'),
                    ('releaseId', '6196c277c6dce15f9709a2a7')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/_v/cms/api/{builder_id}/{content_type}/{document_id}'.format(builder_id='faststore', content_type='plp', document_id='5af643b5-9a6d-48f2-9b34-919dd762c908'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pagesby_content_type(client):
    """Test case for get_pagesby_content_type

    Get all CMS pages by Content Type
    """
    params = [('versionId', 'e7263fc8-bc68-4052-9e25-dd5a2572d3bb'),
                    ('releaseId', '6196c277c6dce15f9709a2a7'),
                    ('filters[{field}]', 'published')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/_v/cms/api/{builder_id}/{content_type}'.format(builder_id='faststore', content_type='plp'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

