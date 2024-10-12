# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_dealer_db_models_dealers_per_country import APIPagedResponseDealerDBModelsDealersPerCountry


pytestmark = pytest.mark.asyncio

async def test_dealer_by_country_get_countries(client):
    """Test case for dealer_by_country_get_countries

    Get a total count of dealers per country
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/DealerByCountry',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

