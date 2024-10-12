# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.csm_move_resource_envelope import CsmMoveResourceEnvelope


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_global_resource_groups_move_resources(client):
    """Test case for global_resource_groups_move_resources

    
    """
    move_resource_envelope = {"targetResourceGroup":"targetResourceGroup","resources":["resources","resources"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/moveResources'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=move_resource_envelope,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

