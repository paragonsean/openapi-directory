# GitHubV3RestApi.TeamsApi

All URIs are relative to *http://HOSTNAME/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teamsAddMemberLegacy**](TeamsApi.md#teamsAddMemberLegacy) | **PUT** /teams/{team_id}/members/{username} | Add team member (Legacy)
[**teamsAddOrUpdateMembershipForUser**](TeamsApi.md#teamsAddOrUpdateMembershipForUser) | **PUT** /teams/{team_id}/memberships/{username} | Add or update team membership for a user
[**teamsAddOrUpdateProjectPermissions**](TeamsApi.md#teamsAddOrUpdateProjectPermissions) | **PUT** /teams/{team_id}/projects/{project_id} | Add or update team project permissions
[**teamsAddOrUpdateRepoPermissions**](TeamsApi.md#teamsAddOrUpdateRepoPermissions) | **PUT** /teams/{team_id}/repos/{owner}/{repo} | Add or update team repository permissions
[**teamsCheckPermissionsForProject**](TeamsApi.md#teamsCheckPermissionsForProject) | **GET** /teams/{team_id}/projects/{project_id} | Check team permissions for a project
[**teamsCheckPermissionsForRepo**](TeamsApi.md#teamsCheckPermissionsForRepo) | **GET** /teams/{team_id}/repos/{owner}/{repo} | Check team permissions for a repository
[**teamsCreate**](TeamsApi.md#teamsCreate) | **POST** /orgs/{org}/teams | Create a team
[**teamsCreateDiscussion**](TeamsApi.md#teamsCreateDiscussion) | **POST** /teams/{team_id}/discussions | Create a discussion
[**teamsCreateDiscussionComment**](TeamsApi.md#teamsCreateDiscussionComment) | **POST** /teams/{team_id}/discussions/{discussion_number}/comments | Create a discussion comment
[**teamsDelete**](TeamsApi.md#teamsDelete) | **DELETE** /teams/{team_id} | Delete a team
[**teamsDeleteDiscussion**](TeamsApi.md#teamsDeleteDiscussion) | **DELETE** /teams/{team_id}/discussions/{discussion_number} | Delete a discussion
[**teamsDeleteDiscussionComment**](TeamsApi.md#teamsDeleteDiscussionComment) | **DELETE** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number} | Delete a discussion comment
[**teamsGet**](TeamsApi.md#teamsGet) | **GET** /teams/{team_id} | Get a team
[**teamsGetByName**](TeamsApi.md#teamsGetByName) | **GET** /orgs/{org}/teams/{team_slug} | Get a team by name
[**teamsGetDiscussion**](TeamsApi.md#teamsGetDiscussion) | **GET** /teams/{team_id}/discussions/{discussion_number} | Get a discussion
[**teamsGetDiscussionComment**](TeamsApi.md#teamsGetDiscussionComment) | **GET** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number} | Get a discussion comment
[**teamsGetMemberLegacy**](TeamsApi.md#teamsGetMemberLegacy) | **GET** /teams/{team_id}/members/{username} | Get team member (Legacy)
[**teamsGetMembershipForUser**](TeamsApi.md#teamsGetMembershipForUser) | **GET** /teams/{team_id}/memberships/{username} | Get team membership for a user
[**teamsList**](TeamsApi.md#teamsList) | **GET** /orgs/{org}/teams | List teams
[**teamsListChild**](TeamsApi.md#teamsListChild) | **GET** /teams/{team_id}/teams | List child teams
[**teamsListDiscussionComments**](TeamsApi.md#teamsListDiscussionComments) | **GET** /teams/{team_id}/discussions/{discussion_number}/comments | List discussion comments
[**teamsListDiscussions**](TeamsApi.md#teamsListDiscussions) | **GET** /teams/{team_id}/discussions | List discussions
[**teamsListForAuthenticatedUser**](TeamsApi.md#teamsListForAuthenticatedUser) | **GET** /user/teams | List teams for the authenticated user
[**teamsListMembers**](TeamsApi.md#teamsListMembers) | **GET** /teams/{team_id}/members | List team members
[**teamsListProjects**](TeamsApi.md#teamsListProjects) | **GET** /teams/{team_id}/projects | List team projects
[**teamsListRepos**](TeamsApi.md#teamsListRepos) | **GET** /teams/{team_id}/repos | List team repositories
[**teamsRemoveMemberLegacy**](TeamsApi.md#teamsRemoveMemberLegacy) | **DELETE** /teams/{team_id}/members/{username} | Remove team member (Legacy)
[**teamsRemoveMembershipForUser**](TeamsApi.md#teamsRemoveMembershipForUser) | **DELETE** /teams/{team_id}/memberships/{username} | Remove team membership for a user
[**teamsRemoveProject**](TeamsApi.md#teamsRemoveProject) | **DELETE** /teams/{team_id}/projects/{project_id} | Remove a project from a team
[**teamsRemoveRepo**](TeamsApi.md#teamsRemoveRepo) | **DELETE** /teams/{team_id}/repos/{owner}/{repo} | Remove a repository from a team
[**teamsUpdate**](TeamsApi.md#teamsUpdate) | **PATCH** /teams/{team_id} | Update a team
[**teamsUpdateDiscussion**](TeamsApi.md#teamsUpdateDiscussion) | **PATCH** /teams/{team_id}/discussions/{discussion_number} | Update a discussion
[**teamsUpdateDiscussionComment**](TeamsApi.md#teamsUpdateDiscussionComment) | **PATCH** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number} | Update a discussion comment



## teamsAddMemberLegacy

> teamsAddMemberLegacy(teamId, username)

Add team member (Legacy)

The \&quot;Add team member\&quot; endpoint (described below) is deprecated.  We recommend using the [Add or update team membership for a user](https://docs.github.com/enterprise-server@2.20/rest/reference/teams#add-or-update-team-membership-for-a-user) endpoint instead. It allows you to invite new organization members to your teams.  Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  To add someone to a team, the authenticated user must be an organization owner or a team maintainer in the team they&#39;re changing. The person being added to the team must be a member of the team&#39;s organization.  **Note:** When you have team synchronization set up for a team with your organization&#39;s identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team&#39;s membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \&quot;[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\&quot;  Note that you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

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


## teamsAddOrUpdateMembershipForUser

> TeamMembership teamsAddOrUpdateMembershipForUser(teamId, username, opts)

Add or update team membership for a user

If the user is already a member of the team&#39;s organization, this endpoint will add the user to the team. To add a membership between an organization member and a team, the authenticated user must be an organization owner or a team maintainer.  If the user is unaffiliated with the team&#39;s organization, this endpoint will send an invitation to the user via email. This newly-created membership will be in the \&quot;pending\&quot; state until the user accepts the invitation, at which point the membership will transition to the \&quot;active\&quot; state and the user will be added as a member of the team. To add a membership between an unaffiliated user and a team, the authenticated user must be an organization owner.  If the user is already a member of the team, this endpoint will update the role of the team member&#39;s role. To update the membership of a team member, the authenticated user must be an organization owner or a team maintainer.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let username = "username_example"; // String | 
let opts = {
  'teamsAddOrUpdateMembershipForUserRequest': new GitHubV3RestApi.TeamsAddOrUpdateMembershipForUserRequest() // TeamsAddOrUpdateMembershipForUserRequest | 
};
apiInstance.teamsAddOrUpdateMembershipForUser(teamId, username, opts, (error, data, response) => {
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
 **teamsAddOrUpdateMembershipForUserRequest** | [**TeamsAddOrUpdateMembershipForUserRequest**](TeamsAddOrUpdateMembershipForUserRequest.md)|  | [optional] 

### Return type

[**TeamMembership**](TeamMembership.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsAddOrUpdateProjectPermissions

> teamsAddOrUpdateProjectPermissions(accept, teamId, projectId, opts)

Add or update team project permissions

Adds an organization project to a team. To add a project to a team or update the team&#39;s permission on a project, the authenticated user must have &#x60;admin&#x60; permissions for the project. The project and team must be part of the same organization.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let accept = "'application/vnd.github.inertia-preview+json'"; // String | This API is under preview and subject to change.
let teamId = 56; // Number | 
let projectId = 56; // Number | 
let opts = {
  'teamsAddOrUpdateProjectPermissionsRequest': new GitHubV3RestApi.TeamsAddOrUpdateProjectPermissionsRequest() // TeamsAddOrUpdateProjectPermissionsRequest | 
};
apiInstance.teamsAddOrUpdateProjectPermissions(accept, teamId, projectId, opts, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.inertia-preview+json&#39;]
 **teamId** | **Number**|  | 
 **projectId** | **Number**|  | 
 **teamsAddOrUpdateProjectPermissionsRequest** | [**TeamsAddOrUpdateProjectPermissionsRequest**](TeamsAddOrUpdateProjectPermissionsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsAddOrUpdateRepoPermissions

> teamsAddOrUpdateRepoPermissions(teamId, owner, repo, opts)

Add or update team repository permissions

To add a repository to a team or update the team&#39;s permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a &#x60;422 Unprocessable Entity&#x60; status if you attempt to add a repository to a team that is not owned by the organization.  Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
let opts = {
  'teamsAddOrUpdateRepoPermissionsRequest': new GitHubV3RestApi.TeamsAddOrUpdateRepoPermissionsRequest() // TeamsAddOrUpdateRepoPermissionsRequest | 
};
apiInstance.teamsAddOrUpdateRepoPermissions(teamId, owner, repo, opts, (error, data, response) => {
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
 **teamsAddOrUpdateRepoPermissionsRequest** | [**TeamsAddOrUpdateRepoPermissionsRequest**](TeamsAddOrUpdateRepoPermissionsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## teamsCheckPermissionsForProject

> TeamProject teamsCheckPermissionsForProject(accept, teamId, projectId)

Check team permissions for a project

Checks whether a team has &#x60;read&#x60;, &#x60;write&#x60;, or &#x60;admin&#x60; permissions for an organization project. The response includes projects inherited from a parent team.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let accept = "'application/vnd.github.inertia-preview+json'"; // String | This API is under preview and subject to change.
let teamId = 56; // Number | 
let projectId = 56; // Number | 
apiInstance.teamsCheckPermissionsForProject(accept, teamId, projectId, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.inertia-preview+json&#39;]
 **teamId** | **Number**|  | 
 **projectId** | **Number**|  | 

### Return type

[**TeamProject**](TeamProject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsCheckPermissionsForRepo

> MinimalRepository teamsCheckPermissionsForRepo(teamId, owner, repo)

Check team permissions for a repository

**Note**: Repositories inherited through a parent team will also be checked.  You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/enterprise-server@2.20/rest/overview/media-types/) via the &#x60;Accept&#x60; header:

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
apiInstance.teamsCheckPermissionsForRepo(teamId, owner, repo, (error, data, response) => {
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

[**MinimalRepository**](MinimalRepository.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.github.v3.repository+json


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


## teamsCreateDiscussion

> TeamDiscussion teamsCreateDiscussion(teamId, teamsCreateDiscussionRequest)

Create a discussion

Creates a new discussion post on a team&#39;s page. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; for details.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let teamsCreateDiscussionRequest = {"body":"Hi! This is an area for us to collaborate as a team.","title":"Our first team post"}; // TeamsCreateDiscussionRequest | 
apiInstance.teamsCreateDiscussion(teamId, teamsCreateDiscussionRequest, (error, data, response) => {
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
 **teamsCreateDiscussionRequest** | [**TeamsCreateDiscussionRequest**](TeamsCreateDiscussionRequest.md)|  | 

### Return type

[**TeamDiscussion**](TeamDiscussion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsCreateDiscussionComment

> TeamDiscussionComment teamsCreateDiscussionComment(teamId, discussionNumber, teamsCreateDiscussionCommentRequest)

Create a discussion comment

Creates a new comment on a team discussion. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; for details.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
let teamsCreateDiscussionCommentRequest = {"body":"Do you like apples?"}; // TeamsCreateDiscussionCommentRequest | 
apiInstance.teamsCreateDiscussionComment(teamId, discussionNumber, teamsCreateDiscussionCommentRequest, (error, data, response) => {
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
 **teamsCreateDiscussionCommentRequest** | [**TeamsCreateDiscussionCommentRequest**](TeamsCreateDiscussionCommentRequest.md)|  | 

### Return type

[**TeamDiscussionComment**](TeamDiscussionComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsDelete

> teamsDelete(teamId)

Delete a team

To delete a team, the authenticated user must be an organization owner or team maintainer.  If you are an organization owner, deleting a parent team will delete all of its child teams as well.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
apiInstance.teamsDelete(teamId, (error, data, response) => {
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
- **Accept**: Not defined


## teamsDeleteDiscussion

> teamsDeleteDiscussion(teamId, discussionNumber)

Delete a discussion

Delete a discussion from a team&#39;s page. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
apiInstance.teamsDeleteDiscussion(teamId, discussionNumber, (error, data, response) => {
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


## teamsDeleteDiscussionComment

> teamsDeleteDiscussionComment(teamId, discussionNumber, commentNumber)

Delete a discussion comment

Deletes a comment on a team discussion. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
let commentNumber = 56; // Number | 
apiInstance.teamsDeleteDiscussionComment(teamId, discussionNumber, commentNumber, (error, data, response) => {
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


## teamsGet

> TeamFull teamsGet(teamId)

Get a team



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
apiInstance.teamsGet(teamId, (error, data, response) => {
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


## teamsGetDiscussion

> TeamDiscussion teamsGetDiscussion(teamId, discussionNumber)

Get a discussion

Get a specific discussion on a team&#39;s page. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
apiInstance.teamsGetDiscussion(teamId, discussionNumber, (error, data, response) => {
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


## teamsGetDiscussionComment

> TeamDiscussionComment teamsGetDiscussionComment(teamId, discussionNumber, commentNumber)

Get a discussion comment

Get a specific comment on a team discussion. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
let commentNumber = 56; // Number | 
apiInstance.teamsGetDiscussionComment(teamId, discussionNumber, commentNumber, (error, data, response) => {
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


## teamsGetMemberLegacy

> teamsGetMemberLegacy(teamId, username)

Get team member (Legacy)

The \&quot;Get team member\&quot; endpoint (described below) is deprecated.  We recommend using the [Get team membership for a user](https://docs.github.com/enterprise-server@2.20/rest/reference/teams#get-team-membership-for-a-user) endpoint instead. It allows you to get both active and pending memberships.  To list members in a team, the team must be visible to the authenticated user.

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


## teamsGetMembershipForUser

> TeamMembership teamsGetMembershipForUser(teamId, username)

Get team membership for a user

Team members will include the members of child teams.  To get a user&#39;s membership with a team, the team must be visible to the authenticated user.  **Note:** The &#x60;role&#x60; for organization owners returns as &#x60;maintainer&#x60;. For more information about &#x60;maintainer&#x60; roles, see [Create a team](https://docs.github.com/enterprise-server@2.20/rest/reference/teams#create-a-team).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let username = "username_example"; // String | 
apiInstance.teamsGetMembershipForUser(teamId, username, (error, data, response) => {
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


## teamsListChild

> [Team2] teamsListChild(teamId, opts)

List child teams



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.teamsListChild(teamId, opts, (error, data, response) => {
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

[**[Team2]**](Team2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsListDiscussionComments

> [TeamDiscussionComment] teamsListDiscussionComments(teamId, discussionNumber, opts)

List discussion comments

List all comments on a team discussion. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
let opts = {
  'direction': "'desc'", // String | Sorts the discussion comments by the date they were created. To return the oldest comments first, set to `asc`. Can be one of `asc` or `desc`.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.teamsListDiscussionComments(teamId, discussionNumber, opts, (error, data, response) => {
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
 **direction** | **String**| Sorts the discussion comments by the date they were created. To return the oldest comments first, set to &#x60;asc&#x60;. Can be one of &#x60;asc&#x60; or &#x60;desc&#x60;. | [optional] [default to &#39;desc&#39;]
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[TeamDiscussionComment]**](TeamDiscussionComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamsListDiscussions

> [TeamDiscussion] teamsListDiscussions(teamId, opts)

List discussions

List all discussions on a team&#39;s page. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let opts = {
  'direction': "'desc'", // String | Sorts the discussion comments by the date they were created. To return the oldest comments first, set to `asc`. Can be one of `asc` or `desc`.
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.teamsListDiscussions(teamId, opts, (error, data, response) => {
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
 **direction** | **String**| Sorts the discussion comments by the date they were created. To return the oldest comments first, set to &#x60;asc&#x60;. Can be one of &#x60;asc&#x60; or &#x60;desc&#x60;. | [optional] [default to &#39;desc&#39;]
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

List all of the teams across all of the organizations to which the authenticated user belongs. This method requires &#x60;user&#x60;, &#x60;repo&#x60;, or &#x60;read:org&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/) when authenticating via [OAuth](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/).

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


## teamsListMembers

> [SimpleUser] teamsListMembers(teamId, opts)

List team members

Team members will include the members of child teams.  To list members in a team, the team must be visible to the authenticated user.

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
apiInstance.teamsListMembers(teamId, opts, (error, data, response) => {
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


## teamsListProjects

> [TeamProject] teamsListProjects(accept, teamId, opts)

List team projects

Lists the organization projects for a team. If you are an [authenticated](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#authentication) site administrator for your Enterprise instance, you will be able to list all projects for the team.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let accept = "'application/vnd.github.inertia-preview+json'"; // String | This API is under preview and subject to change.
let teamId = 56; // Number | 
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.teamsListProjects(accept, teamId, opts, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.inertia-preview+json&#39;]
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


## teamsListRepos

> [MinimalRepository] teamsListRepos(teamId, opts)

List team repositories

If you are an [authenticated](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#authentication) site administrator for your Enterprise instance, you will be able to list all repositories for the team.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.teamsListRepos(teamId, opts, (error, data, response) => {
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

The \&quot;Remove team member\&quot; endpoint (described below) is deprecated.  We recommend using the [Remove team membership for a user](https://docs.github.com/enterprise-server@2.20/rest/reference/teams#remove-team-membership-for-a-user) endpoint instead. It allows you to remove both active and pending memberships.  Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  To remove a team member, the authenticated user must have &#39;admin&#39; permissions to the team or be an owner of the org that the team is associated with. Removing a team member does not delete the user, it just removes them from the team.  **Note:** When you have team synchronization set up for a team with your organization&#39;s identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team&#39;s membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \&quot;[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\&quot;

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


## teamsRemoveMembershipForUser

> teamsRemoveMembershipForUser(teamId, username)

Remove team membership for a user

To remove a membership between a user and a team, the authenticated user must have &#39;admin&#39; permissions to the team or be an owner of the organization that the team is associated with. Removing team membership does not delete the user, it just removes their membership from the team.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let username = "username_example"; // String | 
apiInstance.teamsRemoveMembershipForUser(teamId, username, (error, data, response) => {
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


## teamsRemoveProject

> teamsRemoveProject(teamId, projectId)

Remove a project from a team

Removes an organization project from a team. An organization owner or a team maintainer can remove any project from the team. To remove a project from a team as an organization member, the authenticated user must have &#x60;read&#x60; access to both the team and project, or &#x60;admin&#x60; access to the team or project. **Note:** This endpoint removes the project from the team, but does not delete it.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let projectId = 56; // Number | 
apiInstance.teamsRemoveProject(teamId, projectId, (error, data, response) => {
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
- **Accept**: Not defined


## teamsRemoveRepo

> teamsRemoveRepo(teamId, owner, repo)

Remove a repository from a team

If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. NOTE: This does not delete the repository, it just removes it from the team.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
apiInstance.teamsRemoveRepo(teamId, owner, repo, (error, data, response) => {
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


## teamsUpdate

> TeamFull teamsUpdate(teamId, opts)

Update a team

To edit a team, the authenticated user must either be an organization owner or a team maintainer.  **Note:** With nested teams, the &#x60;privacy&#x60; for parent teams cannot be &#x60;secret&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let opts = {
  'teamsUpdateRequest': {"description":"new team description","name":"new team name","privacy":"closed"} // TeamsUpdateRequest | 
};
apiInstance.teamsUpdate(teamId, opts, (error, data, response) => {
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
 **teamsUpdateRequest** | [**TeamsUpdateRequest**](TeamsUpdateRequest.md)|  | [optional] 

### Return type

[**TeamFull**](TeamFull.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsUpdateDiscussion

> TeamDiscussion teamsUpdateDiscussion(teamId, discussionNumber, opts)

Update a discussion

Edits the title and body text of a discussion post. Only the parameters you provide are updated. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
let opts = {
  'teamsUpdateDiscussionRequest': {"title":"Welcome to our first team post"} // TeamsUpdateDiscussionRequest | 
};
apiInstance.teamsUpdateDiscussion(teamId, discussionNumber, opts, (error, data, response) => {
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
 **teamsUpdateDiscussionRequest** | [**TeamsUpdateDiscussionRequest**](TeamsUpdateDiscussionRequest.md)|  | [optional] 

### Return type

[**TeamDiscussion**](TeamDiscussion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## teamsUpdateDiscussionComment

> TeamDiscussionComment teamsUpdateDiscussionComment(teamId, discussionNumber, commentNumber, teamsCreateDiscussionCommentRequest)

Update a discussion comment

Edits the body text of a discussion comment. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.TeamsApi();
let teamId = 56; // Number | 
let discussionNumber = 56; // Number | 
let commentNumber = 56; // Number | 
let teamsCreateDiscussionCommentRequest = {"body":"Do you like pineapples?"}; // TeamsCreateDiscussionCommentRequest | 
apiInstance.teamsUpdateDiscussionComment(teamId, discussionNumber, commentNumber, teamsCreateDiscussionCommentRequest, (error, data, response) => {
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
 **teamsCreateDiscussionCommentRequest** | [**TeamsCreateDiscussionCommentRequest**](TeamsCreateDiscussionCommentRequest.md)|  | 

### Return type

[**TeamDiscussionComment**](TeamDiscussionComment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

