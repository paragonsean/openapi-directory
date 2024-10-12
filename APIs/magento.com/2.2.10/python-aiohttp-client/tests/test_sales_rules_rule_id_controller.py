# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sales_rule_data_rule_interface import SalesRuleDataRuleInterface
from openapi_server.models.sales_rule_rule_repository_v1_save_post_request import SalesRuleRuleRepositoryV1SavePostRequest


pytestmark = pytest.mark.asyncio

async def test_sales_rule_rule_repository_v1_delete_by_id_delete(client):
    """Test case for sales_rule_rule_repository_v1_delete_by_id_delete

    salesRules/{ruleId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/salesRules/{rule_id}'.format(rule_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_rule_rule_repository_v1_get_by_id_get(client):
    """Test case for sales_rule_rule_repository_v1_get_by_id_get

    salesRules/{ruleId}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/salesRules/{rule_id}'.format(rule_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_sales_rule_rule_repository_v1_save_put(client):
    """Test case for sales_rule_rule_repository_v1_save_put

    salesRules/{ruleId}
    """
    body = openapi_server.SalesRuleRuleRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/salesRules/{rule_id}'.format(rule_id='rule_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

