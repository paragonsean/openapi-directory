# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_company_repository_v1_save_post_request import CompanyCompanyRepositoryV1SavePostRequest
from openapi_server.models.company_data_company_interface import CompanyDataCompanyInterface
from openapi_server.models.company_data_company_search_results_interface import CompanyDataCompanySearchResultsInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_company_company_repository_v1_get_list_get(client):
    """Test case for company_company_repository_v1_get_list_get

    company/
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
        path='/rest/default/V1/company/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_company_company_repository_v1_save_post(client):
    """Test case for company_company_repository_v1_save_post

    company/
    """
    body = openapi_server.CompanyCompanyRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/company/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

