# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_core_dto_aggregated_aggregated_result import ApiCoreDtoAggregatedAggregatedResult
from openapi_server.models.api_core_dto_click_stream_hit_list_page import ApiCoreDtoClickStreamHitListPage
from openapi_server.models.api_core_dto_conversions_conversion import ApiCoreDtoConversionsConversion
from openapi_server.models.api_core_requests_conversion_patch_body import ApiCoreRequestsConversionPatchBody
from openapi_server.models.api_core_requests_generic_text_patch import ApiCoreRequestsGenericTextPatch
from openapi_server.models.api_core_requests_patch_body_batch import ApiCoreRequestsPatchBodyBatch
from openapi_server.models.api_core_responses_count_responce import ApiCoreResponsesCountResponce
from openapi_server.models.api_core_responses_entities_response_api_core_dto_aggregated_aggregated_result import ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult
from openapi_server.models.api_core_responses_entities_response_api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64
from openapi_server.models.api_core_responses_entity_uri_system_int64 import ApiCoreResponsesEntityUriSystemInt64


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_conversions_conversion_id_datapoints_batch_patch_put(client):
    """Test case for conversions_conversion_id_datapoints_batch_patch_put

    Modify the association between a conversion and multiple datapoints
    """
    body = openapi_server.ApiCoreRequestsPatchBodyBatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/conversions/{conversion_id}/datapoints/batch/patch'.format(conversion_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversions_conversion_id_get(client):
    """Test case for conversions_conversion_id_get

    Retrieve conversion specified by id
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/conversions/{conversion_id}'.format(conversion_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversions_count(client):
    """Test case for conversions_count

    Retrieve a count of conversions
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
        path='/conversions/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversions_delete(client):
    """Test case for conversions_delete

    Delete conversion specified by id
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/conversions/{conversion_id}'.format(conversion_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversions_get(client):
    """Test case for conversions_get

    Retrieve a list of conversions
    """
    params = [('offset', 56),
                    ('limit', 56),
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
        path='/conversions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversions_get_datapoints(client):
    """Test case for conversions_get_datapoints

    Retrieve a list of datapoints connected to this conversion
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('type', 'type_example'),
                    ('status', 'status_example'),
                    ('tags', 'tags_example'),
                    ('textSearch', 'text_search_example'),
                    ('createdAfter', 'created_after_example'),
                    ('createdBefore', 'created_before_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/conversions/{conversion_id}/datapoints'.format(conversion_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversions_get_datapoints_count(client):
    """Test case for conversions_get_datapoints_count

    Retrieve a count of datapoints connected to this conversion
    """
    params = [('type', 'type_example'),
                    ('status', 'status_example'),
                    ('tags', 'tags_example'),
                    ('textSearch', 'text_search_example'),
                    ('createdAfter', 'created_after_example'),
                    ('createdBefore', 'created_before_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/conversions/{conversion_id}/datapoints/count'.format(conversion_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversions_get_hits(client):
    """Test case for conversions_get_hits

    Retrieve the list of events related to this conversion.
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
        path='/conversions/{conversion_id}/hits'.format(conversion_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversions_get_statistics_all_list(client):
    """Test case for conversions_get_statistics_all_list

    Retrieve statistics about this customer for a timeframe related to a subset of conversions grouped by some temporal entity (day/week/month)
    """
    params = [('timeFrame', 'time_frame_example'),
                    ('fromDay', 'from_day_example'),
                    ('toDay', 'to_day_example'),
                    ('status', 'status_example'),
                    ('groupBy', 'group_by_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/conversions/aggregated/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversions_get_statistics_list(client):
    """Test case for conversions_get_statistics_list

    Retrieve statistics about this conversion for a timeframe grouped by some temporal entity (day/week/month)
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
        path='/conversions/{conversion_id}/aggregated/list'.format(conversion_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_conversions_get_statistics_single(client):
    """Test case for conversions_get_statistics_single

    Retrieve statistics about this conversion for a timeframe
    """
    params = [('timeFrame', 'time_frame_example'),
                    ('fromDay', 'from_day_example'),
                    ('toDay', 'to_day_example'),
                    ('tag', 'tag_example'),
                    ('favourite', True),
                    ('hourly', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/conversions/{conversion_id}/aggregated'.format(conversion_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_conversions_patch(client):
    """Test case for conversions_patch

    Modify the association between a conversion and a datapoint
    """
    body = openapi_server.ApiCoreRequestsConversionPatchBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/conversions/{conversion_id}/datapoints/patch'.format(conversion_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_conversions_patch_notes(client):
    """Test case for conversions_patch_notes

    Fast patch the \"notes\" field of a conversion
    """
    body = openapi_server.ApiCoreRequestsGenericTextPatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/conversions/{conversion_id}/notes'.format(conversion_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_conversions_post(client):
    """Test case for conversions_post

    Update conversion specified by id
    """
    body = openapi_server.ApiCoreDtoConversionsConversion()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/conversions/{conversion_id}'.format(conversion_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_conversions_put(client):
    """Test case for conversions_put

    Create a conversion
    """
    body = openapi_server.ApiCoreDtoConversionsConversion()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/conversions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

