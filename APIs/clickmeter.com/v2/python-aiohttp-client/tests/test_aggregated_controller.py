# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_core_dto_aggregated_aggregated_result import ApiCoreDtoAggregatedAggregatedResult
from openapi_server.models.api_core_dto_aggregated_aggregated_summary_result import ApiCoreDtoAggregatedAggregatedSummaryResult
from openapi_server.models.api_core_responses_entities_response_api_core_dto_aggregated_aggregated_result import ApiCoreResponsesEntitiesResponseApiCoreDtoAggregatedAggregatedResult


pytestmark = pytest.mark.asyncio

async def test_aggregated_get_conversions_summary(client):
    """Test case for aggregated_get_conversions_summary

    Retrieve statistics about a subset of conversions for a timeframe with conversions data
    """
    params = [('timeFrame', 'time_frame_example'),
                    ('fromDay', 'from_day_example'),
                    ('toDay', 'to_day_example'),
                    ('status', 'status_example'),
                    ('sortBy', 'sort_by_example'),
                    ('sortDirection', 'sort_direction_example'),
                    ('offset', 56),
                    ('limit', 56),
                    ('textSearch', 'text_search_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/aggregated/summary/conversions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aggregated_get_datapoints_summary(client):
    """Test case for aggregated_get_datapoints_summary

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
                    ('offset', 56),
                    ('limit', 56),
                    ('groupId', 56),
                    ('textSearch', 'text_search_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/aggregated/summary/datapoints',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aggregated_get_groups_summary(client):
    """Test case for aggregated_get_groups_summary

    Retrieve statistics about a subset of groups for a timeframe with groups data
    """
    params = [('timeFrame', 'time_frame_example'),
                    ('fromDay', 'from_day_example'),
                    ('toDay', 'to_day_example'),
                    ('status', 'status_example'),
                    ('tag', 'tag_example'),
                    ('favourite', True),
                    ('sortBy', 'sort_by_example'),
                    ('sortDirection', 'sort_direction_example'),
                    ('offset', 56),
                    ('limit', 56),
                    ('textSearch', 'text_search_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/aggregated/summary/groups',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aggregated_get_statistics_list(client):
    """Test case for aggregated_get_statistics_list

    Retrieve statistics about this customer for a timeframe grouped by some temporal entity (day/week/month)
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
        path='/aggregated/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_aggregated_get_statistics_single(client):
    """Test case for aggregated_get_statistics_single

    Retrieve statistics about this customer for a timeframe
    """
    params = [('timeFrame', 'time_frame_example'),
                    ('fromDay', 'from_day_example'),
                    ('toDay', 'to_day_example'),
                    ('hourly', True),
                    ('onlyFavorites', 'only_favorites_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/aggregated',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

