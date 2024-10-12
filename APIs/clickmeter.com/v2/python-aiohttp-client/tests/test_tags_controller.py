# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_core_dto_tags_tag import ApiCoreDtoTagsTag
from openapi_server.models.api_core_requests_generic_text_patch import ApiCoreRequestsGenericTextPatch
from openapi_server.models.api_core_requests_patch_body import ApiCoreRequestsPatchBody
from openapi_server.models.api_core_responses_count_responce import ApiCoreResponsesCountResponce
from openapi_server.models.api_core_responses_entities_response_api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64
from openapi_server.models.api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntityUriSystemInt64


pytestmark = pytest.mark.asyncio

async def test_tags_count(client):
    """Test case for tags_count

    List of all the groups associated to the user filtered by this tag.
    """
    params = [('name', 'name_example'),
                    ('datapoints', 'datapoints_example'),
                    ('groups', 'groups_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tags/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_delete(client):
    """Test case for tags_delete

    Delete a tag
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tags/{tag_id}'.format(tag_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_delete_related_datapoints(client):
    """Test case for tags_delete_related_datapoints

    Delete the association of this tag with all datapoints
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tags/{tag_id}/datapoints'.format(tag_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_delete_related_groups(client):
    """Test case for tags_delete_related_groups

    Delete the association of this tag with all groups
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tags/{tag_id}/groups'.format(tag_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_get(client):
    """Test case for tags_get

    List of all the groups associated to the user filtered by this tag.
    """
    params = [('offset', 0),
                    ('limit', 20),
                    ('name', 'name_example'),
                    ('datapoints', 'datapoints_example'),
                    ('groups', 'groups_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tags',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_get_datapoints(client):
    """Test case for tags_get_datapoints

    List of all the datapoints associated to the user filtered by this tag
    """
    params = [('offset', 0),
                    ('limit', 20),
                    ('type', 'type_example'),
                    ('status', 'status_example'),
                    ('textSearch', 'text_search_example'),
                    ('createdAfter', 'created_after_example'),
                    ('createdBefore', 'created_before_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tags/{tag_id}/datapoints'.format(tag_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_get_datapoints_count(client):
    """Test case for tags_get_datapoints_count

    Count the datapoints associated to the user filtered by this tag
    """
    params = [('type', 'type_example'),
                    ('status', 'status_example'),
                    ('textSearch', 'text_search_example'),
                    ('createdAfter', 'created_after_example'),
                    ('createdBefore', 'created_before_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tags/{tag_id}/datapoints/count'.format(tag_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_get_groups(client):
    """Test case for tags_get_groups

    List of all the groups associated to the user filtered by this tag.
    """
    params = [('offset', 0),
                    ('limit', 20),
                    ('status', 'status_example'),
                    ('textSearch', 'text_search_example'),
                    ('createdAfter', 'created_after_example'),
                    ('createdBefore', 'created_before_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tags/{tag_id}/groups'.format(tag_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_get_groups_count(client):
    """Test case for tags_get_groups_count

    Count the groups associated to the user filtered by this tag
    """
    params = [('status', 'status_example'),
                    ('textSearch', 'text_search_example'),
                    ('createdAfter', 'created_after_example'),
                    ('createdBefore', 'created_before_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tags/{tag_id}/groups/count'.format(tag_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_tags_patch_data_point(client):
    """Test case for tags_patch_data_point

    Associate/Deassociate a tag with a datapoint
    """
    body = openapi_server.ApiCoreRequestsPatchBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/tags/{tag_id}/datapoints/patch'.format(tag_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_tags_patch_group(client):
    """Test case for tags_patch_group

    Associate/Deassociate a tag with a group
    """
    body = openapi_server.ApiCoreRequestsPatchBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/tags/{tag_id}/groups/patch'.format(tag_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_tags_patch_tag_name(client):
    """Test case for tags_patch_tag_name

    Fast patch a tag name
    """
    body = openapi_server.ApiCoreRequestsGenericTextPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/tags/{tag_id}/name'.format(tag_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_tags_put(client):
    """Test case for tags_put

    Create a tag
    """
    body = openapi_server.ApiCoreDtoTagsTag()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tags',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tags_tag_id_get(client):
    """Test case for tags_tag_id_get

    Retrieve a tag
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tags/{tag_id}'.format(tag_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

