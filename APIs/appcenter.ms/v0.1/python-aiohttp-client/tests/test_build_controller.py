# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.branch_configurations_delete200_response import BranchConfigurationsDelete200Response
from openapi_server.models.branch_configurations_get200_response import BranchConfigurationsGet200Response
from openapi_server.models.branch_configurations_update_request import BranchConfigurationsUpdateRequest
from openapi_server.models.build_configurations_get200_response import BuildConfigurationsGet200Response
from openapi_server.models.builds_create_request import BuildsCreateRequest
from openapi_server.models.builds_distribute200_response import BuildsDistribute200Response
from openapi_server.models.builds_distribute_request import BuildsDistributeRequest
from openapi_server.models.builds_get_download_uri200_response import BuildsGetDownloadUri200Response
from openapi_server.models.builds_get_log200_response import BuildsGetLog200Response
from openapi_server.models.builds_get_status_by_app_id200_response import BuildsGetStatusByAppId200Response
from openapi_server.models.builds_list_branches200_response_inner import BuildsListBranches200ResponseInner
from openapi_server.models.builds_list_branches200_response_inner_last_build import BuildsListBranches200ResponseInnerLastBuild
from openapi_server.models.builds_list_branches_default_response import BuildsListBranchesDefaultResponse
from openapi_server.models.builds_list_toolset_projects200_response import BuildsListToolsetProjects200Response
from openapi_server.models.builds_list_toolsets200_response import BuildsListToolsets200Response
from openapi_server.models.builds_list_toolsets200_response_xamarin_inner import BuildsListToolsets200ResponseXamarinInner
from openapi_server.models.builds_list_toolsets200_response_xcode_inner import BuildsListToolsets200ResponseXcodeInner
from openapi_server.models.builds_update_request import BuildsUpdateRequest
from openapi_server.models.commits_list_by_sha_list200_response_inner import CommitsListByShaList200ResponseInner
from openapi_server.models.file_assets_create200_response import FileAssetsCreate200Response
from openapi_server.models.repositories_list200_response_inner import RepositoriesList200ResponseInner
from openapi_server.models.repository_configurations_create_or_update_request import RepositoryConfigurationsCreateOrUpdateRequest
from openapi_server.models.repository_configurations_list200_response_inner import RepositoryConfigurationsList200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_branch_configurations_create(client):
    """Test case for branch_configurations_create

    
    """
    body = openapi_server.BranchConfigurationsUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/branches/{branch}/config'.format(branch='branch_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_branch_configurations_delete(client):
    """Test case for branch_configurations_delete

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/branches/{branch}/config'.format(branch='branch_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_branch_configurations_get(client):
    """Test case for branch_configurations_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/branches/{branch}/config'.format(branch='branch_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_branch_configurations_update(client):
    """Test case for branch_configurations_update

    
    """
    body = openapi_server.BranchConfigurationsUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v0.1/apps/{owner_name}/{app_name}/branches/{branch}/config'.format(branch='branch_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_build_configurations_get(client):
    """Test case for build_configurations_get

    
    """
    params = [('format', yaml)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/branches/{branch}/export_config'.format(branch='branch_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_create(client):
    """Test case for builds_create

    
    """
    body = openapi_server.BuildsCreateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/branches/{branch}/builds'.format(branch='branch_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_distribute(client):
    """Test case for builds_distribute

    
    """
    body = openapi_server.BuildsDistributeRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/builds/{build_id}/distribute'.format(build_id=56, owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_get(client):
    """Test case for builds_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/builds/{build_id}'.format(build_id=56, owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_get_download_uri(client):
    """Test case for builds_get_download_uri

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/builds/{build_id}/downloads/{download_type}'.format(build_id=56, download_type='download_type_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_get_log(client):
    """Test case for builds_get_log

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/builds/{build_id}/logs'.format(build_id=56, owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_get_status_by_app_id(client):
    """Test case for builds_get_status_by_app_id

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/build_service_status'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_list_branches(client):
    """Test case for builds_list_branches

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/branches'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_list_by_branch(client):
    """Test case for builds_list_by_branch

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/branches/{branch}/builds'.format(branch='branch_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_list_toolset_projects(client):
    """Test case for builds_list_toolset_projects

    
    """
    params = [('os', 'os_example'),
                    ('platform', 'platform_example'),
                    ('maxSearchDepth', 56)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/branches/{branch}/toolset_projects'.format(branch='branch_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_list_toolsets(client):
    """Test case for builds_list_toolsets

    
    """
    params = [('tools', 'tools_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/toolsets'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_list_xamarin_sdk_bundles(client):
    """Test case for builds_list_xamarin_sdk_bundles

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/xamarin_sdk_bundles'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_list_xcode_versions(client):
    """Test case for builds_list_xcode_versions

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/xcode_versions'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_update(client):
    """Test case for builds_update

    
    """
    body = openapi_server.BuildsUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/apps/{owner_name}/{app_name}/builds/{build_id}'.format(build_id=56, owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_builds_webhook(client):
    """Test case for builds_webhook

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/public/hooks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_commits_list_by_sha_list(client):
    """Test case for commits_list_by_sha_list

    
    """
    params = [('hashes', ['hashes_example'])]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/commits/batch'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_assets_create(client):
    """Test case for file_assets_create

    
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/file_asset'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repositories_list(client):
    """Test case for repositories_list

    
    """
    params = [('vstsAccountName', 'vsts_account_name_example'),
                    ('vstsProjectId', 'vsts_project_id_example'),
                    ('service_connection_id', 'service_connection_id_example'),
                    ('form', 'form_example')]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/source_hosts/{source_host}/repositories'.format(source_host='source_host_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repository_configurations_create_or_update(client):
    """Test case for repository_configurations_create_or_update

    
    """
    body = openapi_server.RepositoryConfigurationsCreateOrUpdateRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/repo_config'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repository_configurations_delete(client):
    """Test case for repository_configurations_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/repo_config'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repository_configurations_list(client):
    """Test case for repository_configurations_list

    
    """
    params = [('includeInactive', True)]
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/repo_config'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

