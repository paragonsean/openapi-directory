# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.identity_provider_mapper_representation import IdentityProviderMapperRepresentation
from openapi_server.models.identity_provider_representation import IdentityProviderRepresentation
from openapi_server.models.management_permission_reference import ManagementPermissionReference


pytestmark = pytest.mark.asyncio

async def test_realm_identity_provider_import_config_post(client):
    """Test case for realm_identity_provider_import_config_post

    Import identity provider from uploaded JSON file
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/identity-provider/import-config'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_identity_provider_instances_alias_delete(client):
    """Test case for realm_identity_provider_instances_alias_delete

    Delete the identity provider
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/identity-provider/instances/{alias}'.format(realm='realm_example', alias='alias_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_identity_provider_instances_alias_export_get(client):
    """Test case for realm_identity_provider_instances_alias_export_get

    Export public broker configuration for identity provider
    """
    params = [('format', 'format_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/identity-provider/instances/{alias}/export'.format(realm='realm_example', alias='alias_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_identity_provider_instances_alias_get(client):
    """Test case for realm_identity_provider_instances_alias_get

    Get the identity provider
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/identity-provider/instances/{alias}'.format(realm='realm_example', alias='alias_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_identity_provider_instances_alias_management_permissions_get(client):
    """Test case for realm_identity_provider_instances_alias_management_permissions_get

    Return object stating whether client Authorization permissions have been initialized or not and a reference
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/identity-provider/instances/{alias}/management/permissions'.format(realm='realm_example', alias='alias_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_identity_provider_instances_alias_management_permissions_put(client):
    """Test case for realm_identity_provider_instances_alias_management_permissions_put

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
        path='/{realm}/identity-provider/instances/{alias}/management/permissions'.format(realm='realm_example', alias='alias_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_identity_provider_instances_alias_mapper_types_get(client):
    """Test case for realm_identity_provider_instances_alias_mapper_types_get

    Get mapper types for identity provider
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/identity-provider/instances/{alias}/mapper-types'.format(realm='realm_example', alias='alias_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_identity_provider_instances_alias_mappers_get(client):
    """Test case for realm_identity_provider_instances_alias_mappers_get

    Get mappers for identity provider
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/identity-provider/instances/{alias}/mappers'.format(realm='realm_example', alias='alias_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_identity_provider_instances_alias_mappers_id_delete(client):
    """Test case for realm_identity_provider_instances_alias_mappers_id_delete

    Delete a mapper for the identity provider
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/{realm}/identity-provider/instances/{alias}/mappers/{id}'.format(realm='realm_example', alias='alias_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_identity_provider_instances_alias_mappers_id_get(client):
    """Test case for realm_identity_provider_instances_alias_mappers_id_get

    Get mapper by id for the identity provider
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/identity-provider/instances/{alias}/mappers/{id}'.format(realm='realm_example', alias='alias_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_identity_provider_instances_alias_mappers_id_put(client):
    """Test case for realm_identity_provider_instances_alias_mappers_id_put

    Update a mapper for the identity provider
    """
    body = {"identityProviderAlias":"identityProviderAlias","name":"name","id":"id","config":{"key":""},"identityProviderMapper":"identityProviderMapper"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/identity-provider/instances/{alias}/mappers/{id}'.format(realm='realm_example', alias='alias_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_identity_provider_instances_alias_mappers_post(client):
    """Test case for realm_identity_provider_instances_alias_mappers_post

    Add a mapper to identity provider
    """
    body = {"identityProviderAlias":"identityProviderAlias","name":"name","id":"id","config":{"key":""},"identityProviderMapper":"identityProviderMapper"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/identity-provider/instances/{alias}/mappers'.format(realm='realm_example', alias='alias_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_identity_provider_instances_alias_put(client):
    """Test case for realm_identity_provider_instances_alias_put

    Update the identity provider
    """
    body = {"firstBrokerLoginFlowAlias":"firstBrokerLoginFlowAlias","internalId":"internalId","addReadTokenRoleOnCreate":True,"displayName":"displayName","providerId":"providerId","postBrokerLoginFlowAlias":"postBrokerLoginFlowAlias","alias":"alias","trustEmail":True,"config":{"key":""},"linkOnly":True,"enabled":True,"storeToken":True}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/{realm}/identity-provider/instances/{alias}'.format(realm='realm_example', alias='alias_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_identity_provider_instances_get(client):
    """Test case for realm_identity_provider_instances_get

    Get identity providers
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/identity-provider/instances'.format(realm='realm_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_identity_provider_instances_post(client):
    """Test case for realm_identity_provider_instances_post

    Create a new identity provider
    """
    body = {"firstBrokerLoginFlowAlias":"firstBrokerLoginFlowAlias","internalId":"internalId","addReadTokenRoleOnCreate":True,"displayName":"displayName","providerId":"providerId","postBrokerLoginFlowAlias":"postBrokerLoginFlowAlias","alias":"alias","trustEmail":True,"config":{"key":""},"linkOnly":True,"enabled":True,"storeToken":True}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/{realm}/identity-provider/instances'.format(realm='realm_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_realm_identity_provider_providers_provider_id_get(client):
    """Test case for realm_identity_provider_providers_provider_id_get

    Get identity providers
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{realm}/identity-provider/providers/{provider_id}'.format(realm='realm_example', provider_id='provider_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

