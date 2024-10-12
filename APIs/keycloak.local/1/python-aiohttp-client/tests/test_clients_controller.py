# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_token import AccessToken
from openapi_server.models.client_representation import ClientRepresentation
from openapi_server.models.client_scope_evaluate_resource_protocol_mapper_evaluation_representation import ClientScopeEvaluateResourceProtocolMapperEvaluationRepresentation
from openapi_server.models.client_scope_representation import ClientScopeRepresentation
from openapi_server.models.credential_representation import CredentialRepresentation
from openapi_server.models.global_request_result import GlobalRequestResult
from openapi_server.models.management_permission_reference import ManagementPermissionReference
from openapi_server.models.role_representation import RoleRepresentation
from openapi_server.models.user_representation import UserRepresentation
from openapi_server.models.user_session_representation import UserSessionRepresentation


pytestmark = pytest.mark.asyncio

async def test_realm_clients_get(client):
    """Test case for realm_clients_get

    Get clients belonging to the realm   Returns a list of clients belonging to the realm
    """
    params = [('clientId', 'client_id_example'),
                    ('first', 56),
                    ('max', 56),
                    ('search', True),
                    ('viewableOnly', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients'.format(realm='realm_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_client_secret_get(client):
    """Test case for realm_clients_id_client_secret_get

    Get the client secret
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/client-secret'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_client_secret_post(client):
    """Test case for realm_clients_id_client_secret_post

    Generate a new secret for the client
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clients/{id}/client-secret'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_default_client_scopes_client_scope_id_delete(client):
    """Test case for realm_clients_id_default_client_scopes_client_scope_id_delete

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/clients/{id}/default-client-scopes/{client_scope_id}'.format(realm='realm_example', id='id_example', client_scope_id='client_scope_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_default_client_scopes_client_scope_id_put(client):
    """Test case for realm_clients_id_default_client_scopes_client_scope_id_put

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/clients/{id}/default-client-scopes/{client_scope_id}'.format(realm='realm_example', id='id_example', client_scope_id='client_scope_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_default_client_scopes_get(client):
    """Test case for realm_clients_id_default_client_scopes_get

    Get default client scopes.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/default-client-scopes'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_delete(client):
    """Test case for realm_clients_id_delete

    Delete the client
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/clients/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_evaluate_scopes_generate_example_access_token_get(client):
    """Test case for realm_clients_id_evaluate_scopes_generate_example_access_token_get

    Create JSON with payload of example access token
    """
    params = [('scope', 'scope_example'),
                    ('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/evaluate-scopes/generate-example-access-token'.format(realm='realm_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_evaluate_scopes_protocol_mappers_get(client):
    """Test case for realm_clients_id_evaluate_scopes_protocol_mappers_get

    Return list of all protocol mappers, which will be used when generating tokens issued for particular client.
    """
    params = [('scope', 'scope_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/evaluate-scopes/protocol-mappers'.format(realm='realm_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_granted_get(client):
    """Test case for realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_granted_get

    Get effective scope mapping of all roles of particular role container, which this client is defacto allowed to have in the accessToken issued for him.
    """
    params = [('scope', 'scope_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/evaluate-scopes/scope-mappings/{role_container_id}/granted'.format(realm='realm_example', id='id_example', role_container_id='role_container_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_not_granted_get(client):
    """Test case for realm_clients_id_evaluate_scopes_scope_mappings_role_container_id_not_granted_get

    Get roles, which this client doesn’t have scope for and can’t have them in the accessToken issued for him.
    """
    params = [('scope', 'scope_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/evaluate-scopes/scope-mappings/{role_container_id}/not-granted'.format(realm='realm_example', id='id_example', role_container_id='role_container_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_get(client):
    """Test case for realm_clients_id_get

    Get representation of the client
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_installation_providers_provider_id_get(client):
    """Test case for realm_clients_id_installation_providers_provider_id_get

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/installation/providers/{provider_id}'.format(realm='realm_example', id='id_example', provider_id='provider_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_management_permissions_get(client):
    """Test case for realm_clients_id_management_permissions_get

    Return object stating whether client Authorization permissions have been initialized or not and a reference
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/management/permissions'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_management_permissions_put(client):
    """Test case for realm_clients_id_management_permissions_put

    Return object stating whether client Authorization permissions have been initialized or not and a reference
    """
    body = {"scopePermissions":{"key":""},"resource":"resource","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/clients/{id}/management/permissions'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_nodes_node_delete(client):
    """Test case for realm_clients_id_nodes_node_delete

    Unregister a cluster node from the client
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/clients/{id}/nodes/{node}'.format(realm='realm_example', id='id_example', node='node_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_nodes_post(client):
    """Test case for realm_clients_id_nodes_post

    Register a cluster node with the client   Manually register cluster node to this client - usually it’s not needed to call this directly as adapter should handle  by sending registration request to Keycloak
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clients/{id}/nodes'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_offline_session_count_get(client):
    """Test case for realm_clients_id_offline_session_count_get

    Get application offline session count   Returns a number of offline user sessions associated with this client   {      \"count\": number  }
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/offline-session-count'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_offline_sessions_get(client):
    """Test case for realm_clients_id_offline_sessions_get

    Get offline sessions for client   Returns a list of offline user sessions associated with this client
    """
    params = [('first', 56),
                    ('max', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/offline-sessions'.format(realm='realm_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_optional_client_scopes_client_scope_id_delete(client):
    """Test case for realm_clients_id_optional_client_scopes_client_scope_id_delete

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/clients/{id}/optional-client-scopes/{client_scope_id}'.format(realm='realm_example', id='id_example', client_scope_id='client_scope_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_optional_client_scopes_client_scope_id_put(client):
    """Test case for realm_clients_id_optional_client_scopes_client_scope_id_put

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/clients/{id}/optional-client-scopes/{client_scope_id}'.format(realm='realm_example', id='id_example', client_scope_id='client_scope_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_optional_client_scopes_get(client):
    """Test case for realm_clients_id_optional_client_scopes_get

    Get optional client scopes.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/optional-client-scopes'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_push_revocation_post(client):
    """Test case for realm_clients_id_push_revocation_post

    Push the client’s revocation policy to its admin URL   If the client has an admin URL, push revocation policy to it.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clients/{id}/push-revocation'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_put(client):
    """Test case for realm_clients_id_put

    Update the client
    """
    body = {"optionalClientScopes":["optionalClientScopes","optionalClientScopes"],"publicClient":True,"access":{"key":""},"authorizationSettings":{"clientId":"clientId","name":"name","policies":[{"owner":"owner","policies":["policies","policies"],"resourcesData":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"description":"description","resources":["resources","resources"],"type":"type","scopesData":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"name":"name","id":"id","logic":"POSITIVE","scopes":["scopes","scopes"],"config":{"key":""},"decisionStrategy":"AFFIRMATIVE"},{"owner":"owner","policies":["policies","policies"],"resourcesData":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"description":"description","resources":["resources","resources"],"type":"type","scopesData":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"name":"name","id":"id","logic":"POSITIVE","scopes":["scopes","scopes"],"config":{"key":""},"decisionStrategy":"AFFIRMATIVE"}],"resources":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"allowRemoteResourceManagement":True,"decisionStrategy":"AFFIRMATIVE","policyEnforcementMode":"ENFORCING"},"registeredNodes":{"key":""},"authorizationServicesEnabled":True,"origin":"origin","description":"description","alwaysDisplayInConsole":True,"serviceAccountsEnabled":True,"secret":"secret","consentRequired":True,"clientAuthenticatorType":"clientAuthenticatorType","enabled":True,"notBefore":7,"frontchannelLogout":True,"surrogateAuthRequired":True,"protocol":"protocol","defaultClientScopes":["defaultClientScopes","defaultClientScopes"],"bearerOnly":True,"nodeReRegistrationTimeout":4,"id":"id","adminUrl":"adminUrl","clientId":"clientId","registrationAccessToken":"registrationAccessToken","protocolMappers":[{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}},{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}],"redirectUris":["redirectUris","redirectUris"],"fullScopeAllowed":True,"rootUrl":"rootUrl","directAccessGrantsEnabled":True,"implicitFlowEnabled":True,"baseUrl":"baseUrl","authenticationFlowBindingOverrides":{"key":""},"defaultRoles":["defaultRoles","defaultRoles"],"name":"name","standardFlowEnabled":True,"attributes":{"key":""},"webOrigins":["webOrigins","webOrigins"]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/clients/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_registration_access_token_post(client):
    """Test case for realm_clients_id_registration_access_token_post

    Generate a new registration access token for the client
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clients/{id}/registration-access-token'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_service_account_user_get(client):
    """Test case for realm_clients_id_service_account_user_get

    Get a user dedicated to the service account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/service-account-user'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_session_count_get(client):
    """Test case for realm_clients_id_session_count_get

    Get application session count   Returns a number of user sessions associated with this client   {      \"count\": number  }
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/session-count'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_test_nodes_available_get(client):
    """Test case for realm_clients_id_test_nodes_available_get

    Test if registered cluster nodes are available   Tests availability by sending 'ping' request to all cluster nodes.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/test-nodes-available'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_id_user_sessions_get(client):
    """Test case for realm_clients_id_user_sessions_get

    Get user sessions for client   Returns a list of user sessions associated with this client
    """
    params = [('first', 56),
                    ('max', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/clients/{id}/user-sessions'.format(realm='realm_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clients_post(client):
    """Test case for realm_clients_post

    Create a new client   Client’s client_id must be unique!
    """
    body = {"optionalClientScopes":["optionalClientScopes","optionalClientScopes"],"publicClient":True,"access":{"key":""},"authorizationSettings":{"clientId":"clientId","name":"name","policies":[{"owner":"owner","policies":["policies","policies"],"resourcesData":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"description":"description","resources":["resources","resources"],"type":"type","scopesData":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"name":"name","id":"id","logic":"POSITIVE","scopes":["scopes","scopes"],"config":{"key":""},"decisionStrategy":"AFFIRMATIVE"},{"owner":"owner","policies":["policies","policies"],"resourcesData":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"description":"description","resources":["resources","resources"],"type":"type","scopesData":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"name":"name","id":"id","logic":"POSITIVE","scopes":["scopes","scopes"],"config":{"key":""},"decisionStrategy":"AFFIRMATIVE"}],"resources":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"allowRemoteResourceManagement":True,"decisionStrategy":"AFFIRMATIVE","policyEnforcementMode":"ENFORCING"},"registeredNodes":{"key":""},"authorizationServicesEnabled":True,"origin":"origin","description":"description","alwaysDisplayInConsole":True,"serviceAccountsEnabled":True,"secret":"secret","consentRequired":True,"clientAuthenticatorType":"clientAuthenticatorType","enabled":True,"notBefore":7,"frontchannelLogout":True,"surrogateAuthRequired":True,"protocol":"protocol","defaultClientScopes":["defaultClientScopes","defaultClientScopes"],"bearerOnly":True,"nodeReRegistrationTimeout":4,"id":"id","adminUrl":"adminUrl","clientId":"clientId","registrationAccessToken":"registrationAccessToken","protocolMappers":[{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}},{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}],"redirectUris":["redirectUris","redirectUris"],"fullScopeAllowed":True,"rootUrl":"rootUrl","directAccessGrantsEnabled":True,"implicitFlowEnabled":True,"baseUrl":"baseUrl","authenticationFlowBindingOverrides":{"key":""},"defaultRoles":["defaultRoles","defaultRoles"],"name":"name","standardFlowEnabled":True,"attributes":{"key":""},"webOrigins":["webOrigins","webOrigins"]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clients'.format(realm='realm_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

