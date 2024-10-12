# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.provider_detail_response import ProviderDetailResponse
from openapi_server.models.provider_response import ProviderResponse
from openapi_server.models.providers_count_response import ProvidersCountResponse
from openapi_server.models.yodlee_error import YodleeError


pytestmark = pytest.mark.asyncio

async def test_get_all_providers(client):
    """Test case for get_all_providers

    Get Providers
    """
    params = [('capability', 'capability_example'),
                    ('dataset$filter', 'datasetfilter_example'),
                    ('fullAccountNumberFields', 'full_account_number_fields_example'),
                    ('institutionId', 56),
                    ('name', 'name_example'),
                    ('priority', 'priority_example'),
                    ('providerId', 'provider_id_example'),
                    ('skip', 56),
                    ('top', 56)]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/providers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_provider(client):
    """Test case for get_provider

    Get Provider Details
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/providers/{provider_id}'.format(provider_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_providers_count(client):
    """Test case for get_providers_count

    Get Providers Count
    """
    params = [('capability', 'capability_example'),
                    ('dataset$filter', 'datasetfilter_example'),
                    ('fullAccountNumberFields', 'full_account_number_fields_example'),
                    ('name', 'name_example'),
                    ('priority', 'priority_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/providers/count',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

