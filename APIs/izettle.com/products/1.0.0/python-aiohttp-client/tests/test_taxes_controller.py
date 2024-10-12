# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tax_rate import TaxRate
from openapi_server.models.tax_rate_product_count_response import TaxRateProductCountResponse
from openapi_server.models.tax_rate_update_request import TaxRateUpdateRequest
from openapi_server.models.tax_rates_create_request import TaxRatesCreateRequest
from openapi_server.models.tax_rates_response import TaxRatesResponse
from openapi_server.models.tax_settings_response import TaxSettingsResponse
from openapi_server.models.tax_settings_update_request import TaxSettingsUpdateRequest


pytestmark = pytest.mark.asyncio

async def test_create_tax_rates(client):
    """Test case for create_tax_rates

    Create new tax rates
    """
    body = {"taxRates":[{"default":True,"percentage":8.008281904610115,"label":"label","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},{"default":True,"percentage":8.008281904610115,"label":"label","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},{"default":True,"percentage":8.008281904610115,"label":"label","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},{"default":True,"percentage":8.008281904610115,"label":"label","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"},{"default":True,"percentage":8.008281904610115,"label":"label","uuid":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/taxes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_tax_rate(client):
    """Test case for delete_tax_rate

    Delete a single tax rate
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/taxes/{tax_rate_uuid}'.format(tax_rate_uuid='tax_rate_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_product_count_for_all_taxes(client):
    """Test case for get_product_count_for_all_taxes

    Get all tax rates and a count of products associated with each
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/taxes/count',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tax_rate(client):
    """Test case for get_tax_rate

    Get a single tax rate
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/taxes/{tax_rate_uuid}'.format(tax_rate_uuid='tax_rate_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tax_rates(client):
    """Test case for get_tax_rates

    Get all available tax rates
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/taxes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_tax_settings(client):
    """Test case for get_tax_settings

    Get the organization tax settings 
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/taxes/settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_taxation_mode(client):
    """Test case for set_taxation_mode

    Update the organization tax settings
    """
    body = {"taxationMode":"EXCLUSIVE"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/taxes/settings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_tax_rate(client):
    """Test case for update_tax_rate

    Update a single tax rate
    """
    body = {"default":True,"percentage":8.008281904610115,"label":"label"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/taxes/{tax_rate_uuid}'.format(tax_rate_uuid='tax_rate_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

