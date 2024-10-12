# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.encrypt_request import EncryptRequest
from openapi_server.models.error import Error
from openapi_server.models.project import Project
from openapi_server.models.project_addition import ProjectAddition
from openapi_server.models.project_build_number_update import ProjectBuildNumberUpdate
from openapi_server.models.project_build_results import ProjectBuildResults
from openapi_server.models.project_deployments_results import ProjectDeploymentsResults
from openapi_server.models.project_history import ProjectHistory
from openapi_server.models.project_settings_results import ProjectSettingsResults
from openapi_server.models.project_with_configuration import ProjectWithConfiguration
from openapi_server.models.stored_name_value import StoredNameValue


pytestmark = pytest.mark.asyncio

async def test_add_project(client):
    """Test case for add_project

    Add project
    """
    body = {"repositoryName":"FeodorFitsner/demo-app","repositoryProvider":"gitHub"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/projects',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_project(client):
    """Test case for delete_project

    Delete project
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/projects/{account_name}/{project_slug}'.format(account_name='account_name_example', project_slug='project_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_project_build_cache(client):
    """Test case for delete_project_build_cache

    Delete project build cache
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/projects/{account_name}/{project_slug}/buildcache'.format(account_name='account_name_example', project_slug='project_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_encrypt_value(client):
    """Test case for encrypt_value

    Encrypt a value for use in StoredValue.
    """
    body = {"plainValue":"encryptme"}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/account/encrypt',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_artifact(client):
    """Test case for get_project_artifact

    Get last successful build artifact
    """
    params = [('branch', 'branch_example'),
                    ('tag', 'tag_example'),
                    ('job', 'job_example'),
                    ('all', False),
                    ('pr', True)]
    headers = { 
        'Accept': 'application/octet-stream',
    }
    response = await client.request(
        method='GET',
        path='/api/projects/{account_name}/{project_slug}/artifacts/{artifact_file_name}'.format(account_name='account_name_example', project_slug='project_slug_example', artifact_file_name='artifact_file_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_branch_status_badge(client):
    """Test case for get_project_branch_status_badge

    Get project branch status badge image
    """
    params = [('svg', False),
                    ('retina', False),
                    ('passingText', 'passing_text_example'),
                    ('failingText', 'failing_text_example'),
                    ('pendingText', 'pending_text_example')]
    headers = { 
        'Accept': 'image/png',
    }
    response = await client.request(
        method='GET',
        path='/api/projects/status/{status_badge_id}/branch/{build_branch}'.format(status_badge_id='status_badge_id_example', build_branch='build_branch_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_build_by_version(client):
    """Test case for get_project_build_by_version

    Get project build by version
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/projects/{account_name}/{project_slug}/build/{build_version}'.format(account_name='account_name_example', project_slug='project_slug_example', build_version='build_version_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_deployments(client):
    """Test case for get_project_deployments

    Get project deployments
    """
    params = [('recordsNumber', 56)]
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/projects/{account_name}/{project_slug}/deployments'.format(account_name='account_name_example', project_slug='project_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_environment_variables(client):
    """Test case for get_project_environment_variables

    Get project environment variables
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/projects/{account_name}/{project_slug}/settings/environment-variables'.format(account_name='account_name_example', project_slug='project_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_history(client):
    """Test case for get_project_history

    Get project history
    """
    params = [('recordsNumber', 56),
                    ('startBuildId', 56),
                    ('branch', 'branch_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/projects/{account_name}/{project_slug}/history'.format(account_name='account_name_example', project_slug='project_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_last_build(client):
    """Test case for get_project_last_build

    Get project last build
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/projects/{account_name}/{project_slug}'.format(account_name='account_name_example', project_slug='project_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_last_build_branch(client):
    """Test case for get_project_last_build_branch

    Get project last branch build
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/projects/{account_name}/{project_slug}/branch/{build_branch}'.format(account_name='account_name_example', project_slug='project_slug_example', build_branch='build_branch_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_settings(client):
    """Test case for get_project_settings

    Get project settings
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/projects/{account_name}/{project_slug}/settings'.format(account_name='account_name_example', project_slug='project_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_settings_yaml(client):
    """Test case for get_project_settings_yaml

    Get project settings in YAML
    """
    headers = { 
        'Accept': 'text/plain',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/projects/{account_name}/{project_slug}/settings/yaml'.format(account_name='account_name_example', project_slug='project_slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_status_badge(client):
    """Test case for get_project_status_badge

    Get project status badge image
    """
    params = [('svg', False),
                    ('retina', False),
                    ('passingText', 'passing_text_example'),
                    ('failingText', 'failing_text_example'),
                    ('pendingText', 'pending_text_example')]
    headers = { 
        'Accept': 'image/png',
    }
    response = await client.request(
        method='GET',
        path='/api/projects/status/{status_badge_id}'.format(status_badge_id='status_badge_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_projects(client):
    """Test case for get_projects

    Get projects
    """
    headers = { 
        'Accept': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/projects',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_project_status_badge(client):
    """Test case for get_public_project_status_badge

    Get status badge image for a project with a public repository
    """
    params = [('branch', 'branch_example'),
                    ('svg', False),
                    ('retina', False),
                    ('passingText', 'passing_text_example'),
                    ('failingText', 'failing_text_example'),
                    ('pendingText', 'pending_text_example')]
    headers = { 
        'Accept': 'image/png',
    }
    response = await client.request(
        method='GET',
        path='/api/projects/status/{badge_repo_provider}/{repo_account_name}/{repo_slug}'.format(badge_repo_provider='badge_repo_provider_example', repo_account_name='repo_account_name_example', repo_slug='repo_slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_project(client):
    """Test case for update_project

    Update project
    """
    body = {"sshPublicKey":"sshPublicKey","securityDescriptor":{"accessRightDefinitions":[{"name":"Delete","description":"description"},{"name":"Delete","description":"description"}],"roleAces":[{"roleId":0,"name":"name","accessRights":[{"allowed":True},{"allowed":True}],"isAdmin":True},{"roleId":0,"name":"name","accessRights":[{"allowed":True},{"allowed":True}],"isAdmin":True}]},"nuGetFeed":{"accountId":0,"nuGetFeedId":5,"created":"2000-01-23T04:56:07.000+00:00","name":"name","isPrivateProject":True,"publishingEnabled":True,"id":"id","updated":"2000-01-23T04:56:07.000+00:00","projectId":0},"accountName":"accountName","configuration":{"buildCloud":[{"value":"value"},{"value":"value"}],"packageWebApplicationProjectsXCopy":True,"testCategoriesMatrix":[{"categories":[{"value":"value"},{"value":"value"}]},{"categories":[{"value":"value"},{"value":"value"}]}],"msBuildInParallel":True,"shallowClone":True,"assemblyInformationalVersionFormat":"assemblyInformationalVersionFormat","dotnetCsprojFileVersionFormat":"dotnetCsprojFileVersionFormat","onlyCommitsFiles":[{"value":"value"},{"value":"value"}],"operatingSystem":[{"value":"Previous Ubuntu"},{"value":"Previous Ubuntu"}],"assemblyVersionFormat":"assemblyVersionFormat","onBuildSuccessScripts":[{"language":"cmd","script":"script"},{"language":"cmd","script":"script"}],"branchesMode":"exclude","maxJobs":1,"hostsEntries":[{"ip":"ip","host":"host"},{"ip":"ip","host":"host"}],"packageWebApplicationProjects":True,"dotnetCsprojVersionFormat":"dotnetCsprojVersionFormat","forceHttpsClone":True,"patchDotnetCsproj":True,"installScripts":[{"language":"cmd","script":"script"},{"language":"cmd","script":"script"}],"artifacts":[{"path":"path","name":"name","type":"Auto"},{"path":"path","name":"name","type":"Auto"}],"testAssemblies":[{"value":"value"},{"value":"value"}],"afterBuildScripts":[{"language":"cmd","script":"script"},{"language":"cmd","script":"script"}],"matrixOnly":[{"variables":{"name":"name","value":{"isEncrypted":True,"value":"value"}}},{"variables":{"name":"name","value":{"isEncrypted":True,"value":"value"}}}],"matrixFastFinish":True,"dotnetCsprojAssemblyVersionFormat":"dotnetCsprojAssemblyVersionFormat","deployMode":"providers","stacks":[],"configureNuGetAccountSource":True,"configureNuGetProjectSource":True,"msBuildVerbosity":"quiet","dotnetCsprojPackageVersionFormat":"dotnetCsprojPackageVersionFormat","testCategoriesMode":"exclude","packageNuGetProjects":True,"assemblyFileVersionFormat":"assemblyFileVersionFormat","xamarinRegisterAndroidProduct":True,"beforePackageScripts":[{"language":"cmd","script":"script"},{"language":"cmd","script":"script"}],"cloneScripts":[{"language":"cmd","script":"script"},{"language":"cmd","script":"script"}],"dotnetCsprojInformationalVersionFormat":"dotnetCsprojInformationalVersionFormat","buildScripts":[{"language":"cmd","script":"script"},{"language":"cmd","script":"script"}],"notifications":[{"settings":{"template":"template","authToken":{"isEncrypted":True,"value":"value"},"channel":"channel","onBuildFailure":True,"onBuildStatusChanged":True,"addCustomRequestBody":True,"password":{"isEncrypted":True,"value":"value"},"serverUrl":"https://openapi-generator.tech","from":"from","subjectTemplate":"subjectTemplate","onBuildSuccess":True,"headers":[{"name":"name","value":{"isEncrypted":True,"value":"value"}},{"name":"name","value":{"isEncrypted":True,"value":"value"}}],"method":"GET","customRequestBody":"customRequestBody","room":"room","url":"https://openapi-generator.tech","$type":"Appveyor.Models.CampfireNotificationSettings, Appveyor.Models","customRequestBodyContentType":"customRequestBodyContentType","recipientsValue":"recipientsValue","headersValue":"headersValue","incomingWebhookUrl":"https://openapi-generator.tech","bodyTemplate":"bodyTemplate","recipients":[{"value":"value"},{"value":"value"}],"vsoAccount":"vsoAccount","account":"account","username":"username"},"provider":"Campfire"},{"settings":{"template":"template","authToken":{"isEncrypted":True,"value":"value"},"channel":"channel","onBuildFailure":True,"onBuildStatusChanged":True,"addCustomRequestBody":True,"password":{"isEncrypted":True,"value":"value"},"serverUrl":"https://openapi-generator.tech","from":"from","subjectTemplate":"subjectTemplate","onBuildSuccess":True,"headers":[{"name":"name","value":{"isEncrypted":True,"value":"value"}},{"name":"name","value":{"isEncrypted":True,"value":"value"}}],"method":"GET","customRequestBody":"customRequestBody","room":"room","url":"https://openapi-generator.tech","$type":"Appveyor.Models.CampfireNotificationSettings, Appveyor.Models","customRequestBodyContentType":"customRequestBodyContentType","recipientsValue":"recipientsValue","headersValue":"headersValue","incomingWebhookUrl":"https://openapi-generator.tech","bodyTemplate":"bodyTemplate","recipients":[{"value":"value"},{"value":"value"}],"vsoAccount":"vsoAccount","account":"account","username":"username"},"provider":"Campfire"}],"beforeBuildScripts":[{"language":"cmd","script":"script"},{"language":"cmd","script":"script"}],"dotnetCsprojFile":"dotnetCsprojFile","packageWebApplicationProjectsOctopus":True,"hotFixScripts":[{"language":"cmd","script":"script"},{"language":"cmd","script":"script"}],"packageWebApplicationProjectsBeanstalk":True,"configuration":[{"value":"value"},{"value":"value"}],"buildMode":"msbuild","assemblyInfoFile":"assemblyInfoFile","disableNuGetPublishOnPullRequests":True,"platform":[{"value":"ARM"},{"value":"ARM"}],"skipNonTags":True,"afterTestScripts":[{"language":"cmd","script":"script"},{"language":"cmd","script":"script"}],"afterDeployScripts":[{"language":"cmd","script":"script"},{"language":"cmd","script":"script"}],"deployScripts":[{"language":"cmd","script":"script"},{"language":"cmd","script":"script"}],"packageAspNetCoreProjects":True,"skipCommitsFiles":[{"value":"value"},{"value":"value"}],"msBuildProjectFileName":"msBuildProjectFileName","packageNuGetSymbols":True,"doNotIncrementBuildNumberOnPullRequests":True,"skipTags":True,"cloneFolder":"cloneFolder","initScripts":[{"language":"cmd","script":"script"},{"language":"cmd","script":"script"}],"packageDotnetConsoleProjects":True,"matrixExclude":[{"variables":{"name":"name","value":{"isEncrypted":True,"value":"value"}}},{"variables":{"name":"name","value":{"isEncrypted":True,"value":"value"}}}],"xamarinRegisterIosProduct":True,"matrixExcept":[{"variables":{"name":"name","value":{"isEncrypted":True,"value":"value"}}},{"variables":{"name":"name","value":{"isEncrypted":True,"value":"value"}}}],"onBuildErrorScripts":[{"language":"cmd","script":"script"},{"language":"cmd","script":"script"}],"beforeDeployScripts":[{"language":"cmd","script":"script"},{"language":"cmd","script":"script"}],"matrixAllowFailures":[{"variables":{"name":"name","value":{"isEncrypted":True,"value":"value"}}},{"variables":{"name":"name","value":{"isEncrypted":True,"value":"value"}}}],"onBuildFinishScripts":[{"language":"cmd","script":"script"},{"language":"cmd","script":"script"}],"beforeTestScripts":[{"language":"cmd","script":"script"},{"language":"cmd","script":"script"}],"services":[{"value":"iis"},{"value":"iis"}],"includeBranches":[{"value":"value"},{"value":"value"}],"patchAssemblyInfo":True,"cacheEntries":[{"value":"value"},{"value":"value"}],"includeNuGetReferences":True,"deployments":[{"onBranch":[{"value":"value"},{"value":"value"}],"provider":"Agent","providerSettings":[{"name":"name","value":{"isEncrypted":True,"value":"value"}},{"name":"name","value":{"isEncrypted":True,"value":"value"}}],"onEnvironmentVariables":[{"name":"name","value":{"isEncrypted":True,"value":"value"}},{"name":"name","value":{"isEncrypted":True,"value":"value"}}]},{"onBranch":[{"value":"value"},{"value":"value"}],"provider":"Agent","providerSettings":[{"name":"name","value":{"isEncrypted":True,"value":"value"}},{"name":"name","value":{"isEncrypted":True,"value":"value"}}],"onEnvironmentVariables":[{"name":"name","value":{"isEncrypted":True,"value":"value"}},{"name":"name","value":{"isEncrypted":True,"value":"value"}}]}],"environmentVariablesMatrix":[{"variables":{"name":"name","value":{"isEncrypted":True,"value":"value"}}},{"variables":{"name":"name","value":{"isEncrypted":True,"value":"value"}}}],"environmentVariables":[{"name":"name","value":{"isEncrypted":True,"value":"value"}},{"name":"name","value":{"isEncrypted":True,"value":"value"}}],"testCategories":[{"value":"value"},{"value":"value"}],"testMode":"auto","cloneDepth":1,"disableNuGetPublishForOctopusPackages":True,"excludeBranches":[{"value":"value"},{"value":"value"}],"testScripts":[{"language":"cmd","script":"script"},{"language":"cmd","script":"script"}],"skipBranchWithPullRequests":True,"packageAzureCloudServiceProjects":True},"statusBadgeId":"statusBadgeId","repositoryUsername":"repositoryUsername","enableSecureVariablesInPullRequestsFromSameRepo":True,"isPrivate":True,"enableDeploymentInPullRequests":True,"disablePullRequestWebhooks":True,"disablePushWebhooks":True,"nextBuildNumber":7,"alwaysBuildClosedPullRequests":True,"scheduleCrontabExpression":"scheduleCrontabExpression","builds":[{"committed":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","jobs":[{"compilationWarningsCount":0,"created":"2000-01-23T04:56:07.000+00:00","artifactsCount":0,"compilationErrorsCount":0,"finished":"2000-01-23T04:56:07.000+00:00","started":"2000-01-23T04:56:07.000+00:00","failedTestsCount":0,"passedTestsCount":0,"testsCount":0,"jobId":"jobId","allowFailure":True,"compilationMessagesCount":0,"name":"name","osType":"Ubuntu","messagesCount":0,"updated":"2000-01-23T04:56:07.000+00:00","status":"cancelled"},{"compilationWarningsCount":0,"created":"2000-01-23T04:56:07.000+00:00","artifactsCount":0,"compilationErrorsCount":0,"finished":"2000-01-23T04:56:07.000+00:00","started":"2000-01-23T04:56:07.000+00:00","failedTestsCount":0,"passedTestsCount":0,"testsCount":0,"jobId":"jobId","allowFailure":True,"compilationMessagesCount":0,"name":"name","osType":"Ubuntu","messagesCount":0,"updated":"2000-01-23T04:56:07.000+00:00","status":"cancelled"}],"authorUsername":"authorUsername","buildId":0,"finished":"2000-01-23T04:56:07.000+00:00","started":"2000-01-23T04:56:07.000+00:00","commitId":"commitId","message":"message","pullRequestId":1,"branch":"branch","version":"version","buildNumber":0,"isTag":True,"pullRequestName":"pullRequestName","authorName":"authorName","messages":[{"created":"2000-01-23T04:56:07.000+00:00","category":"information","message":"message"},{"created":"2000-01-23T04:56:07.000+00:00","category":"information","message":"message"}],"messageExtended":"messageExtended","committerName":"committerName","updated":"2000-01-23T04:56:07.000+00:00","projectId":0,"committerUsername":"committerUsername"},{"committed":"2000-01-23T04:56:07.000+00:00","created":"2000-01-23T04:56:07.000+00:00","jobs":[{"compilationWarningsCount":0,"created":"2000-01-23T04:56:07.000+00:00","artifactsCount":0,"compilationErrorsCount":0,"finished":"2000-01-23T04:56:07.000+00:00","started":"2000-01-23T04:56:07.000+00:00","failedTestsCount":0,"passedTestsCount":0,"testsCount":0,"jobId":"jobId","allowFailure":True,"compilationMessagesCount":0,"name":"name","osType":"Ubuntu","messagesCount":0,"updated":"2000-01-23T04:56:07.000+00:00","status":"cancelled"},{"compilationWarningsCount":0,"created":"2000-01-23T04:56:07.000+00:00","artifactsCount":0,"compilationErrorsCount":0,"finished":"2000-01-23T04:56:07.000+00:00","started":"2000-01-23T04:56:07.000+00:00","failedTestsCount":0,"passedTestsCount":0,"testsCount":0,"jobId":"jobId","allowFailure":True,"compilationMessagesCount":0,"name":"name","osType":"Ubuntu","messagesCount":0,"updated":"2000-01-23T04:56:07.000+00:00","status":"cancelled"}],"authorUsername":"authorUsername","buildId":0,"finished":"2000-01-23T04:56:07.000+00:00","started":"2000-01-23T04:56:07.000+00:00","commitId":"commitId","message":"message","pullRequestId":1,"branch":"branch","version":"version","buildNumber":0,"isTag":True,"pullRequestName":"pullRequestName","authorName":"authorName","messages":[{"created":"2000-01-23T04:56:07.000+00:00","category":"information","message":"message"},{"created":"2000-01-23T04:56:07.000+00:00","category":"information","message":"message"}],"messageExtended":"messageExtended","committerName":"committerName","updated":"2000-01-23T04:56:07.000+00:00","projectId":0,"committerUsername":"committerUsername"}],"repositoryScm":"git","versionFormat":"versionFormat","repositoryBranch":"repositoryBranch","slug":"slug","customYmlName":"customYmlName","saveBuildCacheInPullRequests":True,"webhookId":"webhookId","repositoryAuthentication":"credentials","created":"2000-01-23T04:56:07.000+00:00","rollingBuilds":True,"repositoryName":"repositoryName","webhookUrl":"https://openapi-generator.tech","tags":"tags","currentBuildId":0,"accountId":0,"enableSecureVariablesInPullRequests":True,"buildPriority":1,"rollingBuildsOnlyForPullRequests":True,"ignoreAppveyorYml":True,"name":"name","repositoryType":"bitBucket","rollingBuildsDoNotCancelRunningBuilds":True,"isGitHubApp":True,"projectId":0,"updated":"2000-01-23T04:56:07.000+00:00","skipBranchesWithoutAppveyorYml":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/projects',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_project_build_number(client):
    """Test case for update_project_build_number

    Update project build number
    """
    body = {"nextBuildNumber":35}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/projects/{account_name}/{project_slug}/settings/build-number'.format(account_name='account_name_example', project_slug='project_slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_project_environment_variables(client):
    """Test case for update_project_environment_variables

    Update project environment variables
    """
    body = {"name":"name","value":{"isEncrypted":True,"value":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/projects/{account_name}/{project_slug}/settings/environment-variables'.format(account_name='account_name_example', project_slug='project_slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_update_project_settings_yaml(client):
    """Test case for update_project_settings_yaml

    Update project settings in YAML
    """
    body = '/path/to/file'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'apiToken': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/projects/{account_name}/{project_slug}/settings/yaml'.format(account_name='account_name_example', project_slug='project_slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

