# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_core_dto_retargeting_retargeting_script import ApiCoreDtoRetargetingRetargetingScript
from openapi_server.models.api_core_responses_count_responce import ApiCoreResponsesCountResponce
from openapi_server.models.api_core_responses_entities_response_api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64
from openapi_server.models.api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntityUriSystemInt64


pytestmark = pytest.mark.asyncio

async def test_retargeting_count(client):
    """Test case for retargeting_count

    Retrieve count of retargeting scripts
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/retargeting/count',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retargeting_delete(client):
    """Test case for retargeting_delete

    Deletes a retargeting script (and remove associations)
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/retargeting/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retargeting_get(client):
    """Test case for retargeting_get

    List of all the retargeting scripts associated to the user
    """
    params = [('offset', 0),
                    ('limit', 20)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/retargeting',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retargeting_get_datapoints(client):
    """Test case for retargeting_get_datapoints

    List of all the datapoints associated to the retargeting script.
    """
    params = [('offset', 0),
                    ('limit', 20),
                    ('status', 'status_example'),
                    ('tags', 'tags_example'),
                    ('textSearch', 'text_search_example'),
                    ('onlyFavorites', True),
                    ('sortBy', 'sort_by_example'),
                    ('sortDirection', 'sort_direction_example'),
                    ('createdAfter', 'created_after_example'),
                    ('createdBefore', 'created_before_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/retargeting/{id}/datapoints'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retargeting_get_datapoints_count(client):
    """Test case for retargeting_get_datapoints_count

    Count the datapoints associated to the retargeting script.
    """
    params = [('status', 'status_example'),
                    ('tags', 'tags_example'),
                    ('textSearch', 'text_search_example'),
                    ('onlyFavorites', True),
                    ('createdAfter', 'created_after_example'),
                    ('createdBefore', 'created_before_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/retargeting/{id}/datapoints/count'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retargeting_id_get(client):
    """Test case for retargeting_id_get

    Get a retargeting script object
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/retargeting/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_retargeting_post(client):
    """Test case for retargeting_post

    Updates a retargeting script
    """
    body = openapi_server.ApiCoreDtoRetargetingRetargetingScript()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/retargeting/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_retargeting_put(client):
    """Test case for retargeting_put

    Creates a retargeting script
    """
    body = openapi_server.ApiCoreDtoRetargetingRetargetingScript()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/retargeting',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

