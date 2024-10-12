# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_masking_rule import DataMaskingRule
from openapi_server.models.data_masking_rule_list_result import DataMaskingRuleListResult


pytestmark = pytest.mark.asyncio

async def test_data_masking_rules_create_or_update(client):
    """Test case for data_masking_rules_create_or_update

    
    """
    parameters = {"kind":"kind","location":"location","properties":{"ruleState":"Disabled","aliasName":"aliasName","replacementString":"replacementString","suffixSize":"suffixSize","numberFrom":"numberFrom","id":"id","numberTo":"numberTo","schemaName":"schemaName","maskingFunction":"Default","columnName":"columnName","prefixSize":"prefixSize","tableName":"tableName"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/dataMaskingPolicies/{data_masking_policy_name}/rules/{data_masking_rule_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', data_masking_policy_name='data_masking_policy_name_example', data_masking_rule_name='data_masking_rule_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_masking_rules_list_by_database(client):
    """Test case for data_masking_rules_list_by_database

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/dataMaskingPolicies/{data_masking_policy_name}/rules'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', data_masking_policy_name='data_masking_policy_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

