# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authentication_execution_info_representation import AuthenticationExecutionInfoRepresentation
from openapi_server.models.authentication_execution_representation import AuthenticationExecutionRepresentation
from openapi_server.models.authentication_flow_representation import AuthenticationFlowRepresentation
from openapi_server.models.authenticator_config_info_representation import AuthenticatorConfigInfoRepresentation
from openapi_server.models.authenticator_config_representation import AuthenticatorConfigRepresentation
from openapi_server.models.required_action_provider_representation import RequiredActionProviderRepresentation


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_authenticator_providers_get(client):
    """Test case for realm_authentication_authenticator_providers_get

    Get authenticator providers   Returns a list of authenticator providers.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/authentication/authenticator-providers'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_client_authenticator_providers_get(client):
    """Test case for realm_authentication_client_authenticator_providers_get

    Get client authenticator providers   Returns a list of client authenticator providers.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/authentication/client-authenticator-providers'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_config_description_provider_id_get(client):
    """Test case for realm_authentication_config_description_provider_id_get

    Get authenticator provider’s configuration description
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/authentication/config-description/{provider_id}'.format(realm='realm_example', provider_id='provider_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_config_id_delete(client):
    """Test case for realm_authentication_config_id_delete

    Delete authenticator configuration
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/authentication/config/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_config_id_get(client):
    """Test case for realm_authentication_config_id_get

    Get authenticator configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/authentication/config/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_config_id_put(client):
    """Test case for realm_authentication_config_id_put

    Update authenticator configuration
    """
    body = {"alias":"alias","id":"id","config":{"key":""}}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/authentication/config/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_executions_execution_id_config_post(client):
    """Test case for realm_authentication_executions_execution_id_config_post

    Update execution with new configuration
    """
    body = {"alias":"alias","id":"id","config":{"key":""}}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/authentication/executions/{execution_id}/config'.format(realm='realm_example', execution_id='execution_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_executions_execution_id_delete(client):
    """Test case for realm_authentication_executions_execution_id_delete

    Delete execution
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/authentication/executions/{execution_id}'.format(realm='realm_example', execution_id='execution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_executions_execution_id_get(client):
    """Test case for realm_authentication_executions_execution_id_get

    Get Single Execution
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/authentication/executions/{execution_id}'.format(realm='realm_example', execution_id='execution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_executions_execution_id_lower_priority_post(client):
    """Test case for realm_authentication_executions_execution_id_lower_priority_post

    Lower execution’s priority
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/authentication/executions/{execution_id}/lower-priority'.format(realm='realm_example', execution_id='execution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_executions_execution_id_raise_priority_post(client):
    """Test case for realm_authentication_executions_execution_id_raise_priority_post

    Raise execution’s priority
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/authentication/executions/{execution_id}/raise-priority'.format(realm='realm_example', execution_id='execution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_executions_post(client):
    """Test case for realm_authentication_executions_post

    Add new authentication execution
    """
    body = {"authenticatorConfig":"authenticatorConfig","authenticatorFlow":True,"id":"id","requirement":"requirement","parentFlow":"parentFlow","priority":0,"authenticator":"authenticator","flowId":"flowId","autheticatorFlow":True}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/authentication/executions'.format(realm='realm_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_flows_flow_alias_copy_post(client):
    """Test case for realm_authentication_flows_flow_alias_copy_post

    Copy existing authentication flow under a new name   The new name is given as 'newName' attribute of the passed JSON object
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/authentication/flows/{flow_alias}/copy'.format(realm='realm_example', flow_alias='flow_alias_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_flows_flow_alias_executions_execution_post(client):
    """Test case for realm_authentication_flows_flow_alias_executions_execution_post

    Add new authentication execution to a flow
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/authentication/flows/{flow_alias}/executions/execution'.format(realm='realm_example', flow_alias='flow_alias_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_flows_flow_alias_executions_flow_post(client):
    """Test case for realm_authentication_flows_flow_alias_executions_flow_post

    Add new flow with new execution to existing flow
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/authentication/flows/{flow_alias}/executions/flow'.format(realm='realm_example', flow_alias='flow_alias_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_flows_flow_alias_executions_get(client):
    """Test case for realm_authentication_flows_flow_alias_executions_get

    Get authentication executions for a flow
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/authentication/flows/{flow_alias}/executions'.format(realm='realm_example', flow_alias='flow_alias_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_flows_flow_alias_executions_put(client):
    """Test case for realm_authentication_flows_flow_alias_executions_put

    Update authentication executions of a flow
    """
    body = {"requirementChoices":["requirementChoices","requirementChoices"],"authenticationFlow":True,"level":6,"displayName":"displayName","providerId":"providerId","alias":"alias","index":0,"id":"id","requirement":"requirement","authenticationConfig":"authenticationConfig","flowId":"flowId","configurable":True}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/authentication/flows/{flow_alias}/executions'.format(realm='realm_example', flow_alias='flow_alias_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_flows_get(client):
    """Test case for realm_authentication_flows_get

    Get authentication flows   Returns a list of authentication flows.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/authentication/flows'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_flows_id_delete(client):
    """Test case for realm_authentication_flows_id_delete

    Delete an authentication flow
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/authentication/flows/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_flows_id_get(client):
    """Test case for realm_authentication_flows_id_get

    Get authentication flow for id
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/authentication/flows/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_flows_id_put(client):
    """Test case for realm_authentication_flows_id_put

    Update an authentication flow
    """
    body = {"authenticationExecutions":[{"authenticatorConfig":"authenticatorConfig","authenticatorFlow":True,"userSetupAllowed":True,"requirement":"requirement","flowAlias":"flowAlias","priority":9,"authenticator":"authenticator","autheticatorFlow":True},{"authenticatorConfig":"authenticatorConfig","authenticatorFlow":True,"userSetupAllowed":True,"requirement":"requirement","flowAlias":"flowAlias","priority":9,"authenticator":"authenticator","autheticatorFlow":True}],"providerId":"providerId","topLevel":True,"builtIn":True,"alias":"alias","description":"description","id":"id"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/authentication/flows/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_flows_post(client):
    """Test case for realm_authentication_flows_post

    Create a new authentication flow
    """
    body = {"authenticationExecutions":[{"authenticatorConfig":"authenticatorConfig","authenticatorFlow":True,"userSetupAllowed":True,"requirement":"requirement","flowAlias":"flowAlias","priority":9,"authenticator":"authenticator","autheticatorFlow":True},{"authenticatorConfig":"authenticatorConfig","authenticatorFlow":True,"userSetupAllowed":True,"requirement":"requirement","flowAlias":"flowAlias","priority":9,"authenticator":"authenticator","autheticatorFlow":True}],"providerId":"providerId","topLevel":True,"builtIn":True,"alias":"alias","description":"description","id":"id"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/authentication/flows'.format(realm='realm_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_form_action_providers_get(client):
    """Test case for realm_authentication_form_action_providers_get

    Get form action providers   Returns a list of form action providers.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/authentication/form-action-providers'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_form_providers_get(client):
    """Test case for realm_authentication_form_providers_get

    Get form providers   Returns a list of form providers.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/authentication/form-providers'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_per_client_config_description_get(client):
    """Test case for realm_authentication_per_client_config_description_get

    Get configuration descriptions for all clients
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/authentication/per-client-config-description'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_register_required_action_post(client):
    """Test case for realm_authentication_register_required_action_post

    Register a new required actions
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/authentication/register-required-action'.format(realm='realm_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_required_actions_alias_delete(client):
    """Test case for realm_authentication_required_actions_alias_delete

    Delete required action
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/authentication/required-actions/{alias}'.format(realm='realm_example', alias='alias_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_required_actions_alias_get(client):
    """Test case for realm_authentication_required_actions_alias_get

    Get required action for alias
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/authentication/required-actions/{alias}'.format(realm='realm_example', alias='alias_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_required_actions_alias_lower_priority_post(client):
    """Test case for realm_authentication_required_actions_alias_lower_priority_post

    Lower required action’s priority
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/authentication/required-actions/{alias}/lower-priority'.format(realm='realm_example', alias='alias_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_required_actions_alias_put(client):
    """Test case for realm_authentication_required_actions_alias_put

    Update required action
    """
    body = {"defaultAction":True,"providerId":"providerId","name":"name","alias":"alias","priority":3,"config":{"key":""},"enabled":True}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/authentication/required-actions/{alias}'.format(realm='realm_example', alias='alias_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_required_actions_alias_raise_priority_post(client):
    """Test case for realm_authentication_required_actions_alias_raise_priority_post

    Raise required action’s priority
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/authentication/required-actions/{alias}/raise-priority'.format(realm='realm_example', alias='alias_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_required_actions_get(client):
    """Test case for realm_authentication_required_actions_get

    Get required actions   Returns a list of required actions.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/authentication/required-actions'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_authentication_unregistered_required_actions_get(client):
    """Test case for realm_authentication_unregistered_required_actions_get

    Get unregistered required actions   Returns a list of unregistered required actions.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/authentication/unregistered-required-actions'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

