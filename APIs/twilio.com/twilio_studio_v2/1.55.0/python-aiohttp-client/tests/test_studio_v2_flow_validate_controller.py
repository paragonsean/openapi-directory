# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flow_validate_enum_status import FlowValidateEnumStatus
from openapi_server.models.studio_v2_flow_validate import StudioV2FlowValidate


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_flow_validate(client):
    """Test case for update_flow_validate

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'commit_message': 'commit_message_example',
        'definition': None,
        'friendly_name': 'friendly_name_example',
        'status': openapi_server.FlowValidateEnumStatus()
        }
    response = await client.request(
        method='POST',
        path='/v2/Flows/Validate',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

