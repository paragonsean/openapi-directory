# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_core_dto_aggregated_aggregated_result import ApiCoreDtoAggregatedAggregatedResult
from openapi_server.models.api_core_dto_click_stream_hit_list_page import ApiCoreDtoClickStreamHitListPage
from openapi_server.models.api_core_dto_datapoints_datapoint import ApiCoreDtoDatapointsDatapoint
from openapi_server.models.api_core_requests_datapoints_batch import ApiCoreRequestsDatapointsBatch
from openapi_server.models.api_core_requests_delete_batch import ApiCoreRequestsDeleteBatch
from openapi_server.models.api_core_requests_generic_text_patch import ApiCoreRequestsGenericTextPatch
from openapi_server.models.api_core_responses_count_responce import ApiCoreResponsesCountResponce
from openapi_server.models.api_core_responses_entities_response_api_core_dto_aggregated_aggregated_result import ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult
from openapi_server.models.api_core_responses_entities_response_api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64
from openapi_server.models.api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntityUriSystemInt64
from openapi_server.models.api_core_responses_modify_batch_item_responce_api_core_dto_datapoints_datapoint_system_int64 import ApiCoreResponsesModifyBatchItemResponceApiCoreDtoDatapointsDatapointSystemInt64


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_data_points_batch_delete(client):
    """Test case for data_points_batch_delete

    Delete multiple datapoints
    """
    body = openapi_server.ApiCoreRequestsDeleteBatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/datapoints/batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_data_points_batch_post(client):
    """Test case for data_points_batch_post

    Update multiple datapoints
    """
    body = openapi_server.ApiCoreRequestsDatapointsBatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/datapoints/batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_data_points_batch_put(client):
    """Test case for data_points_batch_put

    Create multiple datapoints
    """
    body = openapi_server.ApiCoreRequestsDatapointsBatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/datapoints/batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_points_count(client):
    """Test case for data_points_count

    Count the datapoints associated to the user
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
        path='/datapoints/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_points_delete(client):
    """Test case for data_points_delete

    Delete a datapoint
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/datapoints/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_points_get(client):
    """Test case for data_points_get

    List of all the datapoints associated to the user
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
        path='/datapoints',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_points_get_hits(client):
    """Test case for data_points_get_hits

    Retrieve the list of events related to this datapoint.
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
        path='/datapoints/{id}/hits'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_points_get_statistics_aggregated_single(client):
    """Test case for data_points_get_statistics_aggregated_single

    Retrieve statistics about this customer for a timeframe by groups
    """
    params = [('timeFrame', 'time_frame_example'),
                    ('type', 'type_example'),
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
        path='/datapoints/aggregated',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_points_get_statistics_all_list(client):
    """Test case for data_points_get_statistics_all_list

    Retrieve statistics about all datapoints of this customer for a timeframe grouped by some temporal entity (day/week/month)
    """
    params = [('type', 'type_example'),
                    ('timeFrame', 'time_frame_example'),
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
        path='/datapoints/aggregated/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_points_get_statistics_list(client):
    """Test case for data_points_get_statistics_list

    Retrieve statistics about this datapoint for a timeframe grouped by some temporal entity (day/week/month)
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
        path='/datapoints/{id}/aggregated/list'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_points_get_statistics_single(client):
    """Test case for data_points_get_statistics_single

    Retrieve statistics about this datapoint for a timeframe
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
        path='/datapoints/{id}/aggregated'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_points_patch_favourite(client):
    """Test case for data_points_patch_favourite

    Fast switch the \"favourite\" field of a datapoint
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/datapoints/{id}/favourite'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_data_points_patch_notes(client):
    """Test case for data_points_patch_notes

    Fast patch the \"notes\" field of a datapoint
    """
    body = openapi_server.ApiCoreRequestsGenericTextPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/datapoints/{id}/notes'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_data_points_post(client):
    """Test case for data_points_post

    Update a datapoint
    """
    body = openapi_server.ApiCoreDtoDatapointsDatapoint()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/datapoints/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_data_points_put(client):
    """Test case for data_points_put

    Create a datapoint
    """
    body = openapi_server.ApiCoreDtoDatapointsDatapoint()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/datapoints',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_datapoints_id_get(client):
    """Test case for datapoints_id_get

    Get a datapoint
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/datapoints/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

