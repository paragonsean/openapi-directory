# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tax_data_tax_rule_interface import TaxDataTaxRuleInterface
from openapi_server.models.tax_tax_rule_repository_v1_save_put_request import TaxTaxRuleRepositoryV1SavePutRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_tax_tax_rule_repository_v1_save_post(client):
    """Test case for tax_tax_rule_repository_v1_save_post

    taxRules
    """
    body = openapi_server.TaxTaxRuleRepositoryV1SavePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/taxRules',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_tax_tax_rule_repository_v1_save_put(client):
    """Test case for tax_tax_rule_repository_v1_save_put

    taxRules
    """
    body = openapi_server.TaxTaxRuleRepositoryV1SavePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/taxRules',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

