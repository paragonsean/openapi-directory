# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_reference_entities_code200_response import GetReferenceEntitiesCode200Response
from openapi_server.models.patch_reference_entity_code_request import PatchReferenceEntityCodeRequest
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.reference_entities import ReferenceEntities


pytestmark = pytest.mark.asyncio

async def test_get_reference_entities(client):
    """Test case for get_reference_entities

    Get list of reference entities
    """
    params = [('search_after', 'cursor to the first page')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/reference-entities',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reference_entities_code(client):
    """Test case for get_reference_entities_code

    Get a reference entity
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/reference-entities/{code}'.format(code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_reference_entity_code(client):
    """Test case for patch_reference_entity_code

    Update/create a reference entity
    """
    body = openapi_server.PatchReferenceEntityCodeRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/reference-entities/{code}'.format(code='code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

