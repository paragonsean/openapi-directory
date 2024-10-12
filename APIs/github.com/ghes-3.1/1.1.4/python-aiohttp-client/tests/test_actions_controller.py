# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.actions_create_or_update_org_secret_request import ActionsCreateOrUpdateOrgSecretRequest
from openapi_server.models.actions_create_or_update_repo_secret_request import ActionsCreateOrUpdateRepoSecretRequest
from openapi_server.models.actions_create_self_hosted_runner_group_for_org_request import ActionsCreateSelfHostedRunnerGroupForOrgRequest
from openapi_server.models.actions_create_workflow_dispatch_request import ActionsCreateWorkflowDispatchRequest
from openapi_server.models.actions_get_workflow_workflow_id_parameter import ActionsGetWorkflowWorkflowIdParameter
from openapi_server.models.actions_list_artifacts_for_repo200_response import ActionsListArtifactsForRepo200Response
from openapi_server.models.actions_list_jobs_for_workflow_run200_response import ActionsListJobsForWorkflowRun200Response
from openapi_server.models.actions_list_org_secrets200_response import ActionsListOrgSecrets200Response
from openapi_server.models.actions_list_repo_access_to_self_hosted_runner_group_in_org200_response import ActionsListRepoAccessToSelfHostedRunnerGroupInOrg200Response
from openapi_server.models.actions_list_repo_secrets200_response import ActionsListRepoSecrets200Response
from openapi_server.models.actions_list_repo_workflows200_response import ActionsListRepoWorkflows200Response
from openapi_server.models.actions_list_selected_repos_for_org_secret200_response import ActionsListSelectedReposForOrgSecret200Response
from openapi_server.models.actions_list_selected_repositories_enabled_github_actions_organization200_response import ActionsListSelectedRepositoriesEnabledGithubActionsOrganization200Response
from openapi_server.models.actions_list_self_hosted_runner_groups_for_org200_response import ActionsListSelfHostedRunnerGroupsForOrg200Response
from openapi_server.models.actions_list_self_hosted_runners_for_org200_response import ActionsListSelfHostedRunnersForOrg200Response
from openapi_server.models.actions_list_workflow_runs_for_repo200_response import ActionsListWorkflowRunsForRepo200Response
from openapi_server.models.actions_organization_permissions import ActionsOrganizationPermissions
from openapi_server.models.actions_public_key import ActionsPublicKey
from openapi_server.models.actions_repository_permissions import ActionsRepositoryPermissions
from openapi_server.models.actions_secret import ActionsSecret
from openapi_server.models.actions_set_github_actions_permissions_organization_request import ActionsSetGithubActionsPermissionsOrganizationRequest
from openapi_server.models.actions_set_github_actions_permissions_repository_request import ActionsSetGithubActionsPermissionsRepositoryRequest
from openapi_server.models.actions_set_repo_access_to_self_hosted_runner_group_in_org_request import ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest
from openapi_server.models.actions_set_selected_repos_for_org_secret_request import ActionsSetSelectedReposForOrgSecretRequest
from openapi_server.models.actions_set_selected_repositories_enabled_github_actions_organization_request import ActionsSetSelectedRepositoriesEnabledGithubActionsOrganizationRequest
from openapi_server.models.actions_update_self_hosted_runner_group_for_org_request import ActionsUpdateSelfHostedRunnerGroupForOrgRequest
from openapi_server.models.artifact import Artifact
from openapi_server.models.authentication_token import AuthenticationToken
from openapi_server.models.basic_error import BasicError
from openapi_server.models.enterprise_admin_list_self_hosted_runners_in_group_for_enterprise200_response import EnterpriseAdminListSelfHostedRunnersInGroupForEnterprise200Response
from openapi_server.models.enterprise_admin_set_self_hosted_runners_in_group_for_enterprise_request import EnterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest
from openapi_server.models.job import Job
from openapi_server.models.organization_actions_secret import OrganizationActionsSecret
from openapi_server.models.runner import Runner
from openapi_server.models.runner_application import RunnerApplication
from openapi_server.models.runner_groups_org import RunnerGroupsOrg
from openapi_server.models.selected_actions import SelectedActions
from openapi_server.models.workflow import Workflow
from openapi_server.models.workflow_run import WorkflowRun


pytestmark = pytest.mark.asyncio

async def test_actions_add_repo_access_to_self_hosted_runner_group_in_org(client):
    """Test case for actions_add_repo_access_to_self_hosted_runner_group_in_org

    Add repository access to a self-hosted runner group in an organization
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id}'.format(org='org_example', runner_group_id=56, repository_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_add_selected_repo_to_org_secret(client):
    """Test case for actions_add_selected_repo_to_org_secret

    Add selected repository to an organization secret
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}'.format(org='org_example', secret_name='secret_name_example', repository_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_add_self_hosted_runner_to_group_for_org(client):
    """Test case for actions_add_self_hosted_runner_to_group_for_org

    Add a self-hosted runner to a group for an organization
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id}'.format(org='org_example', runner_group_id=56, runner_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_cancel_workflow_run(client):
    """Test case for actions_cancel_workflow_run

    Cancel a workflow run
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/actions/runs/{run_id}/cancel'.format(owner='owner_example', repo='repo_example', run_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_create_or_update_org_secret(client):
    """Test case for actions_create_or_update_org_secret

    Create or update an organization secret
    """
    body = {"encrypted_value":"c2VjcmV0","key_id":"012345678912345678","selected_repository_ids":[1296269,1296280],"visibility":"selected"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/orgs/{org}/actions/secrets/{secret_name}'.format(org='org_example', secret_name='secret_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_create_or_update_repo_secret(client):
    """Test case for actions_create_or_update_repo_secret

    Create or update a repository secret
    """
    body = {"encrypted_value":"c2VjcmV0","key_id":"012345678912345678"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/actions/secrets/{secret_name}'.format(owner='owner_example', repo='repo_example', secret_name='secret_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_create_registration_token_for_org(client):
    """Test case for actions_create_registration_token_for_org

    Create a registration token for an organization
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/orgs/{org}/actions/runners/registration-token'.format(org='org_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_create_registration_token_for_repo(client):
    """Test case for actions_create_registration_token_for_repo

    Create a registration token for a repository
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/actions/runners/registration-token'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_create_remove_token_for_org(client):
    """Test case for actions_create_remove_token_for_org

    Create a remove token for an organization
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/orgs/{org}/actions/runners/remove-token'.format(org='org_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_create_remove_token_for_repo(client):
    """Test case for actions_create_remove_token_for_repo

    Create a remove token for a repository
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/actions/runners/remove-token'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_create_self_hosted_runner_group_for_org(client):
    """Test case for actions_create_self_hosted_runner_group_for_org

    Create a self-hosted runner group for an organization
    """
    body = {"name":"Expensive hardware runners","runners":[9,2],"selected_repository_ids":[32,91],"visibility":"selected"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/orgs/{org}/actions/runner-groups'.format(org='org_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_create_workflow_dispatch(client):
    """Test case for actions_create_workflow_dispatch

    Create a workflow dispatch event
    """
    body = {"inputs":{"home":"San Francisco, CA","name":"Mona the Octocat"},"ref":"topic-branch"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches'.format(owner='owner_example', repo='repo_example', workflow_id=openapi_server.ActionsGetWorkflowWorkflowIdParameter()),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_delete_artifact(client):
    """Test case for actions_delete_artifact

    Delete an artifact
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/actions/artifacts/{artifact_id}'.format(owner='owner_example', repo='repo_example', artifact_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_delete_org_secret(client):
    """Test case for actions_delete_org_secret

    Delete an organization secret
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/actions/secrets/{secret_name}'.format(org='org_example', secret_name='secret_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_delete_repo_secret(client):
    """Test case for actions_delete_repo_secret

    Delete a repository secret
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/actions/secrets/{secret_name}'.format(owner='owner_example', repo='repo_example', secret_name='secret_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_delete_self_hosted_runner_from_org(client):
    """Test case for actions_delete_self_hosted_runner_from_org

    Delete a self-hosted runner from an organization
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/actions/runners/{runner_id}'.format(org='org_example', runner_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_delete_self_hosted_runner_from_repo(client):
    """Test case for actions_delete_self_hosted_runner_from_repo

    Delete a self-hosted runner from a repository
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/actions/runners/{runner_id}'.format(owner='owner_example', repo='repo_example', runner_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_delete_self_hosted_runner_group_from_org(client):
    """Test case for actions_delete_self_hosted_runner_group_from_org

    Delete a self-hosted runner group from an organization
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/actions/runner-groups/{runner_group_id}'.format(org='org_example', runner_group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_delete_workflow_run(client):
    """Test case for actions_delete_workflow_run

    Delete a workflow run
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/actions/runs/{run_id}'.format(owner='owner_example', repo='repo_example', run_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_delete_workflow_run_logs(client):
    """Test case for actions_delete_workflow_run_logs

    Delete workflow run logs
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/actions/runs/{run_id}/logs'.format(owner='owner_example', repo='repo_example', run_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_disable_selected_repository_github_actions_organization(client):
    """Test case for actions_disable_selected_repository_github_actions_organization

    Disable a selected repository for GitHub Actions in an organization
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/actions/permissions/repositories/{repository_id}'.format(org='org_example', repository_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_disable_workflow(client):
    """Test case for actions_disable_workflow

    Disable a workflow
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/actions/workflows/{workflow_id}/disable'.format(owner='owner_example', repo='repo_example', workflow_id=openapi_server.ActionsGetWorkflowWorkflowIdParameter()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_download_artifact(client):
    """Test case for actions_download_artifact

    Download an artifact
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format}'.format(owner='owner_example', repo='repo_example', artifact_id=56, archive_format='archive_format_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_download_job_logs_for_workflow_run(client):
    """Test case for actions_download_job_logs_for_workflow_run

    Download job logs for a workflow run
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/jobs/{job_id}/logs'.format(owner='owner_example', repo='repo_example', job_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_download_workflow_run_logs(client):
    """Test case for actions_download_workflow_run_logs

    Download workflow run logs
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/runs/{run_id}/logs'.format(owner='owner_example', repo='repo_example', run_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_enable_selected_repository_github_actions_organization(client):
    """Test case for actions_enable_selected_repository_github_actions_organization

    Enable a selected repository for GitHub Actions in an organization
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/orgs/{org}/actions/permissions/repositories/{repository_id}'.format(org='org_example', repository_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_enable_workflow(client):
    """Test case for actions_enable_workflow

    Enable a workflow
    """
    headers = { 
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable'.format(owner='owner_example', repo='repo_example', workflow_id=openapi_server.ActionsGetWorkflowWorkflowIdParameter()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_get_allowed_actions_organization(client):
    """Test case for actions_get_allowed_actions_organization

    Get allowed actions for an organization
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/actions/permissions/selected-actions'.format(org='org_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_get_allowed_actions_repository(client):
    """Test case for actions_get_allowed_actions_repository

    Get allowed actions for a repository
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/permissions/selected-actions'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_get_artifact(client):
    """Test case for actions_get_artifact

    Get an artifact
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/artifacts/{artifact_id}'.format(owner='owner_example', repo='repo_example', artifact_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_get_github_actions_permissions_organization(client):
    """Test case for actions_get_github_actions_permissions_organization

    Get GitHub Actions permissions for an organization
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/actions/permissions'.format(org='org_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_get_github_actions_permissions_repository(client):
    """Test case for actions_get_github_actions_permissions_repository

    Get GitHub Actions permissions for a repository
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/permissions'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_get_job_for_workflow_run(client):
    """Test case for actions_get_job_for_workflow_run

    Get a job for a workflow run
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/jobs/{job_id}'.format(owner='owner_example', repo='repo_example', job_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_get_org_public_key(client):
    """Test case for actions_get_org_public_key

    Get an organization public key
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/actions/secrets/public-key'.format(org='org_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_get_org_secret(client):
    """Test case for actions_get_org_secret

    Get an organization secret
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/actions/secrets/{secret_name}'.format(org='org_example', secret_name='secret_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_get_repo_public_key(client):
    """Test case for actions_get_repo_public_key

    Get a repository public key
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/secrets/public-key'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_get_repo_secret(client):
    """Test case for actions_get_repo_secret

    Get a repository secret
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/secrets/{secret_name}'.format(owner='owner_example', repo='repo_example', secret_name='secret_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_get_self_hosted_runner_for_org(client):
    """Test case for actions_get_self_hosted_runner_for_org

    Get a self-hosted runner for an organization
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/actions/runners/{runner_id}'.format(org='org_example', runner_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_get_self_hosted_runner_for_repo(client):
    """Test case for actions_get_self_hosted_runner_for_repo

    Get a self-hosted runner for a repository
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/runners/{runner_id}'.format(owner='owner_example', repo='repo_example', runner_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_get_self_hosted_runner_group_for_org(client):
    """Test case for actions_get_self_hosted_runner_group_for_org

    Get a self-hosted runner group for an organization
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/actions/runner-groups/{runner_group_id}'.format(org='org_example', runner_group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_get_workflow(client):
    """Test case for actions_get_workflow

    Get a workflow
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/workflows/{workflow_id}'.format(owner='owner_example', repo='repo_example', workflow_id=openapi_server.ActionsGetWorkflowWorkflowIdParameter()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_get_workflow_run(client):
    """Test case for actions_get_workflow_run

    Get a workflow run
    """
    params = [('exclude_pull_requests', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/runs/{run_id}'.format(owner='owner_example', repo='repo_example', run_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_list_artifacts_for_repo(client):
    """Test case for actions_list_artifacts_for_repo

    List artifacts for a repository
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/artifacts'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_list_jobs_for_workflow_run(client):
    """Test case for actions_list_jobs_for_workflow_run

    List jobs for a workflow run
    """
    params = [('filter', latest),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/runs/{run_id}/jobs'.format(owner='owner_example', repo='repo_example', run_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_list_org_secrets(client):
    """Test case for actions_list_org_secrets

    List organization secrets
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/actions/secrets'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_list_repo_access_to_self_hosted_runner_group_in_org(client):
    """Test case for actions_list_repo_access_to_self_hosted_runner_group_in_org

    List repository access to a self-hosted runner group in an organization
    """
    params = [('page', 1),
                    ('per_page', 30)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories'.format(org='org_example', runner_group_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_list_repo_secrets(client):
    """Test case for actions_list_repo_secrets

    List repository secrets
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/secrets'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_list_repo_workflows(client):
    """Test case for actions_list_repo_workflows

    List repository workflows
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/workflows'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_list_runner_applications_for_org(client):
    """Test case for actions_list_runner_applications_for_org

    List runner applications for an organization
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/actions/runners/downloads'.format(org='org_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_list_runner_applications_for_repo(client):
    """Test case for actions_list_runner_applications_for_repo

    List runner applications for a repository
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/runners/downloads'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_list_selected_repos_for_org_secret(client):
    """Test case for actions_list_selected_repos_for_org_secret

    List selected repositories for an organization secret
    """
    params = [('page', 1),
                    ('per_page', 30)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/actions/secrets/{secret_name}/repositories'.format(org='org_example', secret_name='secret_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_list_selected_repositories_enabled_github_actions_organization(client):
    """Test case for actions_list_selected_repositories_enabled_github_actions_organization

    List selected repositories enabled for GitHub Actions in an organization
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/actions/permissions/repositories'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_list_self_hosted_runner_groups_for_org(client):
    """Test case for actions_list_self_hosted_runner_groups_for_org

    List self-hosted runner groups for an organization
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/actions/runner-groups'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_list_self_hosted_runners_for_org(client):
    """Test case for actions_list_self_hosted_runners_for_org

    List self-hosted runners for an organization
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/actions/runners'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_list_self_hosted_runners_for_repo(client):
    """Test case for actions_list_self_hosted_runners_for_repo

    List self-hosted runners for a repository
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/runners'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_list_self_hosted_runners_in_group_for_org(client):
    """Test case for actions_list_self_hosted_runners_in_group_for_org

    List self-hosted runners in a group for an organization
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/actions/runner-groups/{runner_group_id}/runners'.format(org='org_example', runner_group_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_list_workflow_run_artifacts(client):
    """Test case for actions_list_workflow_run_artifacts

    List workflow run artifacts
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts'.format(owner='owner_example', repo='repo_example', run_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_list_workflow_runs(client):
    """Test case for actions_list_workflow_runs

    List workflow runs
    """
    params = [('actor', 'actor_example'),
                    ('branch', 'branch_example'),
                    ('event', 'event_example'),
                    ('status', 'status_example'),
                    ('per_page', 30),
                    ('page', 1),
                    ('created', '2013-10-20T19:20:30+01:00'),
                    ('exclude_pull_requests', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs'.format(owner='owner_example', repo='repo_example', workflow_id=openapi_server.ActionsGetWorkflowWorkflowIdParameter()),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_list_workflow_runs_for_repo(client):
    """Test case for actions_list_workflow_runs_for_repo

    List workflow runs for a repository
    """
    params = [('actor', 'actor_example'),
                    ('branch', 'branch_example'),
                    ('event', 'event_example'),
                    ('status', 'status_example'),
                    ('per_page', 30),
                    ('page', 1),
                    ('created', '2013-10-20T19:20:30+01:00'),
                    ('exclude_pull_requests', False)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/actions/runs'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_re_run_workflow(client):
    """Test case for actions_re_run_workflow

    Re-run a workflow
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/repos/{owner}/{repo}/actions/runs/{run_id}/rerun'.format(owner='owner_example', repo='repo_example', run_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_remove_repo_access_to_self_hosted_runner_group_in_org(client):
    """Test case for actions_remove_repo_access_to_self_hosted_runner_group_in_org

    Remove repository access to a self-hosted runner group in an organization
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories/{repository_id}'.format(org='org_example', runner_group_id=56, repository_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_remove_selected_repo_from_org_secret(client):
    """Test case for actions_remove_selected_repo_from_org_secret

    Remove selected repository from an organization secret
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/actions/secrets/{secret_name}/repositories/{repository_id}'.format(org='org_example', secret_name='secret_name_example', repository_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_remove_self_hosted_runner_from_group_for_org(client):
    """Test case for actions_remove_self_hosted_runner_from_group_for_org

    Remove a self-hosted runner from a group for an organization
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/orgs/{org}/actions/runner-groups/{runner_group_id}/runners/{runner_id}'.format(org='org_example', runner_group_id=56, runner_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_set_allowed_actions_organization(client):
    """Test case for actions_set_allowed_actions_organization

    Set allowed actions for an organization
    """
    body = openapi_server.SelectedActions()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/orgs/{org}/actions/permissions/selected-actions'.format(org='org_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_set_allowed_actions_repository(client):
    """Test case for actions_set_allowed_actions_repository

    Set allowed actions for a repository
    """
    body = openapi_server.SelectedActions()
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/actions/permissions/selected-actions'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_set_github_actions_permissions_organization(client):
    """Test case for actions_set_github_actions_permissions_organization

    Set GitHub Actions permissions for an organization
    """
    body = {"allowed_actions":"selected","enabled_repositories":"all"}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/orgs/{org}/actions/permissions'.format(org='org_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_set_github_actions_permissions_repository(client):
    """Test case for actions_set_github_actions_permissions_repository

    Set GitHub Actions permissions for a repository
    """
    body = {"allowed_actions":"selected","enabled":true}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/actions/permissions'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_set_repo_access_to_self_hosted_runner_group_in_org(client):
    """Test case for actions_set_repo_access_to_self_hosted_runner_group_in_org

    Set repository access for a self-hosted runner group in an organization
    """
    body = {"selected_repository_ids":[32,91]}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories'.format(org='org_example', runner_group_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_set_selected_repos_for_org_secret(client):
    """Test case for actions_set_selected_repos_for_org_secret

    Set selected repositories for an organization secret
    """
    body = {"selected_repository_ids":[64780797]}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/orgs/{org}/actions/secrets/{secret_name}/repositories'.format(org='org_example', secret_name='secret_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_set_selected_repositories_enabled_github_actions_organization(client):
    """Test case for actions_set_selected_repositories_enabled_github_actions_organization

    Set selected repositories enabled for GitHub Actions in an organization
    """
    body = {"selected_repository_ids":[32,42]}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/orgs/{org}/actions/permissions/repositories'.format(org='org_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_set_self_hosted_runners_in_group_for_org(client):
    """Test case for actions_set_self_hosted_runners_in_group_for_org

    Set self-hosted runners in a group for an organization
    """
    body = {"runners":[9,2]}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/orgs/{org}/actions/runner-groups/{runner_group_id}/runners'.format(org='org_example', runner_group_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_actions_update_self_hosted_runner_group_for_org(client):
    """Test case for actions_update_self_hosted_runner_group_for_org

    Update a self-hosted runner group for an organization
    """
    body = {"name":"Expensive hardware runners","visibility":"selected"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/orgs/{org}/actions/runner-groups/{runner_group_id}'.format(org='org_example', runner_group_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

