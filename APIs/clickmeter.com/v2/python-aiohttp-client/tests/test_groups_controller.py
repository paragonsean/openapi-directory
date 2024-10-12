# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_core_dto_aggregated_aggregated_result import ApiCoreDtoAggregatedAggregatedResult
from openapi_server.models.api_core_dto_aggregated_aggregated_summary_result import ApiCoreDtoAggregatedAggregatedSummaryResult
from openapi_server.models.api_core_dto_click_stream_hit_list_page import ApiCoreDtoClickStreamHitListPage
from openapi_server.models.api_core_dto_datapoints_datapoint import ApiCoreDtoDatapointsDatapoint
from openapi_server.models.api_core_dto_groups_group import ApiCoreDtoGroupsGroup
from openapi_server.models.api_core_requests_generic_text_patch import ApiCoreRequestsGenericTextPatch
from openapi_server.models.api_core_responses_count_responce import ApiCoreResponsesCountResponce
from openapi_server.models.api_core_responses_entities_response_api_core_dto_aggregated_aggregated_result import ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult
from openapi_server.models.api_core_responses_entities_response_api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64
from openapi_server.models.api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntityUriSystemInt64


pytestmark = pytest.mark.asyncio

async def test_groups_count(client):
    """Test case for groups_count

    Count the groups associated to the user.
    """
    params = [('status', 'status_example'),
                    ('tags', 'tags_example'),
                    ('textSearch', 'text_search_example'),
                    ('createdAfter', 'created_after_example'),
                    ('createdBefore', 'created_before_example'),
                    ('write', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_delete(client):
    """Test case for groups_delete

    Delete group specified by id
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_get(client):
    """Test case for groups_get

    List of all the groups associated to the user.
    """
    params = [('offset', 0),
                    ('limit', 20),
                    ('status', 'status_example'),
                    ('tags', 'tags_example'),
                    ('textSearch', 'text_search_example'),
                    ('createdAfter', 'created_after_example'),
                    ('createdBefore', 'created_before_example'),
                    ('write', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_get_datapoints(client):
    """Test case for groups_get_datapoints

    List of all the datapoints associated to the user in this group.
    """
    params = [('offset', 0),
                    ('limit', 20),
                    ('type', 'type_example'),
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
        path='/groups/{id}/datapoints'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_get_datapoints_count(client):
    """Test case for groups_get_datapoints_count

    Count the datapoints associated to the user in this group.
    """
    params = [('type', 'type_example'),
                    ('status', 'status_example'),
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
        path='/groups/{id}/datapoints/count'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_get_datapoints_summary(client):
    """Test case for groups_get_datapoints_summary

    Retrieve statistics about a subset of datapoints for a timeframe with datapoints data
    """
    params = [('timeFrame', 'time_frame_example'),
                    ('type', 'type_example'),
                    ('fromDay', 'from_day_example'),
                    ('toDay', 'to_day_example'),
                    ('status', 'status_example'),
                    ('tag', 'tag_example'),
                    ('favourite', True),
                    ('sortBy', 'sort_by_example'),
                    ('sortDirection', 'sort_direction_example'),
                    ('offset', 0),
                    ('limit', 20),
                    ('textSearch', 'text_search_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/{id}/aggregated/summary'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_get_hits(client):
    """Test case for groups_get_hits

    Retrieve the list of events related to this group.
    """
    params = [('timeframe', 'timeframe_example'),
                    ('limit', 56),
                    ('offset', 'offset_example'),
                    ('fromDay', 'from_day_example'),
                    ('toDay', 'to_day_example'),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/{id}/hits'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_get_statistics_aggregated_single(client):
    """Test case for groups_get_statistics_aggregated_single

    Retrieve statistics about this customer for a timeframe by groups
    """
    params = [('timeFrame', 'time_frame_example'),
                    ('fromDay', 'from_day_example'),
                    ('toDay', 'to_day_example'),
                    ('hourly', True),
                    ('status', 'status_example'),
                    ('tag', 'tag_example'),
                    ('favourite', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/aggregated',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_get_statistics_all_list(client):
    """Test case for groups_get_statistics_all_list

    Retrieve statistics about all groups of this customer for a timeframe grouped by some temporal entity (day/week/month)
    """
    params = [('timeFrame', 'time_frame_example'),
                    ('fromDay', 'from_day_example'),
                    ('toDay', 'to_day_example'),
                    ('status', 'status_example'),
                    ('tag', 'tag_example'),
                    ('favourite', True),
                    ('groupBy', 'group_by_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/aggregated/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_get_statistics_list(client):
    """Test case for groups_get_statistics_list

    Retrieve statistics about this group for a timeframe grouped by some temporal entity (day/week/month)
    """
    params = [('timeFrame', 'time_frame_example'),
                    ('fromDay', 'from_day_example'),
                    ('toDay', 'to_day_example'),
                    ('groupBy', 'group_by_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/{id}/aggregated/list'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_get_statistics_single(client):
    """Test case for groups_get_statistics_single

    Retrieve statistics about this group for a timeframe
    """
    params = [('timeFrame', 'time_frame_example'),
                    ('fromDay', 'from_day_example'),
                    ('toDay', 'to_day_example'),
                    ('hourly', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/{id}/aggregated'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_id_get(client):
    """Test case for groups_id_get

    Get a group
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/groups/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_patch_favourite(client):
    """Test case for groups_patch_favourite

    Fast switch the \"favourite\" field of a group
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/groups/{id}/favourite'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_groups_patch_notes(client):
    """Test case for groups_patch_notes

    Fast patch the \"notes\" field of a group
    """
    body = openapi_server.ApiCoreRequestsGenericTextPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/groups/{id}/notes'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_groups_post(client):
    """Test case for groups_post

    Update a group
    """
    body = openapi_server.ApiCoreDtoGroupsGroup()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/groups/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_groups_put(client):
    """Test case for groups_put

    Create a group
    """
    body = openapi_server.ApiCoreDtoGroupsGroup()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/groups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_groups_put_datapoint(client):
    """Test case for groups_put_datapoint

    Create a datapoint in this group
    """
    body = openapi_server.ApiCoreDtoDatapointsDatapoint()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/groups/{id}/datapoints'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

