# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.api_paged_response_dealer_db_models_license import APIPagedResponseDealerDBModelsLicense
from openapi_server.models.dealer_db_models_license import DealerDBModelsLicense


pytestmark = pytest.mark.asyncio

async def test_api_v2_licenses_idget(client):
    """Test case for api_v2_licenses_idget

    Get a license.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Licenses/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_licenses_get(client):
    """Test case for licenses_get

    Gets a list of licenses with the specified criteria.
    """
    params = [('VoucherCode', 'voucher_code_example'),
                    ('DealerCode', 'dealer_code_example'),
                    ('Status', 'status_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/Licenses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

