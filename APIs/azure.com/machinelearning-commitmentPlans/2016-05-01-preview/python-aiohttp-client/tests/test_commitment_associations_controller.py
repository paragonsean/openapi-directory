# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.commitment_association import CommitmentAssociation
from openapi_server.models.commitment_association_list_result import CommitmentAssociationListResult
from openapi_server.models.move_commitment_association_request import MoveCommitmentAssociationRequest


pytestmark = pytest.mark.asyncio

async def test_commitment_associations_get(client):
    """Test case for commitment_associations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearning/commitmentPlans/{commitment_plan_name}/commitmentAssociations/{commitment_association_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', commitment_plan_name='commitment_plan_name_example', commitment_association_name='commitment_association_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commitment_associations_list(client):
    """Test case for commitment_associations_list

    
    """
    params = [('$skipToken', 'skip_token_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearning/commitmentPlans/{commitment_plan_name}/commitmentAssociations'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', commitment_plan_name='commitment_plan_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commitment_associations_move(client):
    """Test case for commitment_associations_move

    
    """
    move_payload = {"destinationPlanId":"destinationPlanId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearning/commitmentPlans/{commitment_plan_name}/commitmentAssociations/{commitment_association_name}/move'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', commitment_plan_name='commitment_plan_name_example', commitment_association_name='commitment_association_name_example'),
        headers=headers,
        json=move_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

