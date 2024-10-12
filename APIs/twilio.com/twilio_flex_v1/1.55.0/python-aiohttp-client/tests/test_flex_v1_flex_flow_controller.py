# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flex_flow_enum_channel_type import FlexFlowEnumChannelType
from openapi_server.models.flex_flow_enum_integration_type import FlexFlowEnumIntegrationType
from openapi_server.models.flex_v1_flex_flow import FlexV1FlexFlow
from openapi_server.models.list_flex_flow_response import ListFlexFlowResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_flex_flow(client):
    """Test case for create_flex_flow

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'channel_type': openapi_server.FlexFlowEnumChannelType(),
        'chat_service_sid': 'chat_service_sid_example',
        'contact_identity': 'contact_identity_example',
        'enabled': True,
        'friendly_name': 'friendly_name_example',
        'integration_channel': 'integration_channel_example',
        'integration_creation_on_message': True,
        'integration_flow_sid': 'integration_flow_sid_example',
        'integration_priority': 56,
        'integration_retry_count': 56,
        'integration_timeout': 56,
        'integration_url': 'integration_url_example',
        'integration_workflow_sid': 'integration_workflow_sid_example',
        'integration_workspace_sid': 'integration_workspace_sid_example',
        'integration_type': openapi_server.FlexFlowEnumIntegrationType(),
        'janitor_enabled': True,
        'long_lived': True
        }
    response = await client.request(
        method='POST',
        path='/v1/FlexFlows',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_flex_flow(client):
    """Test case for delete_flex_flow

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/FlexFlows/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_flex_flow(client):
    """Test case for fetch_flex_flow

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/FlexFlows/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_flex_flow(client):
    """Test case for list_flex_flow

    
    """
    params = [('FriendlyName', 'friendly_name_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/FlexFlows',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_flex_flow(client):
    """Test case for update_flex_flow

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'channel_type': openapi_server.FlexFlowEnumChannelType(),
        'chat_service_sid': 'chat_service_sid_example',
        'contact_identity': 'contact_identity_example',
        'enabled': True,
        'friendly_name': 'friendly_name_example',
        'integration_channel': 'integration_channel_example',
        'integration_creation_on_message': True,
        'integration_flow_sid': 'integration_flow_sid_example',
        'integration_priority': 56,
        'integration_retry_count': 56,
        'integration_timeout': 56,
        'integration_url': 'integration_url_example',
        'integration_workflow_sid': 'integration_workflow_sid_example',
        'integration_workspace_sid': 'integration_workspace_sid_example',
        'integration_type': openapi_server.FlexFlowEnumIntegrationType(),
        'janitor_enabled': True,
        'long_lived': True
        }
    response = await client.request(
        method='POST',
        path='/v1/FlexFlows/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

