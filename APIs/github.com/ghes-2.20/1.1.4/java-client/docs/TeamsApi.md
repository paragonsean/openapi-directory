# TeamsApi

All URIs are relative to *http://HOSTNAME/api/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**teamsAddMemberLegacy**](TeamsApi.md#teamsAddMemberLegacy) | **PUT** /teams/{team_id}/members/{username} | Add team member (Legacy) |
| [**teamsAddOrUpdateMembershipForUser**](TeamsApi.md#teamsAddOrUpdateMembershipForUser) | **PUT** /teams/{team_id}/memberships/{username} | Add or update team membership for a user |
| [**teamsAddOrUpdateProjectPermissions**](TeamsApi.md#teamsAddOrUpdateProjectPermissions) | **PUT** /teams/{team_id}/projects/{project_id} | Add or update team project permissions |
| [**teamsAddOrUpdateRepoPermissions**](TeamsApi.md#teamsAddOrUpdateRepoPermissions) | **PUT** /teams/{team_id}/repos/{owner}/{repo} | Add or update team repository permissions |
| [**teamsCheckPermissionsForProject**](TeamsApi.md#teamsCheckPermissionsForProject) | **GET** /teams/{team_id}/projects/{project_id} | Check team permissions for a project |
| [**teamsCheckPermissionsForRepo**](TeamsApi.md#teamsCheckPermissionsForRepo) | **GET** /teams/{team_id}/repos/{owner}/{repo} | Check team permissions for a repository |
| [**teamsCreate**](TeamsApi.md#teamsCreate) | **POST** /orgs/{org}/teams | Create a team |
| [**teamsCreateDiscussion**](TeamsApi.md#teamsCreateDiscussion) | **POST** /teams/{team_id}/discussions | Create a discussion |
| [**teamsCreateDiscussionComment**](TeamsApi.md#teamsCreateDiscussionComment) | **POST** /teams/{team_id}/discussions/{discussion_number}/comments | Create a discussion comment |
| [**teamsDelete**](TeamsApi.md#teamsDelete) | **DELETE** /teams/{team_id} | Delete a team |
| [**teamsDeleteDiscussion**](TeamsApi.md#teamsDeleteDiscussion) | **DELETE** /teams/{team_id}/discussions/{discussion_number} | Delete a discussion |
| [**teamsDeleteDiscussionComment**](TeamsApi.md#teamsDeleteDiscussionComment) | **DELETE** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number} | Delete a discussion comment |
| [**teamsGet**](TeamsApi.md#teamsGet) | **GET** /teams/{team_id} | Get a team |
| [**teamsGetByName**](TeamsApi.md#teamsGetByName) | **GET** /orgs/{org}/teams/{team_slug} | Get a team by name |
| [**teamsGetDiscussion**](TeamsApi.md#teamsGetDiscussion) | **GET** /teams/{team_id}/discussions/{discussion_number} | Get a discussion |
| [**teamsGetDiscussionComment**](TeamsApi.md#teamsGetDiscussionComment) | **GET** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number} | Get a discussion comment |
| [**teamsGetMemberLegacy**](TeamsApi.md#teamsGetMemberLegacy) | **GET** /teams/{team_id}/members/{username} | Get team member (Legacy) |
| [**teamsGetMembershipForUser**](TeamsApi.md#teamsGetMembershipForUser) | **GET** /teams/{team_id}/memberships/{username} | Get team membership for a user |
| [**teamsList**](TeamsApi.md#teamsList) | **GET** /orgs/{org}/teams | List teams |
| [**teamsListChild**](TeamsApi.md#teamsListChild) | **GET** /teams/{team_id}/teams | List child teams |
| [**teamsListDiscussionComments**](TeamsApi.md#teamsListDiscussionComments) | **GET** /teams/{team_id}/discussions/{discussion_number}/comments | List discussion comments |
| [**teamsListDiscussions**](TeamsApi.md#teamsListDiscussions) | **GET** /teams/{team_id}/discussions | List discussions |
| [**teamsListForAuthenticatedUser**](TeamsApi.md#teamsListForAuthenticatedUser) | **GET** /user/teams | List teams for the authenticated user |
| [**teamsListMembers**](TeamsApi.md#teamsListMembers) | **GET** /teams/{team_id}/members | List team members |
| [**teamsListProjects**](TeamsApi.md#teamsListProjects) | **GET** /teams/{team_id}/projects | List team projects |
| [**teamsListRepos**](TeamsApi.md#teamsListRepos) | **GET** /teams/{team_id}/repos | List team repositories |
| [**teamsRemoveMemberLegacy**](TeamsApi.md#teamsRemoveMemberLegacy) | **DELETE** /teams/{team_id}/members/{username} | Remove team member (Legacy) |
| [**teamsRemoveMembershipForUser**](TeamsApi.md#teamsRemoveMembershipForUser) | **DELETE** /teams/{team_id}/memberships/{username} | Remove team membership for a user |
| [**teamsRemoveProject**](TeamsApi.md#teamsRemoveProject) | **DELETE** /teams/{team_id}/projects/{project_id} | Remove a project from a team |
| [**teamsRemoveRepo**](TeamsApi.md#teamsRemoveRepo) | **DELETE** /teams/{team_id}/repos/{owner}/{repo} | Remove a repository from a team |
| [**teamsUpdate**](TeamsApi.md#teamsUpdate) | **PATCH** /teams/{team_id} | Update a team |
| [**teamsUpdateDiscussion**](TeamsApi.md#teamsUpdateDiscussion) | **PATCH** /teams/{team_id}/discussions/{discussion_number} | Update a discussion |
| [**teamsUpdateDiscussionComment**](TeamsApi.md#teamsUpdateDiscussionComment) | **PATCH** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number} | Update a discussion comment |


<a id="teamsAddMemberLegacy"></a>
# **teamsAddMemberLegacy**
> teamsAddMemberLegacy(teamId, username)

Add team member (Legacy)

The \&quot;Add team member\&quot; endpoint (described below) is deprecated.  We recommend using the [Add or update team membership for a user](https://docs.github.com/enterprise-server@2.20/rest/reference/teams#add-or-update-team-membership-for-a-user) endpoint instead. It allows you to invite new organization members to your teams.  Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  To add someone to a team, the authenticated user must be an organization owner or a team maintainer in the team they&#39;re changing. The person being added to the team must be a member of the team&#39;s organization.  **Note:** When you have team synchronization set up for a team with your organization&#39;s identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team&#39;s membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \&quot;[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\&quot;  Note that you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    String username = "username_example"; // String | 
    try {
      apiInstance.teamsAddMemberLegacy(teamId, username);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsAddMemberLegacy");
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
| **teamId** | **Integer**|  | |
| **username** | **String**|  | |

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
| **404** | Not Found if team synchronization is set up |  -  |
| **422** | Unprocessable Entity if you attempt to add an organization to a team or you attempt to add a user to a team when they are not a member of at least one other team in the same organization |  -  |

<a id="teamsAddOrUpdateMembershipForUser"></a>
# **teamsAddOrUpdateMembershipForUser**
> TeamMembership teamsAddOrUpdateMembershipForUser(teamId, username, teamsAddOrUpdateMembershipForUserRequest)

Add or update team membership for a user

If the user is already a member of the team&#39;s organization, this endpoint will add the user to the team. To add a membership between an organization member and a team, the authenticated user must be an organization owner or a team maintainer.  If the user is unaffiliated with the team&#39;s organization, this endpoint will send an invitation to the user via email. This newly-created membership will be in the \&quot;pending\&quot; state until the user accepts the invitation, at which point the membership will transition to the \&quot;active\&quot; state and the user will be added as a member of the team. To add a membership between an unaffiliated user and a team, the authenticated user must be an organization owner.  If the user is already a member of the team, this endpoint will update the role of the team member&#39;s role. To update the membership of a team member, the authenticated user must be an organization owner or a team maintainer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    String username = "username_example"; // String | 
    TeamsAddOrUpdateMembershipForUserRequest teamsAddOrUpdateMembershipForUserRequest = new TeamsAddOrUpdateMembershipForUserRequest(); // TeamsAddOrUpdateMembershipForUserRequest | 
    try {
      TeamMembership result = apiInstance.teamsAddOrUpdateMembershipForUser(teamId, username, teamsAddOrUpdateMembershipForUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsAddOrUpdateMembershipForUser");
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
| **teamId** | **Integer**|  | |
| **username** | **String**|  | |
| **teamsAddOrUpdateMembershipForUserRequest** | [**TeamsAddOrUpdateMembershipForUserRequest**](TeamsAddOrUpdateMembershipForUserRequest.md)|  | [optional] |

### Return type

[**TeamMembership**](TeamMembership.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **422** | Unprocessable Entity if you attempt to add an organization to a team |  -  |

<a id="teamsAddOrUpdateProjectPermissions"></a>
# **teamsAddOrUpdateProjectPermissions**
> teamsAddOrUpdateProjectPermissions(accept, teamId, projectId, teamsAddOrUpdateProjectPermissionsRequest)

Add or update team project permissions

Adds an organization project to a team. To add a project to a team or update the team&#39;s permission on a project, the authenticated user must have &#x60;admin&#x60; permissions for the project. The project and team must be part of the same organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String accept = "application/vnd.github.inertia-preview+json"; // String | This API is under preview and subject to change.
    Integer teamId = 56; // Integer | 
    Integer projectId = 56; // Integer | 
    TeamsAddOrUpdateProjectPermissionsRequest teamsAddOrUpdateProjectPermissionsRequest = new TeamsAddOrUpdateProjectPermissionsRequest(); // TeamsAddOrUpdateProjectPermissionsRequest | 
    try {
      apiInstance.teamsAddOrUpdateProjectPermissions(accept, teamId, projectId, teamsAddOrUpdateProjectPermissionsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsAddOrUpdateProjectPermissions");
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
| **accept** | **String**| This API is under preview and subject to change. | [default to application/vnd.github.inertia-preview+json] |
| **teamId** | **Integer**|  | |
| **projectId** | **Integer**|  | |
| **teamsAddOrUpdateProjectPermissionsRequest** | [**TeamsAddOrUpdateProjectPermissionsRequest**](TeamsAddOrUpdateProjectPermissionsRequest.md)|  | [optional] |

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
| **403** | Forbidden if the project is not owned by the organization |  -  |

<a id="teamsAddOrUpdateRepoPermissions"></a>
# **teamsAddOrUpdateRepoPermissions**
> teamsAddOrUpdateRepoPermissions(teamId, owner, repo, teamsAddOrUpdateRepoPermissionsRequest)

Add or update team repository permissions

To add a repository to a team or update the team&#39;s permission on a repository, the authenticated user must have admin access to the repository, and must be able to see the team. The repository must be owned by the organization, or a direct fork of a repository owned by the organization. You will get a &#x60;422 Unprocessable Entity&#x60; status if you attempt to add a repository to a team that is not owned by the organization.  Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    TeamsAddOrUpdateRepoPermissionsRequest teamsAddOrUpdateRepoPermissionsRequest = new TeamsAddOrUpdateRepoPermissionsRequest(); // TeamsAddOrUpdateRepoPermissionsRequest | 
    try {
      apiInstance.teamsAddOrUpdateRepoPermissions(teamId, owner, repo, teamsAddOrUpdateRepoPermissionsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsAddOrUpdateRepoPermissions");
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
| **teamId** | **Integer**|  | |
| **owner** | **String**|  | |
| **repo** | **String**|  | |
| **teamsAddOrUpdateRepoPermissionsRequest** | [**TeamsAddOrUpdateRepoPermissionsRequest**](TeamsAddOrUpdateRepoPermissionsRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |

<a id="teamsCheckPermissionsForProject"></a>
# **teamsCheckPermissionsForProject**
> TeamProject teamsCheckPermissionsForProject(accept, teamId, projectId)

Check team permissions for a project

Checks whether a team has &#x60;read&#x60;, &#x60;write&#x60;, or &#x60;admin&#x60; permissions for an organization project. The response includes projects inherited from a parent team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String accept = "application/vnd.github.inertia-preview+json"; // String | This API is under preview and subject to change.
    Integer teamId = 56; // Integer | 
    Integer projectId = 56; // Integer | 
    try {
      TeamProject result = apiInstance.teamsCheckPermissionsForProject(accept, teamId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsCheckPermissionsForProject");
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
| **accept** | **String**| This API is under preview and subject to change. | [default to application/vnd.github.inertia-preview+json] |
| **teamId** | **Integer**|  | |
| **projectId** | **Integer**|  | |

### Return type

[**TeamProject**](TeamProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Not Found if project is not managed by this team |  -  |

<a id="teamsCheckPermissionsForRepo"></a>
# **teamsCheckPermissionsForRepo**
> MinimalRepository teamsCheckPermissionsForRepo(teamId, owner, repo)

Check team permissions for a repository

**Note**: Repositories inherited through a parent team will also be checked.  You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/enterprise-server@2.20/rest/overview/media-types/) via the &#x60;Accept&#x60; header:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      MinimalRepository result = apiInstance.teamsCheckPermissionsForRepo(teamId, owner, repo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsCheckPermissionsForRepo");
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
| **teamId** | **Integer**|  | |
| **owner** | **String**|  | |
| **repo** | **String**|  | |

### Return type

[**MinimalRepository**](MinimalRepository.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.github.v3.repository+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Alternative response with extra repository information |  -  |
| **204** | Response if repository is managed by this team |  -  |
| **404** | Not Found if repository is not managed by this team |  -  |

<a id="teamsCreate"></a>
# **teamsCreate**
> TeamFull teamsCreate(org, teamsCreateRequest)

Create a team

To create a team, the authenticated user must be a member or owner of &#x60;{org}&#x60;. By default, organization members can create teams. Organization owners can limit team creation to organization owners. For more information, see \&quot;[Setting team creation permissions](https://help.github.com/en/articles/setting-team-creation-permissions-in-your-organization).\&quot;  When you create a new team, you automatically become a team maintainer without explicitly adding yourself to the optional array of &#x60;maintainers&#x60;. For more information, see \&quot;[About teams](https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/about-teams)\&quot;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String org = "org_example"; // String | 
    TeamsCreateRequest teamsCreateRequest = new TeamsCreateRequest(); // TeamsCreateRequest | 
    try {
      TeamFull result = apiInstance.teamsCreate(org, teamsCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsCreate");
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
| **teamsCreateRequest** | [**TeamsCreateRequest**](TeamsCreateRequest.md)|  | |

### Return type

[**TeamFull**](TeamFull.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |
| **403** | Forbidden |  -  |
| **422** | Validation failed |  -  |

<a id="teamsCreateDiscussion"></a>
# **teamsCreateDiscussion**
> TeamDiscussion teamsCreateDiscussion(teamId, teamsCreateDiscussionRequest)

Create a discussion

Creates a new discussion post on a team&#39;s page. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; for details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    TeamsCreateDiscussionRequest teamsCreateDiscussionRequest = new TeamsCreateDiscussionRequest(); // TeamsCreateDiscussionRequest | 
    try {
      TeamDiscussion result = apiInstance.teamsCreateDiscussion(teamId, teamsCreateDiscussionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsCreateDiscussion");
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
| **teamId** | **Integer**|  | |
| **teamsCreateDiscussionRequest** | [**TeamsCreateDiscussionRequest**](TeamsCreateDiscussionRequest.md)|  | |

### Return type

[**TeamDiscussion**](TeamDiscussion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="teamsCreateDiscussionComment"></a>
# **teamsCreateDiscussionComment**
> TeamDiscussionComment teamsCreateDiscussionComment(teamId, discussionNumber, teamsCreateDiscussionCommentRequest)

Create a discussion comment

Creates a new comment on a team discussion. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; for details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    Integer discussionNumber = 56; // Integer | 
    TeamsCreateDiscussionCommentRequest teamsCreateDiscussionCommentRequest = new TeamsCreateDiscussionCommentRequest(); // TeamsCreateDiscussionCommentRequest | 
    try {
      TeamDiscussionComment result = apiInstance.teamsCreateDiscussionComment(teamId, discussionNumber, teamsCreateDiscussionCommentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsCreateDiscussionComment");
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
| **teamId** | **Integer**|  | |
| **discussionNumber** | **Integer**|  | |
| **teamsCreateDiscussionCommentRequest** | [**TeamsCreateDiscussionCommentRequest**](TeamsCreateDiscussionCommentRequest.md)|  | |

### Return type

[**TeamDiscussionComment**](TeamDiscussionComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="teamsDelete"></a>
# **teamsDelete**
> teamsDelete(teamId)

Delete a team

To delete a team, the authenticated user must be an organization owner or team maintainer.  If you are an organization owner, deleting a parent team will delete all of its child teams as well.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    try {
      apiInstance.teamsDelete(teamId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsDelete");
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
| **teamId** | **Integer**|  | |

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

<a id="teamsDeleteDiscussion"></a>
# **teamsDeleteDiscussion**
> teamsDeleteDiscussion(teamId, discussionNumber)

Delete a discussion

Delete a discussion from a team&#39;s page. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    Integer discussionNumber = 56; // Integer | 
    try {
      apiInstance.teamsDeleteDiscussion(teamId, discussionNumber);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsDeleteDiscussion");
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
| **teamId** | **Integer**|  | |
| **discussionNumber** | **Integer**|  | |

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

<a id="teamsDeleteDiscussionComment"></a>
# **teamsDeleteDiscussionComment**
> teamsDeleteDiscussionComment(teamId, discussionNumber, commentNumber)

Delete a discussion comment

Deletes a comment on a team discussion. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    Integer discussionNumber = 56; // Integer | 
    Integer commentNumber = 56; // Integer | 
    try {
      apiInstance.teamsDeleteDiscussionComment(teamId, discussionNumber, commentNumber);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsDeleteDiscussionComment");
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
| **teamId** | **Integer**|  | |
| **discussionNumber** | **Integer**|  | |
| **commentNumber** | **Integer**|  | |

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

<a id="teamsGet"></a>
# **teamsGet**
> TeamFull teamsGet(teamId)

Get a team



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    try {
      TeamFull result = apiInstance.teamsGet(teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsGet");
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
| **teamId** | **Integer**|  | |

### Return type

[**TeamFull**](TeamFull.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="teamsGetByName"></a>
# **teamsGetByName**
> TeamFull teamsGetByName(org, teamSlug)

Get a team by name

Gets a team using the team&#39;s &#x60;slug&#x60;. GitHub Enterprise Server generates the &#x60;slug&#x60; from the team &#x60;name&#x60;.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/{org_id}/team/{team_id}&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String org = "org_example"; // String | 
    String teamSlug = "teamSlug_example"; // String | team_slug parameter
    try {
      TeamFull result = apiInstance.teamsGetByName(org, teamSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsGetByName");
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
| **teamSlug** | **String**| team_slug parameter | |

### Return type

[**TeamFull**](TeamFull.md)

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

<a id="teamsGetDiscussion"></a>
# **teamsGetDiscussion**
> TeamDiscussion teamsGetDiscussion(teamId, discussionNumber)

Get a discussion

Get a specific discussion on a team&#39;s page. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    Integer discussionNumber = 56; // Integer | 
    try {
      TeamDiscussion result = apiInstance.teamsGetDiscussion(teamId, discussionNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsGetDiscussion");
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
| **teamId** | **Integer**|  | |
| **discussionNumber** | **Integer**|  | |

### Return type

[**TeamDiscussion**](TeamDiscussion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="teamsGetDiscussionComment"></a>
# **teamsGetDiscussionComment**
> TeamDiscussionComment teamsGetDiscussionComment(teamId, discussionNumber, commentNumber)

Get a discussion comment

Get a specific comment on a team discussion. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    Integer discussionNumber = 56; // Integer | 
    Integer commentNumber = 56; // Integer | 
    try {
      TeamDiscussionComment result = apiInstance.teamsGetDiscussionComment(teamId, discussionNumber, commentNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsGetDiscussionComment");
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
| **teamId** | **Integer**|  | |
| **discussionNumber** | **Integer**|  | |
| **commentNumber** | **Integer**|  | |

### Return type

[**TeamDiscussionComment**](TeamDiscussionComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="teamsGetMemberLegacy"></a>
# **teamsGetMemberLegacy**
> teamsGetMemberLegacy(teamId, username)

Get team member (Legacy)

The \&quot;Get team member\&quot; endpoint (described below) is deprecated.  We recommend using the [Get team membership for a user](https://docs.github.com/enterprise-server@2.20/rest/reference/teams#get-team-membership-for-a-user) endpoint instead. It allows you to get both active and pending memberships.  To list members in a team, the team must be visible to the authenticated user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    String username = "username_example"; // String | 
    try {
      apiInstance.teamsGetMemberLegacy(teamId, username);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsGetMemberLegacy");
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
| **teamId** | **Integer**|  | |
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
| **204** | if user is a member |  -  |
| **404** | if user is not a member |  -  |

<a id="teamsGetMembershipForUser"></a>
# **teamsGetMembershipForUser**
> TeamMembership teamsGetMembershipForUser(teamId, username)

Get team membership for a user

Team members will include the members of child teams.  To get a user&#39;s membership with a team, the team must be visible to the authenticated user.  **Note:** The &#x60;role&#x60; for organization owners returns as &#x60;maintainer&#x60;. For more information about &#x60;maintainer&#x60; roles, see [Create a team](https://docs.github.com/enterprise-server@2.20/rest/reference/teams#create-a-team).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    String username = "username_example"; // String | 
    try {
      TeamMembership result = apiInstance.teamsGetMembershipForUser(teamId, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsGetMembershipForUser");
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
| **teamId** | **Integer**|  | |
| **username** | **String**|  | |

### Return type

[**TeamMembership**](TeamMembership.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="teamsList"></a>
# **teamsList**
> List&lt;Team&gt; teamsList(org, perPage, page)

List teams

Lists all teams in an organization that are visible to the authenticated user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String org = "org_example"; // String | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Team> result = apiInstance.teamsList(org, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsList");
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
| **403** | Forbidden |  -  |

<a id="teamsListChild"></a>
# **teamsListChild**
> List&lt;Team2&gt; teamsListChild(teamId, perPage, page)

List child teams



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Team2> result = apiInstance.teamsListChild(teamId, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsListChild");
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
| **teamId** | **Integer**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Team2&gt;**](Team2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | if child teams exist |  * Link -  <br>  |

<a id="teamsListDiscussionComments"></a>
# **teamsListDiscussionComments**
> List&lt;TeamDiscussionComment&gt; teamsListDiscussionComments(teamId, discussionNumber, direction, perPage, page)

List discussion comments

List all comments on a team discussion. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    Integer discussionNumber = 56; // Integer | 
    String direction = "asc"; // String | Sorts the discussion comments by the date they were created. To return the oldest comments first, set to `asc`. Can be one of `asc` or `desc`.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<TeamDiscussionComment> result = apiInstance.teamsListDiscussionComments(teamId, discussionNumber, direction, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsListDiscussionComments");
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
| **teamId** | **Integer**|  | |
| **discussionNumber** | **Integer**|  | |
| **direction** | **String**| Sorts the discussion comments by the date they were created. To return the oldest comments first, set to &#x60;asc&#x60;. Can be one of &#x60;asc&#x60; or &#x60;desc&#x60;. | [optional] [default to desc] [enum: asc, desc] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;TeamDiscussionComment&gt;**](TeamDiscussionComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="teamsListDiscussions"></a>
# **teamsListDiscussions**
> List&lt;TeamDiscussion&gt; teamsListDiscussions(teamId, direction, perPage, page)

List discussions

List all discussions on a team&#39;s page. OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    String direction = "asc"; // String | Sorts the discussion comments by the date they were created. To return the oldest comments first, set to `asc`. Can be one of `asc` or `desc`.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<TeamDiscussion> result = apiInstance.teamsListDiscussions(teamId, direction, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsListDiscussions");
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
| **teamId** | **Integer**|  | |
| **direction** | **String**| Sorts the discussion comments by the date they were created. To return the oldest comments first, set to &#x60;asc&#x60;. Can be one of &#x60;asc&#x60; or &#x60;desc&#x60;. | [optional] [default to desc] [enum: asc, desc] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;TeamDiscussion&gt;**](TeamDiscussion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="teamsListForAuthenticatedUser"></a>
# **teamsListForAuthenticatedUser**
> List&lt;TeamFull&gt; teamsListForAuthenticatedUser(perPage, page)

List teams for the authenticated user

List all of the teams across all of the organizations to which the authenticated user belongs. This method requires &#x60;user&#x60;, &#x60;repo&#x60;, or &#x60;read:org&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/) when authenticating via [OAuth](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<TeamFull> result = apiInstance.teamsListForAuthenticatedUser(perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsListForAuthenticatedUser");
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

[**List&lt;TeamFull&gt;**](TeamFull.md)

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
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="teamsListMembers"></a>
# **teamsListMembers**
> List&lt;SimpleUser&gt; teamsListMembers(teamId, role, perPage, page)

List team members

Team members will include the members of child teams.  To list members in a team, the team must be visible to the authenticated user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    String role = "member"; // String | Filters members returned by their role in the team. Can be one of:   \\* `member` - normal members of the team.   \\* `maintainer` - team maintainers.   \\* `all` - all members of the team.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<SimpleUser> result = apiInstance.teamsListMembers(teamId, role, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsListMembers");
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
| **teamId** | **Integer**|  | |
| **role** | **String**| Filters members returned by their role in the team. Can be one of:   \\* &#x60;member&#x60; - normal members of the team.   \\* &#x60;maintainer&#x60; - team maintainers.   \\* &#x60;all&#x60; - all members of the team. | [optional] [default to all] [enum: member, maintainer, all] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

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
| **200** | Response |  * Link -  <br>  |

<a id="teamsListProjects"></a>
# **teamsListProjects**
> List&lt;TeamProject&gt; teamsListProjects(accept, teamId, perPage, page)

List team projects

Lists the organization projects for a team. If you are an [authenticated](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#authentication) site administrator for your Enterprise instance, you will be able to list all projects for the team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    String accept = "application/vnd.github.inertia-preview+json"; // String | This API is under preview and subject to change.
    Integer teamId = 56; // Integer | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<TeamProject> result = apiInstance.teamsListProjects(accept, teamId, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsListProjects");
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
| **accept** | **String**| This API is under preview and subject to change. | [default to application/vnd.github.inertia-preview+json] |
| **teamId** | **Integer**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;TeamProject&gt;**](TeamProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="teamsListRepos"></a>
# **teamsListRepos**
> List&lt;MinimalRepository&gt; teamsListRepos(teamId, perPage, page)

List team repositories

If you are an [authenticated](https://docs.github.com/enterprise-server@2.20/rest/overview/resources-in-the-rest-api#authentication) site administrator for your Enterprise instance, you will be able to list all repositories for the team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<MinimalRepository> result = apiInstance.teamsListRepos(teamId, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsListRepos");
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
| **teamId** | **Integer**|  | |
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

<a id="teamsRemoveMemberLegacy"></a>
# **teamsRemoveMemberLegacy**
> teamsRemoveMemberLegacy(teamId, username)

Remove team member (Legacy)

The \&quot;Remove team member\&quot; endpoint (described below) is deprecated.  We recommend using the [Remove team membership for a user](https://docs.github.com/enterprise-server@2.20/rest/reference/teams#remove-team-membership-for-a-user) endpoint instead. It allows you to remove both active and pending memberships.  Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  To remove a team member, the authenticated user must have &#39;admin&#39; permissions to the team or be an owner of the org that the team is associated with. Removing a team member does not delete the user, it just removes them from the team.  **Note:** When you have team synchronization set up for a team with your organization&#39;s identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team&#39;s membership. If you have access to manage group membership in your IdP, you can manage GitHub Enterprise Server team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see \&quot;[Synchronizing teams between your identity provider and GitHub Enterprise Server](https://help.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/).\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    String username = "username_example"; // String | 
    try {
      apiInstance.teamsRemoveMemberLegacy(teamId, username);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsRemoveMemberLegacy");
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
| **teamId** | **Integer**|  | |
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
| **404** | Not Found if team synchronization is setup |  -  |

<a id="teamsRemoveMembershipForUser"></a>
# **teamsRemoveMembershipForUser**
> teamsRemoveMembershipForUser(teamId, username)

Remove team membership for a user

To remove a membership between a user and a team, the authenticated user must have &#39;admin&#39; permissions to the team or be an owner of the organization that the team is associated with. Removing team membership does not delete the user, it just removes their membership from the team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    String username = "username_example"; // String | 
    try {
      apiInstance.teamsRemoveMembershipForUser(teamId, username);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsRemoveMembershipForUser");
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
| **teamId** | **Integer**|  | |
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

<a id="teamsRemoveProject"></a>
# **teamsRemoveProject**
> teamsRemoveProject(teamId, projectId)

Remove a project from a team

Removes an organization project from a team. An organization owner or a team maintainer can remove any project from the team. To remove a project from a team as an organization member, the authenticated user must have &#x60;read&#x60; access to both the team and project, or &#x60;admin&#x60; access to the team or project. **Note:** This endpoint removes the project from the team, but does not delete it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    Integer projectId = 56; // Integer | 
    try {
      apiInstance.teamsRemoveProject(teamId, projectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsRemoveProject");
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
| **teamId** | **Integer**|  | |
| **projectId** | **Integer**|  | |

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

<a id="teamsRemoveRepo"></a>
# **teamsRemoveRepo**
> teamsRemoveRepo(teamId, owner, repo)

Remove a repository from a team

If the authenticated user is an organization owner or a team maintainer, they can remove any repositories from the team. To remove a repository from a team as an organization member, the authenticated user must have admin access to the repository and must be able to see the team. NOTE: This does not delete the repository, it just removes it from the team.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    try {
      apiInstance.teamsRemoveRepo(teamId, owner, repo);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsRemoveRepo");
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
| **teamId** | **Integer**|  | |
| **owner** | **String**|  | |
| **repo** | **String**|  | |

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

<a id="teamsUpdate"></a>
# **teamsUpdate**
> TeamFull teamsUpdate(teamId, teamsUpdateRequest)

Update a team

To edit a team, the authenticated user must either be an organization owner or a team maintainer.  **Note:** With nested teams, the &#x60;privacy&#x60; for parent teams cannot be &#x60;secret&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    TeamsUpdateRequest teamsUpdateRequest = new TeamsUpdateRequest(); // TeamsUpdateRequest | 
    try {
      TeamFull result = apiInstance.teamsUpdate(teamId, teamsUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsUpdate");
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
| **teamId** | **Integer**|  | |
| **teamsUpdateRequest** | [**TeamsUpdateRequest**](TeamsUpdateRequest.md)|  | [optional] |

### Return type

[**TeamFull**](TeamFull.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="teamsUpdateDiscussion"></a>
# **teamsUpdateDiscussion**
> TeamDiscussion teamsUpdateDiscussion(teamId, discussionNumber, teamsUpdateDiscussionRequest)

Update a discussion

Edits the title and body text of a discussion post. Only the parameters you provide are updated. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    Integer discussionNumber = 56; // Integer | 
    TeamsUpdateDiscussionRequest teamsUpdateDiscussionRequest = new TeamsUpdateDiscussionRequest(); // TeamsUpdateDiscussionRequest | 
    try {
      TeamDiscussion result = apiInstance.teamsUpdateDiscussion(teamId, discussionNumber, teamsUpdateDiscussionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsUpdateDiscussion");
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
| **teamId** | **Integer**|  | |
| **discussionNumber** | **Integer**|  | |
| **teamsUpdateDiscussionRequest** | [**TeamsUpdateDiscussionRequest**](TeamsUpdateDiscussionRequest.md)|  | [optional] |

### Return type

[**TeamDiscussion**](TeamDiscussion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="teamsUpdateDiscussionComment"></a>
# **teamsUpdateDiscussionComment**
> TeamDiscussionComment teamsUpdateDiscussionComment(teamId, discussionNumber, commentNumber, teamsCreateDiscussionCommentRequest)

Update a discussion comment

Edits the body text of a discussion comment. OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.20/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TeamsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    TeamsApi apiInstance = new TeamsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    Integer discussionNumber = 56; // Integer | 
    Integer commentNumber = 56; // Integer | 
    TeamsCreateDiscussionCommentRequest teamsCreateDiscussionCommentRequest = new TeamsCreateDiscussionCommentRequest(); // TeamsCreateDiscussionCommentRequest | 
    try {
      TeamDiscussionComment result = apiInstance.teamsUpdateDiscussionComment(teamId, discussionNumber, commentNumber, teamsCreateDiscussionCommentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TeamsApi#teamsUpdateDiscussionComment");
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
| **teamId** | **Integer**|  | |
| **discussionNumber** | **Integer**|  | |
| **commentNumber** | **Integer**|  | |
| **teamsCreateDiscussionCommentRequest** | [**TeamsCreateDiscussionCommentRequest**](TeamsCreateDiscussionCommentRequest.md)|  | |

### Return type

[**TeamDiscussionComment**](TeamDiscussionComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

