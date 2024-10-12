# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.access_policy_response import AccessPolicyResponse
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.factory import Factory
from openapi_server.models.factory_list_response import FactoryListResponse
from openapi_server.models.factory_repo_update import FactoryRepoUpdate
from openapi_server.models.factory_update_parameters import FactoryUpdateParameters
from openapi_server.models.git_hub_access_token_request import GitHubAccessTokenRequest
from openapi_server.models.git_hub_access_token_response import GitHubAccessTokenResponse
from openapi_server.models.user_access_policy import UserAccessPolicy


pytestmark = pytest.mark.asyncio

async def test_factories_configure_factory_repo(client):
    """Test case for factories_configure_factory_repo

    
    """
    factory_repo_update = {"repoConfiguration":{"accountName":"accountName","collaborationBranch":"collaborationBranch","lastCommitId":"lastCommitId","rootFolder":"rootFolder","repositoryName":"repositoryName","type":"type"},"factoryResourceId":"factoryResourceId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DataFactory/locations/{location_id}/configureFactoryRepo'.format(subscription_id='subscription_id_example', location_id='location_id_example'),
        headers=headers,
        json=factory_repo_update,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_factories_create_or_update(client):
    """Test case for factories_create_or_update

    
    """
    factory = {"identity":{"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","principalId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","type":"SystemAssigned"},"properties":{"createTime":"2000-01-23T04:56:07.000+00:00","repoConfiguration":{"accountName":"accountName","collaborationBranch":"collaborationBranch","lastCommitId":"lastCommitId","rootFolder":"rootFolder","repositoryName":"repositoryName","type":"type"},"provisioningState":"provisioningState","version":"version"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example'),
        headers=headers,
        json=factory,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_factories_delete(client):
    """Test case for factories_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_factories_get(client):
    """Test case for factories_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_none_match': 'if_none_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_factories_get_data_plane_access(client):
    """Test case for factories_get_data_plane_access

    
    """
    policy = {"profileName":"profileName","expireTime":"expireTime","permissions":"permissions","accessResourcePath":"accessResourcePath","startTime":"startTime"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/getDataPlaneAccess'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example'),
        headers=headers,
        json=policy,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_factories_get_git_hub_access_token(client):
    """Test case for factories_get_git_hub_access_token

    
    """
    git_hub_access_token_request = {"gitHubClientId":"gitHubClientId","gitHubAccessCode":"gitHubAccessCode","gitHubAccessTokenBaseUrl":"gitHubAccessTokenBaseUrl"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}/getGitHubAccessToken'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example'),
        headers=headers,
        json=git_hub_access_token_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_factories_list(client):
    """Test case for factories_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DataFactory/factories'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_factories_list_by_resource_group(client):
    """Test case for factories_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_factories_update(client):
    """Test case for factories_update

    
    """
    factory_update_parameters = {"identity":{"tenantId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","principalId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","type":"SystemAssigned"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.DataFactory/factories/{factory_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', factory_name='factory_name_example'),
        headers=headers,
        json=factory_update_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

