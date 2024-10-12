# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.credential_representation import CredentialRepresentation
from openapi_server.models.federated_identity_representation import FederatedIdentityRepresentation
from openapi_server.models.group_representation import GroupRepresentation
from openapi_server.models.user_representation import UserRepresentation
from openapi_server.models.user_session_representation import UserSessionRepresentation


pytestmark = pytest.mark.asyncio

async def test_realm_users_count_get(client):
    """Test case for realm_users_count_get

    Returns the number of users that match the given criteria.
    """
    params = [('email', 'email_example'),
                    ('firstName', 'first_name_example'),
                    ('lastName', 'last_name_example'),
                    ('search', 'search_example'),
                    ('username', 'username_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users/count'.format(realm='realm_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_get(client):
    """Test case for realm_users_get

    Get users   Returns a list of users, filtered according to query parameters
    """
    params = [('briefRepresentation', True),
                    ('email', 'email_example'),
                    ('first', 56),
                    ('firstName', 'first_name_example'),
                    ('lastName', 'last_name_example'),
                    ('max', 56),
                    ('search', 'search_example'),
                    ('username', 'username_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users'.format(realm='realm_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_configured_user_storage_credential_types_get(client):
    """Test case for realm_users_id_configured_user_storage_credential_types_get

    Return credential types, which are provided by the user storage where user is stored.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users/{id}/configured-user-storage-credential-types'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_consents_client_delete(client):
    """Test case for realm_users_id_consents_client_delete

    Revoke consent and offline tokens for particular client from user
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/users/{id}/consents/{client}'.format(realm='realm_example', id='id_example', client='client_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_consents_get(client):
    """Test case for realm_users_id_consents_get

    Get consents granted by the user
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users/{id}/consents'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_credentials_credential_id_delete(client):
    """Test case for realm_users_id_credentials_credential_id_delete

    Remove a credential for a user
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/users/{id}/credentials/{credential_id}'.format(realm='realm_example', id='id_example', credential_id='credential_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_credentials_credential_id_move_after_new_previous_credential_id_post(client):
    """Test case for realm_users_id_credentials_credential_id_move_after_new_previous_credential_id_post

    Move a credential to a position behind another credential
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/users/{id}/credentials/{credential_id}/moveAfter/{new_previous_credential_id}'.format(realm='realm_example', id='id_example', credential_id='credential_id_example', new_previous_credential_id='new_previous_credential_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_credentials_credential_id_move_to_first_post(client):
    """Test case for realm_users_id_credentials_credential_id_move_to_first_post

    Move a credential to a first position in the credentials list of the user
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/users/{id}/credentials/{credential_id}/moveToFirst'.format(realm='realm_example', id='id_example', credential_id='credential_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_realm_users_id_credentials_credential_id_user_label_put(client):
    """Test case for realm_users_id_credentials_credential_id_user_label_put

    Update a credential label for a user
    """
    body = 'body_example'
    headers = { 
        'Content-Type': 'text/plain',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/users/{id}/credentials/{credential_id}/userLabel'.format(realm='realm_example', id='id_example', credential_id='credential_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_credentials_get(client):
    """Test case for realm_users_id_credentials_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users/{id}/credentials'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_delete(client):
    """Test case for realm_users_id_delete

    Delete the user
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/users/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_disable_credential_types_put(client):
    """Test case for realm_users_id_disable_credential_types_put

    Disable all credentials for a user of a specific type
    """
    body = ['body_example']
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/users/{id}/disable-credential-types'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_execute_actions_email_put(client):
    """Test case for realm_users_id_execute_actions_email_put

    Send a update account email to the user   An email contains a link the user can click to perform a set of required actions.
    """
    body = ['body_example']
    params = [('client_id', 'client_id_example'),
                    ('lifespan', 56),
                    ('redirect_uri', 'redirect_uri_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/users/{id}/execute-actions-email'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_federated_identity_get(client):
    """Test case for realm_users_id_federated_identity_get

    Get social logins associated with the user
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users/{id}/federated-identity'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_federated_identity_provider_delete(client):
    """Test case for realm_users_id_federated_identity_provider_delete

    Remove a social login provider from user
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/users/{id}/federated-identity/{provider}'.format(realm='realm_example', id='id_example', provider='provider_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_federated_identity_provider_post(client):
    """Test case for realm_users_id_federated_identity_provider_post

    Add a social login provider to the user
    """
    body = {"userName":"userName","userId":"userId","identityProvider":"identityProvider"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/users/{id}/federated-identity/{provider}'.format(realm='realm_example', id='id_example', provider='provider_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_get(client):
    """Test case for realm_users_id_get

    Get representation of the user
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_groups_count_get(client):
    """Test case for realm_users_id_groups_count_get

    
    """
    params = [('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users/{id}/groups/count'.format(realm='realm_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_groups_get(client):
    """Test case for realm_users_id_groups_get

    
    """
    params = [('briefRepresentation', True),
                    ('first', 56),
                    ('max', 56),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users/{id}/groups'.format(realm='realm_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_groups_group_id_delete(client):
    """Test case for realm_users_id_groups_group_id_delete

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/users/{id}/groups/{group_id}'.format(realm='realm_example', id='id_example', group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_groups_group_id_put(client):
    """Test case for realm_users_id_groups_group_id_put

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/users/{id}/groups/{group_id}'.format(realm='realm_example', id='id_example', group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_impersonation_post(client):
    """Test case for realm_users_id_impersonation_post

    Impersonate the user
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/users/{id}/impersonation'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_logout_post(client):
    """Test case for realm_users_id_logout_post

    Remove all user sessions associated with the user   Also send notification to all clients that have an admin URL to invalidate the sessions for the particular user.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/users/{id}/logout'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_offline_sessions_client_id_get(client):
    """Test case for realm_users_id_offline_sessions_client_id_get

    Get offline sessions associated with the user and client
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users/{id}/offline-sessions/{client_id}'.format(realm='realm_example', id='id_example', client_id='client_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_put(client):
    """Test case for realm_users_id_put

    Update the user
    """
    body = {"lastName":"lastName","serviceAccountClientId":"serviceAccountClientId","access":{"key":""},"federatedIdentities":[{"userName":"userName","userId":"userId","identityProvider":"identityProvider"},{"userName":"userName","userId":"userId","identityProvider":"identityProvider"}],"credentials":[{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"},{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"}],"createdTimestamp":4,"origin":"origin","groups":["groups","groups"],"clientConsents":[{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]},{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]}],"enabled":True,"notBefore":9,"disableableCredentialTypes":["disableableCredentialTypes","disableableCredentialTypes"],"emailVerified":True,"firstName":"firstName","realmRoles":["realmRoles","realmRoles"],"requiredActions":["requiredActions","requiredActions"],"federationLink":"federationLink","self":"self","attributes":{"key":""},"id":"id","clientRoles":{"key":""},"email":"email","username":"username"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/users/{id}'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_reset_password_put(client):
    """Test case for realm_users_id_reset_password_put

    Set up a new password for the user.
    """
    body = {"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/users/{id}/reset-password'.format(realm='realm_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_send_verify_email_put(client):
    """Test case for realm_users_id_send_verify_email_put

    Send an email-verification email to the user   An email contains a link the user can click to verify their email address.
    """
    params = [('client_id', 'client_id_example'),
                    ('redirect_uri', 'redirect_uri_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/users/{id}/send-verify-email'.format(realm='realm_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_id_sessions_get(client):
    """Test case for realm_users_id_sessions_get

    Get sessions associated with the user
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users/{id}/sessions'.format(realm='realm_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_post(client):
    """Test case for realm_users_post

    Create a new user   Username must be unique.
    """
    body = {"lastName":"lastName","serviceAccountClientId":"serviceAccountClientId","access":{"key":""},"federatedIdentities":[{"userName":"userName","userId":"userId","identityProvider":"identityProvider"},{"userName":"userName","userId":"userId","identityProvider":"identityProvider"}],"credentials":[{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"},{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"}],"createdTimestamp":4,"origin":"origin","groups":["groups","groups"],"clientConsents":[{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]},{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]}],"enabled":True,"notBefore":9,"disableableCredentialTypes":["disableableCredentialTypes","disableableCredentialTypes"],"emailVerified":True,"firstName":"firstName","realmRoles":["realmRoles","realmRoles"],"requiredActions":["requiredActions","requiredActions"],"federationLink":"federationLink","self":"self","attributes":{"key":""},"id":"id","clientRoles":{"key":""},"email":"email","username":"username"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/users'.format(realm='realm_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

