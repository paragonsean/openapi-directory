# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cms_data_block_search_results_interface import CmsDataBlockSearchResultsInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_cms_block_repository_v1_get_list_get(client):
    """Test case for cms_block_repository_v1_get_list_get

    cmsBlock/search
    """
    params = [('searchCriteria[filterGroups][0][filters][0][field]', 'search_criteria_filter_groups_0_filters_0_field_example'),
                    ('searchCriteria[filterGroups][0][filters][0][value]', 'search_criteria_filter_groups_0_filters_0_value_example'),
                    ('searchCriteria[filterGroups][0][filters][0][conditionType]', 'search_criteria_filter_groups_0_filters_0_condition_type_example'),
                    ('searchCriteria[sortOrders][0][field]', 'search_criteria_sort_orders_0_field_example'),
                    ('searchCriteria[sortOrders][0][direction]', 'search_criteria_sort_orders_0_direction_example'),
                    ('searchCriteria[pageSize]', 56),
                    ('searchCriteria[currentPage]', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/cmsBlock/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

