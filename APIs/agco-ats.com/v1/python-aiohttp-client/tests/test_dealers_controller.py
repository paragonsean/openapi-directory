# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_dealer_db_models_dealer import APIPagedResponseDealerDBModelsDealer
from openapi_server.models.dealer_db_models_dealer import DealerDBModelsDealer


pytestmark = pytest.mark.asyncio

async def test_dealers_get_dealerby_dealer_code(client):
    """Test case for dealers_get_dealerby_dealer_code

    Lookup a dealer using a dealer code.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Dealers/{dealer_code}'.format(dealer_code='dealer_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dealers_get_dealers(client):
    """Test case for dealers_get_dealers

    Get a list of dealers.
    """
    params = [('Brand', 'brand_example'),
                    ('ShippingCountry', 'shipping_country_example'),
                    ('DealerName', 'dealer_name_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Dealers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

