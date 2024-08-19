# ReposApi

All URIs are relative to *http://HOSTNAME/api/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reposAcceptInvitationForAuthenticatedUser**](ReposApi.md#reposAcceptInvitationForAuthenticatedUser) | **PATCH** /user/repository_invitations/{invitation_id} | Accept a repository invitation |
| [**reposAddAppAccessRestrictions**](ReposApi.md#reposAddAppAccessRestrictions) | **POST** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | Add app access restrictions |
| [**reposAddCollaborator**](ReposApi.md#reposAddCollaborator) | **PUT** /repos/{owner}/{repo}/collaborators/{username} | Add a repository collaborator |
| [**reposAddStatusCheckContexts**](ReposApi.md#reposAddStatusCheckContexts) | **POST** /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | Add status check contexts |
| [**reposAddTeamAccessRestrictions**](ReposApi.md#reposAddTeamAccessRestrictions) | **POST** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | Add team access restrictions |
| [**reposAddUserAccessRestrictions**](ReposApi.md#reposAddUserAccessRestrictions) | **POST** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | Add user access restrictions |
| [**reposCheckCollaborator**](ReposApi.md#reposCheckCollaborator) | **GET** /repos/{owner}/{repo}/collaborators/{username} | Check if a user is a repository collaborator |
| [**reposCompareCommits**](ReposApi.md#reposCompareCommits) | **GET** /repos/{owner}/{repo}/compare/{basehead} | Compare two commits |
| [**reposCreateCommitComment**](ReposApi.md#reposCreateCommitComment) | **POST** /repos/{owner}/{repo}/commits/{commit_sha}/comments | Create a commit comment |
| [**reposCreateCommitSignatureProtection**](ReposApi.md#reposCreateCommitSignatureProtection) | **POST** /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures | Create commit signature protection |
| [**reposCreateCommitStatus**](ReposApi.md#reposCreateCommitStatus) | **POST** /repos/{owner}/{repo}/statuses/{sha} | Create a commit status |
| [**reposCreateDeployKey**](ReposApi.md#reposCreateDeployKey) | **POST** /repos/{owner}/{repo}/keys | Create a deploy key |
| [**reposCreateDeployment**](ReposApi.md#reposCreateDeployment) | **POST** /repos/{owner}/{repo}/deployments | Create a deployment |
| [**reposCreateDeploymentStatus**](ReposApi.md#reposCreateDeploymentStatus) | **POST** /repos/{owner}/{repo}/deployments/{deployment_id}/statuses | Create a deployment status |
| [**reposCreateDispatchEvent**](ReposApi.md#reposCreateDispatchEvent) | **POST** /repos/{owner}/{repo}/dispatches | Create a repository dispatch event |
| [**reposCreateForAuthenticatedUser**](ReposApi.md#reposCreateForAuthenticatedUser) | **POST** /user/repos | Create a repository for the authenticated user |
| [**reposCreateFork**](ReposApi.md#reposCreateFork) | **POST** /repos/{owner}/{repo}/forks | Create a fork |
| [**reposCreateInOrg**](ReposApi.md#reposCreateInOrg) | **POST** /orgs/{org}/repos | Create an organization repository |
| [**reposCreateOrUpdateFileContents**](ReposApi.md#reposCreateOrUpdateFileContents) | **PUT** /repos/{owner}/{repo}/contents/{path} | Create or update file contents |
| [**reposCreatePagesSite**](ReposApi.md#reposCreatePagesSite) | **POST** /repos/{owner}/{repo}/pages | Create a GitHub Enterprise Server Pages site |
| [**reposCreateRelease**](ReposApi.md#reposCreateRelease) | **POST** /repos/{owner}/{repo}/releases | Create a release |
| [**reposCreateUsingTemplate**](ReposApi.md#reposCreateUsingTemplate) | **POST** /repos/{template_owner}/{template_repo}/generate | Create a repository using a template |
| [**reposCreateWebhook**](ReposApi.md#reposCreateWebhook) | **POST** /repos/{owner}/{repo}/hooks | Create a repository webhook |
| [**reposDeclineInvitationForAuthenticatedUser**](ReposApi.md#reposDeclineInvitationForAuthenticatedUser) | **DELETE** /user/repository_invitations/{invitation_id} | Decline a repository invitation |
| [**reposDelete**](ReposApi.md#reposDelete) | **DELETE** /repos/{owner}/{repo} | Delete a repository |
| [**reposDeleteAccessRestrictions**](ReposApi.md#reposDeleteAccessRestrictions) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions | Delete access restrictions |
| [**reposDeleteAdminBranchProtection**](ReposApi.md#reposDeleteAdminBranchProtection) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins | Delete admin branch protection |
| [**reposDeleteBranchProtection**](ReposApi.md#reposDeleteBranchProtection) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection | Delete branch protection |
| [**reposDeleteCommitComment**](ReposApi.md#reposDeleteCommitComment) | **DELETE** /repos/{owner}/{repo}/comments/{comment_id} | Delete a commit comment |
| [**reposDeleteCommitSignatureProtection**](ReposApi.md#reposDeleteCommitSignatureProtection) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures | Delete commit signature protection |
| [**reposDeleteDeployKey**](ReposApi.md#reposDeleteDeployKey) | **DELETE** /repos/{owner}/{repo}/keys/{key_id} | Delete a deploy key |
| [**reposDeleteDeployment**](ReposApi.md#reposDeleteDeployment) | **DELETE** /repos/{owner}/{repo}/deployments/{deployment_id} | Delete a deployment |
| [**reposDeleteFile**](ReposApi.md#reposDeleteFile) | **DELETE** /repos/{owner}/{repo}/contents/{path} | Delete a file |
| [**reposDeleteInvitation**](ReposApi.md#reposDeleteInvitation) | **DELETE** /repos/{owner}/{repo}/invitations/{invitation_id} | Delete a repository invitation |
| [**reposDeletePagesSite**](ReposApi.md#reposDeletePagesSite) | **DELETE** /repos/{owner}/{repo}/pages | Delete a GitHub Enterprise Server Pages site |
| [**reposDeletePullRequestReviewProtection**](ReposApi.md#reposDeletePullRequestReviewProtection) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews | Delete pull request review protection |
| [**reposDeleteRelease**](ReposApi.md#reposDeleteRelease) | **DELETE** /repos/{owner}/{repo}/releases/{release_id} | Delete a release |
| [**reposDeleteReleaseAsset**](ReposApi.md#reposDeleteReleaseAsset) | **DELETE** /repos/{owner}/{repo}/releases/assets/{asset_id} | Delete a release asset |
| [**reposDeleteWebhook**](ReposApi.md#reposDeleteWebhook) | **DELETE** /repos/{owner}/{repo}/hooks/{hook_id} | Delete a repository webhook |
| [**reposDownloadTarballArchive**](ReposApi.md#reposDownloadTarballArchive) | **GET** /repos/{owner}/{repo}/tarball/{ref} | Download a repository archive (tar) |
| [**reposDownloadZipballArchive**](ReposApi.md#reposDownloadZipballArchive) | **GET** /repos/{owner}/{repo}/zipball/{ref} | Download a repository archive (zip) |
| [**reposGet**](ReposApi.md#reposGet) | **GET** /repos/{owner}/{repo} | Get a repository |
| [**reposGetAccessRestrictions**](ReposApi.md#reposGetAccessRestrictions) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions | Get access restrictions |
| [**reposGetAdminBranchProtection**](ReposApi.md#reposGetAdminBranchProtection) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins | Get admin branch protection |
| [**reposGetAllStatusCheckContexts**](ReposApi.md#reposGetAllStatusCheckContexts) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | Get all status check contexts |
| [**reposGetAllTopics**](ReposApi.md#reposGetAllTopics) | **GET** /repos/{owner}/{repo}/topics | Get all repository topics |
| [**reposGetAppsWithAccessToProtectedBranch**](ReposApi.md#reposGetAppsWithAccessToProtectedBranch) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | Get apps with access to the protected branch |
| [**reposGetBranch**](ReposApi.md#reposGetBranch) | **GET** /repos/{owner}/{repo}/branches/{branch} | Get a branch |
| [**reposGetBranchProtection**](ReposApi.md#reposGetBranchProtection) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection | Get branch protection |
| [**reposGetCodeFrequencyStats**](ReposApi.md#reposGetCodeFrequencyStats) | **GET** /repos/{owner}/{repo}/stats/code_frequency | Get the weekly commit activity |
| [**reposGetCollaboratorPermissionLevel**](ReposApi.md#reposGetCollaboratorPermissionLevel) | **GET** /repos/{owner}/{repo}/collaborators/{username}/permission | Get repository permissions for a user |
| [**reposGetCombinedStatusForRef**](ReposApi.md#reposGetCombinedStatusForRef) | **GET** /repos/{owner}/{repo}/commits/{ref}/status | Get the combined status for a specific reference |
| [**reposGetCommit**](ReposApi.md#reposGetCommit) | **GET** /repos/{owner}/{repo}/commits/{ref} | Get a commit |
| [**reposGetCommitActivityStats**](ReposApi.md#reposGetCommitActivityStats) | **GET** /repos/{owner}/{repo}/stats/commit_activity | Get the last year of commit activity |
| [**reposGetCommitComment**](ReposApi.md#reposGetCommitComment) | **GET** /repos/{owner}/{repo}/comments/{comment_id} | Get a commit comment |
| [**reposGetCommitSignatureProtection**](ReposApi.md#reposGetCommitSignatureProtection) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures | Get commit signature protection |
| [**reposGetContent**](ReposApi.md#reposGetContent) | **GET** /repos/{owner}/{repo}/contents/{path} | Get repository content |
| [**reposGetContributorsStats**](ReposApi.md#reposGetContributorsStats) | **GET** /repos/{owner}/{repo}/stats/contributors | Get all contributor commit activity |
| [**reposGetDeployKey**](ReposApi.md#reposGetDeployKey) | **GET** /repos/{owner}/{repo}/keys/{key_id} | Get a deploy key |
| [**reposGetDeployment**](ReposApi.md#reposGetDeployment) | **GET** /repos/{owner}/{repo}/deployments/{deployment_id} | Get a deployment |
| [**reposGetDeploymentStatus**](ReposApi.md#reposGetDeploymentStatus) | **GET** /repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id} | Get a deployment status |
| [**reposGetLatestPagesBuild**](ReposApi.md#reposGetLatestPagesBuild) | **GET** /repos/{owner}/{repo}/pages/builds/latest | Get latest Pages build |
| [**reposGetLatestRelease**](ReposApi.md#reposGetLatestRelease) | **GET** /repos/{owner}/{repo}/releases/latest | Get the latest release |
| [**reposGetPages**](ReposApi.md#reposGetPages) | **GET** /repos/{owner}/{repo}/pages | Get a GitHub Enterprise Server Pages site |
| [**reposGetPagesBuild**](ReposApi.md#reposGetPagesBuild) | **GET** /repos/{owner}/{repo}/pages/builds/{build_id} | Get GitHub Enterprise Server Pages build |
| [**reposGetParticipationStats**](ReposApi.md#reposGetParticipationStats) | **GET** /repos/{owner}/{repo}/stats/participation | Get the weekly commit count |
| [**reposGetPullRequestReviewProtection**](ReposApi.md#reposGetPullRequestReviewProtection) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews | Get pull request review protection |
| [**reposGetPunchCardStats**](ReposApi.md#reposGetPunchCardStats) | **GET** /repos/{owner}/{repo}/stats/punch_card | Get the hourly commit count for each day |
| [**reposGetReadme**](ReposApi.md#reposGetReadme) | **GET** /repos/{owner}/{repo}/readme | Get a repository README |
| [**reposGetReadmeInDirectory**](ReposApi.md#reposGetReadmeInDirectory) | **GET** /repos/{owner}/{repo}/readme/{dir} | Get a repository README for a directory |
| [**reposGetRelease**](ReposApi.md#reposGetRelease) | **GET** /repos/{owner}/{repo}/releases/{release_id} | Get a release |
| [**reposGetReleaseAsset**](ReposApi.md#reposGetReleaseAsset) | **GET** /repos/{owner}/{repo}/releases/assets/{asset_id} | Get a release asset |
| [**reposGetReleaseByTag**](ReposApi.md#reposGetReleaseByTag) | **GET** /repos/{owner}/{repo}/releases/tags/{tag} | Get a release by tag name |
| [**reposGetStatusChecksProtection**](ReposApi.md#reposGetStatusChecksProtection) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks | Get status checks protection |
| [**reposGetTeamsWithAccessToProtectedBranch**](ReposApi.md#reposGetTeamsWithAccessToProtectedBranch) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | Get teams with access to the protected branch |
| [**reposGetUsersWithAccessToProtectedBranch**](ReposApi.md#reposGetUsersWithAccessToProtectedBranch) | **GET** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | Get users with access to the protected branch |
| [**reposGetWebhook**](ReposApi.md#reposGetWebhook) | **GET** /repos/{owner}/{repo}/hooks/{hook_id} | Get a repository webhook |
| [**reposListBranches**](ReposApi.md#reposListBranches) | **GET** /repos/{owner}/{repo}/branches | List branches |
| [**reposListBranchesForHeadCommit**](ReposApi.md#reposListBranchesForHeadCommit) | **GET** /repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head | List branches for HEAD commit |
| [**reposListCollaborators**](ReposApi.md#reposListCollaborators) | **GET** /repos/{owner}/{repo}/collaborators | List repository collaborators |
| [**reposListCommentsForCommit**](ReposApi.md#reposListCommentsForCommit) | **GET** /repos/{owner}/{repo}/commits/{commit_sha}/comments | List commit comments |
| [**reposListCommitCommentsForRepo**](ReposApi.md#reposListCommitCommentsForRepo) | **GET** /repos/{owner}/{repo}/comments | List commit comments for a repository |
| [**reposListCommitStatusesForRef**](ReposApi.md#reposListCommitStatusesForRef) | **GET** /repos/{owner}/{repo}/commits/{ref}/statuses | List commit statuses for a reference |
| [**reposListCommits**](ReposApi.md#reposListCommits) | **GET** /repos/{owner}/{repo}/commits | List commits |
| [**reposListContributors**](ReposApi.md#reposListContributors) | **GET** /repos/{owner}/{repo}/contributors | List repository contributors |
| [**reposListDeployKeys**](ReposApi.md#reposListDeployKeys) | **GET** /repos/{owner}/{repo}/keys | List deploy keys |
| [**reposListDeploymentStatuses**](ReposApi.md#reposListDeploymentStatuses) | **GET** /repos/{owner}/{repo}/deployments/{deployment_id}/statuses | List deployment statuses |
| [**reposListDeployments**](ReposApi.md#reposListDeployments) | **GET** /repos/{owner}/{repo}/deployments | List deployments |
| [**reposListForAuthenticatedUser**](ReposApi.md#reposListForAuthenticatedUser) | **GET** /user/repos | List repositories for the authenticated user |
| [**reposListForOrg**](ReposApi.md#reposListForOrg) | **GET** /orgs/{org}/repos | List organization repositories |
| [**reposListForUser**](ReposApi.md#reposListForUser) | **GET** /users/{username}/repos | List repositories for a user |
| [**reposListForks**](ReposApi.md#reposListForks) | **GET** /repos/{owner}/{repo}/forks | List forks |
| [**reposListInvitations**](ReposApi.md#reposListInvitations) | **GET** /repos/{owner}/{repo}/invitations | List repository invitations |
| [**reposListInvitationsForAuthenticatedUser**](ReposApi.md#reposListInvitationsForAuthenticatedUser) | **GET** /user/repository_invitations | List repository invitations for the authenticated user |
| [**reposListLanguages**](ReposApi.md#reposListLanguages) | **GET** /repos/{owner}/{repo}/languages | List repository languages |
| [**reposListPagesBuilds**](ReposApi.md#reposListPagesBuilds) | **GET** /repos/{owner}/{repo}/pages/builds | List GitHub Enterprise Server Pages builds |
| [**reposListPublic**](ReposApi.md#reposListPublic) | **GET** /repositories | List public repositories |
| [**reposListPullRequestsAssociatedWithCommit**](ReposApi.md#reposListPullRequestsAssociatedWithCommit) | **GET** /repos/{owner}/{repo}/commits/{commit_sha}/pulls | List pull requests associated with a commit |
| [**reposListReleaseAssets**](ReposApi.md#reposListReleaseAssets) | **GET** /repos/{owner}/{repo}/releases/{release_id}/assets | List release assets |
| [**reposListReleases**](ReposApi.md#reposListReleases) | **GET** /repos/{owner}/{repo}/releases | List releases |
| [**reposListTags**](ReposApi.md#reposListTags) | **GET** /repos/{owner}/{repo}/tags | List repository tags |
| [**reposListTeams**](ReposApi.md#reposListTeams) | **GET** /repos/{owner}/{repo}/teams | List repository teams |
| [**reposListWebhooks**](ReposApi.md#reposListWebhooks) | **GET** /repos/{owner}/{repo}/hooks | List repository webhooks |
| [**reposMerge**](ReposApi.md#reposMerge) | **POST** /repos/{owner}/{repo}/merges | Merge a branch |
| [**reposPingWebhook**](ReposApi.md#reposPingWebhook) | **POST** /repos/{owner}/{repo}/hooks/{hook_id}/pings | Ping a repository webhook |
| [**reposRemoveAppAccessRestrictions**](ReposApi.md#reposRemoveAppAccessRestrictions) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | Remove app access restrictions |
| [**reposRemoveCollaborator**](ReposApi.md#reposRemoveCollaborator) | **DELETE** /repos/{owner}/{repo}/collaborators/{username} | Remove a repository collaborator |
| [**reposRemoveStatusCheckContexts**](ReposApi.md#reposRemoveStatusCheckContexts) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | Remove status check contexts |
| [**reposRemoveStatusCheckProtection**](ReposApi.md#reposRemoveStatusCheckProtection) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks | Remove status check protection |
| [**reposRemoveTeamAccessRestrictions**](ReposApi.md#reposRemoveTeamAccessRestrictions) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | Remove team access restrictions |
| [**reposRemoveUserAccessRestrictions**](ReposApi.md#reposRemoveUserAccessRestrictions) | **DELETE** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | Remove user access restrictions |
| [**reposReplaceAllTopics**](ReposApi.md#reposReplaceAllTopics) | **PUT** /repos/{owner}/{repo}/topics | Replace all repository topics |
| [**reposRequestPagesBuild**](ReposApi.md#reposRequestPagesBuild) | **POST** /repos/{owner}/{repo}/pages/builds | Request a GitHub Enterprise Server Pages build |
| [**reposSetAdminBranchProtection**](ReposApi.md#reposSetAdminBranchProtection) | **POST** /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins | Set admin branch protection |
| [**reposSetAppAccessRestrictions**](ReposApi.md#reposSetAppAccessRestrictions) | **PUT** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps | Set app access restrictions |
| [**reposSetStatusCheckContexts**](ReposApi.md#reposSetStatusCheckContexts) | **PUT** /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts | Set status check contexts |
| [**reposSetTeamAccessRestrictions**](ReposApi.md#reposSetTeamAccessRestrictions) | **PUT** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams | Set team access restrictions |
| [**reposSetUserAccessRestrictions**](ReposApi.md#reposSetUserAccessRestrictions) | **PUT** /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users | Set user access restrictions |
| [**reposTestPushWebhook**](ReposApi.md#reposTestPushWebhook) | **POST** /repos/{owner}/{repo}/hooks/{hook_id}/tests | Test the push repository webhook |
| [**reposTransfer**](ReposApi.md#reposTransfer) | **POST** /repos/{owner}/{repo}/transfer | Transfer a repository |
| [**reposUpdate**](ReposApi.md#reposUpdate) | **PATCH** /repos/{owner}/{repo} | Update a repository |
| [**reposUpdateBranchProtection**](ReposApi.md#reposUpdateBranchProtection) | **PUT** /repos/{owner}/{repo}/branches/{branch}/protection | Update branch protection |
| [**reposUpdateCommitComment**](ReposApi.md#reposUpdateCommitComment) | **PATCH** /repos/{owner}/{repo}/comments/{comment_id} | Update a commit comment |
| [**reposUpdateInformationAboutPagesSite**](ReposApi.md#reposUpdateInformationAboutPagesSite) | **PUT** /repos/{owner}/{repo}/pages | Update information about a GitHub Enterprise Server Pages site |
| [**reposUpdateInvitation**](ReposApi.md#reposUpdateInvitation) | **PATCH** /repos/{owner}/{repo}/invitations/{invitation_id} | Update a repository invitation |
| [**reposUpdatePullRequestReviewProtection**](ReposApi.md#reposUpdatePullRequestReviewProtection) | **PATCH** /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews | Update pull request review protection |
| [**reposUpdateRelease**](ReposApi.md#reposUpdateRelease) | **PATCH** /repos/{owner}/{repo}/releases/{release_id} | Update a release |
| [**reposUpdateReleaseAsset**](ReposApi.md#reposUpdateReleaseAsset) | **PATCH** /repos/{owner}/{repo}/releases/assets/{asset_id} | Update a release asset |
| [**reposUpdateStatusCheckProtection**](ReposApi.md#reposUpdateStatusCheckProtection) | **PATCH** /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks | Update status check protection |
| [**reposUpdateWebhook**](ReposApi.md#reposUpdateWebhook) | **PATCH** /repos/{owner}/{repo}/hooks/{hook_id} | Update a repository webhook |
| [**reposUploadReleaseAsset**](ReposApi.md#reposUploadReleaseAsset) | **POST** /repos/{owner}/{repo}/releases/{release_id}/assets | Upload a release asset |


<a id="reposAcceptInvitationForAuthenticatedUser"></a>
# **reposAcceptInvitationForAuthenticatedUser**
> reposAcceptInvitationForAuthenticatedUser(invitationId)

Accept a repository invitation



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    Integer invitationId = 56; // Integer | invitation_id parameter
    try {
      apiInstance.reposAcceptInvitationForAuthenticatedUser(invitationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposAcceptInvitationForAuthenticatedUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **invitationId** | **Integer**| invitation_id parameter | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **409** | Conflict |  -  |

<a id="reposAddAppAccessRestrictions"></a>
# **reposAddAppAccessRestrictions**
> List&lt;Integration&gt; reposAddAppAccessRestrictions(owner, repo, branch, reposSetAppAccessRestrictionsRequest)

Add app access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Grants the specified apps push access for this branch. Only installed GitHub Apps with &#x60;write&#x60; access to the &#x60;contents&#x60; permission can be added as authorized actors on a protected branch.  | Type    | Description                                                                                                                                                | | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | | &#x60;array&#x60; | The GitHub Apps that have push access to this branch. Use the app&#39;s &#x60;slug&#x60;. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    ReposSetAppAccessRestrictionsRequest reposSetAppAccessRestrictionsRequest = new ReposSetAppAccessRestrictionsRequest(); // ReposSetAppAccessRestrictionsRequest | 
    try {
      List<Integration> result = apiInstance.reposAddAppAccessRestrictions(owner, repo, branch, reposSetAppAccessRestrictionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposAddAppAccessRestrictions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |
| **reposSetAppAccessRestrictionsRequest** | [**ReposSetAppAccessRestrictionsRequest**](ReposSetAppAccessRestrictionsRequest.md)|  | [optional] |

### Return type

[**List&lt;Integration&gt;**](Integration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **422** | Validation failed |  -  |

<a id="reposAddCollaborator"></a>
# **reposAddCollaborator**
> RepositoryInvitation reposAddCollaborator(owner, repo, username, reposAddCollaboratorRequest)

Add a repository collaborator

This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.22/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.  For more information on permission levels, see \&quot;[Repository permission levels for an organization](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)\&quot;.  Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;  The invitee will receive a notification that they have been invited to the repository, which they must accept or decline. They may do this via the notifications page, the email they receive, or by using the [repository invitations API endpoints](https://docs.github.com/enterprise-server@2.22/rest/reference/repos#invitations).  **Rate limits**  You are limited to sending 50 invitations to a repository per 24 hour period. Note there is no limit if you are inviting organization members to an organization repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String username = "username_example"; // String | 
    ReposAddCollaboratorRequest reposAddCollaboratorRequest = new ReposAddCollaboratorRequest(); // ReposAddCollaboratorRequest | 
    try {
      RepositoryInvitation result = apiInstance.reposAddCollaborator(owner, repo, username, reposAddCollaboratorRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposAddCollaborator");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **username** | **String**|  | |
| **reposAddCollaboratorRequest** | [**ReposAddCollaboratorRequest**](ReposAddCollaboratorRequest.md)|  | [optional] |

### Return type

[**RepositoryInvitation**](RepositoryInvitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response when a new invitation is created |  -  |
| **204** | Response when person is already a collaborator |  -  |
| **403** | Forbidden |  -  |
| **422** | Validation failed |  -  |

<a id="reposAddStatusCheckContexts"></a>
# **reposAddStatusCheckContexts**
> List&lt;String&gt; reposAddStatusCheckContexts(owner, repo, branch, reposSetStatusCheckContextsRequest)

Add status check contexts

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    ReposSetStatusCheckContextsRequest reposSetStatusCheckContextsRequest = new ReposSetStatusCheckContextsRequest(); // ReposSetStatusCheckContextsRequest | 
    try {
      List<String> result = apiInstance.reposAddStatusCheckContexts(owner, repo, branch, reposSetStatusCheckContextsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposAddStatusCheckContexts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |
| **reposSetStatusCheckContextsRequest** | [**ReposSetStatusCheckContextsRequest**](ReposSetStatusCheckContextsRequest.md)|  | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="reposAddTeamAccessRestrictions"></a>
# **reposAddTeamAccessRestrictions**
> List&lt;Team&gt; reposAddTeamAccessRestrictions(owner, repo, branch, reposSetTeamAccessRestrictionsRequest)

Add team access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Grants the specified teams push access for this branch. You can also give push access to child teams.  | Type    | Description                                                                                                                                | | ------- | ------------------------------------------------------------------------------------------------------------------------------------------ | | &#x60;array&#x60; | The teams that can have push access. Use the team&#39;s &#x60;slug&#x60;. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    ReposSetTeamAccessRestrictionsRequest reposSetTeamAccessRestrictionsRequest = new ReposSetTeamAccessRestrictionsRequest(); // ReposSetTeamAccessRestrictionsRequest | 
    try {
      List<Team> result = apiInstance.reposAddTeamAccessRestrictions(owner, repo, branch, reposSetTeamAccessRestrictionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposAddTeamAccessRestrictions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |
| **reposSetTeamAccessRestrictionsRequest** | [**ReposSetTeamAccessRestrictionsRequest**](ReposSetTeamAccessRestrictionsRequest.md)|  | [optional] |

### Return type

[**List&lt;Team&gt;**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **422** | Validation failed |  -  |

<a id="reposAddUserAccessRestrictions"></a>
# **reposAddUserAccessRestrictions**
> List&lt;SimpleUser&gt; reposAddUserAccessRestrictions(owner, repo, branch, reposSetUserAccessRestrictionsRequest)

Add user access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Grants the specified people push access for this branch.  | Type    | Description                                                                                                                   | | ------- | ----------------------------------------------------------------------------------------------------------------------------- | | &#x60;array&#x60; | Usernames for people who can have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    ReposSetUserAccessRestrictionsRequest reposSetUserAccessRestrictionsRequest = new ReposSetUserAccessRestrictionsRequest(); // ReposSetUserAccessRestrictionsRequest | 
    try {
      List<SimpleUser> result = apiInstance.reposAddUserAccessRestrictions(owner, repo, branch, reposSetUserAccessRestrictionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposAddUserAccessRestrictions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |
| **reposSetUserAccessRestrictionsRequest** | [**ReposSetUserAccessRestrictionsRequest**](ReposSetUserAccessRestrictionsRequest.md)|  | [optional] |

### Return type

[**List&lt;SimpleUser&gt;**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **422** | Validation failed |  -  |

<a id="reposCheckCollaborator"></a>
# **reposCheckCollaborator**
> reposCheckCollaborator(owner, repo, username)

Check if a user is a repository collaborator

For organization-owned repositories, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners.  Team members will include the members of child teams.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String username = "username_example"; // String | 
    try {
      apiInstance.reposCheckCollaborator(owner, repo, username);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposCheckCollaborator");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **username** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response if user is a collaborator |  -  |
| **404** | Not Found if user is not a collaborator |  -  |

<a id="reposCompareCommits"></a>
# **reposCompareCommits**
> CommitComparison reposCompareCommits(owner, repo, basehead)

Compare two commits

The &#x60;basehead&#x60; param is comprised of two parts: &#x60;base&#x60; and &#x60;head&#x60;. Both must be branch names in &#x60;repo&#x60;. To compare branches across other repositories in the same network as &#x60;repo&#x60;, use the format &#x60;&lt;USERNAME&gt;:branch&#x60;.  The response from the API is equivalent to running the &#x60;git log base..head&#x60; command; however, commits are returned in chronological order. Pass the appropriate [media type](https://docs.github.com/enterprise-server@2.22/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) to fetch diff and patch formats.  The response also includes details on the files that were changed between the two commits. This includes the status of the change (for example, if a file was added, removed, modified, or renamed), and details of the change itself. For example, files with a &#x60;renamed&#x60; status have a &#x60;previous_filename&#x60; field showing the previous filename of the file, and files with a &#x60;modified&#x60; status have a &#x60;patch&#x60; field showing the changes made to the file.  **Working with large comparisons**  The response will include a comparison of up to 250 commits. If you are working with a larger commit range, you can use the [List commits](https://docs.github.com/enterprise-server@2.22/rest/reference/repos#list-commits) to enumerate all commits in the range.  For comparisons with extremely large diffs, you may receive an error response indicating that the diff took too long to generate. You can typically resolve this error by using a smaller commit range.  **Signature verification object**  The response will include a &#x60;verification&#x60; object that describes the result of verifying the commit&#39;s signature. The following fields are included in the &#x60;verification&#x60; object:  | Name | Type | Description | | ---- | ---- | ----------- | | &#x60;verified&#x60; | &#x60;boolean&#x60; | Indicates whether GitHub considers the signature in this commit to be verified. | | &#x60;reason&#x60; | &#x60;string&#x60; | The reason for verified value. Possible values and their meanings are enumerated in table below. | | &#x60;signature&#x60; | &#x60;string&#x60; | The signature that was extracted from the commit. | | &#x60;payload&#x60; | &#x60;string&#x60; | The value that was signed. |  These are the possible values for &#x60;reason&#x60; in the &#x60;verification&#x60; object:  | Value | Description | | ----- | ----------- | | &#x60;expired_key&#x60; | The key that made the signature is expired. | | &#x60;not_signing_key&#x60; | The \&quot;signing\&quot; flag is not among the usage flags in the GPG key that made the signature. | | &#x60;gpgverify_error&#x60; | There was an error communicating with the signature verification service. | | &#x60;gpgverify_unavailable&#x60; | The signature verification service is currently unavailable. | | &#x60;unsigned&#x60; | The object does not include a signature. | | &#x60;unknown_signature_type&#x60; | A non-PGP signature was found in the commit. | | &#x60;no_user&#x60; | No user was associated with the &#x60;committer&#x60; email address in the commit. | | &#x60;unverified_email&#x60; | The &#x60;committer&#x60; email address in the commit was associated with a user, but the email address is not verified on her/his account. | | &#x60;bad_email&#x60; | The &#x60;committer&#x60; email address in the commit is not included in the identities of the PGP key that made the signature. | | &#x60;unknown_key&#x60; | The key that made the signature has not been registered with any user&#39;s account. | | &#x60;malformed_signature&#x60; | There was an error parsing the signature. | | &#x60;invalid&#x60; | The signature could not be cryptographically verified using the key whose key-id was found in the signature. | | &#x60;valid&#x60; | None of the above errors applied, so the signature is considered to be verified. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String basehead = "basehead_example"; // String | The base branch and head branch to compare. This parameter expects the format `{base}...{head}`.
    try {
      CommitComparison result = apiInstance.reposCompareCommits(owner, repo, basehead);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposCompareCommits");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **basehead** | **String**| The base branch and head branch to compare. This parameter expects the format &#x60;{base}...{head}&#x60;. | |

### Return type

[**CommitComparison**](CommitComparison.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal Error |  -  |

<a id="reposCreateCommitComment"></a>
# **reposCreateCommitComment**
> CommitComment reposCreateCommitComment(owner, repo, commitSha, reposCreateCommitCommentRequest)

Create a commit comment

Create a comment for a commit using its &#x60;:commit_sha&#x60;.  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.22/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String commitSha = "commitSha_example"; // String | commit_sha parameter
    ReposCreateCommitCommentRequest reposCreateCommitCommentRequest = new ReposCreateCommitCommentRequest(); // ReposCreateCommitCommentRequest | 
    try {
      CommitComment result = apiInstance.reposCreateCommitComment(owner, repo, commitSha, reposCreateCommitCommentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposCreateCommitComment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **commitSha** | **String**| commit_sha parameter | |
| **reposCreateCommitCommentRequest** | [**ReposCreateCommitCommentRequest**](ReposCreateCommitCommentRequest.md)|  | |

### Return type

[**CommitComment**](CommitComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  * Location -  <br>  |
| **403** | Forbidden |  -  |
| **422** | Validation failed |  -  |

<a id="reposCreateCommitSignatureProtection"></a>
# **reposCreateCommitSignatureProtection**
> ProtectedBranchAdminEnforced reposCreateCommitSignatureProtection(owner, repo, branch)

Create commit signature protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  When authenticated with admin or owner permissions to the repository, you can use this endpoint to require signed commits on a branch. You must enable branch protection to require signed commits.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      ProtectedBranchAdminEnforced result = apiInstance.reposCreateCommitSignatureProtection(owner, repo, branch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposCreateCommitSignatureProtection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

[**ProtectedBranchAdminEnforced**](ProtectedBranchAdminEnforced.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposCreateCommitStatus"></a>
# **reposCreateCommitStatus**
> Status reposCreateCommitStatus(owner, repo, sha, reposCreateCommitStatusRequest)

Create a commit status

Users with push access in a repository can create commit statuses for a given SHA.  Note: there is a limit of 1000 statuses per &#x60;sha&#x60; and &#x60;context&#x60; within a repository. Attempts to create more than 1000 statuses will result in a validation error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String sha = "sha_example"; // String | 
    ReposCreateCommitStatusRequest reposCreateCommitStatusRequest = new ReposCreateCommitStatusRequest(); // ReposCreateCommitStatusRequest | 
    try {
      Status result = apiInstance.reposCreateCommitStatus(owner, repo, sha, reposCreateCommitStatusRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposCreateCommitStatus");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **sha** | **String**|  | |
| **reposCreateCommitStatusRequest** | [**ReposCreateCommitStatusRequest**](ReposCreateCommitStatusRequest.md)|  | |

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  * Location -  <br>  |

<a id="reposCreateDeployKey"></a>
# **reposCreateDeployKey**
> DeployKey reposCreateDeployKey(owner, repo, reposCreateDeployKeyRequest)

Create a deploy key

You can create a read-only deploy key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    ReposCreateDeployKeyRequest reposCreateDeployKeyRequest = new ReposCreateDeployKeyRequest(); // ReposCreateDeployKeyRequest | 
    try {
      DeployKey result = apiInstance.reposCreateDeployKey(owner, repo, reposCreateDeployKeyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposCreateDeployKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **reposCreateDeployKeyRequest** | [**ReposCreateDeployKeyRequest**](ReposCreateDeployKeyRequest.md)|  | |

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  * Location -  <br>  |
| **422** | Validation failed |  -  |

<a id="reposCreateDeployment"></a>
# **reposCreateDeployment**
> Deployment reposCreateDeployment(owner, repo, reposCreateDeploymentRequest)

Create a deployment

Deployments offer a few configurable parameters with certain defaults.  The &#x60;ref&#x60; parameter can be any named branch, tag, or SHA. At GitHub Enterprise Server we often deploy branches and verify them before we merge a pull request.  The &#x60;environment&#x60; parameter allows deployments to be issued to different runtime environments. Teams often have multiple environments for verifying their applications, such as &#x60;production&#x60;, &#x60;staging&#x60;, and &#x60;qa&#x60;. This parameter makes it easier to track which environments have requested deployments. The default environment is &#x60;production&#x60;.  The &#x60;auto_merge&#x60; parameter is used to ensure that the requested ref is not behind the repository&#39;s default branch. If the ref _is_ behind the default branch for the repository, we will attempt to merge it for you. If the merge succeeds, the API will return a successful merge commit. If merge conflicts prevent the merge from succeeding, the API will return a failure response.  By default, [commit statuses](https://docs.github.com/enterprise-server@2.22/rest/reference/repos#statuses) for every submitted context must be in a &#x60;success&#x60; state. The &#x60;required_contexts&#x60; parameter allows you to specify a subset of contexts that must be &#x60;success&#x60;, or to specify contexts that have not yet been submitted. You are not required to use commit statuses to deploy. If you do not require any contexts or create any commit statuses, the deployment will always succeed.  The &#x60;payload&#x60; parameter is available for any extra information that a deployment system might need. It is a JSON text field that will be passed on when a deployment event is dispatched.  The &#x60;task&#x60; parameter is used by the deployment system to allow different execution paths. In the web world this might be &#x60;deploy:migrations&#x60; to run schema changes on the system. In the compiled world this could be a flag to compile an application with debugging enabled.  Users with &#x60;repo&#x60; or &#x60;repo_deployment&#x60; scopes can create a deployment for a given ref.  #### Merged branch response You will see this response when GitHub automatically merges the base branch into the topic branch instead of creating a deployment. This auto-merge happens when: *   Auto-merge option is enabled in the repository *   Topic branch does not include the latest changes on the base branch, which is &#x60;master&#x60; in the response example *   There are no merge conflicts  If there are no new commits in the base branch, a new request to create a deployment should give a successful response.  #### Merge conflict response This error happens when the &#x60;auto_merge&#x60; option is enabled and when the default branch (in this case &#x60;master&#x60;), can&#39;t be merged into the branch that&#39;s being deployed (in this case &#x60;topic-branch&#x60;), due to merge conflicts.  #### Failed commit status checks This error happens when the &#x60;required_contexts&#x60; parameter indicates that one or more contexts need to have a &#x60;success&#x60; status for the commit to be deployed, but one or more of the required contexts do not have a state of &#x60;success&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    ReposCreateDeploymentRequest reposCreateDeploymentRequest = new ReposCreateDeploymentRequest(); // ReposCreateDeploymentRequest | 
    try {
      Deployment result = apiInstance.reposCreateDeployment(owner, repo, reposCreateDeploymentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposCreateDeployment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **reposCreateDeploymentRequest** | [**ReposCreateDeploymentRequest**](ReposCreateDeploymentRequest.md)|  | |

### Return type

[**Deployment**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |
| **202** | Merged branch response |  -  |
| **409** | Conflict when there is a merge conflict or the commit&#39;s status checks failed |  -  |
| **422** | Validation failed |  -  |

<a id="reposCreateDeploymentStatus"></a>
# **reposCreateDeploymentStatus**
> DeploymentStatus reposCreateDeploymentStatus(owner, repo, deploymentId, reposCreateDeploymentStatusRequest)

Create a deployment status

Users with &#x60;push&#x60; access can create deployment statuses for a given deployment.  GitHub Apps require &#x60;read &amp; write&#x60; access to \&quot;Deployments\&quot; and &#x60;read-only&#x60; access to \&quot;Repo contents\&quot; (for private repos). OAuth Apps require the &#x60;repo_deployment&#x60; scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer deploymentId = 56; // Integer | deployment_id parameter
    ReposCreateDeploymentStatusRequest reposCreateDeploymentStatusRequest = new ReposCreateDeploymentStatusRequest(); // ReposCreateDeploymentStatusRequest | 
    try {
      DeploymentStatus result = apiInstance.reposCreateDeploymentStatus(owner, repo, deploymentId, reposCreateDeploymentStatusRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposCreateDeploymentStatus");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **deploymentId** | **Integer**| deployment_id parameter | |
| **reposCreateDeploymentStatusRequest** | [**ReposCreateDeploymentStatusRequest**](ReposCreateDeploymentStatusRequest.md)|  | |

### Return type

[**DeploymentStatus**](DeploymentStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  * Location -  <br>  |
| **422** | Validation failed |  -  |

<a id="reposCreateDispatchEvent"></a>
# **reposCreateDispatchEvent**
> reposCreateDispatchEvent(owner, repo, reposCreateDispatchEventRequest)

Create a repository dispatch event

You can use this endpoint to trigger a webhook event called &#x60;repository_dispatch&#x60; when you want activity that happens outside of GitHub Enterprise Server to trigger a GitHub Actions workflow or GitHub App webhook. You must configure your GitHub Actions workflow or GitHub App to run when the &#x60;repository_dispatch&#x60; event occurs. For an example &#x60;repository_dispatch&#x60; webhook payload, see \&quot;[RepositoryDispatchEvent](https://docs.github.com/enterprise-server@2.22/webhooks/event-payloads/#repository_dispatch).\&quot;  The &#x60;client_payload&#x60; parameter is available for any extra information that your workflow might need. This parameter is a JSON payload that will be passed on when the webhook event is dispatched. For example, the &#x60;client_payload&#x60; can include a message that a user would like to send using a GitHub Actions workflow. Or the &#x60;client_payload&#x60; can be used as a test to debug your workflow.  This endpoint requires write access to the repository by providing either:    - Personal access tokens with &#x60;repo&#x60; scope. For more information, see \&quot;[Creating a personal access token for the command line](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line)\&quot; in the GitHub Help documentation.   - GitHub Apps with both &#x60;metadata:read&#x60; and &#x60;contents:read&amp;write&#x60; permissions.  This input example shows how you can use the &#x60;client_payload&#x60; as a test to debug your workflow.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    ReposCreateDispatchEventRequest reposCreateDispatchEventRequest = new ReposCreateDispatchEventRequest(); // ReposCreateDispatchEventRequest | 
    try {
      apiInstance.reposCreateDispatchEvent(owner, repo, reposCreateDispatchEventRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposCreateDispatchEvent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **reposCreateDispatchEventRequest** | [**ReposCreateDispatchEventRequest**](ReposCreateDispatchEventRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **422** | Validation failed |  -  |

<a id="reposCreateForAuthenticatedUser"></a>
# **reposCreateForAuthenticatedUser**
> Repository reposCreateForAuthenticatedUser(reposCreateForAuthenticatedUserRequest)

Create a repository for the authenticated user

Creates a new repository for the authenticated user.  **OAuth scope requirements**  When using [OAuth](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:  *   &#x60;public_repo&#x60; scope or &#x60;repo&#x60; scope to create a public repository. Note: For GitHub AE, use &#x60;repo&#x60; scope to create an internal repository. *   &#x60;repo&#x60; scope to create a private repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    ReposCreateForAuthenticatedUserRequest reposCreateForAuthenticatedUserRequest = new ReposCreateForAuthenticatedUserRequest(); // ReposCreateForAuthenticatedUserRequest | 
    try {
      Repository result = apiInstance.reposCreateForAuthenticatedUser(reposCreateForAuthenticatedUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposCreateForAuthenticatedUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **reposCreateForAuthenticatedUserRequest** | [**ReposCreateForAuthenticatedUserRequest**](ReposCreateForAuthenticatedUserRequest.md)|  | |

### Return type

[**Repository**](Repository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/scim+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  * Location -  <br>  |
| **304** | Not modified |  -  |
| **400** | Bad Request |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="reposCreateFork"></a>
# **reposCreateFork**
> FullRepository reposCreateFork(owner, repo, reposCreateForkRequest)

Create a fork

Create a fork for the authenticated user.  **Note**: Forking a Repository happens asynchronously. You may have to wait a short period of time before you can access the git objects. If this takes longer than 5 minutes, be sure to contact [GitHub Enterprise Server Support](https://support.github.com/contact?tags&#x3D;dotcom-rest-api).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    ReposCreateForkRequest reposCreateForkRequest = new ReposCreateForkRequest(); // ReposCreateForkRequest | 
    try {
      FullRepository result = apiInstance.reposCreateFork(owner, repo, reposCreateForkRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposCreateFork");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **reposCreateForkRequest** | [**ReposCreateForkRequest**](ReposCreateForkRequest.md)|  | [optional] |

### Return type

[**FullRepository**](FullRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/scim+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Response |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="reposCreateInOrg"></a>
# **reposCreateInOrg**
> Repository reposCreateInOrg(org, reposCreateInOrgRequest)

Create an organization repository

Creates a new repository in the specified organization. The authenticated user must be a member of the organization.  **OAuth scope requirements**  When using [OAuth](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:  *   &#x60;public_repo&#x60; scope or &#x60;repo&#x60; scope to create a public repository. Note: For GitHub AE, use &#x60;repo&#x60; scope to create an internal repository. *   &#x60;repo&#x60; scope to create a private repository

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String org = "org_example"; // String | 
    ReposCreateInOrgRequest reposCreateInOrgRequest = new ReposCreateInOrgRequest(); // ReposCreateInOrgRequest | 
    try {
      Repository result = apiInstance.reposCreateInOrg(org, reposCreateInOrgRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposCreateInOrg");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **org** | **String**|  | |
| **reposCreateInOrgRequest** | [**ReposCreateInOrgRequest**](ReposCreateInOrgRequest.md)|  | |

### Return type

[**Repository**](Repository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  * Location -  <br>  |
| **403** | Forbidden |  -  |
| **422** | Validation failed |  -  |

<a id="reposCreateOrUpdateFileContents"></a>
# **reposCreateOrUpdateFileContents**
> FileCommit reposCreateOrUpdateFileContents(owner, repo, path, reposCreateOrUpdateFileContentsRequest)

Create or update file contents

Creates a new file or replaces an existing file in a repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String path = "path_example"; // String | path parameter
    ReposCreateOrUpdateFileContentsRequest reposCreateOrUpdateFileContentsRequest = new ReposCreateOrUpdateFileContentsRequest(); // ReposCreateOrUpdateFileContentsRequest | 
    try {
      FileCommit result = apiInstance.reposCreateOrUpdateFileContents(owner, repo, path, reposCreateOrUpdateFileContentsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposCreateOrUpdateFileContents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **path** | **String**| path parameter | |
| **reposCreateOrUpdateFileContentsRequest** | [**ReposCreateOrUpdateFileContentsRequest**](ReposCreateOrUpdateFileContentsRequest.md)|  | |

### Return type

[**FileCommit**](FileCommit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **201** | Response |  -  |
| **404** | Resource not found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation failed |  -  |

<a id="reposCreatePagesSite"></a>
# **reposCreatePagesSite**
> Page reposCreatePagesSite(owner, repo, reposCreatePagesSiteRequest)

Create a GitHub Enterprise Server Pages site

Configures a GitHub Enterprise Server Pages site. For more information, see \&quot;[About GitHub Pages](/github/working-with-github-pages/about-github-pages).\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    ReposCreatePagesSiteRequest reposCreatePagesSiteRequest = new ReposCreatePagesSiteRequest(); // ReposCreatePagesSiteRequest | 
    try {
      Page result = apiInstance.reposCreatePagesSite(owner, repo, reposCreatePagesSiteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposCreatePagesSite");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **reposCreatePagesSiteRequest** | [**ReposCreatePagesSiteRequest**](ReposCreatePagesSiteRequest.md)|  | |

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |
| **409** | Conflict |  -  |
| **422** | Validation failed |  -  |

<a id="reposCreateRelease"></a>
# **reposCreateRelease**
> Release reposCreateRelease(owner, repo, reposCreateReleaseRequest)

Create a release

Users with push access to the repository can create a release.  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.22/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    ReposCreateReleaseRequest reposCreateReleaseRequest = new ReposCreateReleaseRequest(); // ReposCreateReleaseRequest | 
    try {
      Release result = apiInstance.reposCreateRelease(owner, repo, reposCreateReleaseRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposCreateRelease");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **reposCreateReleaseRequest** | [**ReposCreateReleaseRequest**](ReposCreateReleaseRequest.md)|  | |

### Return type

[**Release**](Release.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  * Location -  <br>  |
| **422** | Validation failed |  -  |

<a id="reposCreateUsingTemplate"></a>
# **reposCreateUsingTemplate**
> Repository reposCreateUsingTemplate(templateOwner, templateRepo, reposCreateUsingTemplateRequest)

Create a repository using a template

Creates a new repository using a repository template. Use the &#x60;template_owner&#x60; and &#x60;template_repo&#x60; route parameters to specify the repository to use as the template. The authenticated user must own or be a member of an organization that owns the repository. To check if a repository is available to use as a template, get the repository&#39;s information using the [Get a repository](https://docs.github.com/enterprise-server@2.22/rest/reference/repos#get-a-repository) endpoint and check that the &#x60;is_template&#x60; key is &#x60;true&#x60;.  **OAuth scope requirements**  When using [OAuth](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), authorizations must include:  *   &#x60;public_repo&#x60; scope or &#x60;repo&#x60; scope to create a public repository. Note: For GitHub AE, use &#x60;repo&#x60; scope to create an internal repository. *   &#x60;repo&#x60; scope to create a private repository

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String templateOwner = "templateOwner_example"; // String | 
    String templateRepo = "templateRepo_example"; // String | 
    ReposCreateUsingTemplateRequest reposCreateUsingTemplateRequest = new ReposCreateUsingTemplateRequest(); // ReposCreateUsingTemplateRequest | 
    try {
      Repository result = apiInstance.reposCreateUsingTemplate(templateOwner, templateRepo, reposCreateUsingTemplateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposCreateUsingTemplate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **templateOwner** | **String**|  | |
| **templateRepo** | **String**|  | |
| **reposCreateUsingTemplateRequest** | [**ReposCreateUsingTemplateRequest**](ReposCreateUsingTemplateRequest.md)|  | |

### Return type

[**Repository**](Repository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  * Location -  <br>  |

<a id="reposCreateWebhook"></a>
# **reposCreateWebhook**
> Hook reposCreateWebhook(owner, repo, reposCreateWebhookRequest)

Create a repository webhook

Repositories can have multiple webhooks installed. Each webhook should have a unique &#x60;config&#x60;. Multiple webhooks can share the same &#x60;config&#x60; as long as those webhooks do not have any &#x60;events&#x60; that overlap.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    ReposCreateWebhookRequest reposCreateWebhookRequest = new ReposCreateWebhookRequest(); // ReposCreateWebhookRequest | 
    try {
      Hook result = apiInstance.reposCreateWebhook(owner, repo, reposCreateWebhookRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposCreateWebhook");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **reposCreateWebhookRequest** | [**ReposCreateWebhookRequest**](ReposCreateWebhookRequest.md)|  | [optional] |

### Return type

[**Hook**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  * Location -  <br>  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="reposDeclineInvitationForAuthenticatedUser"></a>
# **reposDeclineInvitationForAuthenticatedUser**
> reposDeclineInvitationForAuthenticatedUser(invitationId)

Decline a repository invitation



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    Integer invitationId = 56; // Integer | invitation_id parameter
    try {
      apiInstance.reposDeclineInvitationForAuthenticatedUser(invitationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposDeclineInvitationForAuthenticatedUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **invitationId** | **Integer**| invitation_id parameter | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **304** | Not modified |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **409** | Conflict |  -  |

<a id="reposDelete"></a>
# **reposDelete**
> reposDelete(owner, repo)

Delete a repository

Deleting a repository requires admin access. If OAuth is used, the &#x60;delete_repo&#x60; scope is required.  If an organization owner has configured the organization to prevent members from deleting organization-owned repositories, you will get a &#x60;403 Forbidden&#x60; response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      apiInstance.reposDelete(owner, repo);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **307** | Temporary Redirect |  -  |
| **403** | If an organization owner has configured the organization to prevent members from deleting organization-owned repositories, a member will get this response: |  -  |
| **404** | Resource not found |  -  |

<a id="reposDeleteAccessRestrictions"></a>
# **reposDeleteAccessRestrictions**
> reposDeleteAccessRestrictions(owner, repo, branch)

Delete access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Disables the ability to restrict who can push to this branch.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      apiInstance.reposDeleteAccessRestrictions(owner, repo, branch);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposDeleteAccessRestrictions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="reposDeleteAdminBranchProtection"></a>
# **reposDeleteAdminBranchProtection**
> reposDeleteAdminBranchProtection(owner, repo, branch)

Delete admin branch protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Removing admin enforcement requires admin or owner permissions to the repository and branch protection to be enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      apiInstance.reposDeleteAdminBranchProtection(owner, repo, branch);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposDeleteAdminBranchProtection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposDeleteBranchProtection"></a>
# **reposDeleteBranchProtection**
> reposDeleteBranchProtection(owner, repo, branch)

Delete branch protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      apiInstance.reposDeleteBranchProtection(owner, repo, branch);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposDeleteBranchProtection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **403** | Forbidden |  -  |

<a id="reposDeleteCommitComment"></a>
# **reposDeleteCommitComment**
> reposDeleteCommitComment(owner, repo, commentId)

Delete a commit comment



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer commentId = 56; // Integer | comment_id parameter
    try {
      apiInstance.reposDeleteCommitComment(owner, repo, commentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposDeleteCommitComment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **commentId** | **Integer**| comment_id parameter | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposDeleteCommitSignatureProtection"></a>
# **reposDeleteCommitSignatureProtection**
> reposDeleteCommitSignatureProtection(owner, repo, branch)

Delete commit signature protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  When authenticated with admin or owner permissions to the repository, you can use this endpoint to disable required signed commits on a branch. You must enable branch protection to require signed commits.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      apiInstance.reposDeleteCommitSignatureProtection(owner, repo, branch);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposDeleteCommitSignatureProtection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposDeleteDeployKey"></a>
# **reposDeleteDeployKey**
> reposDeleteDeployKey(owner, repo, keyId)

Delete a deploy key

Deploy keys are immutable. If you need to update a key, remove the key and create a new one instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer keyId = 56; // Integer | key_id parameter
    try {
      apiInstance.reposDeleteDeployKey(owner, repo, keyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposDeleteDeployKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **keyId** | **Integer**| key_id parameter | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="reposDeleteDeployment"></a>
# **reposDeleteDeployment**
> reposDeleteDeployment(owner, repo, deploymentId)

Delete a deployment

To ensure there can always be an active deployment, you can only delete an _inactive_ deployment. Anyone with &#x60;repo&#x60; or &#x60;repo_deployment&#x60; scopes can delete an inactive deployment.  To set a deployment as inactive, you must:  *   Create a new deployment that is active so that the system has a record of the current state, then delete the previously active deployment. *   Mark the active deployment as inactive by adding any non-successful deployment status.  For more information, see \&quot;[Create a deployment](https://docs.github.com/enterprise-server@2.22/rest/reference/repos/#create-a-deployment)\&quot; and \&quot;[Create a deployment status](https://docs.github.com/enterprise-server@2.22/rest/reference/repos#create-a-deployment-status).\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer deploymentId = 56; // Integer | deployment_id parameter
    try {
      apiInstance.reposDeleteDeployment(owner, repo, deploymentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposDeleteDeployment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **deploymentId** | **Integer**| deployment_id parameter | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="reposDeleteFile"></a>
# **reposDeleteFile**
> FileCommit reposDeleteFile(owner, repo, path, reposDeleteFileRequest)

Delete a file

Deletes a file in a repository.  You can provide an additional &#x60;committer&#x60; parameter, which is an object containing information about the committer. Or, you can provide an &#x60;author&#x60; parameter, which is an object containing information about the author.  The &#x60;author&#x60; section is optional and is filled in with the &#x60;committer&#x60; information if omitted. If the &#x60;committer&#x60; information is omitted, the authenticated user&#39;s information is used.  You must provide values for both &#x60;name&#x60; and &#x60;email&#x60;, whether you choose to use &#x60;author&#x60; or &#x60;committer&#x60;. Otherwise, you&#39;ll receive a &#x60;422&#x60; status code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String path = "path_example"; // String | path parameter
    ReposDeleteFileRequest reposDeleteFileRequest = new ReposDeleteFileRequest(); // ReposDeleteFileRequest | 
    try {
      FileCommit result = apiInstance.reposDeleteFile(owner, repo, path, reposDeleteFileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposDeleteFile");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **path** | **String**| path parameter | |
| **reposDeleteFileRequest** | [**ReposDeleteFileRequest**](ReposDeleteFileRequest.md)|  | |

### Return type

[**FileCommit**](FileCommit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation failed |  -  |
| **503** | Service unavailable |  -  |

<a id="reposDeleteInvitation"></a>
# **reposDeleteInvitation**
> reposDeleteInvitation(owner, repo, invitationId)

Delete a repository invitation



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer invitationId = 56; // Integer | invitation_id parameter
    try {
      apiInstance.reposDeleteInvitation(owner, repo, invitationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposDeleteInvitation");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **invitationId** | **Integer**| invitation_id parameter | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="reposDeletePagesSite"></a>
# **reposDeletePagesSite**
> reposDeletePagesSite(owner, repo)

Delete a GitHub Enterprise Server Pages site



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      apiInstance.reposDeletePagesSite(owner, repo);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposDeletePagesSite");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="reposDeletePullRequestReviewProtection"></a>
# **reposDeletePullRequestReviewProtection**
> reposDeletePullRequestReviewProtection(owner, repo, branch)

Delete pull request review protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      apiInstance.reposDeletePullRequestReviewProtection(owner, repo, branch);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposDeletePullRequestReviewProtection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposDeleteRelease"></a>
# **reposDeleteRelease**
> reposDeleteRelease(owner, repo, releaseId)

Delete a release

Users with push access to the repository can delete a release.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer releaseId = 56; // Integer | release_id parameter
    try {
      apiInstance.reposDeleteRelease(owner, repo, releaseId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposDeleteRelease");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **releaseId** | **Integer**| release_id parameter | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="reposDeleteReleaseAsset"></a>
# **reposDeleteReleaseAsset**
> reposDeleteReleaseAsset(owner, repo, assetId)

Delete a release asset



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer assetId = 56; // Integer | asset_id parameter
    try {
      apiInstance.reposDeleteReleaseAsset(owner, repo, assetId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposDeleteReleaseAsset");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **assetId** | **Integer**| asset_id parameter | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="reposDeleteWebhook"></a>
# **reposDeleteWebhook**
> reposDeleteWebhook(owner, repo, hookId)

Delete a repository webhook



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer hookId = 56; // Integer | 
    try {
      apiInstance.reposDeleteWebhook(owner, repo, hookId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposDeleteWebhook");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **hookId** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposDownloadTarballArchive"></a>
# **reposDownloadTarballArchive**
> reposDownloadTarballArchive(owner, repo, ref)

Download a repository archive (tar)

Gets a redirect URL to download a tar archive for a repository. If you omit &#x60;:ref&#x60;, the repository’s default branch (usually &#x60;master&#x60;) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use the &#x60;Location&#x60; header to make a second &#x60;GET&#x60; request. **Note**: For private repositories, these links are temporary and expire after five minutes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String ref = "ref_example"; // String | 
    try {
      apiInstance.reposDownloadTarballArchive(owner, repo, ref);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposDownloadTarballArchive");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **ref** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Response |  * Location -  <br>  |

<a id="reposDownloadZipballArchive"></a>
# **reposDownloadZipballArchive**
> reposDownloadZipballArchive(owner, repo, ref)

Download a repository archive (zip)

Gets a redirect URL to download a zip archive for a repository. If you omit &#x60;:ref&#x60;, the repository’s default branch (usually &#x60;master&#x60;) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use the &#x60;Location&#x60; header to make a second &#x60;GET&#x60; request. **Note**: For private repositories, these links are temporary and expire after five minutes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String ref = "ref_example"; // String | 
    try {
      apiInstance.reposDownloadZipballArchive(owner, repo, ref);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposDownloadZipballArchive");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **ref** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | Response |  * Location -  <br>  |

<a id="reposGet"></a>
# **reposGet**
> FullRepository reposGet(owner, repo)

Get a repository

When you pass the &#x60;scarlet-witch-preview&#x60; media type, requests to get a repository will also return the repository&#39;s code of conduct if it can be detected from the repository&#39;s code of conduct file.  The &#x60;parent&#x60; and &#x60;source&#x60; objects are present when the repository is a fork. &#x60;parent&#x60; is the repository this repository was forked from, &#x60;source&#x60; is the ultimate source for the network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      FullRepository result = apiInstance.reposGet(owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |

### Return type

[**FullRepository**](FullRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **301** | Moved permanently |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetAccessRestrictions"></a>
# **reposGetAccessRestrictions**
> BranchRestrictionPolicy reposGetAccessRestrictions(owner, repo, branch)

Get access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists who has access to this protected branch.  **Note**: Users, apps, and teams &#x60;restrictions&#x60; are only available for organization-owned repositories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      BranchRestrictionPolicy result = apiInstance.reposGetAccessRestrictions(owner, repo, branch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetAccessRestrictions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

[**BranchRestrictionPolicy**](BranchRestrictionPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetAdminBranchProtection"></a>
# **reposGetAdminBranchProtection**
> ProtectedBranchAdminEnforced reposGetAdminBranchProtection(owner, repo, branch)

Get admin branch protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      ProtectedBranchAdminEnforced result = apiInstance.reposGetAdminBranchProtection(owner, repo, branch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetAdminBranchProtection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

[**ProtectedBranchAdminEnforced**](ProtectedBranchAdminEnforced.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="reposGetAllStatusCheckContexts"></a>
# **reposGetAllStatusCheckContexts**
> List&lt;String&gt; reposGetAllStatusCheckContexts(owner, repo, branch)

Get all status check contexts

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      List<String> result = apiInstance.reposGetAllStatusCheckContexts(owner, repo, branch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetAllStatusCheckContexts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetAllTopics"></a>
# **reposGetAllTopics**
> Topic reposGetAllTopics(owner, repo, page, perPage)

Get all repository topics



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer page = 1; // Integer | Page number of the results to fetch.
    Integer perPage = 30; // Integer | Results per page (max 100)
    try {
      Topic result = apiInstance.reposGetAllTopics(owner, repo, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetAllTopics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |

### Return type

[**Topic**](Topic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |
| **415** | Preview header missing |  -  |

<a id="reposGetAppsWithAccessToProtectedBranch"></a>
# **reposGetAppsWithAccessToProtectedBranch**
> List&lt;Integration&gt; reposGetAppsWithAccessToProtectedBranch(owner, repo, branch)

Get apps with access to the protected branch

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists the GitHub Apps that have push access to this branch. Only installed GitHub Apps with &#x60;write&#x60; access to the &#x60;contents&#x60; permission can be added as authorized actors on a protected branch.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      List<Integration> result = apiInstance.reposGetAppsWithAccessToProtectedBranch(owner, repo, branch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetAppsWithAccessToProtectedBranch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

[**List&lt;Integration&gt;**](Integration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetBranch"></a>
# **reposGetBranch**
> BranchWithProtection reposGetBranch(owner, repo, branch)

Get a branch



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      BranchWithProtection result = apiInstance.reposGetBranch(owner, repo, branch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetBranch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

[**BranchWithProtection**](BranchWithProtection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **301** | Moved permanently |  -  |
| **404** | Resource not found |  -  |
| **415** | Preview header missing |  -  |

<a id="reposGetBranchProtection"></a>
# **reposGetBranchProtection**
> BranchProtection reposGetBranchProtection(owner, repo, branch)

Get branch protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      BranchProtection result = apiInstance.reposGetBranchProtection(owner, repo, branch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetBranchProtection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

[**BranchProtection**](BranchProtection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetCodeFrequencyStats"></a>
# **reposGetCodeFrequencyStats**
> List&lt;List&lt;Integer&gt;&gt; reposGetCodeFrequencyStats(owner, repo)

Get the weekly commit activity

Returns a weekly aggregate of the number of additions and deletions pushed to a repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      List<List<Integer>> result = apiInstance.reposGetCodeFrequencyStats(owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetCodeFrequencyStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |

### Return type

[**List&lt;List&lt;Integer&gt;&gt;**](List.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a weekly aggregate of the number of additions and deletions pushed to a repository. |  -  |
| **202** | Accepted |  -  |
| **204** | A header with no content is returned. |  -  |

<a id="reposGetCollaboratorPermissionLevel"></a>
# **reposGetCollaboratorPermissionLevel**
> RepositoryCollaboratorPermission reposGetCollaboratorPermissionLevel(owner, repo, username)

Get repository permissions for a user

Checks the repository permission of a collaborator. The possible repository permissions are &#x60;admin&#x60;, &#x60;write&#x60;, &#x60;read&#x60;, and &#x60;none&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String username = "username_example"; // String | 
    try {
      RepositoryCollaboratorPermission result = apiInstance.reposGetCollaboratorPermissionLevel(owner, repo, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetCollaboratorPermissionLevel");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **username** | **String**|  | |

### Return type

[**RepositoryCollaboratorPermission**](RepositoryCollaboratorPermission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | if user has admin permissions |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetCombinedStatusForRef"></a>
# **reposGetCombinedStatusForRef**
> CombinedCommitStatus reposGetCombinedStatusForRef(owner, repo, ref, perPage, page)

Get the combined status for a specific reference

Users with pull access in a repository can access a combined view of commit statuses for a given ref. The ref can be a SHA, a branch name, or a tag name.   Additionally, a combined &#x60;state&#x60; is returned. The &#x60;state&#x60; is one of:  *   **failure** if any of the contexts report as &#x60;error&#x60; or &#x60;failure&#x60; *   **pending** if there are no statuses or a context is &#x60;pending&#x60; *   **success** if the latest status for all contexts is &#x60;success&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String ref = "ref_example"; // String | ref parameter
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      CombinedCommitStatus result = apiInstance.reposGetCombinedStatusForRef(owner, repo, ref, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetCombinedStatusForRef");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **ref** | **String**| ref parameter | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**CombinedCommitStatus**](CombinedCommitStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetCommit"></a>
# **reposGetCommit**
> Commit reposGetCommit(owner, repo, ref, page, perPage)

Get a commit

Returns the contents of a single commit reference. You must have &#x60;read&#x60; access for the repository to use this endpoint.  **Note:** If there are more than 300 files in the commit diff, the response will include pagination link headers for the remaining files, up to a limit of 3000 files. Each page contains the static commit information, and the only changes are to the file listing.  You can pass the appropriate [media type](https://docs.github.com/enterprise-server@2.22/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) to  fetch &#x60;diff&#x60; and &#x60;patch&#x60; formats. Diffs with binary data will have no &#x60;patch&#x60; property.  To return only the SHA-1 hash of the commit reference, you can provide the &#x60;sha&#x60; custom [media type](https://docs.github.com/enterprise-server@2.22/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) in the &#x60;Accept&#x60; header. You can use this endpoint to check if a remote reference&#39;s SHA-1 hash is the same as your local reference&#39;s SHA-1 hash by providing the local SHA-1 reference as the ETag.  **Signature verification object**  The response will include a &#x60;verification&#x60; object that describes the result of verifying the commit&#39;s signature. The following fields are included in the &#x60;verification&#x60; object:  | Name | Type | Description | | ---- | ---- | ----------- | | &#x60;verified&#x60; | &#x60;boolean&#x60; | Indicates whether GitHub considers the signature in this commit to be verified. | | &#x60;reason&#x60; | &#x60;string&#x60; | The reason for verified value. Possible values and their meanings are enumerated in table below. | | &#x60;signature&#x60; | &#x60;string&#x60; | The signature that was extracted from the commit. | | &#x60;payload&#x60; | &#x60;string&#x60; | The value that was signed. |  These are the possible values for &#x60;reason&#x60; in the &#x60;verification&#x60; object:  | Value | Description | | ----- | ----------- | | &#x60;expired_key&#x60; | The key that made the signature is expired. | | &#x60;not_signing_key&#x60; | The \&quot;signing\&quot; flag is not among the usage flags in the GPG key that made the signature. | | &#x60;gpgverify_error&#x60; | There was an error communicating with the signature verification service. | | &#x60;gpgverify_unavailable&#x60; | The signature verification service is currently unavailable. | | &#x60;unsigned&#x60; | The object does not include a signature. | | &#x60;unknown_signature_type&#x60; | A non-PGP signature was found in the commit. | | &#x60;no_user&#x60; | No user was associated with the &#x60;committer&#x60; email address in the commit. | | &#x60;unverified_email&#x60; | The &#x60;committer&#x60; email address in the commit was associated with a user, but the email address is not verified on her/his account. | | &#x60;bad_email&#x60; | The &#x60;committer&#x60; email address in the commit is not included in the identities of the PGP key that made the signature. | | &#x60;unknown_key&#x60; | The key that made the signature has not been registered with any user&#39;s account. | | &#x60;malformed_signature&#x60; | There was an error parsing the signature. | | &#x60;invalid&#x60; | The signature could not be cryptographically verified using the key whose key-id was found in the signature. | | &#x60;valid&#x60; | None of the above errors applied, so the signature is considered to be verified. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String ref = "ref_example"; // String | ref parameter
    Integer page = 1; // Integer | Page number of the results to fetch.
    Integer perPage = 30; // Integer | Results per page (max 100)
    try {
      Commit result = apiInstance.reposGetCommit(owner, repo, ref, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetCommit");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **ref** | **String**| ref parameter | |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |

### Return type

[**Commit**](Commit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |
| **500** | Internal Error |  -  |

<a id="reposGetCommitActivityStats"></a>
# **reposGetCommitActivityStats**
> List&lt;CommitActivity&gt; reposGetCommitActivityStats(owner, repo)

Get the last year of commit activity

Returns the last year of commit activity grouped by week. The &#x60;days&#x60; array is a group of commits per day, starting on &#x60;Sunday&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      List<CommitActivity> result = apiInstance.reposGetCommitActivityStats(owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetCommitActivityStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |

### Return type

[**List&lt;CommitActivity&gt;**](CommitActivity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **202** | Accepted |  -  |
| **204** | A header with no content is returned. |  -  |

<a id="reposGetCommitComment"></a>
# **reposGetCommitComment**
> CommitComment reposGetCommitComment(owner, repo, commentId)

Get a commit comment



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer commentId = 56; // Integer | comment_id parameter
    try {
      CommitComment result = apiInstance.reposGetCommitComment(owner, repo, commentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetCommitComment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **commentId** | **Integer**| comment_id parameter | |

### Return type

[**CommitComment**](CommitComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetCommitSignatureProtection"></a>
# **reposGetCommitSignatureProtection**
> ProtectedBranchAdminEnforced reposGetCommitSignatureProtection(owner, repo, branch)

Get commit signature protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  When authenticated with admin or owner permissions to the repository, you can use this endpoint to check whether a branch requires signed commits. An enabled status of &#x60;true&#x60; indicates you must sign commits on this branch. For more information, see [Signing commits with GPG](https://help.github.com/articles/signing-commits-with-gpg) in GitHub Help.  **Note**: You must enable branch protection to require signed commits.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      ProtectedBranchAdminEnforced result = apiInstance.reposGetCommitSignatureProtection(owner, repo, branch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetCommitSignatureProtection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

[**ProtectedBranchAdminEnforced**](ProtectedBranchAdminEnforced.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetContent"></a>
# **reposGetContent**
> ReposGetContent200Response reposGetContent(owner, repo, path, ref)

Get repository content

Gets the contents of a file or directory in a repository. Specify the file path or directory in &#x60;:path&#x60;. If you omit &#x60;:path&#x60;, you will receive the contents of the repository&#39;s root directory. See the description below regarding what the API response includes for directories.   Files and symlinks support [a custom media type](https://docs.github.com/enterprise-server@2.22/rest/reference/repos#custom-media-types) for retrieving the raw content or rendered HTML (when supported). All content types support [a custom media type](https://docs.github.com/enterprise-server@2.22/rest/reference/repos#custom-media-types) to ensure the content is returned in a consistent object format.  **Note**: *   To get a repository&#39;s contents recursively, you can [recursively get the tree](https://docs.github.com/enterprise-server@2.22/rest/reference/git#trees). *   This API has an upper limit of 1,000 files for a directory. If you need to retrieve more files, use the [Git Trees API](https://docs.github.com/enterprise-server@2.22/rest/reference/git#get-a-tree). *   This API supports files up to 1 megabyte in size.  #### If the content is a directory The response will be an array of objects, one object for each item in the directory. When listing the contents of a directory, submodules have their \&quot;type\&quot; specified as \&quot;file\&quot;. Logically, the value _should_ be \&quot;submodule\&quot;. This behavior exists in API v3 [for backwards compatibility purposes](https://git.io/v1YCW). In the next major version of the API, the type will be returned as \&quot;submodule\&quot;.  #### If the content is a symlink  If the requested &#x60;:path&#x60; points to a symlink, and the symlink&#39;s target is a normal file in the repository, then the API responds with the content of the file (in the format shown in the example. Otherwise, the API responds with an object  describing the symlink itself.  #### If the content is a submodule The &#x60;submodule_git_url&#x60; identifies the location of the submodule repository, and the &#x60;sha&#x60; identifies a specific commit within the submodule repository. Git uses the given URL when cloning the submodule repository, and checks out the submodule at that specific commit.  If the submodule repository is not hosted on github.com, the Git URLs (&#x60;git_url&#x60; and &#x60;_links[\&quot;git\&quot;]&#x60;) and the github.com URLs (&#x60;html_url&#x60; and &#x60;_links[\&quot;html\&quot;]&#x60;) will have null values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String path = "path_example"; // String | path parameter
    String ref = "ref_example"; // String | The name of the commit/branch/tag. Default: the repository’s default branch (usually `master`)
    try {
      ReposGetContent200Response result = apiInstance.reposGetContent(owner, repo, path, ref);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetContent");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **path** | **String**| path parameter | |
| **ref** | **String**| The name of the commit/branch/tag. Default: the repository’s default branch (usually &#x60;master&#x60;) | [optional] |

### Return type

[**ReposGetContent200Response**](ReposGetContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.github.v3.object

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **302** | Found |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetContributorsStats"></a>
# **reposGetContributorsStats**
> List&lt;ContributorActivity&gt; reposGetContributorsStats(owner, repo)

Get all contributor commit activity

 Returns the &#x60;total&#x60; number of commits authored by the contributor. In addition, the response includes a Weekly Hash (&#x60;weeks&#x60; array) with the following information:  *   &#x60;w&#x60; - Start of the week, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). *   &#x60;a&#x60; - Number of additions *   &#x60;d&#x60; - Number of deletions *   &#x60;c&#x60; - Number of commits

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      List<ContributorActivity> result = apiInstance.reposGetContributorsStats(owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetContributorsStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |

### Return type

[**List&lt;ContributorActivity&gt;**](ContributorActivity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | *   &#x60;w&#x60; - Start of the week, given as a [Unix timestamp](http://en.wikipedia.org/wiki/Unix_time). *   &#x60;a&#x60; - Number of additions *   &#x60;d&#x60; - Number of deletions *   &#x60;c&#x60; - Number of commits |  -  |
| **202** | Accepted |  -  |
| **204** | A header with no content is returned. |  -  |

<a id="reposGetDeployKey"></a>
# **reposGetDeployKey**
> DeployKey reposGetDeployKey(owner, repo, keyId)

Get a deploy key



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer keyId = 56; // Integer | key_id parameter
    try {
      DeployKey result = apiInstance.reposGetDeployKey(owner, repo, keyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetDeployKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **keyId** | **Integer**| key_id parameter | |

### Return type

[**DeployKey**](DeployKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetDeployment"></a>
# **reposGetDeployment**
> Deployment reposGetDeployment(owner, repo, deploymentId)

Get a deployment



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer deploymentId = 56; // Integer | deployment_id parameter
    try {
      Deployment result = apiInstance.reposGetDeployment(owner, repo, deploymentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetDeployment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **deploymentId** | **Integer**| deployment_id parameter | |

### Return type

[**Deployment**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetDeploymentStatus"></a>
# **reposGetDeploymentStatus**
> DeploymentStatus reposGetDeploymentStatus(owner, repo, deploymentId, statusId)

Get a deployment status

Users with pull access can view a deployment status for a deployment:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer deploymentId = 56; // Integer | deployment_id parameter
    Integer statusId = 56; // Integer | 
    try {
      DeploymentStatus result = apiInstance.reposGetDeploymentStatus(owner, repo, deploymentId, statusId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetDeploymentStatus");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **deploymentId** | **Integer**| deployment_id parameter | |
| **statusId** | **Integer**|  | |

### Return type

[**DeploymentStatus**](DeploymentStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetLatestPagesBuild"></a>
# **reposGetLatestPagesBuild**
> PageBuild reposGetLatestPagesBuild(owner, repo)

Get latest Pages build



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      PageBuild result = apiInstance.reposGetLatestPagesBuild(owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetLatestPagesBuild");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |

### Return type

[**PageBuild**](PageBuild.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="reposGetLatestRelease"></a>
# **reposGetLatestRelease**
> Release reposGetLatestRelease(owner, repo)

Get the latest release

View the latest published full release for the repository.  The latest release is the most recent non-prerelease, non-draft release, sorted by the &#x60;created_at&#x60; attribute. The &#x60;created_at&#x60; attribute is the date of the commit used for the release, and not the date when the release was drafted or published.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      Release result = apiInstance.reposGetLatestRelease(owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetLatestRelease");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |

### Return type

[**Release**](Release.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="reposGetPages"></a>
# **reposGetPages**
> Page reposGetPages(owner, repo)

Get a GitHub Enterprise Server Pages site



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      Page result = apiInstance.reposGetPages(owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetPages");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetPagesBuild"></a>
# **reposGetPagesBuild**
> PageBuild reposGetPagesBuild(owner, repo, buildId)

Get GitHub Enterprise Server Pages build



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer buildId = 56; // Integer | 
    try {
      PageBuild result = apiInstance.reposGetPagesBuild(owner, repo, buildId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetPagesBuild");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **buildId** | **Integer**|  | |

### Return type

[**PageBuild**](PageBuild.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="reposGetParticipationStats"></a>
# **reposGetParticipationStats**
> ParticipationStats reposGetParticipationStats(owner, repo)

Get the weekly commit count

Returns the total commit counts for the &#x60;owner&#x60; and total commit counts in &#x60;all&#x60;. &#x60;all&#x60; is everyone combined, including the &#x60;owner&#x60; in the last 52 weeks. If you&#39;d like to get the commit counts for non-owners, you can subtract &#x60;owner&#x60; from &#x60;all&#x60;.  The array order is oldest week (index 0) to most recent week.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      ParticipationStats result = apiInstance.reposGetParticipationStats(owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetParticipationStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |

### Return type

[**ParticipationStats**](ParticipationStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The array order is oldest week (index 0) to most recent week. |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetPullRequestReviewProtection"></a>
# **reposGetPullRequestReviewProtection**
> ProtectedBranchPullRequestReview reposGetPullRequestReviewProtection(owner, repo, branch)

Get pull request review protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      ProtectedBranchPullRequestReview result = apiInstance.reposGetPullRequestReviewProtection(owner, repo, branch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetPullRequestReviewProtection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

[**ProtectedBranchPullRequestReview**](ProtectedBranchPullRequestReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="reposGetPunchCardStats"></a>
# **reposGetPunchCardStats**
> List&lt;List&lt;Integer&gt;&gt; reposGetPunchCardStats(owner, repo)

Get the hourly commit count for each day

Each array contains the day number, hour number, and number of commits:  *   &#x60;0-6&#x60;: Sunday - Saturday *   &#x60;0-23&#x60;: Hour of day *   Number of commits  For example, &#x60;[2, 14, 25]&#x60; indicates that there were 25 total commits, during the 2:00pm hour on Tuesdays. All times are based on the time zone of individual commits.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      List<List<Integer>> result = apiInstance.reposGetPunchCardStats(owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetPunchCardStats");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |

### Return type

[**List&lt;List&lt;Integer&gt;&gt;**](List.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | For example, &#x60;[2, 14, 25]&#x60; indicates that there were 25 total commits, during the 2:00pm hour on Tuesdays. All times are based on the time zone of individual commits. |  -  |
| **204** | A header with no content is returned. |  -  |

<a id="reposGetReadme"></a>
# **reposGetReadme**
> ContentFile reposGetReadme(owner, repo, ref)

Get a repository README

Gets the preferred README for a repository.  READMEs support [custom media types](https://docs.github.com/enterprise-server@2.22/rest/reference/repos#custom-media-types) for retrieving the raw content or rendered HTML.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String ref = "ref_example"; // String | The name of the commit/branch/tag. Default: the repository’s default branch (usually `master`)
    try {
      ContentFile result = apiInstance.reposGetReadme(owner, repo, ref);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetReadme");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **ref** | **String**| The name of the commit/branch/tag. Default: the repository’s default branch (usually &#x60;master&#x60;) | [optional] |

### Return type

[**ContentFile**](ContentFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="reposGetReadmeInDirectory"></a>
# **reposGetReadmeInDirectory**
> ContentFile reposGetReadmeInDirectory(owner, repo, dir, ref)

Get a repository README for a directory

Gets the README from a repository directory.  READMEs support [custom media types](https://docs.github.com/enterprise-server@2.22/rest/reference/repos#custom-media-types) for retrieving the raw content or rendered HTML.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String dir = "dir_example"; // String | The alternate path to look for a README file
    String ref = "ref_example"; // String | The name of the commit/branch/tag. Default: the repository’s default branch (usually `master`)
    try {
      ContentFile result = apiInstance.reposGetReadmeInDirectory(owner, repo, dir, ref);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetReadmeInDirectory");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **dir** | **String**| The alternate path to look for a README file | |
| **ref** | **String**| The name of the commit/branch/tag. Default: the repository’s default branch (usually &#x60;master&#x60;) | [optional] |

### Return type

[**ContentFile**](ContentFile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="reposGetRelease"></a>
# **reposGetRelease**
> Release reposGetRelease(owner, repo, releaseId)

Get a release

**Note:** This returns an &#x60;upload_url&#x60; key corresponding to the endpoint for uploading release assets. This key is a [hypermedia resource](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#hypermedia).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer releaseId = 56; // Integer | release_id parameter
    try {
      Release result = apiInstance.reposGetRelease(owner, repo, releaseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetRelease");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **releaseId** | **Integer**| release_id parameter | |

### Return type

[**Release**](Release.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | **Note:** This returns an &#x60;upload_url&#x60; key corresponding to the endpoint for uploading release assets. This key is a [hypermedia resource](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#hypermedia). |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetReleaseAsset"></a>
# **reposGetReleaseAsset**
> ReleaseAsset reposGetReleaseAsset(owner, repo, assetId)

Get a release asset

To download the asset&#39;s binary content, set the &#x60;Accept&#x60; header of the request to [&#x60;application/octet-stream&#x60;](https://docs.github.com/enterprise-server@2.22/rest/overview/media-types). The API will either redirect the client to the location, or stream it directly if possible. API clients should handle both a &#x60;200&#x60; or &#x60;302&#x60; response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer assetId = 56; // Integer | asset_id parameter
    try {
      ReleaseAsset result = apiInstance.reposGetReleaseAsset(owner, repo, assetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetReleaseAsset");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **assetId** | **Integer**| asset_id parameter | |

### Return type

[**ReleaseAsset**](ReleaseAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | To download the asset&#39;s binary content, set the &#x60;Accept&#x60; header of the request to [&#x60;application/octet-stream&#x60;](https://docs.github.com/enterprise-server@2.22/rest/overview/media-types). The API will either redirect the client to the location, or stream it directly if possible. API clients should handle both a &#x60;200&#x60; or &#x60;302&#x60; response. |  -  |
| **302** | Found |  -  |
| **404** | Resource not found |  -  |
| **415** | Preview header missing |  -  |

<a id="reposGetReleaseByTag"></a>
# **reposGetReleaseByTag**
> Release reposGetReleaseByTag(owner, repo, tag)

Get a release by tag name

Get a published release with the specified tag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String tag = "tag_example"; // String | tag parameter
    try {
      Release result = apiInstance.reposGetReleaseByTag(owner, repo, tag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetReleaseByTag");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **tag** | **String**| tag parameter | |

### Return type

[**Release**](Release.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetStatusChecksProtection"></a>
# **reposGetStatusChecksProtection**
> StatusCheckPolicy reposGetStatusChecksProtection(owner, repo, branch)

Get status checks protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      StatusCheckPolicy result = apiInstance.reposGetStatusChecksProtection(owner, repo, branch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetStatusChecksProtection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

[**StatusCheckPolicy**](StatusCheckPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetTeamsWithAccessToProtectedBranch"></a>
# **reposGetTeamsWithAccessToProtectedBranch**
> List&lt;Team&gt; reposGetTeamsWithAccessToProtectedBranch(owner, repo, branch)

Get teams with access to the protected branch

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists the teams who have push access to this branch. The list includes child teams.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      List<Team> result = apiInstance.reposGetTeamsWithAccessToProtectedBranch(owner, repo, branch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetTeamsWithAccessToProtectedBranch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

[**List&lt;Team&gt;**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetUsersWithAccessToProtectedBranch"></a>
# **reposGetUsersWithAccessToProtectedBranch**
> List&lt;SimpleUser&gt; reposGetUsersWithAccessToProtectedBranch(owner, repo, branch)

Get users with access to the protected branch

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists the people who have push access to this branch.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      List<SimpleUser> result = apiInstance.reposGetUsersWithAccessToProtectedBranch(owner, repo, branch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetUsersWithAccessToProtectedBranch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

[**List&lt;SimpleUser&gt;**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposGetWebhook"></a>
# **reposGetWebhook**
> Hook reposGetWebhook(owner, repo, hookId)

Get a repository webhook

Returns a webhook configured in a repository. To get only the webhook &#x60;config&#x60; properties, see \&quot;[Get a webhook configuration for a repository](/rest/reference/repos#get-a-webhook-configuration-for-a-repository).\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer hookId = 56; // Integer | 
    try {
      Hook result = apiInstance.reposGetWebhook(owner, repo, hookId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposGetWebhook");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **hookId** | **Integer**|  | |

### Return type

[**Hook**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposListBranches"></a>
# **reposListBranches**
> List&lt;ShortBranch&gt; reposListBranches(owner, repo, _protected, perPage, page)

List branches



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Boolean _protected = true; // Boolean | Setting to `true` returns only protected branches. When set to `false`, only unprotected branches are returned. Omitting this parameter returns all branches.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<ShortBranch> result = apiInstance.reposListBranches(owner, repo, _protected, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListBranches");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **_protected** | **Boolean**| Setting to &#x60;true&#x60; returns only protected branches. When set to &#x60;false&#x60;, only unprotected branches are returned. Omitting this parameter returns all branches. | [optional] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;ShortBranch&gt;**](ShortBranch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **404** | Resource not found |  -  |

<a id="reposListBranchesForHeadCommit"></a>
# **reposListBranchesForHeadCommit**
> List&lt;BranchShort&gt; reposListBranchesForHeadCommit(owner, repo, commitSha)

List branches for HEAD commit

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Returns all branches where the given commit SHA is the HEAD, or latest commit for the branch.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String commitSha = "commitSha_example"; // String | commit_sha parameter
    try {
      List<BranchShort> result = apiInstance.reposListBranchesForHeadCommit(owner, repo, commitSha);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListBranchesForHeadCommit");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **commitSha** | **String**| commit_sha parameter | |

### Return type

[**List&lt;BranchShort&gt;**](BranchShort.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **422** | Validation failed |  -  |

<a id="reposListCollaborators"></a>
# **reposListCollaborators**
> List&lt;Collaborator&gt; reposListCollaborators(owner, repo, affiliation, perPage, page)

List repository collaborators

For organization-owned repositories, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners.  Team members will include the members of child teams.  You must have push access to the repository in order to list collaborators.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String affiliation = "outside"; // String | Filter collaborators returned by their affiliation. Can be one of:   \\* `outside`: All outside collaborators of an organization-owned repository.   \\* `direct`: All collaborators with permissions to an organization-owned repository, regardless of organization membership status.   \\* `all`: All collaborators the authenticated user can see.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Collaborator> result = apiInstance.reposListCollaborators(owner, repo, affiliation, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListCollaborators");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **affiliation** | **String**| Filter collaborators returned by their affiliation. Can be one of:   \\* &#x60;outside&#x60;: All outside collaborators of an organization-owned repository.   \\* &#x60;direct&#x60;: All collaborators with permissions to an organization-owned repository, regardless of organization membership status.   \\* &#x60;all&#x60;: All collaborators the authenticated user can see. | [optional] [default to all] [enum: outside, direct, all] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Collaborator&gt;**](Collaborator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **404** | Resource not found |  -  |

<a id="reposListCommentsForCommit"></a>
# **reposListCommentsForCommit**
> List&lt;CommitComment&gt; reposListCommentsForCommit(owner, repo, commitSha, perPage, page)

List commit comments

Use the &#x60;:commit_sha&#x60; to specify the commit that will have its comments listed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String commitSha = "commitSha_example"; // String | commit_sha parameter
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<CommitComment> result = apiInstance.reposListCommentsForCommit(owner, repo, commitSha, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListCommentsForCommit");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **commitSha** | **String**| commit_sha parameter | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;CommitComment&gt;**](CommitComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="reposListCommitCommentsForRepo"></a>
# **reposListCommitCommentsForRepo**
> List&lt;CommitComment&gt; reposListCommitCommentsForRepo(owner, repo, perPage, page)

List commit comments for a repository

Commit Comments use [these custom media types](https://docs.github.com/enterprise-server@2.22/rest/reference/repos#custom-media-types). You can read more about the use of media types in the API [here](https://docs.github.com/enterprise-server@2.22/rest/overview/media-types/).  Comments are ordered by ascending ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<CommitComment> result = apiInstance.reposListCommitCommentsForRepo(owner, repo, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListCommitCommentsForRepo");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;CommitComment&gt;**](CommitComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="reposListCommitStatusesForRef"></a>
# **reposListCommitStatusesForRef**
> List&lt;Status&gt; reposListCommitStatusesForRef(owner, repo, ref, perPage, page)

List commit statuses for a reference

Users with pull access in a repository can view commit statuses for a given ref. The ref can be a SHA, a branch name, or a tag name. Statuses are returned in reverse chronological order. The first status in the list will be the latest one.  This resource is also available via a legacy route: &#x60;GET /repos/:owner/:repo/statuses/:ref&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String ref = "ref_example"; // String | ref parameter
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Status> result = apiInstance.reposListCommitStatusesForRef(owner, repo, ref, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListCommitStatusesForRef");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **ref** | **String**| ref parameter | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Status&gt;**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **301** | Moved permanently |  -  |

<a id="reposListCommits"></a>
# **reposListCommits**
> List&lt;Commit&gt; reposListCommits(owner, repo, sha, path, author, since, until, perPage, page)

List commits

**Signature verification object**  The response will include a &#x60;verification&#x60; object that describes the result of verifying the commit&#39;s signature. The following fields are included in the &#x60;verification&#x60; object:  | Name | Type | Description | | ---- | ---- | ----------- | | &#x60;verified&#x60; | &#x60;boolean&#x60; | Indicates whether GitHub considers the signature in this commit to be verified. | | &#x60;reason&#x60; | &#x60;string&#x60; | The reason for verified value. Possible values and their meanings are enumerated in table below. | | &#x60;signature&#x60; | &#x60;string&#x60; | The signature that was extracted from the commit. | | &#x60;payload&#x60; | &#x60;string&#x60; | The value that was signed. |  These are the possible values for &#x60;reason&#x60; in the &#x60;verification&#x60; object:  | Value | Description | | ----- | ----------- | | &#x60;expired_key&#x60; | The key that made the signature is expired. | | &#x60;not_signing_key&#x60; | The \&quot;signing\&quot; flag is not among the usage flags in the GPG key that made the signature. | | &#x60;gpgverify_error&#x60; | There was an error communicating with the signature verification service. | | &#x60;gpgverify_unavailable&#x60; | The signature verification service is currently unavailable. | | &#x60;unsigned&#x60; | The object does not include a signature. | | &#x60;unknown_signature_type&#x60; | A non-PGP signature was found in the commit. | | &#x60;no_user&#x60; | No user was associated with the &#x60;committer&#x60; email address in the commit. | | &#x60;unverified_email&#x60; | The &#x60;committer&#x60; email address in the commit was associated with a user, but the email address is not verified on her/his account. | | &#x60;bad_email&#x60; | The &#x60;committer&#x60; email address in the commit is not included in the identities of the PGP key that made the signature. | | &#x60;unknown_key&#x60; | The key that made the signature has not been registered with any user&#39;s account. | | &#x60;malformed_signature&#x60; | There was an error parsing the signature. | | &#x60;invalid&#x60; | The signature could not be cryptographically verified using the key whose key-id was found in the signature. | | &#x60;valid&#x60; | None of the above errors applied, so the signature is considered to be verified. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String sha = "sha_example"; // String | SHA or branch to start listing commits from. Default: the repository’s default branch (usually `master`).
    String path = "path_example"; // String | Only commits containing this file path will be returned.
    String author = "author_example"; // String | GitHub login or email address by which to filter by commit author.
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    OffsetDateTime until = OffsetDateTime.now(); // OffsetDateTime | Only commits before this date will be returned. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Commit> result = apiInstance.reposListCommits(owner, repo, sha, path, author, since, until, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListCommits");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **sha** | **String**| SHA or branch to start listing commits from. Default: the repository’s default branch (usually &#x60;master&#x60;). | [optional] |
| **path** | **String**| Only commits containing this file path will be returned. | [optional] |
| **author** | **String**| GitHub login or email address by which to filter by commit author. | [optional] |
| **since** | **OffsetDateTime**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **until** | **OffsetDateTime**| Only commits before this date will be returned. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Commit&gt;**](Commit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **400** | Bad Request |  -  |
| **404** | Resource not found |  -  |
| **409** | Conflict |  -  |
| **500** | Internal Error |  -  |

<a id="reposListContributors"></a>
# **reposListContributors**
> List&lt;Contributor&gt; reposListContributors(owner, repo, anon, perPage, page)

List repository contributors

Lists contributors to the specified repository and sorts them by the number of commits per contributor in descending order. This endpoint may return information that is a few hours old because the GitHub REST API v3 caches contributor data to improve performance.  GitHub identifies contributors by author email address. This endpoint groups contribution counts by GitHub user, which includes all associated email addresses. To improve performance, only the first 500 author email addresses in the repository link to GitHub users. The rest will appear as anonymous contributors without associated GitHub user information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String anon = "anon_example"; // String | Set to `1` or `true` to include anonymous contributors in results.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Contributor> result = apiInstance.reposListContributors(owner, repo, anon, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListContributors");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **anon** | **String**| Set to &#x60;1&#x60; or &#x60;true&#x60; to include anonymous contributors in results. | [optional] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Contributor&gt;**](Contributor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | if repository contains content |  * Link -  <br>  |
| **204** | Response if repository is empty |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="reposListDeployKeys"></a>
# **reposListDeployKeys**
> List&lt;DeployKey&gt; reposListDeployKeys(owner, repo, perPage, page)

List deploy keys



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<DeployKey> result = apiInstance.reposListDeployKeys(owner, repo, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListDeployKeys");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;DeployKey&gt;**](DeployKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="reposListDeploymentStatuses"></a>
# **reposListDeploymentStatuses**
> List&lt;DeploymentStatus&gt; reposListDeploymentStatuses(owner, repo, deploymentId, perPage, page)

List deployment statuses

Users with pull access can view deployment statuses for a deployment:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer deploymentId = 56; // Integer | deployment_id parameter
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<DeploymentStatus> result = apiInstance.reposListDeploymentStatuses(owner, repo, deploymentId, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListDeploymentStatuses");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **deploymentId** | **Integer**| deployment_id parameter | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;DeploymentStatus&gt;**](DeploymentStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **404** | Resource not found |  -  |

<a id="reposListDeployments"></a>
# **reposListDeployments**
> List&lt;Deployment&gt; reposListDeployments(owner, repo, sha, ref, task, environment, perPage, page)

List deployments

Simple filtering of deployments is available via query parameters:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String sha = "none"; // String | The SHA recorded at creation time.
    String ref = "none"; // String | The name of the ref. This can be a branch, tag, or SHA.
    String task = "none"; // String | The name of the task for the deployment (e.g., `deploy` or `deploy:migrations`).
    String environment = "none"; // String | The name of the environment that was deployed to (e.g., `staging` or `production`).
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Deployment> result = apiInstance.reposListDeployments(owner, repo, sha, ref, task, environment, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListDeployments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **sha** | **String**| The SHA recorded at creation time. | [optional] [default to none] |
| **ref** | **String**| The name of the ref. This can be a branch, tag, or SHA. | [optional] [default to none] |
| **task** | **String**| The name of the task for the deployment (e.g., &#x60;deploy&#x60; or &#x60;deploy:migrations&#x60;). | [optional] [default to none] |
| **environment** | **String**| The name of the environment that was deployed to (e.g., &#x60;staging&#x60; or &#x60;production&#x60;). | [optional] [default to none] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Deployment&gt;**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="reposListForAuthenticatedUser"></a>
# **reposListForAuthenticatedUser**
> List&lt;Repository&gt; reposListForAuthenticatedUser(visibility, affiliation, type, sort, direction, perPage, page, since, before)

List repositories for the authenticated user

Lists repositories that the authenticated user has explicit permission (&#x60;:read&#x60;, &#x60;:write&#x60;, or &#x60;:admin&#x60;) to access.  The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String visibility = "all"; // String | Can be one of `all`, `public`, or `private`. Note: For GitHub AE, can be one of `all`, `internal`, or `private`.
    String affiliation = "owner,collaborator,organization_member"; // String | Comma-separated list of values. Can include:   \\* `owner`: Repositories that are owned by the authenticated user.   \\* `collaborator`: Repositories that the user has been added to as a collaborator.   \\* `organization_member`: Repositories that the user has access to through being a member of an organization. This includes every repository on every team that the user is on.
    String type = "all"; // String | Can be one of `all`, `owner`, `public`, `private`, `member`. Note: For GitHub AE, can be one of `all`, `owner`, `internal`, `private`, `member`. Default: `all`      Will cause a `422` error if used in the same request as **visibility** or **affiliation**. Will cause a `422` error if used in the same request as **visibility** or **affiliation**.
    String sort = "created"; // String | Can be one of `created`, `updated`, `pushed`, `full_name`.
    String direction = "asc"; // String | Can be one of `asc` or `desc`. Default: `asc` when using `full_name`, otherwise `desc`
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    OffsetDateTime before = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    try {
      List<Repository> result = apiInstance.reposListForAuthenticatedUser(visibility, affiliation, type, sort, direction, perPage, page, since, before);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListForAuthenticatedUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **visibility** | **String**| Can be one of &#x60;all&#x60;, &#x60;public&#x60;, or &#x60;private&#x60;. Note: For GitHub AE, can be one of &#x60;all&#x60;, &#x60;internal&#x60;, or &#x60;private&#x60;. | [optional] [default to all] [enum: all, public, private] |
| **affiliation** | **String**| Comma-separated list of values. Can include:   \\* &#x60;owner&#x60;: Repositories that are owned by the authenticated user.   \\* &#x60;collaborator&#x60;: Repositories that the user has been added to as a collaborator.   \\* &#x60;organization_member&#x60;: Repositories that the user has access to through being a member of an organization. This includes every repository on every team that the user is on. | [optional] [default to owner,collaborator,organization_member] |
| **type** | **String**| Can be one of &#x60;all&#x60;, &#x60;owner&#x60;, &#x60;public&#x60;, &#x60;private&#x60;, &#x60;member&#x60;. Note: For GitHub AE, can be one of &#x60;all&#x60;, &#x60;owner&#x60;, &#x60;internal&#x60;, &#x60;private&#x60;, &#x60;member&#x60;. Default: &#x60;all&#x60;      Will cause a &#x60;422&#x60; error if used in the same request as **visibility** or **affiliation**. Will cause a &#x60;422&#x60; error if used in the same request as **visibility** or **affiliation**. | [optional] [default to all] [enum: all, owner, public, private, member] |
| **sort** | **String**| Can be one of &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;pushed&#x60;, &#x60;full_name&#x60;. | [optional] [default to full_name] [enum: created, updated, pushed, full_name] |
| **direction** | **String**| Can be one of &#x60;asc&#x60; or &#x60;desc&#x60;. Default: &#x60;asc&#x60; when using &#x60;full_name&#x60;, otherwise &#x60;desc&#x60; | [optional] [enum: asc, desc] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **since** | **OffsetDateTime**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **before** | **OffsetDateTime**| Only show notifications updated before the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |

### Return type

[**List&lt;Repository&gt;**](Repository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |
| **422** | Validation failed |  -  |

<a id="reposListForOrg"></a>
# **reposListForOrg**
> List&lt;MinimalRepository&gt; reposListForOrg(org, type, sort, direction, perPage, page)

List organization repositories

Lists repositories for the specified organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String org = "org_example"; // String | 
    String type = "all"; // String | Specifies the types of repositories you want returned. Can be one of `all`, `public`, `private`, `forks`, `sources`, `member`, `internal`. Note: For GitHub AE, can be one of `all`, `private`, `forks`, `sources`, `member`, `internal`. Default: `all`. If your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+, `type` can also be `internal`. However, the `internal` value is not yet supported when a GitHub App calls this API with an installation access token.
    String sort = "created"; // String | Can be one of `created`, `updated`, `pushed`, `full_name`.
    String direction = "asc"; // String | Can be one of `asc` or `desc`. Default: when using `full_name`: `asc`, otherwise `desc`
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<MinimalRepository> result = apiInstance.reposListForOrg(org, type, sort, direction, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListForOrg");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **org** | **String**|  | |
| **type** | **String**| Specifies the types of repositories you want returned. Can be one of &#x60;all&#x60;, &#x60;public&#x60;, &#x60;private&#x60;, &#x60;forks&#x60;, &#x60;sources&#x60;, &#x60;member&#x60;, &#x60;internal&#x60;. Note: For GitHub AE, can be one of &#x60;all&#x60;, &#x60;private&#x60;, &#x60;forks&#x60;, &#x60;sources&#x60;, &#x60;member&#x60;, &#x60;internal&#x60;. Default: &#x60;all&#x60;. If your organization is associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+, &#x60;type&#x60; can also be &#x60;internal&#x60;. However, the &#x60;internal&#x60; value is not yet supported when a GitHub App calls this API with an installation access token. | [optional] [enum: all, public, private, forks, sources, member, internal] |
| **sort** | **String**| Can be one of &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;pushed&#x60;, &#x60;full_name&#x60;. | [optional] [default to created] [enum: created, updated, pushed, full_name] |
| **direction** | **String**| Can be one of &#x60;asc&#x60; or &#x60;desc&#x60;. Default: when using &#x60;full_name&#x60;: &#x60;asc&#x60;, otherwise &#x60;desc&#x60; | [optional] [enum: asc, desc] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;MinimalRepository&gt;**](MinimalRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="reposListForUser"></a>
# **reposListForUser**
> List&lt;MinimalRepository&gt; reposListForUser(username, type, sort, direction, perPage, page)

List repositories for a user

Lists public repositories for the specified user. Note: For GitHub AE, this endpoint will list internal repositories for the specified user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String username = "username_example"; // String | 
    String type = "all"; // String | Can be one of `all`, `owner`, `member`.
    String sort = "created"; // String | Can be one of `created`, `updated`, `pushed`, `full_name`.
    String direction = "asc"; // String | Can be one of `asc` or `desc`. Default: `asc` when using `full_name`, otherwise `desc`
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<MinimalRepository> result = apiInstance.reposListForUser(username, type, sort, direction, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListForUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**|  | |
| **type** | **String**| Can be one of &#x60;all&#x60;, &#x60;owner&#x60;, &#x60;member&#x60;. | [optional] [default to owner] [enum: all, owner, member] |
| **sort** | **String**| Can be one of &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;pushed&#x60;, &#x60;full_name&#x60;. | [optional] [default to full_name] [enum: created, updated, pushed, full_name] |
| **direction** | **String**| Can be one of &#x60;asc&#x60; or &#x60;desc&#x60;. Default: &#x60;asc&#x60; when using &#x60;full_name&#x60;, otherwise &#x60;desc&#x60; | [optional] [enum: asc, desc] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;MinimalRepository&gt;**](MinimalRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="reposListForks"></a>
# **reposListForks**
> List&lt;MinimalRepository&gt; reposListForks(owner, repo, sort, perPage, page)

List forks



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String sort = "newest"; // String | The sort order. Can be either `newest`, `oldest`, or `stargazers`.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<MinimalRepository> result = apiInstance.reposListForks(owner, repo, sort, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListForks");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **sort** | **String**| The sort order. Can be either &#x60;newest&#x60;, &#x60;oldest&#x60;, or &#x60;stargazers&#x60;. | [optional] [default to newest] [enum: newest, oldest, stargazers, watchers] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;MinimalRepository&gt;**](MinimalRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/scim+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **400** | Bad Request |  -  |

<a id="reposListInvitations"></a>
# **reposListInvitations**
> List&lt;RepositoryInvitation&gt; reposListInvitations(owner, repo, perPage, page)

List repository invitations

When authenticating as a user with admin rights to a repository, this endpoint will list all currently open repository invitations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<RepositoryInvitation> result = apiInstance.reposListInvitations(owner, repo, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListInvitations");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;RepositoryInvitation&gt;**](RepositoryInvitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="reposListInvitationsForAuthenticatedUser"></a>
# **reposListInvitationsForAuthenticatedUser**
> List&lt;RepositoryInvitation&gt; reposListInvitationsForAuthenticatedUser(perPage, page)

List repository invitations for the authenticated user

When authenticating as a user, this endpoint will list all currently open repository invitations for that user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<RepositoryInvitation> result = apiInstance.reposListInvitationsForAuthenticatedUser(perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListInvitationsForAuthenticatedUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;RepositoryInvitation&gt;**](RepositoryInvitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="reposListLanguages"></a>
# **reposListLanguages**
> Map&lt;String, Integer&gt; reposListLanguages(owner, repo)

List repository languages

Lists languages for the specified repository. The value shown for each language is the number of bytes of code written in that language.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      Map<String, Integer> result = apiInstance.reposListLanguages(owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListLanguages");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |

### Return type

**Map&lt;String, Integer&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="reposListPagesBuilds"></a>
# **reposListPagesBuilds**
> List&lt;PageBuild&gt; reposListPagesBuilds(owner, repo, perPage, page)

List GitHub Enterprise Server Pages builds



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<PageBuild> result = apiInstance.reposListPagesBuilds(owner, repo, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListPagesBuilds");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;PageBuild&gt;**](PageBuild.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="reposListPublic"></a>
# **reposListPublic**
> List&lt;MinimalRepository&gt; reposListPublic(since, visibility)

List public repositories

Lists all public repositories in the order that they were created.  Note: - For GitHub Enterprise Server, this endpoint will only list repositories available to all users on the enterprise. - Pagination is powered exclusively by the &#x60;since&#x60; parameter. Use the [Link header](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#link-header) to get the URL for the next page of repositories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    Integer since = 56; // Integer | A repository ID. Only return repositories with an ID greater than this ID.
    String visibility = "all"; // String | Specifies the types of repositories to return. Can be one of `all` or `public`. Default: `public`. Note: For GitHub Enterprise Server and GitHub AE, this endpoint will only list repositories available to all users on the enterprise.
    try {
      List<MinimalRepository> result = apiInstance.reposListPublic(since, visibility);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListPublic");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **since** | **Integer**| A repository ID. Only return repositories with an ID greater than this ID. | [optional] |
| **visibility** | **String**| Specifies the types of repositories to return. Can be one of &#x60;all&#x60; or &#x60;public&#x60;. Default: &#x60;public&#x60;. Note: For GitHub Enterprise Server and GitHub AE, this endpoint will only list repositories available to all users on the enterprise. | [optional] [default to public] [enum: all, public] |

### Return type

[**List&lt;MinimalRepository&gt;**](MinimalRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **304** | Not modified |  -  |
| **422** | Validation failed |  -  |

<a id="reposListPullRequestsAssociatedWithCommit"></a>
# **reposListPullRequestsAssociatedWithCommit**
> List&lt;PullRequestSimple&gt; reposListPullRequestsAssociatedWithCommit(owner, repo, commitSha, perPage, page)

List pull requests associated with a commit

Lists the merged pull request that introduced the commit to the repository. If the commit is not present in the default branch, additionally returns open pull requests associated with the commit. The results may include open and closed pull requests. Additional preview headers may be required to see certain details for associated pull requests, such as whether a pull request is in a draft state. For more information about previews that might affect this endpoint, see the [List pull requests](https://docs.github.com/enterprise-server@2.22/rest/reference/pulls#list-pull-requests) endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String commitSha = "commitSha_example"; // String | commit_sha parameter
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<PullRequestSimple> result = apiInstance.reposListPullRequestsAssociatedWithCommit(owner, repo, commitSha, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListPullRequestsAssociatedWithCommit");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **commitSha** | **String**| commit_sha parameter | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;PullRequestSimple&gt;**](PullRequestSimple.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="reposListReleaseAssets"></a>
# **reposListReleaseAssets**
> List&lt;ReleaseAsset&gt; reposListReleaseAssets(owner, repo, releaseId, perPage, page)

List release assets



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer releaseId = 56; // Integer | release_id parameter
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<ReleaseAsset> result = apiInstance.reposListReleaseAssets(owner, repo, releaseId, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListReleaseAssets");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **releaseId** | **Integer**| release_id parameter | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;ReleaseAsset&gt;**](ReleaseAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="reposListReleases"></a>
# **reposListReleases**
> List&lt;Release&gt; reposListReleases(owner, repo, perPage, page)

List releases

This returns a list of releases, which does not include regular Git tags that have not been associated with a release. To get a list of Git tags, use the [Repository Tags API](https://docs.github.com/enterprise-server@2.22/rest/reference/repos#list-repository-tags).  Information about published releases are available to everyone. Only users with push access will receive listings for draft releases.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Release> result = apiInstance.reposListReleases(owner, repo, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListReleases");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Release&gt;**](Release.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **404** | Resource not found |  -  |

<a id="reposListTags"></a>
# **reposListTags**
> List&lt;Tag&gt; reposListTags(owner, repo, perPage, page)

List repository tags



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Tag> result = apiInstance.reposListTags(owner, repo, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListTags");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Tag&gt;**](Tag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="reposListTeams"></a>
# **reposListTeams**
> List&lt;Team&gt; reposListTeams(owner, repo, perPage, page)

List repository teams



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Team> result = apiInstance.reposListTeams(owner, repo, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListTeams");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Team&gt;**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="reposListWebhooks"></a>
# **reposListWebhooks**
> List&lt;Hook&gt; reposListWebhooks(owner, repo, perPage, page)

List repository webhooks



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Hook> result = apiInstance.reposListWebhooks(owner, repo, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposListWebhooks");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Hook&gt;**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **404** | Resource not found |  -  |

<a id="reposMerge"></a>
# **reposMerge**
> Commit reposMerge(owner, repo, reposMergeRequest)

Merge a branch



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    ReposMergeRequest reposMergeRequest = new ReposMergeRequest(); // ReposMergeRequest | 
    try {
      Commit result = apiInstance.reposMerge(owner, repo, reposMergeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposMerge");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **reposMergeRequest** | [**ReposMergeRequest**](ReposMergeRequest.md)|  | |

### Return type

[**Commit**](Commit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response (The resulting merge commit) |  -  |
| **204** | Response when already merged |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found when the base or head does not exist |  -  |
| **409** | Conflict when there is a merge conflict |  -  |
| **422** | Validation failed |  -  |

<a id="reposPingWebhook"></a>
# **reposPingWebhook**
> reposPingWebhook(owner, repo, hookId)

Ping a repository webhook

This will trigger a [ping event](https://docs.github.com/enterprise-server@2.22/webhooks/#ping-event) to be sent to the hook.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer hookId = 56; // Integer | 
    try {
      apiInstance.reposPingWebhook(owner, repo, hookId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposPingWebhook");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **hookId** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposRemoveAppAccessRestrictions"></a>
# **reposRemoveAppAccessRestrictions**
> List&lt;Integration&gt; reposRemoveAppAccessRestrictions(owner, repo, branch, reposSetAppAccessRestrictionsRequest)

Remove app access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Removes the ability of an app to push to this branch. Only installed GitHub Apps with &#x60;write&#x60; access to the &#x60;contents&#x60; permission can be added as authorized actors on a protected branch.  | Type    | Description                                                                                                                                                | | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | | &#x60;array&#x60; | The GitHub Apps that have push access to this branch. Use the app&#39;s &#x60;slug&#x60;. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    ReposSetAppAccessRestrictionsRequest reposSetAppAccessRestrictionsRequest = new ReposSetAppAccessRestrictionsRequest(); // ReposSetAppAccessRestrictionsRequest | 
    try {
      List<Integration> result = apiInstance.reposRemoveAppAccessRestrictions(owner, repo, branch, reposSetAppAccessRestrictionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposRemoveAppAccessRestrictions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |
| **reposSetAppAccessRestrictionsRequest** | [**ReposSetAppAccessRestrictionsRequest**](ReposSetAppAccessRestrictionsRequest.md)|  | [optional] |

### Return type

[**List&lt;Integration&gt;**](Integration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **422** | Validation failed |  -  |

<a id="reposRemoveCollaborator"></a>
# **reposRemoveCollaborator**
> reposRemoveCollaborator(owner, repo, username)

Remove a repository collaborator



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String username = "username_example"; // String | 
    try {
      apiInstance.reposRemoveCollaborator(owner, repo, username);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposRemoveCollaborator");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **username** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="reposRemoveStatusCheckContexts"></a>
# **reposRemoveStatusCheckContexts**
> List&lt;String&gt; reposRemoveStatusCheckContexts(owner, repo, branch, reposSetStatusCheckContextsRequest)

Remove status check contexts

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    ReposSetStatusCheckContextsRequest reposSetStatusCheckContextsRequest = new ReposSetStatusCheckContextsRequest(); // ReposSetStatusCheckContextsRequest | 
    try {
      List<String> result = apiInstance.reposRemoveStatusCheckContexts(owner, repo, branch, reposSetStatusCheckContextsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposRemoveStatusCheckContexts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |
| **reposSetStatusCheckContextsRequest** | [**ReposSetStatusCheckContextsRequest**](ReposSetStatusCheckContextsRequest.md)|  | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="reposRemoveStatusCheckProtection"></a>
# **reposRemoveStatusCheckProtection**
> reposRemoveStatusCheckProtection(owner, repo, branch)

Remove status check protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      apiInstance.reposRemoveStatusCheckProtection(owner, repo, branch);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposRemoveStatusCheckProtection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="reposRemoveTeamAccessRestrictions"></a>
# **reposRemoveTeamAccessRestrictions**
> List&lt;Team&gt; reposRemoveTeamAccessRestrictions(owner, repo, branch, reposSetTeamAccessRestrictionsRequest)

Remove team access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Removes the ability of a team to push to this branch. You can also remove push access for child teams.  | Type    | Description                                                                                                                                         | | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | | &#x60;array&#x60; | Teams that should no longer have push access. Use the team&#39;s &#x60;slug&#x60;. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    ReposSetTeamAccessRestrictionsRequest reposSetTeamAccessRestrictionsRequest = new ReposSetTeamAccessRestrictionsRequest(); // ReposSetTeamAccessRestrictionsRequest | 
    try {
      List<Team> result = apiInstance.reposRemoveTeamAccessRestrictions(owner, repo, branch, reposSetTeamAccessRestrictionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposRemoveTeamAccessRestrictions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |
| **reposSetTeamAccessRestrictionsRequest** | [**ReposSetTeamAccessRestrictionsRequest**](ReposSetTeamAccessRestrictionsRequest.md)|  | [optional] |

### Return type

[**List&lt;Team&gt;**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **422** | Validation failed |  -  |

<a id="reposRemoveUserAccessRestrictions"></a>
# **reposRemoveUserAccessRestrictions**
> List&lt;SimpleUser&gt; reposRemoveUserAccessRestrictions(owner, repo, branch, reposSetUserAccessRestrictionsRequest)

Remove user access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Removes the ability of a user to push to this branch.  | Type    | Description                                                                                                                                   | | ------- | --------------------------------------------------------------------------------------------------------------------------------------------- | | &#x60;array&#x60; | Usernames of the people who should no longer have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    ReposSetUserAccessRestrictionsRequest reposSetUserAccessRestrictionsRequest = new ReposSetUserAccessRestrictionsRequest(); // ReposSetUserAccessRestrictionsRequest | 
    try {
      List<SimpleUser> result = apiInstance.reposRemoveUserAccessRestrictions(owner, repo, branch, reposSetUserAccessRestrictionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposRemoveUserAccessRestrictions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |
| **reposSetUserAccessRestrictionsRequest** | [**ReposSetUserAccessRestrictionsRequest**](ReposSetUserAccessRestrictionsRequest.md)|  | [optional] |

### Return type

[**List&lt;SimpleUser&gt;**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **422** | Validation failed |  -  |

<a id="reposReplaceAllTopics"></a>
# **reposReplaceAllTopics**
> Topic reposReplaceAllTopics(owner, repo, reposReplaceAllTopicsRequest)

Replace all repository topics



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    ReposReplaceAllTopicsRequest reposReplaceAllTopicsRequest = new ReposReplaceAllTopicsRequest(); // ReposReplaceAllTopicsRequest | 
    try {
      Topic result = apiInstance.reposReplaceAllTopics(owner, repo, reposReplaceAllTopicsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposReplaceAllTopics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **reposReplaceAllTopicsRequest** | [**ReposReplaceAllTopicsRequest**](ReposReplaceAllTopicsRequest.md)|  | |

### Return type

[**Topic**](Topic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |
| **415** | Preview header missing |  -  |
| **422** | Validation failed |  -  |

<a id="reposRequestPagesBuild"></a>
# **reposRequestPagesBuild**
> PageBuildStatus reposRequestPagesBuild(owner, repo)

Request a GitHub Enterprise Server Pages build

You can request that your site be built from the latest revision on the default branch. This has the same effect as pushing a commit to your default branch, but does not require an additional commit. Manually triggering page builds can be helpful when diagnosing build warnings and failures.  Build requests are limited to one concurrent build per repository and one concurrent build per requester. If you request a build while another is still in progress, the second request will be queued until the first completes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      PageBuildStatus result = apiInstance.reposRequestPagesBuild(owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposRequestPagesBuild");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |

### Return type

[**PageBuildStatus**](PageBuildStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="reposSetAdminBranchProtection"></a>
# **reposSetAdminBranchProtection**
> ProtectedBranchAdminEnforced reposSetAdminBranchProtection(owner, repo, branch)

Set admin branch protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Adding admin enforcement requires admin or owner permissions to the repository and branch protection to be enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    try {
      ProtectedBranchAdminEnforced result = apiInstance.reposSetAdminBranchProtection(owner, repo, branch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposSetAdminBranchProtection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |

### Return type

[**ProtectedBranchAdminEnforced**](ProtectedBranchAdminEnforced.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="reposSetAppAccessRestrictions"></a>
# **reposSetAppAccessRestrictions**
> List&lt;Integration&gt; reposSetAppAccessRestrictions(owner, repo, branch, reposSetAppAccessRestrictionsRequest)

Set app access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Replaces the list of apps that have push access to this branch. This removes all apps that previously had push access and grants push access to the new list of apps. Only installed GitHub Apps with &#x60;write&#x60; access to the &#x60;contents&#x60; permission can be added as authorized actors on a protected branch.  | Type    | Description                                                                                                                                                | | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | | &#x60;array&#x60; | The GitHub Apps that have push access to this branch. Use the app&#39;s &#x60;slug&#x60;. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    ReposSetAppAccessRestrictionsRequest reposSetAppAccessRestrictionsRequest = new ReposSetAppAccessRestrictionsRequest(); // ReposSetAppAccessRestrictionsRequest | 
    try {
      List<Integration> result = apiInstance.reposSetAppAccessRestrictions(owner, repo, branch, reposSetAppAccessRestrictionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposSetAppAccessRestrictions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |
| **reposSetAppAccessRestrictionsRequest** | [**ReposSetAppAccessRestrictionsRequest**](ReposSetAppAccessRestrictionsRequest.md)|  | [optional] |

### Return type

[**List&lt;Integration&gt;**](Integration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **422** | Validation failed |  -  |

<a id="reposSetStatusCheckContexts"></a>
# **reposSetStatusCheckContexts**
> List&lt;String&gt; reposSetStatusCheckContexts(owner, repo, branch, reposSetStatusCheckContextsRequest)

Set status check contexts

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    ReposSetStatusCheckContextsRequest reposSetStatusCheckContextsRequest = new ReposSetStatusCheckContextsRequest(); // ReposSetStatusCheckContextsRequest | 
    try {
      List<String> result = apiInstance.reposSetStatusCheckContexts(owner, repo, branch, reposSetStatusCheckContextsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposSetStatusCheckContexts");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |
| **reposSetStatusCheckContextsRequest** | [**ReposSetStatusCheckContextsRequest**](ReposSetStatusCheckContextsRequest.md)|  | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="reposSetTeamAccessRestrictions"></a>
# **reposSetTeamAccessRestrictions**
> List&lt;Team&gt; reposSetTeamAccessRestrictions(owner, repo, branch, reposSetTeamAccessRestrictionsRequest)

Set team access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Replaces the list of teams that have push access to this branch. This removes all teams that previously had push access and grants push access to the new list of teams. Team restrictions include child teams.  | Type    | Description                                                                                                                                | | ------- | ------------------------------------------------------------------------------------------------------------------------------------------ | | &#x60;array&#x60; | The teams that can have push access. Use the team&#39;s &#x60;slug&#x60;. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    ReposSetTeamAccessRestrictionsRequest reposSetTeamAccessRestrictionsRequest = new ReposSetTeamAccessRestrictionsRequest(); // ReposSetTeamAccessRestrictionsRequest | 
    try {
      List<Team> result = apiInstance.reposSetTeamAccessRestrictions(owner, repo, branch, reposSetTeamAccessRestrictionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposSetTeamAccessRestrictions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |
| **reposSetTeamAccessRestrictionsRequest** | [**ReposSetTeamAccessRestrictionsRequest**](ReposSetTeamAccessRestrictionsRequest.md)|  | [optional] |

### Return type

[**List&lt;Team&gt;**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **422** | Validation failed |  -  |

<a id="reposSetUserAccessRestrictions"></a>
# **reposSetUserAccessRestrictions**
> List&lt;SimpleUser&gt; reposSetUserAccessRestrictions(owner, repo, branch, reposSetUserAccessRestrictionsRequest)

Set user access restrictions

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Replaces the list of people that have push access to this branch. This removes all people that previously had push access and grants push access to the new list of people.  | Type    | Description                                                                                                                   | | ------- | ----------------------------------------------------------------------------------------------------------------------------- | | &#x60;array&#x60; | Usernames for people who can have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    ReposSetUserAccessRestrictionsRequest reposSetUserAccessRestrictionsRequest = new ReposSetUserAccessRestrictionsRequest(); // ReposSetUserAccessRestrictionsRequest | 
    try {
      List<SimpleUser> result = apiInstance.reposSetUserAccessRestrictions(owner, repo, branch, reposSetUserAccessRestrictionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposSetUserAccessRestrictions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |
| **reposSetUserAccessRestrictionsRequest** | [**ReposSetUserAccessRestrictionsRequest**](ReposSetUserAccessRestrictionsRequest.md)|  | [optional] |

### Return type

[**List&lt;SimpleUser&gt;**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **422** | Validation failed |  -  |

<a id="reposTestPushWebhook"></a>
# **reposTestPushWebhook**
> reposTestPushWebhook(owner, repo, hookId)

Test the push repository webhook

This will trigger the hook with the latest push to the current repository if the hook is subscribed to &#x60;push&#x60; events. If the hook is not subscribed to &#x60;push&#x60; events, the server will respond with 204 but no test POST will be generated.  **Note**: Previously &#x60;/repos/:owner/:repo/hooks/:hook_id/test&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer hookId = 56; // Integer | 
    try {
      apiInstance.reposTestPushWebhook(owner, repo, hookId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposTestPushWebhook");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **hookId** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposTransfer"></a>
# **reposTransfer**
> MinimalRepository reposTransfer(owner, repo, reposTransferRequest)

Transfer a repository

A transfer request will need to be accepted by the new owner when transferring a personal repository to another user. The response will contain the original &#x60;owner&#x60;, and the transfer will continue asynchronously. For more details on the requirements to transfer personal and organization-owned repositories, see [about repository transfers](https://help.github.com/articles/about-repository-transfers/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    ReposTransferRequest reposTransferRequest = new ReposTransferRequest(); // ReposTransferRequest | 
    try {
      MinimalRepository result = apiInstance.reposTransfer(owner, repo, reposTransferRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposTransfer");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **reposTransferRequest** | [**ReposTransferRequest**](ReposTransferRequest.md)|  | |

### Return type

[**MinimalRepository**](MinimalRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Response |  -  |

<a id="reposUpdate"></a>
# **reposUpdate**
> FullRepository reposUpdate(owner, repo, reposUpdateRequest)

Update a repository

**Note**: To edit a repository&#39;s topics, use the [Replace all repository topics](https://docs.github.com/enterprise-server@2.22/rest/reference/repos#replace-all-repository-topics) endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    ReposUpdateRequest reposUpdateRequest = new ReposUpdateRequest(); // ReposUpdateRequest | 
    try {
      FullRepository result = apiInstance.reposUpdate(owner, repo, reposUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposUpdate");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **reposUpdateRequest** | [**ReposUpdateRequest**](ReposUpdateRequest.md)|  | [optional] |

### Return type

[**FullRepository**](FullRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **307** | Temporary Redirect |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="reposUpdateBranchProtection"></a>
# **reposUpdateBranchProtection**
> ProtectedBranch reposUpdateBranchProtection(owner, repo, branch, reposUpdateBranchProtectionRequest)

Update branch protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Protecting a branch requires admin or owner permissions to the repository.  **Note**: Passing new arrays of &#x60;users&#x60; and &#x60;teams&#x60; replaces their previous values.  **Note**: The list of users, apps, and teams in total is limited to 100 items.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    ReposUpdateBranchProtectionRequest reposUpdateBranchProtectionRequest = new ReposUpdateBranchProtectionRequest(); // ReposUpdateBranchProtectionRequest | 
    try {
      ProtectedBranch result = apiInstance.reposUpdateBranchProtection(owner, repo, branch, reposUpdateBranchProtectionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposUpdateBranchProtection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |
| **reposUpdateBranchProtectionRequest** | [**ReposUpdateBranchProtectionRequest**](ReposUpdateBranchProtectionRequest.md)|  | |

### Return type

[**ProtectedBranch**](ProtectedBranch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="reposUpdateCommitComment"></a>
# **reposUpdateCommitComment**
> CommitComment reposUpdateCommitComment(owner, repo, commentId, reposUpdateCommitCommentRequest)

Update a commit comment



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer commentId = 56; // Integer | comment_id parameter
    ReposUpdateCommitCommentRequest reposUpdateCommitCommentRequest = new ReposUpdateCommitCommentRequest(); // ReposUpdateCommitCommentRequest | 
    try {
      CommitComment result = apiInstance.reposUpdateCommitComment(owner, repo, commentId, reposUpdateCommitCommentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposUpdateCommitComment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **commentId** | **Integer**| comment_id parameter | |
| **reposUpdateCommitCommentRequest** | [**ReposUpdateCommitCommentRequest**](ReposUpdateCommitCommentRequest.md)|  | |

### Return type

[**CommitComment**](CommitComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |

<a id="reposUpdateInformationAboutPagesSite"></a>
# **reposUpdateInformationAboutPagesSite**
> reposUpdateInformationAboutPagesSite(owner, repo, reposUpdateInformationAboutPagesSiteRequest)

Update information about a GitHub Enterprise Server Pages site

Updates information for a GitHub Enterprise Server Pages site. For more information, see \&quot;[About GitHub Pages](/github/working-with-github-pages/about-github-pages).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    ReposUpdateInformationAboutPagesSiteRequest reposUpdateInformationAboutPagesSiteRequest = new ReposUpdateInformationAboutPagesSiteRequest(); // ReposUpdateInformationAboutPagesSiteRequest | 
    try {
      apiInstance.reposUpdateInformationAboutPagesSite(owner, repo, reposUpdateInformationAboutPagesSiteRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposUpdateInformationAboutPagesSite");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **reposUpdateInformationAboutPagesSiteRequest** | [**ReposUpdateInformationAboutPagesSiteRequest**](ReposUpdateInformationAboutPagesSiteRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/scim+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **400** | Bad Request |  -  |
| **422** | Validation failed |  -  |

<a id="reposUpdateInvitation"></a>
# **reposUpdateInvitation**
> RepositoryInvitation reposUpdateInvitation(owner, repo, invitationId, reposUpdateInvitationRequest)

Update a repository invitation



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer invitationId = 56; // Integer | invitation_id parameter
    ReposUpdateInvitationRequest reposUpdateInvitationRequest = new ReposUpdateInvitationRequest(); // ReposUpdateInvitationRequest | 
    try {
      RepositoryInvitation result = apiInstance.reposUpdateInvitation(owner, repo, invitationId, reposUpdateInvitationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposUpdateInvitation");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **invitationId** | **Integer**| invitation_id parameter | |
| **reposUpdateInvitationRequest** | [**ReposUpdateInvitationRequest**](ReposUpdateInvitationRequest.md)|  | [optional] |

### Return type

[**RepositoryInvitation**](RepositoryInvitation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="reposUpdatePullRequestReviewProtection"></a>
# **reposUpdatePullRequestReviewProtection**
> ProtectedBranchPullRequestReview reposUpdatePullRequestReviewProtection(owner, repo, branch, reposUpdatePullRequestReviewProtectionRequest)

Update pull request review protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Updating pull request review enforcement requires admin or owner permissions to the repository and branch protection to be enabled.  **Note**: Passing new arrays of &#x60;users&#x60; and &#x60;teams&#x60; replaces their previous values.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    ReposUpdatePullRequestReviewProtectionRequest reposUpdatePullRequestReviewProtectionRequest = new ReposUpdatePullRequestReviewProtectionRequest(); // ReposUpdatePullRequestReviewProtectionRequest | 
    try {
      ProtectedBranchPullRequestReview result = apiInstance.reposUpdatePullRequestReviewProtection(owner, repo, branch, reposUpdatePullRequestReviewProtectionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposUpdatePullRequestReviewProtection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |
| **reposUpdatePullRequestReviewProtectionRequest** | [**ReposUpdatePullRequestReviewProtectionRequest**](ReposUpdatePullRequestReviewProtectionRequest.md)|  | [optional] |

### Return type

[**ProtectedBranchPullRequestReview**](ProtectedBranchPullRequestReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **422** | Validation failed |  -  |

<a id="reposUpdateRelease"></a>
# **reposUpdateRelease**
> Release reposUpdateRelease(owner, repo, releaseId, reposUpdateReleaseRequest)

Update a release

Users with push access to the repository can edit a release.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer releaseId = 56; // Integer | release_id parameter
    ReposUpdateReleaseRequest reposUpdateReleaseRequest = new ReposUpdateReleaseRequest(); // ReposUpdateReleaseRequest | 
    try {
      Release result = apiInstance.reposUpdateRelease(owner, repo, releaseId, reposUpdateReleaseRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposUpdateRelease");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **releaseId** | **Integer**| release_id parameter | |
| **reposUpdateReleaseRequest** | [**ReposUpdateReleaseRequest**](ReposUpdateReleaseRequest.md)|  | [optional] |

### Return type

[**Release**](Release.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="reposUpdateReleaseAsset"></a>
# **reposUpdateReleaseAsset**
> ReleaseAsset reposUpdateReleaseAsset(owner, repo, assetId, reposUpdateReleaseAssetRequest)

Update a release asset

Users with push access to the repository can edit a release asset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer assetId = 56; // Integer | asset_id parameter
    ReposUpdateReleaseAssetRequest reposUpdateReleaseAssetRequest = new ReposUpdateReleaseAssetRequest(); // ReposUpdateReleaseAssetRequest | 
    try {
      ReleaseAsset result = apiInstance.reposUpdateReleaseAsset(owner, repo, assetId, reposUpdateReleaseAssetRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposUpdateReleaseAsset");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **assetId** | **Integer**| asset_id parameter | |
| **reposUpdateReleaseAssetRequest** | [**ReposUpdateReleaseAssetRequest**](ReposUpdateReleaseAssetRequest.md)|  | [optional] |

### Return type

[**ReleaseAsset**](ReleaseAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="reposUpdateStatusCheckProtection"></a>
# **reposUpdateStatusCheckProtection**
> StatusCheckPolicy reposUpdateStatusCheckProtection(owner, repo, branch, reposUpdateStatusCheckProtectionRequest)

Update status check protection

Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Updating required status checks requires admin or owner permissions to the repository and branch protection to be enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String branch = "branch_example"; // String | The name of the branch.
    ReposUpdateStatusCheckProtectionRequest reposUpdateStatusCheckProtectionRequest = new ReposUpdateStatusCheckProtectionRequest(); // ReposUpdateStatusCheckProtectionRequest | 
    try {
      StatusCheckPolicy result = apiInstance.reposUpdateStatusCheckProtection(owner, repo, branch, reposUpdateStatusCheckProtectionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposUpdateStatusCheckProtection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **branch** | **String**| The name of the branch. | |
| **reposUpdateStatusCheckProtectionRequest** | [**ReposUpdateStatusCheckProtectionRequest**](ReposUpdateStatusCheckProtectionRequest.md)|  | [optional] |

### Return type

[**StatusCheckPolicy**](StatusCheckPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="reposUpdateWebhook"></a>
# **reposUpdateWebhook**
> Hook reposUpdateWebhook(owner, repo, hookId, reposUpdateWebhookRequest)

Update a repository webhook

Updates a webhook configured in a repository. If you previously had a &#x60;secret&#x60; set, you must provide the same &#x60;secret&#x60; or set a new &#x60;secret&#x60; or the secret will be removed. If you are only updating individual webhook &#x60;config&#x60; properties, use \&quot;[Update a webhook configuration for a repository](/rest/reference/repos#update-a-webhook-configuration-for-a-repository).\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer hookId = 56; // Integer | 
    ReposUpdateWebhookRequest reposUpdateWebhookRequest = new ReposUpdateWebhookRequest(); // ReposUpdateWebhookRequest | 
    try {
      Hook result = apiInstance.reposUpdateWebhook(owner, repo, hookId, reposUpdateWebhookRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposUpdateWebhook");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **hookId** | **Integer**|  | |
| **reposUpdateWebhookRequest** | [**ReposUpdateWebhookRequest**](ReposUpdateWebhookRequest.md)|  | |

### Return type

[**Hook**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Resource not found |  -  |
| **422** | Validation failed |  -  |

<a id="reposUploadReleaseAsset"></a>
# **reposUploadReleaseAsset**
> ReleaseAsset reposUploadReleaseAsset(owner, repo, releaseId, name, label, body)

Upload a release asset

This endpoint makes use of [a Hypermedia relation](https://docs.github.com/enterprise-server@2.22/rest/overview/resources-in-the-rest-api#hypermedia) to determine which URL to access. The endpoint you call to upload release assets is specific to your release. Use the &#x60;upload_url&#x60; returned in the response of the [Create a release endpoint](https://docs.github.com/enterprise-server@2.22/rest/reference/repos#create-a-release) to upload a release asset.  You need to use an HTTP client which supports [SNI](http://en.wikipedia.org/wiki/Server_Name_Indication) to make calls to this endpoint.  Most libraries will set the required &#x60;Content-Length&#x60; header automatically. Use the required &#x60;Content-Type&#x60; header to provide the media type of the asset. For a list of media types, see [Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml). For example:   &#x60;application/zip&#x60;  GitHub Enterprise Server expects the asset data in its raw binary form, rather than JSON. You will send the raw binary content of the asset as the request body. Everything else about the endpoint is the same as the rest of the API. For example, you&#39;ll still need to pass your authentication to be able to upload an asset.  When an upstream failure occurs, you will receive a &#x60;502 Bad Gateway&#x60; status. This may leave an empty asset with a state of &#x60;starter&#x60;. It can be safely deleted.  **Notes:** *   GitHub Enterprise Server renames asset filenames that have special characters, non-alphanumeric characters, and leading or trailing periods. The \&quot;[List assets for a release](https://docs.github.com/enterprise-server@2.22/rest/reference/repos#list-assets-for-a-release)\&quot; endpoint lists the renamed filenames. For more information and help, contact [GitHub Enterprise Server Support](https://support.github.com/contact?tags&#x3D;dotcom-rest-api). *   If you upload an asset with the same filename as another uploaded asset, you&#39;ll receive an error and must delete the old file before you can re-upload the new asset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReposApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReposApi apiInstance = new ReposApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer releaseId = 56; // Integer | release_id parameter
    String name = "name_example"; // String | 
    String label = "label_example"; // String | 
    String body = "body_example"; // String | 
    try {
      ReleaseAsset result = apiInstance.reposUploadReleaseAsset(owner, repo, releaseId, name, label, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReposApi#reposUploadReleaseAsset");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **releaseId** | **Integer**| release_id parameter | |
| **name** | **String**|  | |
| **label** | **String**|  | [optional] |
| **body** | **String**|  | [optional] |

### Return type

[**ReleaseAsset**](ReleaseAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response for successful upload |  -  |
| **422** | Response if you upload an asset with the same filename as another uploaded asset |  -  |

