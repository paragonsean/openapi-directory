# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tax_data_tax_rate_interface import TaxDataTaxRateInterface
from openapi_server.models.tax_tax_rate_repository_v1_save_put_request import TaxTaxRateRepositoryV1SavePutRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_tax_tax_rate_repository_v1_save_post(client):
    """Test case for tax_tax_rate_repository_v1_save_post

    taxRates
    """
    body = openapi_server.TaxTaxRateRepositoryV1SavePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/taxRates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_tax_tax_rate_repository_v1_save_put(client):
    """Test case for tax_tax_rate_repository_v1_save_put

    taxRates
    """
    body = openapi_server.TaxTaxRateRepositoryV1SavePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/taxRates',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

