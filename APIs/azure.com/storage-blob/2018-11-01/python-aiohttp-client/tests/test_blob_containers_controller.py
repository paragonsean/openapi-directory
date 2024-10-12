# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.blob_container import BlobContainer
from openapi_server.models.immutability_policy import ImmutabilityPolicy
from openapi_server.models.lease_container_request import LeaseContainerRequest
from openapi_server.models.lease_container_response import LeaseContainerResponse
from openapi_server.models.legal_hold import LegalHold
from openapi_server.models.list_container_items import ListContainerItems


pytestmark = pytest.mark.asyncio

async def test_blob_containers_clear_legal_hold(client):
    """Test case for blob_containers_clear_legal_hold

    
    """
    legal_hold = {"hasLegalHold":True,"tags":["tags","tags"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/blobServices/default/containers/{container_name}/clearLegalHold'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', container_name='container_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=legal_hold,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blob_containers_create(client):
    """Test case for blob_containers_create

    
    """
    blob_container = {"properties":{"metadata":{"key":"metadata"},"hasImmutabilityPolicy":True,"lastModifiedTime":"2000-01-23T04:56:07.000+00:00","publicAccess":"Container","legalHold":{"hasLegalHold":True,"tags":[{"upn":"upn","tenantId":"tenantId","objectIdentifier":"objectIdentifier","tag":"tag","timestamp":"2000-01-23T04:56:07.000+00:00"},{"upn":"upn","tenantId":"tenantId","objectIdentifier":"objectIdentifier","tag":"tag","timestamp":"2000-01-23T04:56:07.000+00:00"}]},"hasLegalHold":True,"leaseState":"Available","immutabilityPolicy":{"etag":"etag","properties":{"immutabilityPeriodSinceCreationInDays":0,"state":"Locked"},"updateHistory":[{"upn":"upn","immutabilityPeriodSinceCreationInDays":6,"tenantId":"tenantId","update":"put","objectIdentifier":"objectIdentifier","timestamp":"2000-01-23T04:56:07.000+00:00"},{"upn":"upn","immutabilityPeriodSinceCreationInDays":6,"tenantId":"tenantId","update":"put","objectIdentifier":"objectIdentifier","timestamp":"2000-01-23T04:56:07.000+00:00"}]},"leaseStatus":"Locked","leaseDuration":"Infinite"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/blobServices/default/containers/{container_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', container_name='container_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=blob_container,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blob_containers_create_or_update_immutability_policy(client):
    """Test case for blob_containers_create_or_update_immutability_policy

    
    """
    parameters = {"properties":{"immutabilityPeriodSinceCreationInDays":0,"state":"Locked"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/blobServices/default/containers/{container_name}/immutabilityPolicies/{immutability_policy_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', container_name='container_name_example', immutability_policy_name='immutability_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blob_containers_delete(client):
    """Test case for blob_containers_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/blobServices/default/containers/{container_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', container_name='container_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blob_containers_delete_immutability_policy(client):
    """Test case for blob_containers_delete_immutability_policy

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/blobServices/default/containers/{container_name}/immutabilityPolicies/{immutability_policy_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', container_name='container_name_example', immutability_policy_name='immutability_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blob_containers_extend_immutability_policy(client):
    """Test case for blob_containers_extend_immutability_policy

    
    """
    parameters = {"properties":{"immutabilityPeriodSinceCreationInDays":0,"state":"Locked"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/blobServices/default/containers/{container_name}/immutabilityPolicies/default/extend'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', container_name='container_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blob_containers_get(client):
    """Test case for blob_containers_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/blobServices/default/containers/{container_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', container_name='container_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blob_containers_get_immutability_policy(client):
    """Test case for blob_containers_get_immutability_policy

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/blobServices/default/containers/{container_name}/immutabilityPolicies/{immutability_policy_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', container_name='container_name_example', immutability_policy_name='immutability_policy_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blob_containers_lease(client):
    """Test case for blob_containers_lease

    
    """
    parameters = {"leaseId":"leaseId","breakPeriod":0,"action":"Acquire","proposedLeaseId":"proposedLeaseId","leaseDuration":6}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/blobServices/default/containers/{container_name}/lease'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', container_name='container_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blob_containers_list(client):
    """Test case for blob_containers_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/blobServices/default/containers'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blob_containers_lock_immutability_policy(client):
    """Test case for blob_containers_lock_immutability_policy

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/blobServices/default/containers/{container_name}/immutabilityPolicies/default/lock'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', container_name='container_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blob_containers_set_legal_hold(client):
    """Test case for blob_containers_set_legal_hold

    
    """
    legal_hold = {"hasLegalHold":True,"tags":["tags","tags"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/blobServices/default/containers/{container_name}/setLegalHold'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', container_name='container_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=legal_hold,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_blob_containers_update(client):
    """Test case for blob_containers_update

    
    """
    blob_container = {"properties":{"metadata":{"key":"metadata"},"hasImmutabilityPolicy":True,"lastModifiedTime":"2000-01-23T04:56:07.000+00:00","publicAccess":"Container","legalHold":{"hasLegalHold":True,"tags":[{"upn":"upn","tenantId":"tenantId","objectIdentifier":"objectIdentifier","tag":"tag","timestamp":"2000-01-23T04:56:07.000+00:00"},{"upn":"upn","tenantId":"tenantId","objectIdentifier":"objectIdentifier","tag":"tag","timestamp":"2000-01-23T04:56:07.000+00:00"}]},"hasLegalHold":True,"leaseState":"Available","immutabilityPolicy":{"etag":"etag","properties":{"immutabilityPeriodSinceCreationInDays":0,"state":"Locked"},"updateHistory":[{"upn":"upn","immutabilityPeriodSinceCreationInDays":6,"tenantId":"tenantId","update":"put","objectIdentifier":"objectIdentifier","timestamp":"2000-01-23T04:56:07.000+00:00"},{"upn":"upn","immutabilityPeriodSinceCreationInDays":6,"tenantId":"tenantId","update":"put","objectIdentifier":"objectIdentifier","timestamp":"2000-01-23T04:56:07.000+00:00"}]},"leaseStatus":"Locked","leaseDuration":"Infinite"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Storage/storageAccounts/{account_name}/blobServices/default/containers/{container_name}'.format(resource_group_name='resource_group_name_example', account_name='account_name_example', container_name='container_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=blob_container,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

