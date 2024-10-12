# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.evaluate_policies_request import EvaluatePoliciesRequest
from openapi_server.models.evaluate_policies_response import EvaluatePoliciesResponse


pytestmark = pytest.mark.asyncio

async def test_policy_sets_evaluate_policies(client):
    """Test case for policy_sets_evaluate_policies

    
    """
    evaluate_policies_request = {"policies":[{"factData":"factData","factName":"factName","valueOffset":"valueOffset"},{"factData":"factData","factName":"factName","valueOffset":"valueOffset"}]}
    params = [('api-version', '2016-05-15')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DevTestLab/labs/{lab_name}/policysets/{name}/evaluatePolicies'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', lab_name='lab_name_example', name='name_example'),
        headers=headers,
        json=evaluate_policies_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

