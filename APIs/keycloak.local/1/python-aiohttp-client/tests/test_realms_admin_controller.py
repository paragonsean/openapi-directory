# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.admin_event_representation import AdminEventRepresentation
from openapi_server.models.client_representation import ClientRepresentation
from openapi_server.models.client_scope_representation import ClientScopeRepresentation
from openapi_server.models.event_representation import EventRepresentation
from openapi_server.models.group_representation import GroupRepresentation
from openapi_server.models.management_permission_reference import ManagementPermissionReference
from openapi_server.models.partial_import_representation import PartialImportRepresentation
from openapi_server.models.realm_events_config_representation import RealmEventsConfigRepresentation
from openapi_server.models.realm_representation import RealmRepresentation
from openapi_server.models.test_ldap_connection_representation import TestLdapConnectionRepresentation


pytestmark = pytest.mark.asyncio

async def test_realm_admin_events_delete(client):
    """Test case for realm_admin_events_delete

    Delete all admin events
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/admin-events'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_admin_events_get(client):
    """Test case for realm_admin_events_get

    Get admin events   Returns all admin events, or filters events based on URL query parameters listed here
    """
    params = [('authClient', 'auth_client_example'),
                    ('authIpAddress', 'auth_ip_address_example'),
                    ('authRealm', 'auth_realm_example'),
                    ('authUser', 'auth_user_example'),
                    ('dateFrom', 'date_from_example'),
                    ('dateTo', 'date_to_example'),
                    ('first', 56),
                    ('max', 56),
                    ('operationTypes', ['operation_types_example']),
                    ('resourcePath', '_resource_path_example'),
                    ('resourceTypes', ['resource_types_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/admin-events'.format(realm='realm_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clear_keys_cache_post(client):
    """Test case for realm_clear_keys_cache_post

    Clear cache of external public keys (Public keys of clients or Identity providers)
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clear-keys-cache'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clear_realm_cache_post(client):
    """Test case for realm_clear_realm_cache_post

    Clear realm cache
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clear-realm-cache'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_clear_user_cache_post(client):
    """Test case for realm_clear_user_cache_post

    Clear user cache
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/clear-user-cache'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_realm_client_description_converter_post(client):
    """Test case for realm_client_description_converter_post

    Base path for importing clients under this realm.
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/client-description-converter'.format(realm='realm_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_client_session_stats_get(client):
    """Test case for realm_client_session_stats_get

    Get client session stats   Returns a JSON map.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/client-session-stats'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_credential_registrators_get(client):
    """Test case for realm_credential_registrators_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/credential-registrators'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_default_default_client_scopes_client_scope_id_delete(client):
    """Test case for realm_default_default_client_scopes_client_scope_id_delete

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/default-default-client-scopes/{client_scope_id}'.format(realm='realm_example', client_scope_id='client_scope_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_default_default_client_scopes_client_scope_id_put(client):
    """Test case for realm_default_default_client_scopes_client_scope_id_put

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/default-default-client-scopes/{client_scope_id}'.format(realm='realm_example', client_scope_id='client_scope_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_default_default_client_scopes_get(client):
    """Test case for realm_default_default_client_scopes_get

    Get realm default client scopes.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/default-default-client-scopes'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_default_groups_get(client):
    """Test case for realm_default_groups_get

    Get group hierarchy.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/default-groups'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_default_groups_group_id_delete(client):
    """Test case for realm_default_groups_group_id_delete

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/default-groups/{group_id}'.format(realm='realm_example', group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_default_groups_group_id_put(client):
    """Test case for realm_default_groups_group_id_put

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/default-groups/{group_id}'.format(realm='realm_example', group_id='group_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_default_optional_client_scopes_client_scope_id_delete(client):
    """Test case for realm_default_optional_client_scopes_client_scope_id_delete

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/default-optional-client-scopes/{client_scope_id}'.format(realm='realm_example', client_scope_id='client_scope_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_default_optional_client_scopes_client_scope_id_put(client):
    """Test case for realm_default_optional_client_scopes_client_scope_id_put

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/default-optional-client-scopes/{client_scope_id}'.format(realm='realm_example', client_scope_id='client_scope_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_default_optional_client_scopes_get(client):
    """Test case for realm_default_optional_client_scopes_get

    Get realm optional client scopes.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/default-optional-client-scopes'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_delete(client):
    """Test case for realm_delete

    Delete the realm
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_events_config_get(client):
    """Test case for realm_events_config_get

    Get the events provider configuration   Returns JSON object with events provider configuration
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/events/config'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_events_config_put(client):
    """Test case for realm_events_config_put

    Update the events provider   Change the events provider and/or its configuration
    """
    body = {"adminEventsDetailsEnabled":True,"enabledEventTypes":["enabledEventTypes","enabledEventTypes"],"eventsEnabled":True,"eventsExpiration":0,"eventsListeners":["eventsListeners","eventsListeners"],"adminEventsEnabled":True}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/events/config'.format(realm='realm_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_events_delete(client):
    """Test case for realm_events_delete

    Delete all events
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/events'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_events_get(client):
    """Test case for realm_events_get

    Get events   Returns all events, or filters them based on URL query parameters listed here
    """
    params = [('client', 'client_example'),
                    ('dateFrom', 'date_from_example'),
                    ('dateTo', 'date_to_example'),
                    ('first', 56),
                    ('ipAddress', 'ip_address_example'),
                    ('max', 56),
                    ('type', ['type_example']),
                    ('user', 'user_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/events'.format(realm='realm_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_get(client):
    """Test case for realm_get

    Get the top-level representation of the realm   It will not include nested information like User and Client representations.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_group_by_path_path_get(client):
    """Test case for realm_group_by_path_path_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/group-by-path/{path}'.format(realm='realm_example', path='path_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_logout_all_post(client):
    """Test case for realm_logout_all_post

    Removes all user sessions.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/logout-all'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_partial_export_post(client):
    """Test case for realm_partial_export_post

    Partial export of existing realm into a JSON file.
    """
    params = [('exportClients', True),
                    ('exportGroupsAndRoles', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/partial-export'.format(realm='realm_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_partial_import_post(client):
    """Test case for realm_partial_import_post

    Partial import from a JSON file to an existing realm.
    """
    body = {"identityProviders":[{"firstBrokerLoginFlowAlias":"firstBrokerLoginFlowAlias","internalId":"internalId","addReadTokenRoleOnCreate":True,"displayName":"displayName","providerId":"providerId","postBrokerLoginFlowAlias":"postBrokerLoginFlowAlias","alias":"alias","trustEmail":True,"config":{"key":""},"linkOnly":True,"enabled":True,"storeToken":True},{"firstBrokerLoginFlowAlias":"firstBrokerLoginFlowAlias","internalId":"internalId","addReadTokenRoleOnCreate":True,"displayName":"displayName","providerId":"providerId","postBrokerLoginFlowAlias":"postBrokerLoginFlowAlias","alias":"alias","trustEmail":True,"config":{"key":""},"linkOnly":True,"enabled":True,"storeToken":True}],"clients":[{"optionalClientScopes":["optionalClientScopes","optionalClientScopes"],"publicClient":True,"access":{"key":""},"authorizationSettings":{"clientId":"clientId","name":"name","policies":[{"owner":"owner","policies":["policies","policies"],"resourcesData":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"description":"description","resources":["resources","resources"],"type":"type","scopesData":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"name":"name","id":"id","logic":"POSITIVE","scopes":["scopes","scopes"],"config":{"key":""},"decisionStrategy":"AFFIRMATIVE"},{"owner":"owner","policies":["policies","policies"],"resourcesData":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"description":"description","resources":["resources","resources"],"type":"type","scopesData":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"name":"name","id":"id","logic":"POSITIVE","scopes":["scopes","scopes"],"config":{"key":""},"decisionStrategy":"AFFIRMATIVE"}],"resources":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"allowRemoteResourceManagement":True,"decisionStrategy":"AFFIRMATIVE","policyEnforcementMode":"ENFORCING"},"registeredNodes":{"key":""},"authorizationServicesEnabled":True,"origin":"origin","description":"description","alwaysDisplayInConsole":True,"serviceAccountsEnabled":True,"secret":"secret","consentRequired":True,"clientAuthenticatorType":"clientAuthenticatorType","enabled":True,"notBefore":7,"frontchannelLogout":True,"surrogateAuthRequired":True,"protocol":"protocol","defaultClientScopes":["defaultClientScopes","defaultClientScopes"],"bearerOnly":True,"nodeReRegistrationTimeout":4,"id":"id","adminUrl":"adminUrl","clientId":"clientId","registrationAccessToken":"registrationAccessToken","protocolMappers":[{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}},{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}],"redirectUris":["redirectUris","redirectUris"],"fullScopeAllowed":True,"rootUrl":"rootUrl","directAccessGrantsEnabled":True,"implicitFlowEnabled":True,"baseUrl":"baseUrl","authenticationFlowBindingOverrides":{"key":""},"defaultRoles":["defaultRoles","defaultRoles"],"name":"name","standardFlowEnabled":True,"attributes":{"key":""},"webOrigins":["webOrigins","webOrigins"]},{"optionalClientScopes":["optionalClientScopes","optionalClientScopes"],"publicClient":True,"access":{"key":""},"authorizationSettings":{"clientId":"clientId","name":"name","policies":[{"owner":"owner","policies":["policies","policies"],"resourcesData":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"description":"description","resources":["resources","resources"],"type":"type","scopesData":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"name":"name","id":"id","logic":"POSITIVE","scopes":["scopes","scopes"],"config":{"key":""},"decisionStrategy":"AFFIRMATIVE"},{"owner":"owner","policies":["policies","policies"],"resourcesData":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"description":"description","resources":["resources","resources"],"type":"type","scopesData":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"name":"name","id":"id","logic":"POSITIVE","scopes":["scopes","scopes"],"config":{"key":""},"decisionStrategy":"AFFIRMATIVE"}],"resources":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"allowRemoteResourceManagement":True,"decisionStrategy":"AFFIRMATIVE","policyEnforcementMode":"ENFORCING"},"registeredNodes":{"key":""},"authorizationServicesEnabled":True,"origin":"origin","description":"description","alwaysDisplayInConsole":True,"serviceAccountsEnabled":True,"secret":"secret","consentRequired":True,"clientAuthenticatorType":"clientAuthenticatorType","enabled":True,"notBefore":7,"frontchannelLogout":True,"surrogateAuthRequired":True,"protocol":"protocol","defaultClientScopes":["defaultClientScopes","defaultClientScopes"],"bearerOnly":True,"nodeReRegistrationTimeout":4,"id":"id","adminUrl":"adminUrl","clientId":"clientId","registrationAccessToken":"registrationAccessToken","protocolMappers":[{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}},{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}],"redirectUris":["redirectUris","redirectUris"],"fullScopeAllowed":True,"rootUrl":"rootUrl","directAccessGrantsEnabled":True,"implicitFlowEnabled":True,"baseUrl":"baseUrl","authenticationFlowBindingOverrides":{"key":""},"defaultRoles":["defaultRoles","defaultRoles"],"name":"name","standardFlowEnabled":True,"attributes":{"key":""},"webOrigins":["webOrigins","webOrigins"]}],"ifResourceExists":"ifResourceExists","roles":{"client":{"key":""},"realm":[{"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"},{"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}]},"groups":[{"path":"path","realmRoles":["realmRoles","realmRoles"],"access":{"key":""},"name":"name","subGroups":[null,null],"attributes":{"key":""},"id":"id","clientRoles":{"key":""}},{"path":"path","realmRoles":["realmRoles","realmRoles"],"access":{"key":""},"name":"name","subGroups":[null,null],"attributes":{"key":""},"id":"id","clientRoles":{"key":""}}],"users":[{"lastName":"lastName","serviceAccountClientId":"serviceAccountClientId","access":{"key":""},"federatedIdentities":[{"userName":"userName","userId":"userId","identityProvider":"identityProvider"},{"userName":"userName","userId":"userId","identityProvider":"identityProvider"}],"credentials":[{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"},{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"}],"createdTimestamp":4,"origin":"origin","groups":["groups","groups"],"clientConsents":[{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]},{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]}],"enabled":True,"notBefore":9,"disableableCredentialTypes":["disableableCredentialTypes","disableableCredentialTypes"],"emailVerified":True,"firstName":"firstName","realmRoles":["realmRoles","realmRoles"],"requiredActions":["requiredActions","requiredActions"],"federationLink":"federationLink","self":"self","attributes":{"key":""},"id":"id","clientRoles":{"key":""},"email":"email","username":"username"},{"lastName":"lastName","serviceAccountClientId":"serviceAccountClientId","access":{"key":""},"federatedIdentities":[{"userName":"userName","userId":"userId","identityProvider":"identityProvider"},{"userName":"userName","userId":"userId","identityProvider":"identityProvider"}],"credentials":[{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"},{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"}],"createdTimestamp":4,"origin":"origin","groups":["groups","groups"],"clientConsents":[{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]},{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]}],"enabled":True,"notBefore":9,"disableableCredentialTypes":["disableableCredentialTypes","disableableCredentialTypes"],"emailVerified":True,"firstName":"firstName","realmRoles":["realmRoles","realmRoles"],"requiredActions":["requiredActions","requiredActions"],"federationLink":"federationLink","self":"self","attributes":{"key":""},"id":"id","clientRoles":{"key":""},"email":"email","username":"username"}],"policy":"SKIP"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/partialImport'.format(realm='realm_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_push_revocation_post(client):
    """Test case for realm_push_revocation_post

    Push the realm’s revocation policy to any client that has an admin url associated with it.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/push-revocation'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_put(client):
    """Test case for realm_put

    Update the top-level information of the realm   Any user, roles or client information in the representation  will be ignored.
    """
    body = {"otpPolicyLookAheadWindow":6,"defaultGroups":["defaultGroups","defaultGroups"],"webAuthnPolicyPasswordlessAcceptableAaguids":["webAuthnPolicyPasswordlessAcceptableAaguids","webAuthnPolicyPasswordlessAcceptableAaguids"],"directGrantFlow":"directGrantFlow","otpPolicyDigits":1,"webAuthnPolicySignatureAlgorithms":["webAuthnPolicySignatureAlgorithms","webAuthnPolicySignatureAlgorithms"],"offlineSessionMaxLifespan":6,"eventsListeners":["eventsListeners","eventsListeners"],"id":"id","adminEventsDetailsEnabled":True,"ssoSessionIdleTimeoutRememberMe":7,"accessCodeLifespanLogin":6,"clientSessionIdleTimeout":3,"quickLoginCheckMilliSeconds":5,"eventsEnabled":True,"registrationFlow":"registrationFlow","clientAuthenticationFlow":"clientAuthenticationFlow","defaultLocale":"defaultLocale","authenticatorConfig":[{"alias":"alias","id":"id","config":{"key":""}},{"alias":"alias","id":"id","config":{"key":""}}],"defaultSignatureAlgorithm":"defaultSignatureAlgorithm","duplicateEmailsAllowed":True,"accessCodeLifespan":0,"eventsExpiration":1,"webAuthnPolicyPasswordlessCreateTimeout":3,"otpPolicyType":"otpPolicyType","components":{"loadFactor":1.2315135,"threshold":1,"empty":True},"clients":[{"optionalClientScopes":["optionalClientScopes","optionalClientScopes"],"publicClient":True,"access":{"key":""},"authorizationSettings":{"clientId":"clientId","name":"name","policies":[{"owner":"owner","policies":["policies","policies"],"resourcesData":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"description":"description","resources":["resources","resources"],"type":"type","scopesData":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"name":"name","id":"id","logic":"POSITIVE","scopes":["scopes","scopes"],"config":{"key":""},"decisionStrategy":"AFFIRMATIVE"},{"owner":"owner","policies":["policies","policies"],"resourcesData":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"description":"description","resources":["resources","resources"],"type":"type","scopesData":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"name":"name","id":"id","logic":"POSITIVE","scopes":["scopes","scopes"],"config":{"key":""},"decisionStrategy":"AFFIRMATIVE"}],"resources":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"allowRemoteResourceManagement":True,"decisionStrategy":"AFFIRMATIVE","policyEnforcementMode":"ENFORCING"},"registeredNodes":{"key":""},"authorizationServicesEnabled":True,"origin":"origin","description":"description","alwaysDisplayInConsole":True,"serviceAccountsEnabled":True,"secret":"secret","consentRequired":True,"clientAuthenticatorType":"clientAuthenticatorType","enabled":True,"notBefore":7,"frontchannelLogout":True,"surrogateAuthRequired":True,"protocol":"protocol","defaultClientScopes":["defaultClientScopes","defaultClientScopes"],"bearerOnly":True,"nodeReRegistrationTimeout":4,"id":"id","adminUrl":"adminUrl","clientId":"clientId","registrationAccessToken":"registrationAccessToken","protocolMappers":[{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}},{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}],"redirectUris":["redirectUris","redirectUris"],"fullScopeAllowed":True,"rootUrl":"rootUrl","directAccessGrantsEnabled":True,"implicitFlowEnabled":True,"baseUrl":"baseUrl","authenticationFlowBindingOverrides":{"key":""},"defaultRoles":["defaultRoles","defaultRoles"],"name":"name","standardFlowEnabled":True,"attributes":{"key":""},"webOrigins":["webOrigins","webOrigins"]},{"optionalClientScopes":["optionalClientScopes","optionalClientScopes"],"publicClient":True,"access":{"key":""},"authorizationSettings":{"clientId":"clientId","name":"name","policies":[{"owner":"owner","policies":["policies","policies"],"resourcesData":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"description":"description","resources":["resources","resources"],"type":"type","scopesData":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"name":"name","id":"id","logic":"POSITIVE","scopes":["scopes","scopes"],"config":{"key":""},"decisionStrategy":"AFFIRMATIVE"},{"owner":"owner","policies":["policies","policies"],"resourcesData":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"description":"description","resources":["resources","resources"],"type":"type","scopesData":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"name":"name","id":"id","logic":"POSITIVE","scopes":["scopes","scopes"],"config":{"key":""},"decisionStrategy":"AFFIRMATIVE"}],"resources":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"allowRemoteResourceManagement":True,"decisionStrategy":"AFFIRMATIVE","policyEnforcementMode":"ENFORCING"},"registeredNodes":{"key":""},"authorizationServicesEnabled":True,"origin":"origin","description":"description","alwaysDisplayInConsole":True,"serviceAccountsEnabled":True,"secret":"secret","consentRequired":True,"clientAuthenticatorType":"clientAuthenticatorType","enabled":True,"notBefore":7,"frontchannelLogout":True,"surrogateAuthRequired":True,"protocol":"protocol","defaultClientScopes":["defaultClientScopes","defaultClientScopes"],"bearerOnly":True,"nodeReRegistrationTimeout":4,"id":"id","adminUrl":"adminUrl","clientId":"clientId","registrationAccessToken":"registrationAccessToken","protocolMappers":[{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}},{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}],"redirectUris":["redirectUris","redirectUris"],"fullScopeAllowed":True,"rootUrl":"rootUrl","directAccessGrantsEnabled":True,"implicitFlowEnabled":True,"baseUrl":"baseUrl","authenticationFlowBindingOverrides":{"key":""},"defaultRoles":["defaultRoles","defaultRoles"],"name":"name","standardFlowEnabled":True,"attributes":{"key":""},"webOrigins":["webOrigins","webOrigins"]}],"displayName":"displayName","otpPolicyAlgorithm":"otpPolicyAlgorithm","webAuthnPolicyAuthenticatorAttachment":"webAuthnPolicyAuthenticatorAttachment","enabled":True,"maxDeltaTimeSeconds":6,"internationalizationEnabled":True,"ssoSessionMaxLifespan":0,"bruteForceProtected":True,"accessTokenLifespanForImplicitFlow":5,"webAuthnPolicyPasswordlessSignatureAlgorithms":["webAuthnPolicyPasswordlessSignatureAlgorithms","webAuthnPolicyPasswordlessSignatureAlgorithms"],"userFederationProviders":[{"changedSyncPeriod":6,"fullSyncPeriod":0,"lastSync":4,"displayName":"displayName","id":"id","priority":8,"config":{"key":""},"providerName":"providerName"},{"changedSyncPeriod":6,"fullSyncPeriod":0,"lastSync":4,"displayName":"displayName","id":"id","priority":8,"config":{"key":""},"providerName":"providerName"}],"identityProviders":[{"firstBrokerLoginFlowAlias":"firstBrokerLoginFlowAlias","internalId":"internalId","addReadTokenRoleOnCreate":True,"displayName":"displayName","providerId":"providerId","postBrokerLoginFlowAlias":"postBrokerLoginFlowAlias","alias":"alias","trustEmail":True,"config":{"key":""},"linkOnly":True,"enabled":True,"storeToken":True},{"firstBrokerLoginFlowAlias":"firstBrokerLoginFlowAlias","internalId":"internalId","addReadTokenRoleOnCreate":True,"displayName":"displayName","providerId":"providerId","postBrokerLoginFlowAlias":"postBrokerLoginFlowAlias","alias":"alias","trustEmail":True,"config":{"key":""},"linkOnly":True,"enabled":True,"storeToken":True}],"supportedLocales":["supportedLocales","supportedLocales"],"webAuthnPolicyAttestationConveyancePreference":"webAuthnPolicyAttestationConveyancePreference","browserSecurityHeaders":{"key":""},"webAuthnPolicyPasswordlessUserVerificationRequirement":"webAuthnPolicyPasswordlessUserVerificationRequirement","webAuthnPolicyPasswordlessAuthenticatorAttachment":"webAuthnPolicyPasswordlessAuthenticatorAttachment","smtpServer":{"key":""},"emailTheme":"emailTheme","enabledEventTypes":["enabledEventTypes","enabledEventTypes"],"otpSupportedApplications":["otpSupportedApplications","otpSupportedApplications"],"actionTokenGeneratedByAdminLifespan":2,"defaultRoles":["defaultRoles","defaultRoles"],"attributes":{"key":""},"registrationEmailAsUsername":True,"otpPolicyPeriod":6,"ssoSessionMaxLifespanRememberMe":7,"otpPolicyInitialCounter":2,"userManagedAccessAllowed":True,"notBefore":6,"resetPasswordAllowed":True,"scopeMappings":[{"roles":["roles","roles"],"client":"client","self":"self","clientScope":"clientScope"},{"roles":["roles","roles"],"client":"client","self":"self","clientScope":"clientScope"}],"actionTokenGeneratedByUserLifespan":7,"clientScopeMappings":{"key":""},"defaultOptionalClientScopes":["defaultOptionalClientScopes","defaultOptionalClientScopes"],"webAuthnPolicyPasswordlessRpEntityName":"webAuthnPolicyPasswordlessRpEntityName","webAuthnPolicyPasswordlessAvoidSameAuthenticatorRegister":True,"webAuthnPolicyPasswordlessRequireResidentKey":"webAuthnPolicyPasswordlessRequireResidentKey","resetCredentialsFlow":"resetCredentialsFlow","webAuthnPolicyUserVerificationRequirement":"webAuthnPolicyUserVerificationRequirement","passwordPolicy":"passwordPolicy","webAuthnPolicyCreateTimeout":3,"keycloakVersion":"keycloakVersion","authenticationFlows":[{"authenticationExecutions":[{"authenticatorConfig":"authenticatorConfig","authenticatorFlow":True,"userSetupAllowed":True,"requirement":"requirement","flowAlias":"flowAlias","priority":9,"authenticator":"authenticator","autheticatorFlow":True},{"authenticatorConfig":"authenticatorConfig","authenticatorFlow":True,"userSetupAllowed":True,"requirement":"requirement","flowAlias":"flowAlias","priority":9,"authenticator":"authenticator","autheticatorFlow":True}],"providerId":"providerId","topLevel":True,"builtIn":True,"alias":"alias","description":"description","id":"id"},{"authenticationExecutions":[{"authenticatorConfig":"authenticatorConfig","authenticatorFlow":True,"userSetupAllowed":True,"requirement":"requirement","flowAlias":"flowAlias","priority":9,"authenticator":"authenticator","autheticatorFlow":True},{"authenticatorConfig":"authenticatorConfig","authenticatorFlow":True,"userSetupAllowed":True,"requirement":"requirement","flowAlias":"flowAlias","priority":9,"authenticator":"authenticator","autheticatorFlow":True}],"providerId":"providerId","topLevel":True,"builtIn":True,"alias":"alias","description":"description","id":"id"}],"revokeRefreshToken":True,"minimumQuickLoginWaitSeconds":9,"adminEventsEnabled":True,"users":[{"lastName":"lastName","serviceAccountClientId":"serviceAccountClientId","access":{"key":""},"federatedIdentities":[{"userName":"userName","userId":"userId","identityProvider":"identityProvider"},{"userName":"userName","userId":"userId","identityProvider":"identityProvider"}],"credentials":[{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"},{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"}],"createdTimestamp":4,"origin":"origin","groups":["groups","groups"],"clientConsents":[{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]},{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]}],"enabled":True,"notBefore":9,"disableableCredentialTypes":["disableableCredentialTypes","disableableCredentialTypes"],"emailVerified":True,"firstName":"firstName","realmRoles":["realmRoles","realmRoles"],"requiredActions":["requiredActions","requiredActions"],"federationLink":"federationLink","self":"self","attributes":{"key":""},"id":"id","clientRoles":{"key":""},"email":"email","username":"username"},{"lastName":"lastName","serviceAccountClientId":"serviceAccountClientId","access":{"key":""},"federatedIdentities":[{"userName":"userName","userId":"userId","identityProvider":"identityProvider"},{"userName":"userName","userId":"userId","identityProvider":"identityProvider"}],"credentials":[{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"},{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"}],"createdTimestamp":4,"origin":"origin","groups":["groups","groups"],"clientConsents":[{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]},{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]}],"enabled":True,"notBefore":9,"disableableCredentialTypes":["disableableCredentialTypes","disableableCredentialTypes"],"emailVerified":True,"firstName":"firstName","realmRoles":["realmRoles","realmRoles"],"requiredActions":["requiredActions","requiredActions"],"federationLink":"federationLink","self":"self","attributes":{"key":""},"id":"id","clientRoles":{"key":""},"email":"email","username":"username"}],"browserFlow":"browserFlow","loginWithEmailAllowed":True,"accessCodeLifespanUserAction":1,"editUsernameAllowed":True,"ssoSessionIdleTimeout":3,"clientSessionMaxLifespan":2,"offlineSessionMaxLifespanEnabled":True,"waitIncrementSeconds":7,"roles":{"client":{"key":""},"realm":[{"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"},{"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}]},"registrationAllowed":True,"displayNameHtml":"displayNameHtml","verifyEmail":True,"sslRequired":"sslRequired","webAuthnPolicyRpEntityName":"webAuthnPolicyRpEntityName","failureFactor":6,"federatedUsers":[{"lastName":"lastName","serviceAccountClientId":"serviceAccountClientId","access":{"key":""},"federatedIdentities":[{"userName":"userName","userId":"userId","identityProvider":"identityProvider"},{"userName":"userName","userId":"userId","identityProvider":"identityProvider"}],"credentials":[{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"},{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"}],"createdTimestamp":4,"origin":"origin","groups":["groups","groups"],"clientConsents":[{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]},{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]}],"enabled":True,"notBefore":9,"disableableCredentialTypes":["disableableCredentialTypes","disableableCredentialTypes"],"emailVerified":True,"firstName":"firstName","realmRoles":["realmRoles","realmRoles"],"requiredActions":["requiredActions","requiredActions"],"federationLink":"federationLink","self":"self","attributes":{"key":""},"id":"id","clientRoles":{"key":""},"email":"email","username":"username"},{"lastName":"lastName","serviceAccountClientId":"serviceAccountClientId","access":{"key":""},"federatedIdentities":[{"userName":"userName","userId":"userId","identityProvider":"identityProvider"},{"userName":"userName","userId":"userId","identityProvider":"identityProvider"}],"credentials":[{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"},{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"}],"createdTimestamp":4,"origin":"origin","groups":["groups","groups"],"clientConsents":[{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]},{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]}],"enabled":True,"notBefore":9,"disableableCredentialTypes":["disableableCredentialTypes","disableableCredentialTypes"],"emailVerified":True,"firstName":"firstName","realmRoles":["realmRoles","realmRoles"],"requiredActions":["requiredActions","requiredActions"],"federationLink":"federationLink","self":"self","attributes":{"key":""},"id":"id","clientRoles":{"key":""},"email":"email","username":"username"}],"loginTheme":"loginTheme","identityProviderMappers":[{"identityProviderAlias":"identityProviderAlias","name":"name","id":"id","config":{"key":""},"identityProviderMapper":"identityProviderMapper"},{"identityProviderAlias":"identityProviderAlias","name":"name","id":"id","config":{"key":""},"identityProviderMapper":"identityProviderMapper"}],"adminTheme":"adminTheme","accessTokenLifespan":5,"refreshTokenMaxReuse":6,"clientScopes":[{"protocol":"protocol","name":"name","description":"description","attributes":{"key":""},"protocolMappers":[{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}},{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}],"id":"id"},{"protocol":"protocol","name":"name","description":"description","attributes":{"key":""},"protocolMappers":[{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}},{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}],"id":"id"}],"defaultDefaultClientScopes":["defaultDefaultClientScopes","defaultDefaultClientScopes"],"permanentLockout":True,"webAuthnPolicyRequireResidentKey":"webAuthnPolicyRequireResidentKey","dockerAuthenticationFlow":"dockerAuthenticationFlow","webAuthnPolicyPasswordlessRpId":"webAuthnPolicyPasswordlessRpId","webAuthnPolicyRpId":"webAuthnPolicyRpId","groups":[{"path":"path","realmRoles":["realmRoles","realmRoles"],"access":{"key":""},"name":"name","subGroups":[null,null],"attributes":{"key":""},"id":"id","clientRoles":{"key":""}},{"path":"path","realmRoles":["realmRoles","realmRoles"],"access":{"key":""},"name":"name","subGroups":[null,null],"attributes":{"key":""},"id":"id","clientRoles":{"key":""}}],"maxFailureWaitSeconds":8,"protocolMappers":[{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}},{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}],"accountTheme":"accountTheme","requiredActions":[{"defaultAction":True,"providerId":"providerId","name":"name","alias":"alias","priority":3,"config":{"key":""},"enabled":True},{"defaultAction":True,"providerId":"providerId","name":"name","alias":"alias","priority":3,"config":{"key":""},"enabled":True}],"webAuthnPolicyAvoidSameAuthenticatorRegister":True,"webAuthnPolicyPasswordlessAttestationConveyancePreference":"webAuthnPolicyPasswordlessAttestationConveyancePreference","realm":"realm","rememberMe":True,"offlineSessionIdleTimeout":3,"webAuthnPolicyAcceptableAaguids":["webAuthnPolicyAcceptableAaguids","webAuthnPolicyAcceptableAaguids"],"userFederationMappers":[{"federationProviderDisplayName":"federationProviderDisplayName","name":"name","id":"id","config":{"key":""},"federationMapperType":"federationMapperType"},{"federationProviderDisplayName":"federationProviderDisplayName","name":"name","id":"id","config":{"key":""},"federationMapperType":"federationMapperType"}]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}'.format(realm='realm_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_sessions_session_delete(client):
    """Test case for realm_sessions_session_delete

    Remove a specific user session.
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/sessions/{session}'.format(realm='realm_example', session='session_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_test_ldap_connection_post(client):
    """Test case for realm_test_ldap_connection_post

    Test LDAP connection
    """
    body = {"bindCredential":"bindCredential","bindDn":"bindDn","componentId":"componentId","startTls":"startTls","useTruststoreSpi":"useTruststoreSpi","action":"action","connectionUrl":"connectionUrl","connectionTimeout":"connectionTimeout"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/testLDAPConnection'.format(realm='realm_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_test_smtp_connection_post(client):
    """Test case for realm_test_smtp_connection_post

    
    """
    body = None
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/testSMTPConnection'.format(realm='realm_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_management_permissions_get(client):
    """Test case for realm_users_management_permissions_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/users-management-permissions'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_users_management_permissions_put(client):
    """Test case for realm_users_management_permissions_put

    
    """
    body = {"scopePermissions":{"key":""},"resource":"resource","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/users-management-permissions'.format(realm='realm_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_root_post(client):
    """Test case for root_post

    Import a realm   Imports a realm from a full representation of that realm.
    """
    body = {"otpPolicyLookAheadWindow":6,"defaultGroups":["defaultGroups","defaultGroups"],"webAuthnPolicyPasswordlessAcceptableAaguids":["webAuthnPolicyPasswordlessAcceptableAaguids","webAuthnPolicyPasswordlessAcceptableAaguids"],"directGrantFlow":"directGrantFlow","otpPolicyDigits":1,"webAuthnPolicySignatureAlgorithms":["webAuthnPolicySignatureAlgorithms","webAuthnPolicySignatureAlgorithms"],"offlineSessionMaxLifespan":6,"eventsListeners":["eventsListeners","eventsListeners"],"id":"id","adminEventsDetailsEnabled":True,"ssoSessionIdleTimeoutRememberMe":7,"accessCodeLifespanLogin":6,"clientSessionIdleTimeout":3,"quickLoginCheckMilliSeconds":5,"eventsEnabled":True,"registrationFlow":"registrationFlow","clientAuthenticationFlow":"clientAuthenticationFlow","defaultLocale":"defaultLocale","authenticatorConfig":[{"alias":"alias","id":"id","config":{"key":""}},{"alias":"alias","id":"id","config":{"key":""}}],"defaultSignatureAlgorithm":"defaultSignatureAlgorithm","duplicateEmailsAllowed":True,"accessCodeLifespan":0,"eventsExpiration":1,"webAuthnPolicyPasswordlessCreateTimeout":3,"otpPolicyType":"otpPolicyType","components":{"loadFactor":1.2315135,"threshold":1,"empty":True},"clients":[{"optionalClientScopes":["optionalClientScopes","optionalClientScopes"],"publicClient":True,"access":{"key":""},"authorizationSettings":{"clientId":"clientId","name":"name","policies":[{"owner":"owner","policies":["policies","policies"],"resourcesData":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"description":"description","resources":["resources","resources"],"type":"type","scopesData":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"name":"name","id":"id","logic":"POSITIVE","scopes":["scopes","scopes"],"config":{"key":""},"decisionStrategy":"AFFIRMATIVE"},{"owner":"owner","policies":["policies","policies"],"resourcesData":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"description":"description","resources":["resources","resources"],"type":"type","scopesData":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"name":"name","id":"id","logic":"POSITIVE","scopes":["scopes","scopes"],"config":{"key":""},"decisionStrategy":"AFFIRMATIVE"}],"resources":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"allowRemoteResourceManagement":True,"decisionStrategy":"AFFIRMATIVE","policyEnforcementMode":"ENFORCING"},"registeredNodes":{"key":""},"authorizationServicesEnabled":True,"origin":"origin","description":"description","alwaysDisplayInConsole":True,"serviceAccountsEnabled":True,"secret":"secret","consentRequired":True,"clientAuthenticatorType":"clientAuthenticatorType","enabled":True,"notBefore":7,"frontchannelLogout":True,"surrogateAuthRequired":True,"protocol":"protocol","defaultClientScopes":["defaultClientScopes","defaultClientScopes"],"bearerOnly":True,"nodeReRegistrationTimeout":4,"id":"id","adminUrl":"adminUrl","clientId":"clientId","registrationAccessToken":"registrationAccessToken","protocolMappers":[{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}},{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}],"redirectUris":["redirectUris","redirectUris"],"fullScopeAllowed":True,"rootUrl":"rootUrl","directAccessGrantsEnabled":True,"implicitFlowEnabled":True,"baseUrl":"baseUrl","authenticationFlowBindingOverrides":{"key":""},"defaultRoles":["defaultRoles","defaultRoles"],"name":"name","standardFlowEnabled":True,"attributes":{"key":""},"webOrigins":["webOrigins","webOrigins"]},{"optionalClientScopes":["optionalClientScopes","optionalClientScopes"],"publicClient":True,"access":{"key":""},"authorizationSettings":{"clientId":"clientId","name":"name","policies":[{"owner":"owner","policies":["policies","policies"],"resourcesData":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"description":"description","resources":["resources","resources"],"type":"type","scopesData":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"name":"name","id":"id","logic":"POSITIVE","scopes":["scopes","scopes"],"config":{"key":""},"decisionStrategy":"AFFIRMATIVE"},{"owner":"owner","policies":["policies","policies"],"resourcesData":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"description":"description","resources":["resources","resources"],"type":"type","scopesData":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"name":"name","id":"id","logic":"POSITIVE","scopes":["scopes","scopes"],"config":{"key":""},"decisionStrategy":"AFFIRMATIVE"}],"resources":[{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"},{"uris":["uris","uris"],"ownerManagedAccess":True,"displayName":"displayName","name":"name","attributes":{"key":""},"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"type":"type","icon_uri":"icon_uri"}],"id":"id","scopes":[{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"},{"displayName":"displayName","name":"name","policies":[null,null],"resources":[null,null],"id":"id","iconUri":"iconUri"}],"allowRemoteResourceManagement":True,"decisionStrategy":"AFFIRMATIVE","policyEnforcementMode":"ENFORCING"},"registeredNodes":{"key":""},"authorizationServicesEnabled":True,"origin":"origin","description":"description","alwaysDisplayInConsole":True,"serviceAccountsEnabled":True,"secret":"secret","consentRequired":True,"clientAuthenticatorType":"clientAuthenticatorType","enabled":True,"notBefore":7,"frontchannelLogout":True,"surrogateAuthRequired":True,"protocol":"protocol","defaultClientScopes":["defaultClientScopes","defaultClientScopes"],"bearerOnly":True,"nodeReRegistrationTimeout":4,"id":"id","adminUrl":"adminUrl","clientId":"clientId","registrationAccessToken":"registrationAccessToken","protocolMappers":[{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}},{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}],"redirectUris":["redirectUris","redirectUris"],"fullScopeAllowed":True,"rootUrl":"rootUrl","directAccessGrantsEnabled":True,"implicitFlowEnabled":True,"baseUrl":"baseUrl","authenticationFlowBindingOverrides":{"key":""},"defaultRoles":["defaultRoles","defaultRoles"],"name":"name","standardFlowEnabled":True,"attributes":{"key":""},"webOrigins":["webOrigins","webOrigins"]}],"displayName":"displayName","otpPolicyAlgorithm":"otpPolicyAlgorithm","webAuthnPolicyAuthenticatorAttachment":"webAuthnPolicyAuthenticatorAttachment","enabled":True,"maxDeltaTimeSeconds":6,"internationalizationEnabled":True,"ssoSessionMaxLifespan":0,"bruteForceProtected":True,"accessTokenLifespanForImplicitFlow":5,"webAuthnPolicyPasswordlessSignatureAlgorithms":["webAuthnPolicyPasswordlessSignatureAlgorithms","webAuthnPolicyPasswordlessSignatureAlgorithms"],"userFederationProviders":[{"changedSyncPeriod":6,"fullSyncPeriod":0,"lastSync":4,"displayName":"displayName","id":"id","priority":8,"config":{"key":""},"providerName":"providerName"},{"changedSyncPeriod":6,"fullSyncPeriod":0,"lastSync":4,"displayName":"displayName","id":"id","priority":8,"config":{"key":""},"providerName":"providerName"}],"identityProviders":[{"firstBrokerLoginFlowAlias":"firstBrokerLoginFlowAlias","internalId":"internalId","addReadTokenRoleOnCreate":True,"displayName":"displayName","providerId":"providerId","postBrokerLoginFlowAlias":"postBrokerLoginFlowAlias","alias":"alias","trustEmail":True,"config":{"key":""},"linkOnly":True,"enabled":True,"storeToken":True},{"firstBrokerLoginFlowAlias":"firstBrokerLoginFlowAlias","internalId":"internalId","addReadTokenRoleOnCreate":True,"displayName":"displayName","providerId":"providerId","postBrokerLoginFlowAlias":"postBrokerLoginFlowAlias","alias":"alias","trustEmail":True,"config":{"key":""},"linkOnly":True,"enabled":True,"storeToken":True}],"supportedLocales":["supportedLocales","supportedLocales"],"webAuthnPolicyAttestationConveyancePreference":"webAuthnPolicyAttestationConveyancePreference","browserSecurityHeaders":{"key":""},"webAuthnPolicyPasswordlessUserVerificationRequirement":"webAuthnPolicyPasswordlessUserVerificationRequirement","webAuthnPolicyPasswordlessAuthenticatorAttachment":"webAuthnPolicyPasswordlessAuthenticatorAttachment","smtpServer":{"key":""},"emailTheme":"emailTheme","enabledEventTypes":["enabledEventTypes","enabledEventTypes"],"otpSupportedApplications":["otpSupportedApplications","otpSupportedApplications"],"actionTokenGeneratedByAdminLifespan":2,"defaultRoles":["defaultRoles","defaultRoles"],"attributes":{"key":""},"registrationEmailAsUsername":True,"otpPolicyPeriod":6,"ssoSessionMaxLifespanRememberMe":7,"otpPolicyInitialCounter":2,"userManagedAccessAllowed":True,"notBefore":6,"resetPasswordAllowed":True,"scopeMappings":[{"roles":["roles","roles"],"client":"client","self":"self","clientScope":"clientScope"},{"roles":["roles","roles"],"client":"client","self":"self","clientScope":"clientScope"}],"actionTokenGeneratedByUserLifespan":7,"clientScopeMappings":{"key":""},"defaultOptionalClientScopes":["defaultOptionalClientScopes","defaultOptionalClientScopes"],"webAuthnPolicyPasswordlessRpEntityName":"webAuthnPolicyPasswordlessRpEntityName","webAuthnPolicyPasswordlessAvoidSameAuthenticatorRegister":True,"webAuthnPolicyPasswordlessRequireResidentKey":"webAuthnPolicyPasswordlessRequireResidentKey","resetCredentialsFlow":"resetCredentialsFlow","webAuthnPolicyUserVerificationRequirement":"webAuthnPolicyUserVerificationRequirement","passwordPolicy":"passwordPolicy","webAuthnPolicyCreateTimeout":3,"keycloakVersion":"keycloakVersion","authenticationFlows":[{"authenticationExecutions":[{"authenticatorConfig":"authenticatorConfig","authenticatorFlow":True,"userSetupAllowed":True,"requirement":"requirement","flowAlias":"flowAlias","priority":9,"authenticator":"authenticator","autheticatorFlow":True},{"authenticatorConfig":"authenticatorConfig","authenticatorFlow":True,"userSetupAllowed":True,"requirement":"requirement","flowAlias":"flowAlias","priority":9,"authenticator":"authenticator","autheticatorFlow":True}],"providerId":"providerId","topLevel":True,"builtIn":True,"alias":"alias","description":"description","id":"id"},{"authenticationExecutions":[{"authenticatorConfig":"authenticatorConfig","authenticatorFlow":True,"userSetupAllowed":True,"requirement":"requirement","flowAlias":"flowAlias","priority":9,"authenticator":"authenticator","autheticatorFlow":True},{"authenticatorConfig":"authenticatorConfig","authenticatorFlow":True,"userSetupAllowed":True,"requirement":"requirement","flowAlias":"flowAlias","priority":9,"authenticator":"authenticator","autheticatorFlow":True}],"providerId":"providerId","topLevel":True,"builtIn":True,"alias":"alias","description":"description","id":"id"}],"revokeRefreshToken":True,"minimumQuickLoginWaitSeconds":9,"adminEventsEnabled":True,"users":[{"lastName":"lastName","serviceAccountClientId":"serviceAccountClientId","access":{"key":""},"federatedIdentities":[{"userName":"userName","userId":"userId","identityProvider":"identityProvider"},{"userName":"userName","userId":"userId","identityProvider":"identityProvider"}],"credentials":[{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"},{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"}],"createdTimestamp":4,"origin":"origin","groups":["groups","groups"],"clientConsents":[{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]},{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]}],"enabled":True,"notBefore":9,"disableableCredentialTypes":["disableableCredentialTypes","disableableCredentialTypes"],"emailVerified":True,"firstName":"firstName","realmRoles":["realmRoles","realmRoles"],"requiredActions":["requiredActions","requiredActions"],"federationLink":"federationLink","self":"self","attributes":{"key":""},"id":"id","clientRoles":{"key":""},"email":"email","username":"username"},{"lastName":"lastName","serviceAccountClientId":"serviceAccountClientId","access":{"key":""},"federatedIdentities":[{"userName":"userName","userId":"userId","identityProvider":"identityProvider"},{"userName":"userName","userId":"userId","identityProvider":"identityProvider"}],"credentials":[{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"},{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"}],"createdTimestamp":4,"origin":"origin","groups":["groups","groups"],"clientConsents":[{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]},{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]}],"enabled":True,"notBefore":9,"disableableCredentialTypes":["disableableCredentialTypes","disableableCredentialTypes"],"emailVerified":True,"firstName":"firstName","realmRoles":["realmRoles","realmRoles"],"requiredActions":["requiredActions","requiredActions"],"federationLink":"federationLink","self":"self","attributes":{"key":""},"id":"id","clientRoles":{"key":""},"email":"email","username":"username"}],"browserFlow":"browserFlow","loginWithEmailAllowed":True,"accessCodeLifespanUserAction":1,"editUsernameAllowed":True,"ssoSessionIdleTimeout":3,"clientSessionMaxLifespan":2,"offlineSessionMaxLifespanEnabled":True,"waitIncrementSeconds":7,"roles":{"client":{"key":""},"realm":[{"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"},{"composites":{"client":{"key":""},"realm":["realm","realm"]},"clientRole":True,"composite":True,"name":"name","description":"description","attributes":{"key":""},"id":"id","containerId":"containerId"}]},"registrationAllowed":True,"displayNameHtml":"displayNameHtml","verifyEmail":True,"sslRequired":"sslRequired","webAuthnPolicyRpEntityName":"webAuthnPolicyRpEntityName","failureFactor":6,"federatedUsers":[{"lastName":"lastName","serviceAccountClientId":"serviceAccountClientId","access":{"key":""},"federatedIdentities":[{"userName":"userName","userId":"userId","identityProvider":"identityProvider"},{"userName":"userName","userId":"userId","identityProvider":"identityProvider"}],"credentials":[{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"},{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"}],"createdTimestamp":4,"origin":"origin","groups":["groups","groups"],"clientConsents":[{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]},{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]}],"enabled":True,"notBefore":9,"disableableCredentialTypes":["disableableCredentialTypes","disableableCredentialTypes"],"emailVerified":True,"firstName":"firstName","realmRoles":["realmRoles","realmRoles"],"requiredActions":["requiredActions","requiredActions"],"federationLink":"federationLink","self":"self","attributes":{"key":""},"id":"id","clientRoles":{"key":""},"email":"email","username":"username"},{"lastName":"lastName","serviceAccountClientId":"serviceAccountClientId","access":{"key":""},"federatedIdentities":[{"userName":"userName","userId":"userId","identityProvider":"identityProvider"},{"userName":"userName","userId":"userId","identityProvider":"identityProvider"}],"credentials":[{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"},{"temporary":True,"userLabel":"userLabel","createdDate":5,"credentialData":"credentialData","id":"id","priority":9,"type":"type","value":"value","secretData":"secretData"}],"createdTimestamp":4,"origin":"origin","groups":["groups","groups"],"clientConsents":[{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]},{"lastUpdatedDate":1,"clientId":"clientId","createdDate":7,"grantedClientScopes":["grantedClientScopes","grantedClientScopes"]}],"enabled":True,"notBefore":9,"disableableCredentialTypes":["disableableCredentialTypes","disableableCredentialTypes"],"emailVerified":True,"firstName":"firstName","realmRoles":["realmRoles","realmRoles"],"requiredActions":["requiredActions","requiredActions"],"federationLink":"federationLink","self":"self","attributes":{"key":""},"id":"id","clientRoles":{"key":""},"email":"email","username":"username"}],"loginTheme":"loginTheme","identityProviderMappers":[{"identityProviderAlias":"identityProviderAlias","name":"name","id":"id","config":{"key":""},"identityProviderMapper":"identityProviderMapper"},{"identityProviderAlias":"identityProviderAlias","name":"name","id":"id","config":{"key":""},"identityProviderMapper":"identityProviderMapper"}],"adminTheme":"adminTheme","accessTokenLifespan":5,"refreshTokenMaxReuse":6,"clientScopes":[{"protocol":"protocol","name":"name","description":"description","attributes":{"key":""},"protocolMappers":[{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}},{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}],"id":"id"},{"protocol":"protocol","name":"name","description":"description","attributes":{"key":""},"protocolMappers":[{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}},{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}],"id":"id"}],"defaultDefaultClientScopes":["defaultDefaultClientScopes","defaultDefaultClientScopes"],"permanentLockout":True,"webAuthnPolicyRequireResidentKey":"webAuthnPolicyRequireResidentKey","dockerAuthenticationFlow":"dockerAuthenticationFlow","webAuthnPolicyPasswordlessRpId":"webAuthnPolicyPasswordlessRpId","webAuthnPolicyRpId":"webAuthnPolicyRpId","groups":[{"path":"path","realmRoles":["realmRoles","realmRoles"],"access":{"key":""},"name":"name","subGroups":[null,null],"attributes":{"key":""},"id":"id","clientRoles":{"key":""}},{"path":"path","realmRoles":["realmRoles","realmRoles"],"access":{"key":""},"name":"name","subGroups":[null,null],"attributes":{"key":""},"id":"id","clientRoles":{"key":""}}],"maxFailureWaitSeconds":8,"protocolMappers":[{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}},{"protocol":"protocol","protocolMapper":"protocolMapper","name":"name","id":"id","config":{"key":""}}],"accountTheme":"accountTheme","requiredActions":[{"defaultAction":True,"providerId":"providerId","name":"name","alias":"alias","priority":3,"config":{"key":""},"enabled":True},{"defaultAction":True,"providerId":"providerId","name":"name","alias":"alias","priority":3,"config":{"key":""},"enabled":True}],"webAuthnPolicyAvoidSameAuthenticatorRegister":True,"webAuthnPolicyPasswordlessAttestationConveyancePreference":"webAuthnPolicyPasswordlessAttestationConveyancePreference","realm":"realm","rememberMe":True,"offlineSessionIdleTimeout":3,"webAuthnPolicyAcceptableAaguids":["webAuthnPolicyAcceptableAaguids","webAuthnPolicyAcceptableAaguids"],"userFederationMappers":[{"federationProviderDisplayName":"federationProviderDisplayName","name":"name","id":"id","config":{"key":""},"federationMapperType":"federationMapperType"},{"federationProviderDisplayName":"federationProviderDisplayName","name":"name","id":"id","config":{"key":""},"federationMapperType":"federationMapperType"}]}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

