# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.build_beta_detail_response import BuildBetaDetailResponse
from openapi_server.models.build_beta_detail_update_request import BuildBetaDetailUpdateRequest
from openapi_server.models.build_beta_details_response import BuildBetaDetailsResponse
from openapi_server.models.build_response import BuildResponse
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_build_beta_details_build_get_to_one_related(client):
    """Test case for build_beta_details_build_get_to_one_related

    
    """
    params = [('fields[builds]', ['fields_builds_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/buildBetaDetails/{id}/build'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_build_beta_details_get_collection(client):
    """Test case for build_beta_details_get_collection

    
    """
    params = [('filter[build]', ['filter_build_example']),
                    ('filter[id]', ['filter_id_example']),
                    ('fields[buildBetaDetails]', ['fields_build_beta_details_example']),
                    ('limit', 56),
                    ('include', ['include_example']),
                    ('fields[builds]', ['fields_builds_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/buildBetaDetails',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_build_beta_details_get_instance(client):
    """Test case for build_beta_details_get_instance

    
    """
    params = [('fields[buildBetaDetails]', ['fields_build_beta_details_example']),
                    ('include', ['include_example']),
                    ('fields[builds]', ['fields_builds_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/buildBetaDetails/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_build_beta_details_update_instance(client):
    """Test case for build_beta_details_update_instance

    
    """
    body = {"data":{"attributes":{"autoNotifyEnabled":True},"id":"id","type":"buildBetaDetails"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/buildBetaDetails/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

