# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.patch_assets200_response_inner import PatchAssets200ResponseInner
from openapi_server.models.patch_reference_entity_records_code_request import PatchReferenceEntityRecordsCodeRequest
from openapi_server.models.patch_reference_entity_records_request_inner import PatchReferenceEntityRecordsRequestInner
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server.models.reference_entity_record import ReferenceEntityRecord


pytestmark = pytest.mark.asyncio

async def test_get_reference_entity_records(client):
    """Test case for get_reference_entity_records

    Get the list of the records of a reference entity
    """
    params = [('search', 'search_example'),
                    ('channel', 'channel_example'),
                    ('locales', 'locales_example'),
                    ('search_after', 'cursor to the first page')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/reference-entities/{reference_entity_code}/records'.format(reference_entity_code='reference_entity_code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reference_entity_records_code(client):
    """Test case for get_reference_entity_records_code

    Get a record of a given reference entity
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/reference-entities/{reference_entity_code}/records/{code}'.format(reference_entity_code='reference_entity_code_example', code='code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_reference_entity_records(client):
    """Test case for patch_reference_entity_records

    Update/create several reference entity records
    """
    body = [openapi_server.PatchReferenceEntityRecordsRequestInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/reference-entities/{reference_entity_code}/records'.format(reference_entity_code='reference_entity_code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_patch_reference_entity_records_code(client):
    """Test case for patch_reference_entity_records_code

    Update/create a record of a given reference entity
    """
    body = openapi_server.PatchReferenceEntityRecordsCodeRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/rest/v1/reference-entities/{reference_entity_code}/records/{code}'.format(reference_entity_code='reference_entity_code_example', code='code_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

