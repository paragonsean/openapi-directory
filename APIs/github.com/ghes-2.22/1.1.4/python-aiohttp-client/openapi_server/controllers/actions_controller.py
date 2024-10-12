from typing import List, Dict
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
from openapi_server.models.actions_list_self_hosted_runner_groups_for_org200_response import ActionsListSelfHostedRunnerGroupsForOrg200Response
from openapi_server.models.actions_list_workflow_runs_for_repo200_response import ActionsListWorkflowRunsForRepo200Response
from openapi_server.models.actions_public_key import ActionsPublicKey
from openapi_server.models.actions_secret import ActionsSecret
from openapi_server.models.actions_set_repo_access_to_self_hosted_runner_group_in_org_request import ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest
from openapi_server.models.actions_set_selected_repos_for_org_secret_request import ActionsSetSelectedReposForOrgSecretRequest
from openapi_server.models.actions_update_self_hosted_runner_group_for_org_request import ActionsUpdateSelfHostedRunnerGroupForOrgRequest
from openapi_server.models.artifact import Artifact
from openapi_server.models.authentication_token import AuthenticationToken
from openapi_server.models.enterprise_admin_list_self_hosted_runners_in_group_for_enterprise200_response import EnterpriseAdminListSelfHostedRunnersInGroupForEnterprise200Response
from openapi_server.models.enterprise_admin_set_self_hosted_runners_in_group_for_enterprise_request import EnterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest
from openapi_server.models.job import Job
from openapi_server.models.organization_actions_secret import OrganizationActionsSecret
from openapi_server.models.runner_application import RunnerApplication
from openapi_server.models.runner_groups_org import RunnerGroupsOrg
from openapi_server.models.runner_no_labels import RunnerNoLabels
from openapi_server.models.workflow import Workflow
from openapi_server.models.workflow_run import WorkflowRun
from openapi_server import util


async def actions_add_repo_access_to_self_hosted_runner_group_in_org(request: web.Request, org, runner_group_id, repository_id) -> web.Response:
    """Add repository access to a self-hosted runner group in an organization

    Adds a repository to the list of selected repositories that can access a self-hosted runner group. The runner group must have &#x60;visibility&#x60; set to &#x60;selected&#x60;. For more information, see \&quot;[Create a self-hosted runner group for an organization](#create-a-self-hosted-runner-group-for-an-organization).\&quot; You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

    :param org: 
    :type org: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int
    :param repository_id: 
    :type repository_id: int

    """
    return web.Response(status=200)


async def actions_add_selected_repo_to_org_secret(request: web.Request, org, secret_name, repository_id) -> web.Response:
    """Add selected repository to an organization secret

    Adds a repository to an organization secret when the &#x60;visibility&#x60; for repository access is set to &#x60;selected&#x60;. The visibility is set when you [Create or update an organization secret](https://docs.github.com/enterprise-server@2.22/rest/reference/actions#create-or-update-an-organization-secret). You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; organization permission to use this endpoint.

    :param org: 
    :type org: str
    :param secret_name: secret_name parameter
    :type secret_name: str
    :param repository_id: 
    :type repository_id: int

    """
    return web.Response(status=200)


async def actions_add_self_hosted_runner_to_group_for_org(request: web.Request, org, runner_group_id, runner_id) -> web.Response:
    """Add a self-hosted runner to a group for an organization

    Adds a self-hosted runner to a runner group configured in an organization. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

    :param org: 
    :type org: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int
    :param runner_id: Unique identifier of the self-hosted runner.
    :type runner_id: int

    """
    return web.Response(status=200)


async def actions_cancel_workflow_run(request: web.Request, owner, repo, run_id) -> web.Response:
    """Cancel a workflow run

    Cancels a workflow run using its &#x60;id&#x60;. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;actions:write&#x60; permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param run_id: The id of the workflow run.
    :type run_id: int

    """
    return web.Response(status=200)


async def actions_create_or_update_org_secret(request: web.Request, org, secret_name, body) -> web.Response:
    """Create or update an organization secret

    Creates or updates an organization secret with an encrypted value. Encrypt your secret using [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; organization permission to use this endpoint.  #### Example encrypting a secret using Node.js  Encrypt your secret using the [tweetsodium](https://github.com/github/tweetsodium) library.  &#x60;&#x60;&#x60; const sodium &#x3D; require(&#39;tweetsodium&#39;);  const key &#x3D; \&quot;base64-encoded-public-key\&quot;; const value &#x3D; \&quot;plain-text-secret\&quot;;  // Convert the message and key to Uint8Array&#39;s (Buffer implements that interface) const messageBytes &#x3D; Buffer.from(value); const keyBytes &#x3D; Buffer.from(key, &#39;base64&#39;);  // Encrypt using LibSodium. const encryptedBytes &#x3D; sodium.seal(messageBytes, keyBytes);  // Base64 the encrypted secret const encrypted &#x3D; Buffer.from(encryptedBytes).toString(&#39;base64&#39;);  console.log(encrypted); &#x60;&#x60;&#x60;   #### Example encrypting a secret using Python  Encrypt your secret using [pynacl](https://pynacl.readthedocs.io/en/stable/public/#nacl-public-sealedbox) with Python 3.  &#x60;&#x60;&#x60; from base64 import b64encode from nacl import encoding, public  def encrypt(public_key: str, secret_value: str) -&gt; str:   \&quot;\&quot;\&quot;Encrypt a Unicode string using the public key.\&quot;\&quot;\&quot;   public_key &#x3D; public.PublicKey(public_key.encode(\&quot;utf-8\&quot;), encoding.Base64Encoder())   sealed_box &#x3D; public.SealedBox(public_key)   encrypted &#x3D; sealed_box.encrypt(secret_value.encode(\&quot;utf-8\&quot;))   return b64encode(encrypted).decode(\&quot;utf-8\&quot;) &#x60;&#x60;&#x60;  #### Example encrypting a secret using C#  Encrypt your secret using the [Sodium.Core](https://www.nuget.org/packages/Sodium.Core/) package.  &#x60;&#x60;&#x60; var secretValue &#x3D; System.Text.Encoding.UTF8.GetBytes(\&quot;mySecret\&quot;); var publicKey &#x3D; Convert.FromBase64String(\&quot;2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvvcCU&#x3D;\&quot;);  var sealedPublicKeyBox &#x3D; Sodium.SealedPublicKeyBox.Create(secretValue, publicKey);  Console.WriteLine(Convert.ToBase64String(sealedPublicKeyBox)); &#x60;&#x60;&#x60;  #### Example encrypting a secret using Ruby  Encrypt your secret using the [rbnacl](https://github.com/RubyCrypto/rbnacl) gem.  &#x60;&#x60;&#x60;ruby require \&quot;rbnacl\&quot; require \&quot;base64\&quot;  key &#x3D; Base64.decode64(\&quot;+ZYvJDZMHUfBkJdyq5Zm9SKqeuBQ4sj+6sfjlH4CgG0&#x3D;\&quot;) public_key &#x3D; RbNaCl::PublicKey.new(key)  box &#x3D; RbNaCl::Boxes::Sealed.from_public_key(public_key) encrypted_secret &#x3D; box.encrypt(\&quot;my_secret\&quot;)  # Print the base64 encoded secret puts Base64.strict_encode64(encrypted_secret) &#x60;&#x60;&#x60;

    :param org: 
    :type org: str
    :param secret_name: secret_name parameter
    :type secret_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = ActionsCreateOrUpdateOrgSecretRequest.from_dict(body)
    return web.Response(status=200)


async def actions_create_or_update_repo_secret(request: web.Request, owner, repo, secret_name, body) -> web.Response:
    """Create or update a repository secret

    Creates or updates a repository secret with an encrypted value. Encrypt your secret using [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; repository permission to use this endpoint.  #### Example encrypting a secret using Node.js  Encrypt your secret using the [tweetsodium](https://github.com/github/tweetsodium) library.  &#x60;&#x60;&#x60; const sodium &#x3D; require(&#39;tweetsodium&#39;);  const key &#x3D; \&quot;base64-encoded-public-key\&quot;; const value &#x3D; \&quot;plain-text-secret\&quot;;  // Convert the message and key to Uint8Array&#39;s (Buffer implements that interface) const messageBytes &#x3D; Buffer.from(value); const keyBytes &#x3D; Buffer.from(key, &#39;base64&#39;);  // Encrypt using LibSodium. const encryptedBytes &#x3D; sodium.seal(messageBytes, keyBytes);  // Base64 the encrypted secret const encrypted &#x3D; Buffer.from(encryptedBytes).toString(&#39;base64&#39;);  console.log(encrypted); &#x60;&#x60;&#x60;   #### Example encrypting a secret using Python  Encrypt your secret using [pynacl](https://pynacl.readthedocs.io/en/stable/public/#nacl-public-sealedbox) with Python 3.  &#x60;&#x60;&#x60; from base64 import b64encode from nacl import encoding, public  def encrypt(public_key: str, secret_value: str) -&gt; str:   \&quot;\&quot;\&quot;Encrypt a Unicode string using the public key.\&quot;\&quot;\&quot;   public_key &#x3D; public.PublicKey(public_key.encode(\&quot;utf-8\&quot;), encoding.Base64Encoder())   sealed_box &#x3D; public.SealedBox(public_key)   encrypted &#x3D; sealed_box.encrypt(secret_value.encode(\&quot;utf-8\&quot;))   return b64encode(encrypted).decode(\&quot;utf-8\&quot;) &#x60;&#x60;&#x60;  #### Example encrypting a secret using C#  Encrypt your secret using the [Sodium.Core](https://www.nuget.org/packages/Sodium.Core/) package.  &#x60;&#x60;&#x60; var secretValue &#x3D; System.Text.Encoding.UTF8.GetBytes(\&quot;mySecret\&quot;); var publicKey &#x3D; Convert.FromBase64String(\&quot;2Sg8iYjAxxmI2LvUXpJjkYrMxURPc8r+dB7TJyvvcCU&#x3D;\&quot;);  var sealedPublicKeyBox &#x3D; Sodium.SealedPublicKeyBox.Create(secretValue, publicKey);  Console.WriteLine(Convert.ToBase64String(sealedPublicKeyBox)); &#x60;&#x60;&#x60;  #### Example encrypting a secret using Ruby  Encrypt your secret using the [rbnacl](https://github.com/RubyCrypto/rbnacl) gem.  &#x60;&#x60;&#x60;ruby require \&quot;rbnacl\&quot; require \&quot;base64\&quot;  key &#x3D; Base64.decode64(\&quot;+ZYvJDZMHUfBkJdyq5Zm9SKqeuBQ4sj+6sfjlH4CgG0&#x3D;\&quot;) public_key &#x3D; RbNaCl::PublicKey.new(key)  box &#x3D; RbNaCl::Boxes::Sealed.from_public_key(public_key) encrypted_secret &#x3D; box.encrypt(\&quot;my_secret\&quot;)  # Print the base64 encoded secret puts Base64.strict_encode64(encrypted_secret) &#x60;&#x60;&#x60;

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param secret_name: secret_name parameter
    :type secret_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = ActionsCreateOrUpdateRepoSecretRequest.from_dict(body)
    return web.Response(status=200)


async def actions_create_registration_token_for_org(request: web.Request, org) -> web.Response:
    """Create a registration token for an organization

    Returns a token that you can pass to the &#x60;config&#x60; script. The token expires after one hour.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.  #### Example using registration token  Configure your self-hosted runner, replacing &#x60;TOKEN&#x60; with the registration token provided by this endpoint.  &#x60;&#x60;&#x60; ./config.sh --url https://github.com/octo-org --token TOKEN &#x60;&#x60;&#x60;

    :param org: 
    :type org: str

    """
    return web.Response(status=200)


async def actions_create_registration_token_for_repo(request: web.Request, owner, repo) -> web.Response:
    """Create a registration token for a repository

    Returns a token that you can pass to the &#x60;config&#x60; script. The token expires after one hour. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint.  #### Example using registration token   Configure your self-hosted runner, replacing &#x60;TOKEN&#x60; with the registration token provided by this endpoint.  &#x60;&#x60;&#x60; ./config.sh --url https://github.com/octo-org/octo-repo-artifacts --token TOKEN &#x60;&#x60;&#x60;

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def actions_create_remove_token_for_org(request: web.Request, org) -> web.Response:
    """Create a remove token for an organization

    Returns a token that you can pass to the &#x60;config&#x60; script to remove a self-hosted runner from an organization. The token expires after one hour.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.  #### Example using remove token  To remove your self-hosted runner from an organization, replace &#x60;TOKEN&#x60; with the remove token provided by this endpoint.  &#x60;&#x60;&#x60; ./config.sh remove --token TOKEN &#x60;&#x60;&#x60;

    :param org: 
    :type org: str

    """
    return web.Response(status=200)


async def actions_create_remove_token_for_repo(request: web.Request, owner, repo) -> web.Response:
    """Create a remove token for a repository

    Returns a token that you can pass to remove a self-hosted runner from a repository. The token expires after one hour. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint.  #### Example using remove token   To remove your self-hosted runner from a repository, replace TOKEN with the remove token provided by this endpoint.  &#x60;&#x60;&#x60; ./config.sh remove --token TOKEN &#x60;&#x60;&#x60;

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def actions_create_self_hosted_runner_group_for_org(request: web.Request, org, body) -> web.Response:
    """Create a self-hosted runner group for an organization

    The self-hosted runner groups REST API is available with GitHub Enterprise Cloud and GitHub Enterprise Server. For more information, see \&quot;[GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products).\&quot;  Creates a new self-hosted runner group for an organization.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

    :param org: 
    :type org: str
    :param body: 
    :type body: dict | bytes

    """
    body = ActionsCreateSelfHostedRunnerGroupForOrgRequest.from_dict(body)
    return web.Response(status=200)


async def actions_create_workflow_dispatch(request: web.Request, owner, repo, workflow_id, body) -> web.Response:
    """Create a workflow dispatch event

    You can use this endpoint to manually trigger a GitHub Actions workflow run. You can replace &#x60;workflow_id&#x60; with the workflow file name. For example, you could use &#x60;main.yaml&#x60;.  You must configure your GitHub Actions workflow to run when the [&#x60;workflow_dispatch&#x60; webhook](/developers/webhooks-and-events/webhook-events-and-payloads#workflow_dispatch) event occurs. The &#x60;inputs&#x60; are configured in the workflow file. For more information about how to configure the &#x60;workflow_dispatch&#x60; event in the workflow file, see \&quot;[Events that trigger workflows](/actions/reference/events-that-trigger-workflows#workflow_dispatch).\&quot;  You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;actions:write&#x60; permission to use this endpoint. For more information, see \&quot;[Creating a personal access token for the command line](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line).\&quot;

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param workflow_id: The ID of the workflow. You can also pass the workflow file name as a string.
    :type workflow_id: dict | bytes
    :param body: 
    :type body: dict | bytes

    """
    workflow_id = .from_dict(workflow_id)
    body = ActionsCreateWorkflowDispatchRequest.from_dict(body)
    return web.Response(status=200)


async def actions_delete_artifact(request: web.Request, owner, repo, artifact_id) -> web.Response:
    """Delete an artifact

    Deletes an artifact for a workflow run. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;actions:write&#x60; permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param artifact_id: artifact_id parameter
    :type artifact_id: int

    """
    return web.Response(status=200)


async def actions_delete_org_secret(request: web.Request, org, secret_name) -> web.Response:
    """Delete an organization secret

    Deletes a secret in an organization using the secret name. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; organization permission to use this endpoint.

    :param org: 
    :type org: str
    :param secret_name: secret_name parameter
    :type secret_name: str

    """
    return web.Response(status=200)


async def actions_delete_repo_secret(request: web.Request, owner, repo, secret_name) -> web.Response:
    """Delete a repository secret

    Deletes a secret in a repository using the secret name. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; repository permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param secret_name: secret_name parameter
    :type secret_name: str

    """
    return web.Response(status=200)


async def actions_delete_self_hosted_runner_from_org(request: web.Request, org, runner_id) -> web.Response:
    """Delete a self-hosted runner from an organization

    Forces the removal of a self-hosted runner from an organization. You can use this endpoint to completely remove the runner when the machine you were using no longer exists.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

    :param org: 
    :type org: str
    :param runner_id: Unique identifier of the self-hosted runner.
    :type runner_id: int

    """
    return web.Response(status=200)


async def actions_delete_self_hosted_runner_from_repo(request: web.Request, owner, repo, runner_id) -> web.Response:
    """Delete a self-hosted runner from a repository

    Forces the removal of a self-hosted runner from a repository. You can use this endpoint to completely remove the runner when the machine you were using no longer exists.  You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param runner_id: Unique identifier of the self-hosted runner.
    :type runner_id: int

    """
    return web.Response(status=200)


async def actions_delete_self_hosted_runner_group_from_org(request: web.Request, org, runner_group_id) -> web.Response:
    """Delete a self-hosted runner group from an organization

    Deletes a self-hosted runner group for an organization. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

    :param org: 
    :type org: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int

    """
    return web.Response(status=200)


async def actions_delete_workflow_run(request: web.Request, owner, repo, run_id) -> web.Response:
    """Delete a workflow run

    Delete a specific workflow run. Anyone with write access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:write&#x60; permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param run_id: The id of the workflow run.
    :type run_id: int

    """
    return web.Response(status=200)


async def actions_delete_workflow_run_logs(request: web.Request, owner, repo, run_id) -> web.Response:
    """Delete workflow run logs

    Deletes all logs for a workflow run. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;actions:write&#x60; permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param run_id: The id of the workflow run.
    :type run_id: int

    """
    return web.Response(status=200)


async def actions_download_artifact(request: web.Request, owner, repo, artifact_id, archive_format) -> web.Response:
    """Download an artifact

    Gets a redirect URL to download an archive for a repository. This URL expires after 1 minute. Look for &#x60;Location:&#x60; in the response header to find the URL for the download. The &#x60;:archive_format&#x60; must be &#x60;zip&#x60;. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param artifact_id: artifact_id parameter
    :type artifact_id: int
    :param archive_format: 
    :type archive_format: str

    """
    return web.Response(status=200)


async def actions_download_job_logs_for_workflow_run(request: web.Request, owner, repo, job_id) -> web.Response:
    """Download job logs for a workflow run

    Gets a redirect URL to download a plain text file of logs for a workflow job. This link expires after 1 minute. Look for &#x60;Location:&#x60; in the response header to find the URL for the download. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param job_id: job_id parameter
    :type job_id: int

    """
    return web.Response(status=200)


async def actions_download_workflow_run_logs(request: web.Request, owner, repo, run_id) -> web.Response:
    """Download workflow run logs

    Gets a redirect URL to download an archive of log files for a workflow run. This link expires after 1 minute. Look for &#x60;Location:&#x60; in the response header to find the URL for the download. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param run_id: The id of the workflow run.
    :type run_id: int

    """
    return web.Response(status=200)


async def actions_get_artifact(request: web.Request, owner, repo, artifact_id) -> web.Response:
    """Get an artifact

    Gets a specific artifact for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param artifact_id: artifact_id parameter
    :type artifact_id: int

    """
    return web.Response(status=200)


async def actions_get_job_for_workflow_run(request: web.Request, owner, repo, job_id) -> web.Response:
    """Get a job for a workflow run

    Gets a specific job in a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param job_id: job_id parameter
    :type job_id: int

    """
    return web.Response(status=200)


async def actions_get_org_public_key(request: web.Request, org) -> web.Response:
    """Get an organization public key

    Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; organization permission to use this endpoint.

    :param org: 
    :type org: str

    """
    return web.Response(status=200)


async def actions_get_org_secret(request: web.Request, org, secret_name) -> web.Response:
    """Get an organization secret

    Gets a single organization secret without revealing its encrypted value. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; organization permission to use this endpoint.

    :param org: 
    :type org: str
    :param secret_name: secret_name parameter
    :type secret_name: str

    """
    return web.Response(status=200)


async def actions_get_repo_public_key(request: web.Request, owner, repo) -> web.Response:
    """Get a repository public key

    Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;secrets&#x60; repository permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def actions_get_repo_secret(request: web.Request, owner, repo, secret_name) -> web.Response:
    """Get a repository secret

    Gets a single repository secret without revealing its encrypted value. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; repository permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param secret_name: secret_name parameter
    :type secret_name: str

    """
    return web.Response(status=200)


async def actions_get_self_hosted_runner_for_org(request: web.Request, org, runner_id) -> web.Response:
    """Get a self-hosted runner for an organization

    Gets a specific self-hosted runner configured in an organization.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

    :param org: 
    :type org: str
    :param runner_id: Unique identifier of the self-hosted runner.
    :type runner_id: int

    """
    return web.Response(status=200)


async def actions_get_self_hosted_runner_for_repo(request: web.Request, owner, repo, runner_id) -> web.Response:
    """Get a self-hosted runner for a repository

    Gets a specific self-hosted runner configured in a repository.  You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param runner_id: Unique identifier of the self-hosted runner.
    :type runner_id: int

    """
    return web.Response(status=200)


async def actions_get_self_hosted_runner_group_for_org(request: web.Request, org, runner_group_id) -> web.Response:
    """Get a self-hosted runner group for an organization

    Gets a specific self-hosted runner group for an organization. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

    :param org: 
    :type org: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int

    """
    return web.Response(status=200)


async def actions_get_workflow(request: web.Request, owner, repo, workflow_id) -> web.Response:
    """Get a workflow

    Gets a specific workflow. You can replace &#x60;workflow_id&#x60; with the workflow file name. For example, you could use &#x60;main.yaml&#x60;. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param workflow_id: The ID of the workflow. You can also pass the workflow file name as a string.
    :type workflow_id: dict | bytes

    """
    workflow_id = .from_dict(workflow_id)
    return web.Response(status=200)


async def actions_get_workflow_run(request: web.Request, owner, repo, run_id, exclude_pull_requests=None) -> web.Response:
    """Get a workflow run

    Gets a specific workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param run_id: The id of the workflow run.
    :type run_id: int
    :param exclude_pull_requests: If &#x60;true&#x60; pull requests are omitted from the response (empty array).
    :type exclude_pull_requests: bool

    """
    return web.Response(status=200)


async def actions_list_artifacts_for_repo(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List artifacts for a repository

    Lists all artifacts for a repository. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def actions_list_jobs_for_workflow_run(request: web.Request, owner, repo, run_id, filter=None, per_page=None, page=None) -> web.Response:
    """List jobs for a workflow run

    Lists jobs for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#parameters).

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param run_id: The id of the workflow run.
    :type run_id: int
    :param filter: Filters jobs by their &#x60;completed_at&#x60; timestamp. Can be one of:   \\* &#x60;latest&#x60;: Returns jobs from the most recent execution of the workflow run.   \\* &#x60;all&#x60;: Returns all jobs for a workflow run, including from old executions of the workflow run.
    :type filter: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def actions_list_org_secrets(request: web.Request, org, per_page=None, page=None) -> web.Response:
    """List organization secrets

    Lists all secrets available in an organization without revealing their encrypted values. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; organization permission to use this endpoint.

    :param org: 
    :type org: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def actions_list_repo_access_to_self_hosted_runner_group_in_org(request: web.Request, org, runner_group_id, page=None, per_page=None) -> web.Response:
    """List repository access to a self-hosted runner group in an organization

    The self-hosted runner groups REST API is available with GitHub Enterprise Cloud and GitHub Enterprise Server. For more information, see \&quot;[GitHub&#39;s products](https://docs.github.com/github/getting-started-with-github/githubs-products).\&quot;  Lists the repositories with access to a self-hosted runner group configured in an organization.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

    :param org: 
    :type org: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int
    :param page: Page number of the results to fetch.
    :type page: int
    :param per_page: Results per page (max 100)
    :type per_page: int

    """
    return web.Response(status=200)


async def actions_list_repo_secrets(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List repository secrets

    Lists all secrets available in a repository without revealing their encrypted values. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; repository permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def actions_list_repo_workflows(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List repository workflows

    Lists the workflows in a repository. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def actions_list_runner_applications_for_org(request: web.Request, org) -> web.Response:
    """List runner applications for an organization

    Lists binaries for the runner application that you can download and run.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

    :param org: 
    :type org: str

    """
    return web.Response(status=200)


async def actions_list_runner_applications_for_repo(request: web.Request, owner, repo) -> web.Response:
    """List runner applications for a repository

    Lists binaries for the runner application that you can download and run.  You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str

    """
    return web.Response(status=200)


async def actions_list_selected_repos_for_org_secret(request: web.Request, org, secret_name, page=None, per_page=None) -> web.Response:
    """List selected repositories for an organization secret

    Lists all repositories that have been selected when the &#x60;visibility&#x60; for repository access to a secret is set to &#x60;selected&#x60;. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; organization permission to use this endpoint.

    :param org: 
    :type org: str
    :param secret_name: secret_name parameter
    :type secret_name: str
    :param page: Page number of the results to fetch.
    :type page: int
    :param per_page: Results per page (max 100)
    :type per_page: int

    """
    return web.Response(status=200)


async def actions_list_self_hosted_runner_groups_for_org(request: web.Request, org, per_page=None, page=None) -> web.Response:
    """List self-hosted runner groups for an organization

    Lists all self-hosted runner groups configured in an organization and inherited from an enterprise. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

    :param org: 
    :type org: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def actions_list_self_hosted_runners_for_org(request: web.Request, org, per_page=None, page=None) -> web.Response:
    """List self-hosted runners for an organization

    Lists all self-hosted runners configured in an organization.  You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

    :param org: 
    :type org: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def actions_list_self_hosted_runners_for_repo(request: web.Request, owner, repo, per_page=None, page=None) -> web.Response:
    """List self-hosted runners for a repository

    Lists all self-hosted runners configured in a repository. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def actions_list_self_hosted_runners_in_group_for_org(request: web.Request, org, runner_group_id, per_page=None, page=None) -> web.Response:
    """List self-hosted runners in a group for an organization

    Lists self-hosted runners that are in a specific organization group. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

    :param org: 
    :type org: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def actions_list_workflow_run_artifacts(request: web.Request, owner, repo, run_id, per_page=None, page=None) -> web.Response:
    """List workflow run artifacts

    Lists artifacts for a workflow run. Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param run_id: The id of the workflow run.
    :type run_id: int
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int

    """
    return web.Response(status=200)


async def actions_list_workflow_runs(request: web.Request, owner, repo, workflow_id, actor=None, branch=None, event=None, status=None, per_page=None, page=None, created=None, exclude_pull_requests=None) -> web.Response:
    """List workflow runs

    List all workflow runs for a workflow. You can replace &#x60;workflow_id&#x60; with the workflow file name. For example, you could use &#x60;main.yaml&#x60;. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#parameters).  Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param workflow_id: The ID of the workflow. You can also pass the workflow file name as a string.
    :type workflow_id: dict | bytes
    :param actor: Returns someone&#39;s workflow runs. Use the login for the user who created the &#x60;push&#x60; associated with the check suite or workflow run.
    :type actor: str
    :param branch: Returns workflow runs associated with a branch. Use the name of the branch of the &#x60;push&#x60;.
    :type branch: str
    :param event: Returns workflow run triggered by the event you specify. For example, &#x60;push&#x60;, &#x60;pull_request&#x60; or &#x60;issue&#x60;. For more information, see \&quot;[Events that trigger workflows](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/events-that-trigger-workflows).\&quot;
    :type event: str
    :param status: Returns workflow runs with the check run &#x60;status&#x60; or &#x60;conclusion&#x60; that you specify. For example, a conclusion can be &#x60;success&#x60; or a status can be &#x60;in_progress&#x60;. Only GitHub can set a status of &#x60;waiting&#x60; or &#x60;requested&#x60;. For a list of the possible &#x60;status&#x60; and &#x60;conclusion&#x60; options, see \&quot;[Create a check run](https://docs.github.com/enterprise-server@2.22/rest/reference/checks#create-a-check-run).\&quot;
    :type status: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int
    :param created: 
    :type created: str
    :param exclude_pull_requests: If &#x60;true&#x60; pull requests are omitted from the response (empty array).
    :type exclude_pull_requests: bool

    """
    workflow_id = .from_dict(workflow_id)
    created = util.deserialize_datetime(created)
    return web.Response(status=200)


async def actions_list_workflow_runs_for_repo(request: web.Request, owner, repo, actor=None, branch=None, event=None, status=None, per_page=None, page=None, created=None, exclude_pull_requests=None) -> web.Response:
    """List workflow runs for a repository

    Lists all workflow runs for a repository. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#parameters).  Anyone with read access to the repository can use this endpoint. If the repository is private you must use an access token with the &#x60;repo&#x60; scope. GitHub Apps must have the &#x60;actions:read&#x60; permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param actor: Returns someone&#39;s workflow runs. Use the login for the user who created the &#x60;push&#x60; associated with the check suite or workflow run.
    :type actor: str
    :param branch: Returns workflow runs associated with a branch. Use the name of the branch of the &#x60;push&#x60;.
    :type branch: str
    :param event: Returns workflow run triggered by the event you specify. For example, &#x60;push&#x60;, &#x60;pull_request&#x60; or &#x60;issue&#x60;. For more information, see \&quot;[Events that trigger workflows](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/events-that-trigger-workflows).\&quot;
    :type event: str
    :param status: Returns workflow runs with the check run &#x60;status&#x60; or &#x60;conclusion&#x60; that you specify. For example, a conclusion can be &#x60;success&#x60; or a status can be &#x60;in_progress&#x60;. Only GitHub can set a status of &#x60;waiting&#x60; or &#x60;requested&#x60;. For a list of the possible &#x60;status&#x60; and &#x60;conclusion&#x60; options, see \&quot;[Create a check run](https://docs.github.com/enterprise-server@2.22/rest/reference/checks#create-a-check-run).\&quot;
    :type status: str
    :param per_page: Results per page (max 100)
    :type per_page: int
    :param page: Page number of the results to fetch.
    :type page: int
    :param created: 
    :type created: str
    :param exclude_pull_requests: If &#x60;true&#x60; pull requests are omitted from the response (empty array).
    :type exclude_pull_requests: bool

    """
    created = util.deserialize_datetime(created)
    return web.Response(status=200)


async def actions_re_run_workflow(request: web.Request, owner, repo, run_id) -> web.Response:
    """Re-run a workflow

    Re-runs your workflow run using its &#x60;id&#x60;. You must authenticate using an access token with the &#x60;repo&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;actions:write&#x60; permission to use this endpoint.

    :param owner: 
    :type owner: str
    :param repo: 
    :type repo: str
    :param run_id: The id of the workflow run.
    :type run_id: int

    """
    return web.Response(status=200)


async def actions_remove_repo_access_to_self_hosted_runner_group_in_org(request: web.Request, org, runner_group_id, repository_id) -> web.Response:
    """Remove repository access to a self-hosted runner group in an organization

    Removes a repository from the list of selected repositories that can access a self-hosted runner group. The runner group must have &#x60;visibility&#x60; set to &#x60;selected&#x60;. For more information, see \&quot;[Create a self-hosted runner group for an organization](#create-a-self-hosted-runner-group-for-an-organization).\&quot; You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

    :param org: 
    :type org: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int
    :param repository_id: 
    :type repository_id: int

    """
    return web.Response(status=200)


async def actions_remove_selected_repo_from_org_secret(request: web.Request, org, secret_name, repository_id) -> web.Response:
    """Remove selected repository from an organization secret

    Removes a repository from an organization secret when the &#x60;visibility&#x60; for repository access is set to &#x60;selected&#x60;. The visibility is set when you [Create or update an organization secret](https://docs.github.com/enterprise-server@2.22/rest/reference/actions#create-or-update-an-organization-secret). You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; organization permission to use this endpoint.

    :param org: 
    :type org: str
    :param secret_name: secret_name parameter
    :type secret_name: str
    :param repository_id: 
    :type repository_id: int

    """
    return web.Response(status=200)


async def actions_remove_self_hosted_runner_from_group_for_org(request: web.Request, org, runner_group_id, runner_id) -> web.Response:
    """Remove a self-hosted runner from a group for an organization

    Removes a self-hosted runner from a group configured in an organization. The runner is then returned to the default group. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

    :param org: 
    :type org: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int
    :param runner_id: Unique identifier of the self-hosted runner.
    :type runner_id: int

    """
    return web.Response(status=200)


async def actions_set_repo_access_to_self_hosted_runner_group_in_org(request: web.Request, org, runner_group_id, body) -> web.Response:
    """Set repository access for a self-hosted runner group in an organization

    Replaces the list of repositories that have access to a self-hosted runner group configured in an organization. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

    :param org: 
    :type org: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ActionsSetRepoAccessToSelfHostedRunnerGroupInOrgRequest.from_dict(body)
    return web.Response(status=200)


async def actions_set_selected_repos_for_org_secret(request: web.Request, org, secret_name, body) -> web.Response:
    """Set selected repositories for an organization secret

    Replaces all repositories for an organization secret when the &#x60;visibility&#x60; for repository access is set to &#x60;selected&#x60;. The visibility is set when you [Create or update an organization secret](https://docs.github.com/enterprise-server@2.22/rest/reference/actions#create-or-update-an-organization-secret). You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint. GitHub Apps must have the &#x60;secrets&#x60; organization permission to use this endpoint.

    :param org: 
    :type org: str
    :param secret_name: secret_name parameter
    :type secret_name: str
    :param body: 
    :type body: dict | bytes

    """
    body = ActionsSetSelectedReposForOrgSecretRequest.from_dict(body)
    return web.Response(status=200)


async def actions_set_self_hosted_runners_in_group_for_org(request: web.Request, org, runner_group_id, body) -> web.Response:
    """Set self-hosted runners in a group for an organization

    Replaces the list of self-hosted runners that are part of an organization runner group. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

    :param org: 
    :type org: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = EnterpriseAdminSetSelfHostedRunnersInGroupForEnterpriseRequest.from_dict(body)
    return web.Response(status=200)


async def actions_update_self_hosted_runner_group_for_org(request: web.Request, org, runner_group_id, body) -> web.Response:
    """Update a self-hosted runner group for an organization

    Updates the &#x60;name&#x60; and &#x60;visibility&#x60; of a self-hosted runner group in an organization. You must authenticate using an access token with the &#x60;admin:org&#x60; scope to use this endpoint.

    :param org: 
    :type org: str
    :param runner_group_id: Unique identifier of the self-hosted runner group.
    :type runner_group_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ActionsUpdateSelfHostedRunnerGroupForOrgRequest.from_dict(body)
    return web.Response(status=200)
