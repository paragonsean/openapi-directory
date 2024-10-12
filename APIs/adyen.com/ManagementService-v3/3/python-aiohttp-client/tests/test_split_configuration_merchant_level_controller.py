# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.split_configuration import SplitConfiguration
from openapi_server.models.split_configuration_list import SplitConfigurationList
from openapi_server.models.split_configuration_rule import SplitConfigurationRule
from openapi_server.models.update_split_configuration_logic_request import UpdateSplitConfigurationLogicRequest
from openapi_server.models.update_split_configuration_request import UpdateSplitConfigurationRequest
from openapi_server.models.update_split_configuration_rule_request import UpdateSplitConfigurationRuleRequest


pytestmark = pytest.mark.asyncio

async def test_delete_merchants_merchant_id_split_configurations_split_configuration_id(client):
    """Test case for delete_merchants_merchant_id_split_configurations_split_configuration_id

    Delete a split configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/merchants/{merchant_id}/splitConfigurations/{split_configuration_id}'.format(merchant_id='merchant_id_example', split_configuration_id='split_configuration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id(client):
    """Test case for delete_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id

    Delete a split configuration rule
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/merchants/{merchant_id}/splitConfigurations/{split_configuration_id}/rules/{rule_id}'.format(merchant_id='merchant_id_example', split_configuration_id='split_configuration_id_example', rule_id='rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_split_configurations(client):
    """Test case for get_merchants_merchant_id_split_configurations

    Get a list of split configurations
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/merchants/{merchant_id}/splitConfigurations'.format(merchant_id='merchant_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_split_configurations_split_configuration_id(client):
    """Test case for get_merchants_merchant_id_split_configurations_split_configuration_id

    Get a split configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/merchants/{merchant_id}/splitConfigurations/{split_configuration_id}'.format(merchant_id='merchant_id_example', split_configuration_id='split_configuration_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_merchants_merchant_id_split_configurations_split_configuration_id(client):
    """Test case for patch_merchants_merchant_id_split_configurations_split_configuration_id

    Update split configuration description
    """
    body = {"description":"description"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/merchants/{merchant_id}/splitConfigurations/{split_configuration_id}'.format(merchant_id='merchant_id_example', split_configuration_id='split_configuration_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id(client):
    """Test case for patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id

    Update split conditions
    """
    body = {"paymentMethod":"paymentMethod","shopperInteraction":"shopperInteraction","currency":"currency","fundingSource":"fundingSource"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/merchants/{merchant_id}/splitConfigurations/{split_configuration_id}/rules/{rule_id}'.format(merchant_id='merchant_id_example', split_configuration_id='split_configuration_id_example', rule_id='rule_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id_split_logic_split_logic_id(client):
    """Test case for patch_merchants_merchant_id_split_configurations_split_configuration_id_rules_rule_id_split_logic_split_logic_id

    Update the split logic
    """
    body = {"surcharge":"addToLiableAccount","adyenMarkup":"deductFromLiableAccount","paymentFee":"deductFromLiableAccount","acquiringFees":"deductFromLiableAccount","schemeFee":"deductFromLiableAccount","splitLogicId":"splitLogicId","adyenFees":"deductFromLiableAccount","additionalCommission":{"balanceAccountId":"balanceAccountId","variablePercentage":6,"fixedAmount":0},"chargeback":"deductFromLiableAccount","adyenCommission":"deductFromLiableAccount","chargebackCostAllocation":"deductFromLiableAccount","commission":{"variablePercentage":5,"fixedAmount":1},"tip":"addToLiableAccount","remainder":"addToLiableAccount","interchange":"deductFromLiableAccount"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/merchants/{merchant_id}/splitConfigurations/{split_configuration_id}/rules/{rule_id}/splitLogic/{split_logic_id}'.format(merchant_id='merchant_id_example', split_configuration_id='split_configuration_id_example', rule_id='rule_id_example', split_logic_id='split_logic_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_merchants_merchant_id_split_configurations(client):
    """Test case for post_merchants_merchant_id_split_configurations

    Create a split configuration
    """
    body = {"stores":["stores","stores"],"description":"description","rules":[{"splitLogic":{"surcharge":"addToLiableAccount","adyenMarkup":"deductFromLiableAccount","paymentFee":"deductFromLiableAccount","acquiringFees":"deductFromLiableAccount","schemeFee":"deductFromLiableAccount","splitLogicId":"splitLogicId","adyenFees":"deductFromLiableAccount","additionalCommission":{"balanceAccountId":"balanceAccountId","variablePercentage":6,"fixedAmount":0},"chargeback":"deductFromLiableAccount","adyenCommission":"deductFromLiableAccount","chargebackCostAllocation":"deductFromLiableAccount","commission":{"variablePercentage":5,"fixedAmount":1},"tip":"addToLiableAccount","remainder":"addToLiableAccount","interchange":"deductFromLiableAccount"},"paymentMethod":"paymentMethod","shopperInteraction":"Ecommerce","currency":"currency","fundingSource":"credit","ruleId":"ruleId"},{"splitLogic":{"surcharge":"addToLiableAccount","adyenMarkup":"deductFromLiableAccount","paymentFee":"deductFromLiableAccount","acquiringFees":"deductFromLiableAccount","schemeFee":"deductFromLiableAccount","splitLogicId":"splitLogicId","adyenFees":"deductFromLiableAccount","additionalCommission":{"balanceAccountId":"balanceAccountId","variablePercentage":6,"fixedAmount":0},"chargeback":"deductFromLiableAccount","adyenCommission":"deductFromLiableAccount","chargebackCostAllocation":"deductFromLiableAccount","commission":{"variablePercentage":5,"fixedAmount":1},"tip":"addToLiableAccount","remainder":"addToLiableAccount","interchange":"deductFromLiableAccount"},"paymentMethod":"paymentMethod","shopperInteraction":"Ecommerce","currency":"currency","fundingSource":"credit","ruleId":"ruleId"}],"splitConfigurationId":"splitConfigurationId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/merchants/{merchant_id}/splitConfigurations'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_merchants_merchant_id_split_configurations_split_configuration_id(client):
    """Test case for post_merchants_merchant_id_split_configurations_split_configuration_id

    Create a rule
    """
    body = {"splitLogic":{"surcharge":"addToLiableAccount","adyenMarkup":"deductFromLiableAccount","paymentFee":"deductFromLiableAccount","acquiringFees":"deductFromLiableAccount","schemeFee":"deductFromLiableAccount","splitLogicId":"splitLogicId","adyenFees":"deductFromLiableAccount","additionalCommission":{"balanceAccountId":"balanceAccountId","variablePercentage":6,"fixedAmount":0},"chargeback":"deductFromLiableAccount","adyenCommission":"deductFromLiableAccount","chargebackCostAllocation":"deductFromLiableAccount","commission":{"variablePercentage":5,"fixedAmount":1},"tip":"addToLiableAccount","remainder":"addToLiableAccount","interchange":"deductFromLiableAccount"},"paymentMethod":"paymentMethod","shopperInteraction":"Ecommerce","currency":"currency","fundingSource":"credit","ruleId":"ruleId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/merchants/{merchant_id}/splitConfigurations/{split_configuration_id}'.format(merchant_id='merchant_id_example', split_configuration_id='split_configuration_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

