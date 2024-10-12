# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_metadata_templates_type200_response import GetMetadataTemplatesType200Response
from openapi_server.models.get_metadata_templates_type200_response_metadata_templates_inner import GetMetadataTemplatesType200ResponseMetadataTemplatesInner
from openapi_server.models.get_root200_response import GetRoot200Response


pytestmark = pytest.mark.asyncio

async def test_get_metadata_template(client):
    """Test case for get_metadata_template

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/metadata_templates/{metadata_template_type}/{metadata_template_name}'.format(source=catalog, metadata_template_type=basic, metadata_template_name='metadata_template_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_metadata_templates_type(client):
    """Test case for get_metadata_templates_type

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/metadata_templates/{metadata_template_type}'.format(source=catalog, metadata_template_type=basic),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_metadata_templates_types(client):
    """Test case for get_metadata_templates_types

    
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{source}/metadata_templates'.format(source=catalog),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

