# GitHubV3RestApi.TeamsApi

All URIs are relative to *http://HOSTNAME/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teamsAddMemberLegacy**](TeamsApi.md#teamsAddMemberLegacy) | **PUT** /teams/{team_id}/members/{username} | Add team member (Legacy)
[**teamsAddOrUpdateMembershipForUserInOrg**](TeamsApi.md#teamsAddOrUpdateMembershipForUserInOrg) | **PUT** /orgs/{org}/teams/{team_slug}/memberships/{username} | Add or update team membership for a user
[**teamsAddOrUpdateMembershipForUserLegacy**](TeamsApi.md#teamsAddOrUpdateMembershipForUserLegacy) | **PUT** /teams/{team_id}/memberships/{username} | Add or update team membership for a user (Legacy)
[**teamsAddOrUpdateProjectPermissionsInOrg**](TeamsApi.md#teamsAddOrUpdateProjectPermissionsInOrg) | **PUT** /orgs/{org}/teams/{team_slug}/projects/{project_id} | Add or update team project permissions
[**teamsAddOrUpdateProjectPermissionsLegacy**](TeamsApi.md#teamsAddOrUpdateProjectPermissionsLegacy) | **PUT** /teams/{team_id}/projects/{project_id} | Add or update team project permissions (Legacy)
[**teamsAddOrUpdateRepoPermissionsInOrg**](TeamsApi.md#teamsAddOrUpdateRepoPermissionsInOrg) | **PUT** /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | Add or update team repository permissions
[**teamsAddOrUpdateRepoPermissionsLegacy**](TeamsApi.md#teamsAddOrUpdateRepoPermissionsLegacy) | **PUT** /teams/{team_id}/repos/{owner}/{repo} | Add or update team repository permissions (Legacy)
[**teamsCheckPermissionsForProjectInOrg**](TeamsApi.md#teamsCheckPermissionsForProjectInOrg) | **GET** /orgs/{org}/teams/{team_slug}/projects/{project_id} | Check team permissions for a project
[**teamsCheckPermissionsForProjectLegacy**](TeamsApi.md#teamsCheckPermissionsForProjectLegacy) | **GET** /teams/{team_id}/projects/{project_id} | Check team permissions for a project (Legacy)
[**teamsCheckPermissionsForRepoInOrg**](TeamsApi.md#teamsCheckPermissionsForRepoInOrg) | **GET** /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | Check team permissions for a repository
[**teamsCheckPermissionsForRepoLegacy**](TeamsApi.md#teamsCheckPermissionsForRepoLegacy) | **GET** /teams/{team_id}/repos/{owner}/{repo} | Check team permissions for a repository (Legacy)
[**teamsCreate**](TeamsApi.md#teamsCreate) | **POST** /orgs/{org}/teams | Create a team
[**teamsCreateDiscussionCommentInOrg**](TeamsApi.md#teamsCreateDiscussionCommentInOrg) | **POST** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments | Create a discussion comment
[**teamsCreateDiscussionCommentLegacy**](TeamsApi.md#teamsCreateDiscussionCommentLegacy) | **POST** /teams/{team_id}/discussions/{discussion_number}/comments | Create a discussion comment (Legacy)
[**teamsCreateDiscussionInOrg**](TeamsApi.md#teamsCreateDiscussionInOrg) | **POST** /orgs/{org}/teams/{team_slug}/discussions | Create a discussion
[**teamsCreateDiscussionLegacy**](TeamsApi.md#teamsCreateDiscussionLegacy) | **POST** /teams/{team_id}/discussions | Create a discussion (Legacy)
[**teamsDeleteDiscussionCommentInOrg**](TeamsApi.md#teamsDeleteDiscussionCommentInOrg) | **DELETE** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number} | Delete a discussion comment
[**teamsDeleteDiscussionCommentLegacy**](TeamsApi.md#teamsDeleteDiscussionCommentLegacy) | **DELETE** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number} | Delete a discussion comment (Legacy)
[**teamsDeleteDiscussionInOrg**](TeamsApi.md#teamsDeleteDiscussionInOrg) | **DELETE** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number} | Delete a discussion
[**teamsDeleteDiscussionLegacy**](TeamsApi.md#teamsDeleteDiscussionLegacy) | **DELETE** /teams/{team_id}/discussions/{discussion_number} | Delete a discussion (Legacy)
[**teamsDeleteInOrg**](TeamsApi.md#teamsDeleteInOrg) | **DELETE** /orgs/{org}/teams/{team_slug} | Delete a team
[**teamsDeleteLegacy**](TeamsApi.md#teamsDeleteLegacy) | **DELETE** /teams/{team_id} | Delete a team (Legacy)
[**teamsGetByName**](TeamsApi.md#teamsGetByName) | **GET** /orgs/{org}/teams/{team_slug} | Get a team by name
[**teamsGetDiscussionCommentInOrg**](TeamsApi.md#teamsGetDiscussionCommentInOrg) | **GET** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number} | Get a discussion comment
[**teamsGetDiscussionCommentLegacy**](TeamsApi.md#teamsGetDiscussionCommentLegacy) | **GET** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number} | Get a discussion comment (Legacy)
[**teamsGetDiscussionInOrg**](TeamsApi.md#teamsGetDiscussionInOrg) | **GET** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number} | Get a discussion
[**teamsGetDiscussionLegacy**](TeamsApi.md#teamsGetDiscussionLegacy) | **GET** /teams/{team_id}/discussions/{discussion_number} | Get a discussion (Legacy)
[**teamsGetLegacy**](TeamsApi.md#teamsGetLegacy) | **GET** /teams/{team_id} | Get a team (Legacy)
[**teamsGetMemberLegacy**](TeamsApi.md#teamsGetMemberLegacy) | **GET** /teams/{team_id}/members/{username} | Get team member (Legacy)
[**teamsGetMembershipForUserInOrg**](TeamsApi.md#teamsGetMembershipForUserInOrg) | **GET** /orgs/{org}/teams/{team_slug}/memberships/{username} | Get team membership for a user
[**teamsGetMembershipForUserLegacy**](TeamsApi.md#teamsGetMembershipForUserLegacy) | **GET** /teams/{team_id}/memberships/{username} | Get team membership for a user (Legacy)
[**teamsList**](TeamsApi.md#teamsList) | **GET** /orgs/{org}/teams | List teams
[**teamsListChildInOrg**](TeamsApi.md#teamsListChildInOrg) | **GET** /orgs/{org}/teams/{team_slug}/teams | List child teams
[**teamsListChildLegacy**](TeamsApi.md#teamsListChildLegacy) | **GET** /teams/{team_id}/teams | List child teams (Legacy)
[**teamsListDiscussionCommentsInOrg**](TeamsApi.md#teamsListDiscussionCommentsInOrg) | **GET** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments | List discussion comments
[**teamsListDiscussionCommentsLegacy**](TeamsApi.md#teamsListDiscussionCommentsLegacy) | **GET** /teams/{team_id}/discussions/{discussion_number}/comments | List discussion comments (Legacy)
[**teamsListDiscussionsInOrg**](TeamsApi.md#teamsListDiscussionsInOrg) | **GET** /orgs/{org}/teams/{team_slug}/discussions | List discussions
[**teamsListDiscussionsLegacy**](TeamsApi.md#teamsListDiscussionsLegacy) | **GET** /teams/{team_id}/discussions | List discussions (Legacy)
[**teamsListForAuthenticatedUser**](TeamsApi.md#teamsListForAuthenticatedUser) | **GET** /user/teams | List teams for the authenticated user
[**teamsListMembersInOrg**](TeamsApi.md#teamsListMembersInOrg) | **GET** /orgs/{org}/teams/{team_slug}/members | List team members
[**teamsListMembersLegacy**](TeamsApi.md#teamsListMembersLegacy) | **GET** /teams/{team_id}/members | List team members (Legacy)
[**teamsListProjectsInOrg**](TeamsApi.md#teamsListProjectsInOrg) | **GET** /orgs/{org}/teams/{team_slug}/projects | List team projects
[**teamsListProjectsLegacy**](TeamsApi.md#teamsListProjectsLegacy) | **GET** /teams/{team_id}/projects | List team projects (Legacy)
[**teamsListReposInOrg**](TeamsApi.md#teamsListReposInOrg) | **GET** /orgs/{org}/teams/{team_slug}/repos | List team repositories
[**teamsListReposLegacy**](TeamsApi.md#teamsListReposLegacy) | **GET** /teams/{team_id}/repos | List team repositories (Legacy)
[**teamsRemoveMemberLegacy**](TeamsApi.md#teamsRemoveMemberLegacy) | **DELETE** /teams/{team_id}/members/{username} | Remove team member (Legacy)
[**teamsRemoveMembershipForUserInOrg**](TeamsApi.md#teamsRemoveMembershipForUserInOrg) | **DELETE** /orgs/{org}/teams/{team_slug}/memberships/{username} | Remove team membership for a user
[**teamsRemoveMembershipForUserLegacy**](TeamsApi.md#teamsRemoveMembershipForUserLegacy) | **DELETE** /teams/{team_id}/memberships/{username} | Remove team membership for a user (Legacy)
[**teamsRemoveProjectInOrg**](TeamsApi.md#teamsRemoveProjectInOrg) | **DELETE** /orgs/{org}/teams/{team_slug}/projects/{project_id} | Remove a project from a team
[**teamsRemoveProjectLegacy**](TeamsApi.md#teamsRemoveProjectLegacy) | **DELETE** /teams/{team_id}/projects/{project_id} | Remove a project from a team (Legacy)
[**teamsRemoveRepoInOrg**](TeamsApi.md#teamsRemoveRepoInOrg) | **DELETE** /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo} | Remove a repository from a team
[**teamsRemoveRepoLegacy**](TeamsApi.md#teamsRemoveRepoLegacy) | **DELETE** /teams/{team_id}/repos/{owner}/{repo} | Remove a repository from a team (Legacy)
[**teamsUpdateDiscussionCommentInOrg**](TeamsApi.md#teamsUpdateDiscussionCommentInOrg) | **PATCH** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number} | Update a discussion comment
[**teamsUpdateDiscussionCommentLegacy**](TeamsApi.md#teamsUpdateDiscussionCommentLegacy) | **PATCH** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number} | Update a discussion comment (Legacy)
[**teamsUpdateDiscussionInOrg**](TeamsApi.md#teamsUpdateDiscussionInOrg) | **PATCH** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number} | Update a discussion
[**teamsUpdateDiscussionLegacy**](TeamsApi.md#teamsUpdateDiscussionLegacy) | **PATCH** /teams/{team_id}/discussions/{discussion_number} | Update a discussion (Legacy)
[**teamsUpdateInOrg**](TeamsApi.md#teamsUpdateInOrg) | **PATCH** /orgs/{org}/teams/{team_slug} | Update a team
[**teamsUpdateLegacy**](TeamsApi.md#teamsUpdateLegacy) | **PATCH** /teams/{team_id} | Update a team (Legacy)



## teamsAddMemberLegacy

> teamsAddMemberLegacy(teamId, username)

Add team member (Legacy)

The \&quot;Add team member\&quot; endpoint (described below) is deprecated.  We recommend using the [Add or update team membership for a user](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#add-or-update-team-membership-for-a-user) endpoint instead. It allows you to invite new organization members to your teams.  Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  To add someone to a team, the authenticated user must be an organization owner or a team maintainer in the team they&#39;re changing. The person being added to the team must be a member of the team&#39;s organization.  **Note:** When you have team synchronization set up for a team with your organization&#39;s identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team&#39;s membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \&quot;[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\&quot;  Note that you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.21/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let username = "username_example"; // String | 
apiInstance.teamsAddMemberLegacy(teamId, username, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **username** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsAddOrUpdateMembershipForUserInOrg

> TeamMembership teamsAddOrUpdateMembershipForUserInOrg(org, teamSlug, username, opts)

Add or update team membership for a user

Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Adds an organization member to a team. An authenticated organization owner or team maintainer can add organization members to a team.  **Note:** When you have team synchronization set up for a team with your organization&#39;s identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team&#39;s membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \&quot;[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\&quot;  An organization owner can add someone who is not part of the team&#39;s organization to a team. When an organization owner adds someone to a team who is not an organization member, this endpoint will send an invitation to the person via email. This newly-created membership will be in the \&quot;pending\&quot; state until the person accepts the invitation, at which point the membership will transition to the \&quot;active\&quot; state and the user will be added as a member of the team.  If the user is already a member of the team, this endpoint will update the role of the team member&#39;s role. To update the membership of a team member, the authenticated user must be an organization owner or a team maintainer.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;PUT /organizations/{org_id}/team/{team_id}/memberships/{username}&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let username = "username_example"; // String | 
let opts = {
  'teamsAddOrUpdateMembershipForUserInOrgRequest': new GitHubV3RestApi.TeamsAddOrUpdateMembershipForUserInOrgRequest() // TeamsAddOrUpdateMembershipForUserInOrgRequest | 
};
apiInstance.teamsAddOrUpdateMembershipForUserInOrg(org, teamSlug, username, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **username** | **String**|  | 
 **teamsAddOrUpdateMembershipForUserInOrgRequest** | [**TeamsAddOrUpdateMembershipForUserInOrgRequest**](TeamsAddOrUpdateMembershipForUserInOrgRequest.md)|  | [optional] 

### Return type

[**TeamMembership**](TeamMembership.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsAddOrUpdateMembershipForUserLegacy

> TeamMembership teamsAddOrUpdateMembershipForUserLegacy(teamId, username, opts)

Add or update team membership for a user (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Add or update team membership for a user](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#add-or-update-team-membership-for-a-user) endpoint.  Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  If the user is already a member of the team&#39;s organization, this endpoint will add the user to the team. To add a membership between an organization member and a team, the authenticated user must be an organization owner or a team maintainer.  **Note:** When you have team synchronization set up for a team with your organization&#39;s identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team&#39;s membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \&quot;[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\&quot;  If the user is unaffiliated with the team&#39;s organization, this endpoint will send an invitation to the user via email. This newly-created membership will be in the \&quot;pending\&quot; state until the user accepts the invitation, at which point the membership will transition to the \&quot;active\&quot; state and the user will be added as a member of the team. To add a membership between an unaffiliated user and a team, the authenticated user must be an organization owner.  If the user is already a member of the team, this endpoint will update the role of the team member&#39;s role. To update the membership of a team member, the authenticated user must be an organization owner or a team maintainer.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let username = "username_example"; // String | 
let opts = {
  'teamsAddOrUpdateMembershipForUserInOrgRequest': new GitHubV3RestApi.TeamsAddOrUpdateMembershipForUserInOrgRequest() // TeamsAddOrUpdateMembershipForUserInOrgRequest | 
};
apiInstance.teamsAddOrUpdateMembershipForUserLegacy(teamId, username, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **username** | **String**|  | 
 **teamsAddOrUpdateMembershipForUserInOrgRequest** | [**TeamsAddOrUpdateMembershipForUserInOrgRequest**](TeamsAddOrUpdateMembershipForUserInOrgRequest.md)|  | [optional] 

### Return type

[**TeamMembership**](TeamMembership.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsAddOrUpdateProjectPermissionsInOrg

> teamsAddOrUpdateProjectPermissionsInOrg(org, teamSlug, projectId, opts)

Add or update team project permissions

Adds an organization project to a team. To add a project to a team or update the team&#39;s permission on a project, the authenticated user must have &#x60;admin&#x60; permissions for the project. The project and team must be part of the same organization.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;PUT /organizations/{org_id}/team/{team_id}/projects/{project_id}&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let projectId = 56; // Number | 
let opts = {
  'teamsAddOrUpdateProjectPermissionsInOrgRequest': new GitHubV3RestApi.TeamsAddOrUpdateProjectPermissionsInOrgRequest() // TeamsAddOrUpdateProjectPermissionsInOrgRequest | 
};
apiInstance.teamsAddOrUpdateProjectPermissionsInOrg(org, teamSlug, projectId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **projectId** | **Number**|  | 
 **teamsAddOrUpdateProjectPermissionsInOrgRequest** | [**TeamsAddOrUpdateProjectPermissionsInOrgRequest**](TeamsAddOrUpdateProjectPermissionsInOrgRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsAddOrUpdateProjectPermissionsLegacy

> teamsAddOrUpdateProjectPermissionsLegacy(teamId, projectId, opts)

Add or update team project permissions (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Add or update team project permissions](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#add-or-update-team-project-permissions) endpoint.  Adds an organization project to a team. To add a project to a team or update the team&#39;s permission on a project, the authenticated user must have &#x60;admin&#x60; permissions for the project. The project and team must be part of the same organization.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let projectId = 56; // Number | 
let opts = {
  'teamsAddOrUpdateProjectPermissionsLegacyRequest': new GitHubV3RestApi.TeamsAddOrUpdateProjectPermissionsLegacyRequest() // TeamsAddOrUpdateProjectPermissionsLegacyRequest | 
};
apiInstance.teamsAddOrUpdateProjectPermissionsLegacy(teamId, projectId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **projectId** | **Number**|  | 
 **teamsAddOrUpdateProjectPermissionsLegacyRequest** | [**TeamsAddOrUpdateProjectPermissionsLegacyRequest**](TeamsAddOrUpdateProjectPermissionsLegacyRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsAddOrUpdateRepoPermissionsInOrg

> teamsAddOrUpdateRepoPermissionsInOrg(org, teamSlug, owner, repo, opts)

Add or update team repository permissions

To add a repository to a team or update the team&#39;s permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a &#x60;422 Unprocessable Entity&#x60; status if you attempt to add a repository to a team that is not owned by the organization. Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.21/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;PUT /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}&#x60;.  For more information about the permission levels, see \&quot;[Repository permission levels for an organization](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)\&quot;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let opts = {
  'teamsAddOrUpdateRepoPermissionsInOrgRequest': new GitHubV3RestApi.TeamsAddOrUpdateRepoPermissionsInOrgRequest() // TeamsAddOrUpdateRepoPermissionsInOrgRequest | 
};
apiInstance.teamsAddOrUpdateRepoPermissionsInOrg(org, teamSlug, owner, repo, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **teamsAddOrUpdateRepoPermissionsInOrgRequest** | [**TeamsAddOrUpdateRepoPermissionsInOrgRequest**](TeamsAddOrUpdateRepoPermissionsInOrgRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## teamsAddOrUpdateRepoPermissionsLegacy

> teamsAddOrUpdateRepoPermissionsLegacy(teamId, owner, repo, opts)

Add or update team repository permissions (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new \&quot;[Add or update team repository permissions](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#add-or-update-team-repository-permissions)\&quot; endpoint.  To add a repository to a team or update the team&#39;s permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a &#x60;422 Unprocessable Entity&#x60; status if you attempt to add a repository to a team that is not owned by the organization.  Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.21/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let opts = {
  'teamsAddOrUpdateRepoPermissionsLegacyRequest': new GitHubV3RestApi.TeamsAddOrUpdateRepoPermissionsLegacyRequest() // TeamsAddOrUpdateRepoPermissionsLegacyRequest | 
};
apiInstance.teamsAddOrUpdateRepoPermissionsLegacy(teamId, owner, repo, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **owner** | **String**|  | 
 **repo** | **String**|  | 
 **teamsAddOrUpdateRepoPermissionsLegacyRequest** | [**TeamsAddOrUpdateRepoPermissionsLegacyRequest**](TeamsAddOrUpdateRepoPermissionsLegacyRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsCheckPermissionsForProjectInOrg

> TeamProject teamsCheckPermissionsForProjectInOrg(org, teamSlug, projectId)

Check team permissions for a project

Checks whether a team has &#x60;read&#x60;, &#x60;write&#x60;, or &#x60;admin&#x60; permissions for an organization project. The response includes projects inherited from a parent team.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/projects/{project_id}&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let projectId = 56; // Number | 
apiInstance.teamsCheckPermissionsForProjectInOrg(org, teamSlug, projectId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **projectId** | **Number**|  | 

### Return type

[**TeamProject**](TeamProject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsCheckPermissionsForProjectLegacy

> TeamProject teamsCheckPermissionsForProjectLegacy(teamId, projectId)

Check team permissions for a project (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a project](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#check-team-permissions-for-a-project) endpoint.  Checks whether a team has &#x60;read&#x60;, &#x60;write&#x60;, or &#x60;admin&#x60; permissions for an organization project. The response includes projects inherited from a parent team.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let projectId = 56; // Number | 
apiInstance.teamsCheckPermissionsForProjectLegacy(teamId, projectId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **projectId** | **Number**|  | 

### Return type

[**TeamProject**](TeamProject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsCheckPermissionsForRepoInOrg

> TeamRepository teamsCheckPermissionsForRepoInOrg(org, teamSlug, owner, repo)

Check team permissions for a repository

Checks whether a team has &#x60;admin&#x60;, &#x60;push&#x60;, &#x60;maintain&#x60;, &#x60;triage&#x60;, or &#x60;pull&#x60; permission for a repository. Repositories inherited through a parent team will also be checked.  You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/enterprise-server@2.21/rest/overview/media-types/) via the &#x60;application/vnd.github.v3.repository+json&#x60; accept header.  If a team doesn&#39;t have permission for the repository, you will receive a &#x60;404 Not Found&#x60; response status.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
apiInstance.teamsCheckPermissionsForRepoInOrg(org, teamSlug, owner, repo, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **owner** | **String**|  | 
 **repo** | **String**|  | 

### Return type

[**TeamRepository**](TeamRepository.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsCheckPermissionsForRepoLegacy

> TeamRepository teamsCheckPermissionsForRepoLegacy(teamId, owner, repo)

Check team permissions for a repository (Legacy)

**Note**: Repositories inherited through a parent team will also be checked.  **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a repository](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#check-team-permissions-for-a-repository) endpoint.  You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/enterprise-server@2.21/rest/overview/media-types/) via the &#x60;Accept&#x60; header:

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
apiInstance.teamsCheckPermissionsForRepoLegacy(teamId, owner, repo, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **owner** | **String**|  | 
 **repo** | **String**|  | 

### Return type

[**TeamRepository**](TeamRepository.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsCreate

> TeamFull teamsCreate(org, teamsCreateRequest)

Create a team

To create a team, the authenticated user must be a member or owner of &#x60;{org}&#x60;. By default, organization members can create teams. Organization owners can limit team creation to organization owners. For more information, see \&quot;[Setting team creation permissions](https://help.github.com/en/articles/setting-team-creation-permissions-in-your-organization).\&quot;  When you create a new team, you automatically become a team maintainer without explicitly adding yourself to the optional array of &#x60;maintainers&#x60;. For more information, see \&quot;[About teams](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/about-teams)\&quot;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamsCreateRequest = {"description":"A great team","name":"Justice League","permission":"admin","privacy":"closed"}; // TeamsCreateRequest | 
apiInstance.teamsCreate(org, teamsCreateRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamsCreateRequest** | [**TeamsCreateRequest**](TeamsCreateRequest.md)|  | 

### Return type

[**TeamFull**](TeamFull.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsCreateDiscussionCommentInOrg

> TeamDiscussionComment teamsCreateDiscussionCommentInOrg(org, teamSlug, discussionNumber, teamsCreateDiscussionCommentInOrgRequest)

Create a discussion comment

Creates a new comment on a team discussion. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.21/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.21/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;POST /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let discussionNumber = 56; // Number | 
let teamsCreateDiscussionCommentInOrgRequest = {"body":"Do you like apples?"}; // TeamsCreateDiscussionCommentInOrgRequest | 
apiInstance.teamsCreateDiscussionCommentInOrg(org, teamSlug, discussionNumber, teamsCreateDiscussionCommentInOrgRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **discussionNumber** | **Number**|  | 
 **teamsCreateDiscussionCommentInOrgRequest** | [**TeamsCreateDiscussionCommentInOrgRequest**](TeamsCreateDiscussionCommentInOrgRequest.md)|  | 

### Return type

[**TeamDiscussionComment**](TeamDiscussionComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsCreateDiscussionCommentLegacy

> TeamDiscussionComment teamsCreateDiscussionCommentLegacy(teamId, discussionNumber, teamsCreateDiscussionCommentInOrgRequest)

Create a discussion comment (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Create a discussion comment](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#create-a-discussion-comment) endpoint.  Creates a new comment on a team discussion. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.21/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.21/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
let teamsCreateDiscussionCommentInOrgRequest = {"body":"Do you like apples?"}; // TeamsCreateDiscussionCommentInOrgRequest | 
apiInstance.teamsCreateDiscussionCommentLegacy(teamId, discussionNumber, teamsCreateDiscussionCommentInOrgRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **discussionNumber** | **Number**|  | 
 **teamsCreateDiscussionCommentInOrgRequest** | [**TeamsCreateDiscussionCommentInOrgRequest**](TeamsCreateDiscussionCommentInOrgRequest.md)|  | 

### Return type

[**TeamDiscussionComment**](TeamDiscussionComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsCreateDiscussionInOrg

> TeamDiscussion teamsCreateDiscussionInOrg(org, teamSlug, teamsCreateDiscussionInOrgRequest)

Create a discussion

Creates a new discussion post on a team&#39;s page. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.21/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.21/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;POST /organizations/{org_id}/team/{team_id}/discussions&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let teamsCreateDiscussionInOrgRequest = {"body":"Hi! This is an area for us to collaborate as a team.","title":"Our first team post"}; // TeamsCreateDiscussionInOrgRequest | 
apiInstance.teamsCreateDiscussionInOrg(org, teamSlug, teamsCreateDiscussionInOrgRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **teamsCreateDiscussionInOrgRequest** | [**TeamsCreateDiscussionInOrgRequest**](TeamsCreateDiscussionInOrgRequest.md)|  | 

### Return type

[**TeamDiscussion**](TeamDiscussion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsCreateDiscussionLegacy

> TeamDiscussion teamsCreateDiscussionLegacy(teamId, teamsCreateDiscussionInOrgRequest)

Create a discussion (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [&#x60;Create a discussion&#x60;](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#create-a-discussion) endpoint.  Creates a new discussion post on a team&#39;s page. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.21/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.21/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let teamsCreateDiscussionInOrgRequest = {"body":"Hi! This is an area for us to collaborate as a team.","title":"Our first team post"}; // TeamsCreateDiscussionInOrgRequest | 
apiInstance.teamsCreateDiscussionLegacy(teamId, teamsCreateDiscussionInOrgRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **teamsCreateDiscussionInOrgRequest** | [**TeamsCreateDiscussionInOrgRequest**](TeamsCreateDiscussionInOrgRequest.md)|  | 

### Return type

[**TeamDiscussion**](TeamDiscussion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsDeleteDiscussionCommentInOrg

> teamsDeleteDiscussionCommentInOrg(org, teamSlug, discussionNumber, commentNumber)

Delete a discussion comment

Deletes a comment on a team discussion. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;DELETE /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments/{comment_number}&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let discussionNumber = 56; // Number | 
let commentNumber = 56; // Number | 
apiInstance.teamsDeleteDiscussionCommentInOrg(org, teamSlug, discussionNumber, commentNumber, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **discussionNumber** | **Number**|  | 
 **commentNumber** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## teamsDeleteDiscussionCommentLegacy

> teamsDeleteDiscussionCommentLegacy(teamId, discussionNumber, commentNumber)

Delete a discussion comment (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Delete a discussion comment](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#delete-a-discussion-comment) endpoint.  Deletes a comment on a team discussion. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
let commentNumber = 56; // Number | 
apiInstance.teamsDeleteDiscussionCommentLegacy(teamId, discussionNumber, commentNumber, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **discussionNumber** | **Number**|  | 
 **commentNumber** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## teamsDeleteDiscussionInOrg

> teamsDeleteDiscussionInOrg(org, teamSlug, discussionNumber)

Delete a discussion

Delete a discussion from a team&#39;s page. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;DELETE /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let discussionNumber = 56; // Number | 
apiInstance.teamsDeleteDiscussionInOrg(org, teamSlug, discussionNumber, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **discussionNumber** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## teamsDeleteDiscussionLegacy

> teamsDeleteDiscussionLegacy(teamId, discussionNumber)

Delete a discussion (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [&#x60;Delete a discussion&#x60;](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#delete-a-discussion) endpoint.  Delete a discussion from a team&#39;s page. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
apiInstance.teamsDeleteDiscussionLegacy(teamId, discussionNumber, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **discussionNumber** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## teamsDeleteInOrg

> teamsDeleteInOrg(org, teamSlug)

Delete a team

To delete a team, the authenticated user must be an organization owner or team maintainer.  If you are an organization owner, deleting a parent team will delete all of its child teams as well.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;DELETE /organizations/{org_id}/team/{team_id}&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
apiInstance.teamsDeleteInOrg(org, teamSlug, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## teamsDeleteLegacy

> teamsDeleteLegacy(teamId)

Delete a team (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Delete a team](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#delete-a-team) endpoint.  To delete a team, the authenticated user must be an organization owner or team maintainer.  If you are an organization owner, deleting a parent team will delete all of its child teams as well.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
apiInstance.teamsDeleteLegacy(teamId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsGetByName

> TeamFull teamsGetByName(org, teamSlug)

Get a team by name

Gets a team using the team&#39;s &#x60;slug&#x60;. GitHub Enterprise Server generates the &#x60;slug&#x60; from the team &#x60;name&#x60;.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
apiInstance.teamsGetByName(org, teamSlug, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 

### Return type

[**TeamFull**](TeamFull.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsGetDiscussionCommentInOrg

> TeamDiscussionComment teamsGetDiscussionCommentInOrg(org, teamSlug, discussionNumber, commentNumber)

Get a discussion comment

Get a specific comment on a team discussion. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments/{comment_number}&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let discussionNumber = 56; // Number | 
let commentNumber = 56; // Number | 
apiInstance.teamsGetDiscussionCommentInOrg(org, teamSlug, discussionNumber, commentNumber, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **discussionNumber** | **Number**|  | 
 **commentNumber** | **Number**|  | 

### Return type

[**TeamDiscussionComment**](TeamDiscussionComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsGetDiscussionCommentLegacy

> TeamDiscussionComment teamsGetDiscussionCommentLegacy(teamId, discussionNumber, commentNumber)

Get a discussion comment (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get a discussion comment](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#get-a-discussion-comment) endpoint.  Get a specific comment on a team discussion. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
let commentNumber = 56; // Number | 
apiInstance.teamsGetDiscussionCommentLegacy(teamId, discussionNumber, commentNumber, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **discussionNumber** | **Number**|  | 
 **commentNumber** | **Number**|  | 

### Return type

[**TeamDiscussionComment**](TeamDiscussionComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsGetDiscussionInOrg

> TeamDiscussion teamsGetDiscussionInOrg(org, teamSlug, discussionNumber)

Get a discussion

Get a specific discussion on a team&#39;s page. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let discussionNumber = 56; // Number | 
apiInstance.teamsGetDiscussionInOrg(org, teamSlug, discussionNumber, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **discussionNumber** | **Number**|  | 

### Return type

[**TeamDiscussion**](TeamDiscussion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsGetDiscussionLegacy

> TeamDiscussion teamsGetDiscussionLegacy(teamId, discussionNumber)

Get a discussion (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get a discussion](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#get-a-discussion) endpoint.  Get a specific discussion on a team&#39;s page. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
apiInstance.teamsGetDiscussionLegacy(teamId, discussionNumber, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **discussionNumber** | **Number**|  | 

### Return type

[**TeamDiscussion**](TeamDiscussion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsGetLegacy

> TeamFull teamsGetLegacy(teamId)

Get a team (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the [Get a team by name](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#get-a-team-by-name) endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
apiInstance.teamsGetLegacy(teamId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 

### Return type

[**TeamFull**](TeamFull.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsGetMemberLegacy

> teamsGetMemberLegacy(teamId, username)

Get team member (Legacy)

The \&quot;Get team member\&quot; endpoint (described below) is deprecated.  We recommend using the [Get team membership for a user](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#get-team-membership-for-a-user) endpoint instead. It allows you to get both active and pending memberships.  To list members in a team, the team must be visible to the authenticated user.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let username = "username_example"; // String | 
apiInstance.teamsGetMemberLegacy(teamId, username, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **username** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## teamsGetMembershipForUserInOrg

> TeamMembership teamsGetMembershipForUserInOrg(org, teamSlug, username)

Get team membership for a user

Team members will include the members of child teams.  To get a user&#39;s membership with a team, the team must be visible to the authenticated user.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/memberships/{username}&#x60;.  **Note:** The response contains the &#x60;state&#x60; of the membership and the member&#39;s &#x60;role&#x60;.  The &#x60;role&#x60; for organization owners is set to &#x60;maintainer&#x60;. For more information about &#x60;maintainer&#x60; roles, see see [Create a team](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#create-a-team).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let username = "username_example"; // String | 
apiInstance.teamsGetMembershipForUserInOrg(org, teamSlug, username, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **username** | **String**|  | 

### Return type

[**TeamMembership**](TeamMembership.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsGetMembershipForUserLegacy

> TeamMembership teamsGetMembershipForUserLegacy(teamId, username)

Get team membership for a user (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get team membership for a user](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#get-team-membership-for-a-user) endpoint.  Team members will include the members of child teams.  To get a user&#39;s membership with a team, the team must be visible to the authenticated user.  **Note:** The response contains the &#x60;state&#x60; of the membership and the member&#39;s &#x60;role&#x60;.  The &#x60;role&#x60; for organization owners is set to &#x60;maintainer&#x60;. For more information about &#x60;maintainer&#x60; roles, see [Create a team](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#create-a-team).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let username = "username_example"; // String | 
apiInstance.teamsGetMembershipForUserLegacy(teamId, username, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **username** | **String**|  | 

### Return type

[**TeamMembership**](TeamMembership.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsList

> [Team] teamsList(org, opts)

List teams

Lists all teams in an organization that are visible to the authenticated user.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.teamsList(org, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Team]**](Team.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsListChildInOrg

> [Team] teamsListChildInOrg(org, teamSlug, opts)

List child teams

Lists the child teams of the team specified by &#x60;{team_slug}&#x60;.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/teams&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.teamsListChildInOrg(org, teamSlug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Team]**](Team.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsListChildLegacy

> [Team] teamsListChildLegacy(teamId, opts)

List child teams (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [&#x60;List child teams&#x60;](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#list-child-teams) endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.teamsListChildLegacy(teamId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Team]**](Team.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsListDiscussionCommentsInOrg

> [TeamDiscussionComment] teamsListDiscussionCommentsInOrg(org, teamSlug, discussionNumber, opts)

List discussion comments

List all comments on a team discussion. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let discussionNumber = 56; // Number | 
let opts = {
  'direction': "'desc'", // String | One of `asc` (ascending) or `desc` (descending).
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.teamsListDiscussionCommentsInOrg(org, teamSlug, discussionNumber, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **discussionNumber** | **Number**|  | 
 **direction** | **String**| One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending). | [optional] [default to &#39;desc&#39;]
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[TeamDiscussionComment]**](TeamDiscussionComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsListDiscussionCommentsLegacy

> [TeamDiscussionComment] teamsListDiscussionCommentsLegacy(teamId, discussionNumber, opts)

List discussion comments (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [List discussion comments](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#list-discussion-comments) endpoint.  List all comments on a team discussion. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
let opts = {
  'direction': "'desc'", // String | One of `asc` (ascending) or `desc` (descending).
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.teamsListDiscussionCommentsLegacy(teamId, discussionNumber, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **discussionNumber** | **Number**|  | 
 **direction** | **String**| One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending). | [optional] [default to &#39;desc&#39;]
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[TeamDiscussionComment]**](TeamDiscussionComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsListDiscussionsInOrg

> [TeamDiscussion] teamsListDiscussionsInOrg(org, teamSlug, opts)

List discussions

List all discussions on a team&#39;s page. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/discussions&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let opts = {
  'direction': "'desc'", // String | One of `asc` (ascending) or `desc` (descending).
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1, // Number | Page number of the results to fetch.
  'pinned': "pinned_example" // String | Pinned discussions only filter
};
apiInstance.teamsListDiscussionsInOrg(org, teamSlug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **direction** | **String**| One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending). | [optional] [default to &#39;desc&#39;]
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **pinned** | **String**| Pinned discussions only filter | [optional] 

### Return type

[**[TeamDiscussion]**](TeamDiscussion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsListDiscussionsLegacy

> [TeamDiscussion] teamsListDiscussionsLegacy(teamId, opts)

List discussions (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [&#x60;List discussions&#x60;](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#list-discussions) endpoint.  List all discussions on a team&#39;s page. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let opts = {
  'direction': "'desc'", // String | One of `asc` (ascending) or `desc` (descending).
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.teamsListDiscussionsLegacy(teamId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **direction** | **String**| One of &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending). | [optional] [default to &#39;desc&#39;]
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[TeamDiscussion]**](TeamDiscussion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsListForAuthenticatedUser

> [TeamFull] teamsListForAuthenticatedUser(opts)

List teams for the authenticated user

List all of the teams across all of the organizations to which the authenticated user belongs. This method requires &#x60;user&#x60;, &#x60;repo&#x60;, or &#x60;read:org&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/) when authenticating via [OAuth](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.teamsListForAuthenticatedUser(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[TeamFull]**](TeamFull.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsListMembersInOrg

> [SimpleUser] teamsListMembersInOrg(org, teamSlug, opts)

List team members

Team members will include the members of child teams.  To list members in a team, the team must be visible to the authenticated user.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let opts = {
  'role': "'all'", // String | Filters members returned by their role in the team. Can be one of:   \\* `member` - normal members of the team.   \\* `maintainer` - team maintainers.   \\* `all` - all members of the team.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.teamsListMembersInOrg(org, teamSlug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **role** | **String**| Filters members returned by their role in the team. Can be one of:   \\* &#x60;member&#x60; - normal members of the team.   \\* &#x60;maintainer&#x60; - team maintainers.   \\* &#x60;all&#x60; - all members of the team. | [optional] [default to &#39;all&#39;]
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[SimpleUser]**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsListMembersLegacy

> [SimpleUser] teamsListMembersLegacy(teamId, opts)

List team members (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [&#x60;List team members&#x60;](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#list-team-members) endpoint.  Team members will include the members of child teams.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let opts = {
  'role': "'all'", // String | Filters members returned by their role in the team. Can be one of:   \\* `member` - normal members of the team.   \\* `maintainer` - team maintainers.   \\* `all` - all members of the team.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.teamsListMembersLegacy(teamId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **role** | **String**| Filters members returned by their role in the team. Can be one of:   \\* &#x60;member&#x60; - normal members of the team.   \\* &#x60;maintainer&#x60; - team maintainers.   \\* &#x60;all&#x60; - all members of the team. | [optional] [default to &#39;all&#39;]
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[SimpleUser]**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsListProjectsInOrg

> [TeamProject] teamsListProjectsInOrg(org, teamSlug, opts)

List team projects

Lists the organization projects for a team.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/projects&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.teamsListProjectsInOrg(org, teamSlug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[TeamProject]**](TeamProject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsListProjectsLegacy

> [TeamProject] teamsListProjectsLegacy(teamId, opts)

List team projects (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [&#x60;List team projects&#x60;](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#list-team-projects) endpoint.  Lists the organization projects for a team.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.teamsListProjectsLegacy(teamId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[TeamProject]**](TeamProject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsListReposInOrg

> [MinimalRepository] teamsListReposInOrg(org, teamSlug, opts)

List team repositories

Lists a team&#39;s repositories visible to the authenticated user.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}/repos&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.teamsListReposInOrg(org, teamSlug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[MinimalRepository]**](MinimalRepository.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsListReposLegacy

> [MinimalRepository] teamsListReposLegacy(teamId, opts)

List team repositories (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [List team repositories](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#list-team-repositories) endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.teamsListReposLegacy(teamId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[MinimalRepository]**](MinimalRepository.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsRemoveMemberLegacy

> teamsRemoveMemberLegacy(teamId, username)

Remove team member (Legacy)

The \&quot;Remove team member\&quot; endpoint (described below) is deprecated.  We recommend using the [Remove team membership for a user](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#remove-team-membership-for-a-user) endpoint instead. It allows you to remove both active and pending memberships.  Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  To remove a team member, the authenticated user must have &#39;admin&#39; permissions to the team or be an owner of the org that the team is associated with. Removing a team member does not delete the user, it just removes them from the team.  **Note:** When you have team synchronization set up for a team with your organization&#39;s identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team&#39;s membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \&quot;[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let username = "username_example"; // String | 
apiInstance.teamsRemoveMemberLegacy(teamId, username, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **username** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## teamsRemoveMembershipForUserInOrg

> teamsRemoveMembershipForUserInOrg(org, teamSlug, username)

Remove team membership for a user

Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  To remove a membership between a user and a team, the authenticated user must have &#39;admin&#39; permissions to the team or be an owner of the organization that the team is associated with. Removing team membership does not delete the user, it just removes their membership from the team.  **Note:** When you have team synchronization set up for a team with your organization&#39;s identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team&#39;s membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \&quot;[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\&quot;  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;DELETE /organizations/{org_id}/team/{team_id}/memberships/{username}&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let username = "username_example"; // String | 
apiInstance.teamsRemoveMembershipForUserInOrg(org, teamSlug, username, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **username** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## teamsRemoveMembershipForUserLegacy

> teamsRemoveMembershipForUserLegacy(teamId, username)

Remove team membership for a user (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove team membership for a user](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#remove-team-membership-for-a-user) endpoint.  Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  To remove a membership between a user and a team, the authenticated user must have &#39;admin&#39; permissions to the team or be an owner of the organization that the team is associated with. Removing team membership does not delete the user, it just removes their membership from the team.  **Note:** When you have team synchronization set up for a team with your organization&#39;s identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team&#39;s membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \&quot;[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let username = "username_example"; // String | 
apiInstance.teamsRemoveMembershipForUserLegacy(teamId, username, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **username** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## teamsRemoveProjectInOrg

> teamsRemoveProjectInOrg(org, teamSlug, projectId)

Remove a project from a team

Removes an organization project from a team. An organization owner or a team maintainer can remove any project from the team. To remove a project from a team as an organization member, the authenticated user must have &#x60;read&#x60; access to both the team and project, or &#x60;admin&#x60; access to the team or project. This endpoint removes the project from the team, but does not delete the project.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;DELETE /organizations/{org_id}/team/{team_id}/projects/{project_id}&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let projectId = 56; // Number | 
apiInstance.teamsRemoveProjectInOrg(org, teamSlug, projectId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **projectId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## teamsRemoveProjectLegacy

> teamsRemoveProjectLegacy(teamId, projectId)

Remove a project from a team (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a project from a team](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#remove-a-project-from-a-team) endpoint.  Removes an organization project from a team. An organization owner or a team maintainer can remove any project from the team. To remove a project from a team as an organization member, the authenticated user must have &#x60;read&#x60; access to both the team and project, or &#x60;admin&#x60; access to the team or project. **Note:** This endpoint removes the project from the team, but does not delete it.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let projectId = 56; // Number | 
apiInstance.teamsRemoveProjectLegacy(teamId, projectId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **projectId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsRemoveRepoInOrg

> teamsRemoveRepoInOrg(org, teamSlug, owner, repo)

Remove a repository from a team

If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. This does not delete the repository, it just removes it from the team.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;DELETE /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
apiInstance.teamsRemoveRepoInOrg(org, teamSlug, owner, repo, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **owner** | **String**|  | 
 **repo** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## teamsRemoveRepoLegacy

> teamsRemoveRepoLegacy(teamId, owner, repo)

Remove a repository from a team (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Remove a repository from a team](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#remove-a-repository-from-a-team) endpoint.  If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. NOTE: This does not delete the repository, it just removes it from the team.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
apiInstance.teamsRemoveRepoLegacy(teamId, owner, repo, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **owner** | **String**|  | 
 **repo** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## teamsUpdateDiscussionCommentInOrg

> TeamDiscussionComment teamsUpdateDiscussionCommentInOrg(org, teamSlug, discussionNumber, commentNumber, teamsCreateDiscussionCommentInOrgRequest)

Update a discussion comment

Edits the body text of a discussion comment. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;PATCH /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments/{comment_number}&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let discussionNumber = 56; // Number | 
let commentNumber = 56; // Number | 
let teamsCreateDiscussionCommentInOrgRequest = {"body":"Do you like pineapples?"}; // TeamsCreateDiscussionCommentInOrgRequest | 
apiInstance.teamsUpdateDiscussionCommentInOrg(org, teamSlug, discussionNumber, commentNumber, teamsCreateDiscussionCommentInOrgRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **discussionNumber** | **Number**|  | 
 **commentNumber** | **Number**|  | 
 **teamsCreateDiscussionCommentInOrgRequest** | [**TeamsCreateDiscussionCommentInOrgRequest**](TeamsCreateDiscussionCommentInOrgRequest.md)|  | 

### Return type

[**TeamDiscussionComment**](TeamDiscussionComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsUpdateDiscussionCommentLegacy

> TeamDiscussionComment teamsUpdateDiscussionCommentLegacy(teamId, discussionNumber, commentNumber, teamsCreateDiscussionCommentInOrgRequest)

Update a discussion comment (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a discussion comment](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#update-a-discussion-comment) endpoint.  Edits the body text of a discussion comment. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
let commentNumber = 56; // Number | 
let teamsCreateDiscussionCommentInOrgRequest = {"body":"Do you like pineapples?"}; // TeamsCreateDiscussionCommentInOrgRequest | 
apiInstance.teamsUpdateDiscussionCommentLegacy(teamId, discussionNumber, commentNumber, teamsCreateDiscussionCommentInOrgRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **discussionNumber** | **Number**|  | 
 **commentNumber** | **Number**|  | 
 **teamsCreateDiscussionCommentInOrgRequest** | [**TeamsCreateDiscussionCommentInOrgRequest**](TeamsCreateDiscussionCommentInOrgRequest.md)|  | 

### Return type

[**TeamDiscussionComment**](TeamDiscussionComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsUpdateDiscussionInOrg

> TeamDiscussion teamsUpdateDiscussionInOrg(org, teamSlug, discussionNumber, opts)

Update a discussion

Edits the title and body text of a discussion post. Only the parameters you provide are updated. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;PATCH /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let discussionNumber = 56; // Number | 
let opts = {
  'teamsUpdateDiscussionInOrgRequest': {"title":"Welcome to our first team post"} // TeamsUpdateDiscussionInOrgRequest | 
};
apiInstance.teamsUpdateDiscussionInOrg(org, teamSlug, discussionNumber, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **discussionNumber** | **Number**|  | 
 **teamsUpdateDiscussionInOrgRequest** | [**TeamsUpdateDiscussionInOrgRequest**](TeamsUpdateDiscussionInOrgRequest.md)|  | [optional] 

### Return type

[**TeamDiscussion**](TeamDiscussion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsUpdateDiscussionLegacy

> TeamDiscussion teamsUpdateDiscussionLegacy(teamId, discussionNumber, opts)

Update a discussion (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a discussion](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#update-a-discussion) endpoint.  Edits the title and body text of a discussion post. Only the parameters you provide are updated. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.21/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
let opts = {
  'teamsUpdateDiscussionInOrgRequest': {"title":"Welcome to our first team post"} // TeamsUpdateDiscussionInOrgRequest | 
};
apiInstance.teamsUpdateDiscussionLegacy(teamId, discussionNumber, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **discussionNumber** | **Number**|  | 
 **teamsUpdateDiscussionInOrgRequest** | [**TeamsUpdateDiscussionInOrgRequest**](TeamsUpdateDiscussionInOrgRequest.md)|  | [optional] 

### Return type

[**TeamDiscussion**](TeamDiscussion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsUpdateInOrg

> TeamFull teamsUpdateInOrg(org, teamSlug, opts)

Update a team

To edit a team, the authenticated user must either be an organization owner or a team maintainer.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;PATCH /organizations/{org_id}/team/{team_id}&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let org = "org_example"; // String | 
let teamSlug = "teamSlug_example"; // String | team_slug parameter
let opts = {
  'teamsUpdateInOrgRequest': {"description":"new team description","name":"new team name","privacy":"closed"} // TeamsUpdateInOrgRequest | 
};
apiInstance.teamsUpdateInOrg(org, teamSlug, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**|  | 
 **teamSlug** | **String**| team_slug parameter | 
 **teamsUpdateInOrgRequest** | [**TeamsUpdateInOrgRequest**](TeamsUpdateInOrgRequest.md)|  | [optional] 

### Return type

[**TeamFull**](TeamFull.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsUpdateLegacy

> TeamFull teamsUpdateLegacy(teamId, teamsUpdateLegacyRequest)

Update a team (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Update a team](https://docs.github.com/enterprise-server@2.21/rest/reference/teams#update-a-team) endpoint.  To edit a team, the authenticated user must either be an organization owner or a team maintainer.  **Note:** With nested teams, the &#x60;privacy&#x60; for parent teams cannot be &#x60;secret&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let teamsUpdateLegacyRequest = {"description":"new team description","name":"new team name","privacy":"closed"}; // TeamsUpdateLegacyRequest | 
apiInstance.teamsUpdateLegacy(teamId, teamsUpdateLegacyRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **teamId** | **Number**|  | 
 **teamsUpdateLegacyRequest** | [**TeamsUpdateLegacyRequest**](TeamsUpdateLegacyRequest.md)|  | 

### Return type

[**TeamFull**](TeamFull.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

