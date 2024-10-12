# ReactionsApi

All URIs are relative to *http://HOSTNAME/api/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reactionsCreateForCommitComment**](ReactionsApi.md#reactionsCreateForCommitComment) | **POST** /repos/{owner}/{repo}/comments/{comment_id}/reactions | Create reaction for a commit comment |
| [**reactionsCreateForIssue**](ReactionsApi.md#reactionsCreateForIssue) | **POST** /repos/{owner}/{repo}/issues/{issue_number}/reactions | Create reaction for an issue |
| [**reactionsCreateForIssueComment**](ReactionsApi.md#reactionsCreateForIssueComment) | **POST** /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions | Create reaction for an issue comment |
| [**reactionsCreateForPullRequestReviewComment**](ReactionsApi.md#reactionsCreateForPullRequestReviewComment) | **POST** /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions | Create reaction for a pull request review comment |
| [**reactionsCreateForTeamDiscussionCommentInOrg**](ReactionsApi.md#reactionsCreateForTeamDiscussionCommentInOrg) | **POST** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions | Create reaction for a team discussion comment |
| [**reactionsCreateForTeamDiscussionCommentLegacy**](ReactionsApi.md#reactionsCreateForTeamDiscussionCommentLegacy) | **POST** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions | Create reaction for a team discussion comment (Legacy) |
| [**reactionsCreateForTeamDiscussionInOrg**](ReactionsApi.md#reactionsCreateForTeamDiscussionInOrg) | **POST** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions | Create reaction for a team discussion |
| [**reactionsCreateForTeamDiscussionLegacy**](ReactionsApi.md#reactionsCreateForTeamDiscussionLegacy) | **POST** /teams/{team_id}/discussions/{discussion_number}/reactions | Create reaction for a team discussion (Legacy) |
| [**reactionsDeleteForCommitComment**](ReactionsApi.md#reactionsDeleteForCommitComment) | **DELETE** /repos/{owner}/{repo}/comments/{comment_id}/reactions/{reaction_id} | Delete a commit comment reaction |
| [**reactionsDeleteForIssue**](ReactionsApi.md#reactionsDeleteForIssue) | **DELETE** /repos/{owner}/{repo}/issues/{issue_number}/reactions/{reaction_id} | Delete an issue reaction |
| [**reactionsDeleteForIssueComment**](ReactionsApi.md#reactionsDeleteForIssueComment) | **DELETE** /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions/{reaction_id} | Delete an issue comment reaction |
| [**reactionsDeleteForPullRequestComment**](ReactionsApi.md#reactionsDeleteForPullRequestComment) | **DELETE** /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions/{reaction_id} | Delete a pull request comment reaction |
| [**reactionsDeleteForTeamDiscussion**](ReactionsApi.md#reactionsDeleteForTeamDiscussion) | **DELETE** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions/{reaction_id} | Delete team discussion reaction |
| [**reactionsDeleteForTeamDiscussionComment**](ReactionsApi.md#reactionsDeleteForTeamDiscussionComment) | **DELETE** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions/{reaction_id} | Delete team discussion comment reaction |
| [**reactionsDeleteLegacy**](ReactionsApi.md#reactionsDeleteLegacy) | **DELETE** /reactions/{reaction_id} | Delete a reaction (Legacy) |
| [**reactionsListForCommitComment**](ReactionsApi.md#reactionsListForCommitComment) | **GET** /repos/{owner}/{repo}/comments/{comment_id}/reactions | List reactions for a commit comment |
| [**reactionsListForIssue**](ReactionsApi.md#reactionsListForIssue) | **GET** /repos/{owner}/{repo}/issues/{issue_number}/reactions | List reactions for an issue |
| [**reactionsListForIssueComment**](ReactionsApi.md#reactionsListForIssueComment) | **GET** /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions | List reactions for an issue comment |
| [**reactionsListForPullRequestReviewComment**](ReactionsApi.md#reactionsListForPullRequestReviewComment) | **GET** /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions | List reactions for a pull request review comment |
| [**reactionsListForTeamDiscussionCommentInOrg**](ReactionsApi.md#reactionsListForTeamDiscussionCommentInOrg) | **GET** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions | List reactions for a team discussion comment |
| [**reactionsListForTeamDiscussionCommentLegacy**](ReactionsApi.md#reactionsListForTeamDiscussionCommentLegacy) | **GET** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions | List reactions for a team discussion comment (Legacy) |
| [**reactionsListForTeamDiscussionInOrg**](ReactionsApi.md#reactionsListForTeamDiscussionInOrg) | **GET** /orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions | List reactions for a team discussion |
| [**reactionsListForTeamDiscussionLegacy**](ReactionsApi.md#reactionsListForTeamDiscussionLegacy) | **GET** /teams/{team_id}/discussions/{discussion_number}/reactions | List reactions for a team discussion (Legacy) |


<a id="reactionsCreateForCommitComment"></a>
# **reactionsCreateForCommitComment**
> Reaction reactionsCreateForCommitComment(owner, repo, commentId, reactionsCreateForCommitCommentRequest)

Create reaction for a commit comment

Create a reaction to a [commit comment](https://docs.github.com/enterprise-server@2.22/rest/reference/repos#comments). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this commit comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer commentId = 56; // Integer | comment_id parameter
    ReactionsCreateForCommitCommentRequest reactionsCreateForCommitCommentRequest = new ReactionsCreateForCommitCommentRequest(); // ReactionsCreateForCommitCommentRequest | 
    try {
      Reaction result = apiInstance.reactionsCreateForCommitComment(owner, repo, commentId, reactionsCreateForCommitCommentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsCreateForCommitComment");
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
| **reactionsCreateForCommitCommentRequest** | [**ReactionsCreateForCommitCommentRequest**](ReactionsCreateForCommitCommentRequest.md)|  | |

### Return type

[**Reaction**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reaction exists |  -  |
| **201** | Reaction created |  -  |
| **415** | Preview header missing |  -  |
| **422** | Validation failed |  -  |

<a id="reactionsCreateForIssue"></a>
# **reactionsCreateForIssue**
> Reaction reactionsCreateForIssue(owner, repo, issueNumber, reactionsCreateForIssueRequest)

Create reaction for an issue

Create a reaction to an [issue](https://docs.github.com/enterprise-server@2.22/rest/reference/issues/). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer issueNumber = 56; // Integer | issue_number parameter
    ReactionsCreateForIssueRequest reactionsCreateForIssueRequest = new ReactionsCreateForIssueRequest(); // ReactionsCreateForIssueRequest | 
    try {
      Reaction result = apiInstance.reactionsCreateForIssue(owner, repo, issueNumber, reactionsCreateForIssueRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsCreateForIssue");
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
| **issueNumber** | **Integer**| issue_number parameter | |
| **reactionsCreateForIssueRequest** | [**ReactionsCreateForIssueRequest**](ReactionsCreateForIssueRequest.md)|  | |

### Return type

[**Reaction**](Reaction.md)

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
| **422** | Validation failed |  -  |

<a id="reactionsCreateForIssueComment"></a>
# **reactionsCreateForIssueComment**
> Reaction reactionsCreateForIssueComment(owner, repo, commentId, reactionsCreateForIssueCommentRequest)

Create reaction for an issue comment

Create a reaction to an [issue comment](https://docs.github.com/enterprise-server@2.22/rest/reference/issues#comments). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this issue comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer commentId = 56; // Integer | comment_id parameter
    ReactionsCreateForIssueCommentRequest reactionsCreateForIssueCommentRequest = new ReactionsCreateForIssueCommentRequest(); // ReactionsCreateForIssueCommentRequest | 
    try {
      Reaction result = apiInstance.reactionsCreateForIssueComment(owner, repo, commentId, reactionsCreateForIssueCommentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsCreateForIssueComment");
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
| **reactionsCreateForIssueCommentRequest** | [**ReactionsCreateForIssueCommentRequest**](ReactionsCreateForIssueCommentRequest.md)|  | |

### Return type

[**Reaction**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reaction exists |  -  |
| **201** | Reaction created |  -  |
| **422** | Validation failed |  -  |

<a id="reactionsCreateForPullRequestReviewComment"></a>
# **reactionsCreateForPullRequestReviewComment**
> Reaction reactionsCreateForPullRequestReviewComment(owner, repo, commentId, reactionsCreateForPullRequestReviewCommentRequest)

Create reaction for a pull request review comment

Create a reaction to a [pull request review comment](https://docs.github.com/enterprise-server@2.22/rest/reference/pulls#comments). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this pull request review comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer commentId = 56; // Integer | comment_id parameter
    ReactionsCreateForPullRequestReviewCommentRequest reactionsCreateForPullRequestReviewCommentRequest = new ReactionsCreateForPullRequestReviewCommentRequest(); // ReactionsCreateForPullRequestReviewCommentRequest | 
    try {
      Reaction result = apiInstance.reactionsCreateForPullRequestReviewComment(owner, repo, commentId, reactionsCreateForPullRequestReviewCommentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsCreateForPullRequestReviewComment");
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
| **reactionsCreateForPullRequestReviewCommentRequest** | [**ReactionsCreateForPullRequestReviewCommentRequest**](ReactionsCreateForPullRequestReviewCommentRequest.md)|  | |

### Return type

[**Reaction**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reaction exists |  -  |
| **201** | Reaction created |  -  |
| **422** | Validation failed |  -  |

<a id="reactionsCreateForTeamDiscussionCommentInOrg"></a>
# **reactionsCreateForTeamDiscussionCommentInOrg**
> Reaction reactionsCreateForTeamDiscussionCommentInOrg(org, teamSlug, discussionNumber, commentNumber, reactionsCreateForTeamDiscussionCommentInOrgRequest)

Create reaction for a team discussion comment

Create a reaction to a [team discussion comment](https://docs.github.com/enterprise-server@2.22/rest/reference/teams#discussion-comments). OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this team discussion comment.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;POST /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String org = "org_example"; // String | 
    String teamSlug = "teamSlug_example"; // String | team_slug parameter
    Integer discussionNumber = 56; // Integer | 
    Integer commentNumber = 56; // Integer | 
    ReactionsCreateForTeamDiscussionCommentInOrgRequest reactionsCreateForTeamDiscussionCommentInOrgRequest = new ReactionsCreateForTeamDiscussionCommentInOrgRequest(); // ReactionsCreateForTeamDiscussionCommentInOrgRequest | 
    try {
      Reaction result = apiInstance.reactionsCreateForTeamDiscussionCommentInOrg(org, teamSlug, discussionNumber, commentNumber, reactionsCreateForTeamDiscussionCommentInOrgRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsCreateForTeamDiscussionCommentInOrg");
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
| **discussionNumber** | **Integer**|  | |
| **commentNumber** | **Integer**|  | |
| **reactionsCreateForTeamDiscussionCommentInOrgRequest** | [**ReactionsCreateForTeamDiscussionCommentInOrgRequest**](ReactionsCreateForTeamDiscussionCommentInOrgRequest.md)|  | |

### Return type

[**Reaction**](Reaction.md)

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

<a id="reactionsCreateForTeamDiscussionCommentLegacy"></a>
# **reactionsCreateForTeamDiscussionCommentLegacy**
> Reaction reactionsCreateForTeamDiscussionCommentLegacy(teamId, discussionNumber, commentNumber, reactionsCreateForTeamDiscussionCommentInOrgRequest)

Create reaction for a team discussion comment (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new \&quot;[Create reaction for a team discussion comment](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#create-reaction-for-a-team-discussion-comment)\&quot; endpoint.  Create a reaction to a [team discussion comment](https://docs.github.com/enterprise-server@2.22/rest/reference/teams#discussion-comments). OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this team discussion comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    Integer discussionNumber = 56; // Integer | 
    Integer commentNumber = 56; // Integer | 
    ReactionsCreateForTeamDiscussionCommentInOrgRequest reactionsCreateForTeamDiscussionCommentInOrgRequest = new ReactionsCreateForTeamDiscussionCommentInOrgRequest(); // ReactionsCreateForTeamDiscussionCommentInOrgRequest | 
    try {
      Reaction result = apiInstance.reactionsCreateForTeamDiscussionCommentLegacy(teamId, discussionNumber, commentNumber, reactionsCreateForTeamDiscussionCommentInOrgRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsCreateForTeamDiscussionCommentLegacy");
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
| **reactionsCreateForTeamDiscussionCommentInOrgRequest** | [**ReactionsCreateForTeamDiscussionCommentInOrgRequest**](ReactionsCreateForTeamDiscussionCommentInOrgRequest.md)|  | |

### Return type

[**Reaction**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="reactionsCreateForTeamDiscussionInOrg"></a>
# **reactionsCreateForTeamDiscussionInOrg**
> Reaction reactionsCreateForTeamDiscussionInOrg(org, teamSlug, discussionNumber, reactionsCreateForTeamDiscussionInOrgRequest)

Create reaction for a team discussion

Create a reaction to a [team discussion](https://docs.github.com/enterprise-server@2.22/rest/reference/teams#discussions). OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this team discussion.  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;POST /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String org = "org_example"; // String | 
    String teamSlug = "teamSlug_example"; // String | team_slug parameter
    Integer discussionNumber = 56; // Integer | 
    ReactionsCreateForTeamDiscussionInOrgRequest reactionsCreateForTeamDiscussionInOrgRequest = new ReactionsCreateForTeamDiscussionInOrgRequest(); // ReactionsCreateForTeamDiscussionInOrgRequest | 
    try {
      Reaction result = apiInstance.reactionsCreateForTeamDiscussionInOrg(org, teamSlug, discussionNumber, reactionsCreateForTeamDiscussionInOrgRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsCreateForTeamDiscussionInOrg");
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
| **discussionNumber** | **Integer**|  | |
| **reactionsCreateForTeamDiscussionInOrgRequest** | [**ReactionsCreateForTeamDiscussionInOrgRequest**](ReactionsCreateForTeamDiscussionInOrgRequest.md)|  | |

### Return type

[**Reaction**](Reaction.md)

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

<a id="reactionsCreateForTeamDiscussionLegacy"></a>
# **reactionsCreateForTeamDiscussionLegacy**
> Reaction reactionsCreateForTeamDiscussionLegacy(teamId, discussionNumber, reactionsCreateForTeamDiscussionInOrgRequest)

Create reaction for a team discussion (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [&#x60;Create reaction for a team discussion&#x60;](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#create-reaction-for-a-team-discussion) endpoint.  Create a reaction to a [team discussion](https://docs.github.com/enterprise-server@2.22/rest/reference/teams#discussions). OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this team discussion.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    Integer discussionNumber = 56; // Integer | 
    ReactionsCreateForTeamDiscussionInOrgRequest reactionsCreateForTeamDiscussionInOrgRequest = new ReactionsCreateForTeamDiscussionInOrgRequest(); // ReactionsCreateForTeamDiscussionInOrgRequest | 
    try {
      Reaction result = apiInstance.reactionsCreateForTeamDiscussionLegacy(teamId, discussionNumber, reactionsCreateForTeamDiscussionInOrgRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsCreateForTeamDiscussionLegacy");
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
| **reactionsCreateForTeamDiscussionInOrgRequest** | [**ReactionsCreateForTeamDiscussionInOrgRequest**](ReactionsCreateForTeamDiscussionInOrgRequest.md)|  | |

### Return type

[**Reaction**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="reactionsDeleteForCommitComment"></a>
# **reactionsDeleteForCommitComment**
> reactionsDeleteForCommitComment(owner, repo, commentId, reactionId)

Delete a commit comment reaction

**Note:** You can also specify a repository by &#x60;repository_id&#x60; using the route &#x60;DELETE /repositories/:repository_id/comments/:comment_id/reactions/:reaction_id&#x60;.  Delete a reaction to a [commit comment](https://docs.github.com/enterprise-server@2.22/rest/reference/repos#comments).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer commentId = 56; // Integer | comment_id parameter
    Integer reactionId = 56; // Integer | 
    try {
      apiInstance.reactionsDeleteForCommitComment(owner, repo, commentId, reactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsDeleteForCommitComment");
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
| **reactionId** | **Integer**|  | |

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

<a id="reactionsDeleteForIssue"></a>
# **reactionsDeleteForIssue**
> reactionsDeleteForIssue(owner, repo, issueNumber, reactionId)

Delete an issue reaction

**Note:** You can also specify a repository by &#x60;repository_id&#x60; using the route &#x60;DELETE /repositories/:repository_id/issues/:issue_number/reactions/:reaction_id&#x60;.  Delete a reaction to an [issue](https://docs.github.com/enterprise-server@2.22/rest/reference/issues/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer issueNumber = 56; // Integer | issue_number parameter
    Integer reactionId = 56; // Integer | 
    try {
      apiInstance.reactionsDeleteForIssue(owner, repo, issueNumber, reactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsDeleteForIssue");
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
| **issueNumber** | **Integer**| issue_number parameter | |
| **reactionId** | **Integer**|  | |

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

<a id="reactionsDeleteForIssueComment"></a>
# **reactionsDeleteForIssueComment**
> reactionsDeleteForIssueComment(owner, repo, commentId, reactionId)

Delete an issue comment reaction

**Note:** You can also specify a repository by &#x60;repository_id&#x60; using the route &#x60;DELETE delete /repositories/:repository_id/issues/comments/:comment_id/reactions/:reaction_id&#x60;.  Delete a reaction to an [issue comment](https://docs.github.com/enterprise-server@2.22/rest/reference/issues#comments).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer commentId = 56; // Integer | comment_id parameter
    Integer reactionId = 56; // Integer | 
    try {
      apiInstance.reactionsDeleteForIssueComment(owner, repo, commentId, reactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsDeleteForIssueComment");
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
| **reactionId** | **Integer**|  | |

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

<a id="reactionsDeleteForPullRequestComment"></a>
# **reactionsDeleteForPullRequestComment**
> reactionsDeleteForPullRequestComment(owner, repo, commentId, reactionId)

Delete a pull request comment reaction

**Note:** You can also specify a repository by &#x60;repository_id&#x60; using the route &#x60;DELETE /repositories/:repository_id/pulls/comments/:comment_id/reactions/:reaction_id.&#x60;  Delete a reaction to a [pull request review comment](https://docs.github.com/enterprise-server@2.22/rest/reference/pulls#review-comments).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer commentId = 56; // Integer | comment_id parameter
    Integer reactionId = 56; // Integer | 
    try {
      apiInstance.reactionsDeleteForPullRequestComment(owner, repo, commentId, reactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsDeleteForPullRequestComment");
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
| **reactionId** | **Integer**|  | |

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

<a id="reactionsDeleteForTeamDiscussion"></a>
# **reactionsDeleteForTeamDiscussion**
> reactionsDeleteForTeamDiscussion(org, teamSlug, discussionNumber, reactionId)

Delete team discussion reaction

**Note:** You can also specify a team or organization with &#x60;team_id&#x60; and &#x60;org_id&#x60; using the route &#x60;DELETE /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions/:reaction_id&#x60;.  Delete a reaction to a [team discussion](https://docs.github.com/enterprise-server@2.22/rest/reference/teams#discussions). OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String org = "org_example"; // String | 
    String teamSlug = "teamSlug_example"; // String | team_slug parameter
    Integer discussionNumber = 56; // Integer | 
    Integer reactionId = 56; // Integer | 
    try {
      apiInstance.reactionsDeleteForTeamDiscussion(org, teamSlug, discussionNumber, reactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsDeleteForTeamDiscussion");
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
| **discussionNumber** | **Integer**|  | |
| **reactionId** | **Integer**|  | |

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

<a id="reactionsDeleteForTeamDiscussionComment"></a>
# **reactionsDeleteForTeamDiscussionComment**
> reactionsDeleteForTeamDiscussionComment(org, teamSlug, discussionNumber, commentNumber, reactionId)

Delete team discussion comment reaction

**Note:** You can also specify a team or organization with &#x60;team_id&#x60; and &#x60;org_id&#x60; using the route &#x60;DELETE /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions/:reaction_id&#x60;.  Delete a reaction to a [team discussion comment](https://docs.github.com/enterprise-server@2.22/rest/reference/teams#discussion-comments). OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String org = "org_example"; // String | 
    String teamSlug = "teamSlug_example"; // String | team_slug parameter
    Integer discussionNumber = 56; // Integer | 
    Integer commentNumber = 56; // Integer | 
    Integer reactionId = 56; // Integer | 
    try {
      apiInstance.reactionsDeleteForTeamDiscussionComment(org, teamSlug, discussionNumber, commentNumber, reactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsDeleteForTeamDiscussionComment");
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
| **discussionNumber** | **Integer**|  | |
| **commentNumber** | **Integer**|  | |
| **reactionId** | **Integer**|  | |

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

<a id="reactionsDeleteLegacy"></a>
# **reactionsDeleteLegacy**
> reactionsDeleteLegacy(reactionId)

Delete a reaction (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Reactions API. We recommend migrating your existing code to use the new delete reactions endpoints. For more information, see this [blog post](https://developer.github.com/changes/2020-02-26-new-delete-reactions-endpoints/).  OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), when deleting a [team discussion](https://docs.github.com/enterprise-server@2.22/rest/reference/teams#discussions) or [team discussion comment](https://docs.github.com/enterprise-server@2.22/rest/reference/teams#discussion-comments).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    Integer reactionId = 56; // Integer | 
    try {
      apiInstance.reactionsDeleteLegacy(reactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsDeleteLegacy");
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
| **reactionId** | **Integer**|  | |

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
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |
| **410** | Gone |  -  |

<a id="reactionsListForCommitComment"></a>
# **reactionsListForCommitComment**
> List&lt;Reaction&gt; reactionsListForCommitComment(owner, repo, commentId, content, perPage, page)

List reactions for a commit comment

List the reactions to a [commit comment](https://docs.github.com/enterprise-server@2.22/rest/reference/repos#comments).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer commentId = 56; // Integer | comment_id parameter
    String content = "+1"; // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a commit comment.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Reaction> result = apiInstance.reactionsListForCommitComment(owner, repo, commentId, content, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsListForCommitComment");
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
| **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a commit comment. | [optional] [enum: +1, -1, laugh, confused, heart, hooray, rocket, eyes] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Reaction&gt;**](Reaction.md)

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

<a id="reactionsListForIssue"></a>
# **reactionsListForIssue**
> List&lt;Reaction&gt; reactionsListForIssue(owner, repo, issueNumber, content, perPage, page)

List reactions for an issue

List the reactions to an [issue](https://docs.github.com/enterprise-server@2.22/rest/reference/issues).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer issueNumber = 56; // Integer | issue_number parameter
    String content = "+1"; // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to an issue.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Reaction> result = apiInstance.reactionsListForIssue(owner, repo, issueNumber, content, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsListForIssue");
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
| **issueNumber** | **Integer**| issue_number parameter | |
| **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to an issue. | [optional] [enum: +1, -1, laugh, confused, heart, hooray, rocket, eyes] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Reaction&gt;**](Reaction.md)

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
| **410** | Gone |  -  |

<a id="reactionsListForIssueComment"></a>
# **reactionsListForIssueComment**
> List&lt;Reaction&gt; reactionsListForIssueComment(owner, repo, commentId, content, perPage, page)

List reactions for an issue comment

List the reactions to an [issue comment](https://docs.github.com/enterprise-server@2.22/rest/reference/issues#comments).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer commentId = 56; // Integer | comment_id parameter
    String content = "+1"; // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to an issue comment.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Reaction> result = apiInstance.reactionsListForIssueComment(owner, repo, commentId, content, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsListForIssueComment");
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
| **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to an issue comment. | [optional] [enum: +1, -1, laugh, confused, heart, hooray, rocket, eyes] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Reaction&gt;**](Reaction.md)

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

<a id="reactionsListForPullRequestReviewComment"></a>
# **reactionsListForPullRequestReviewComment**
> List&lt;Reaction&gt; reactionsListForPullRequestReviewComment(owner, repo, commentId, content, perPage, page)

List reactions for a pull request review comment

List the reactions to a [pull request review comment](https://docs.github.com/enterprise-server@2.22/rest/reference/pulls#review-comments).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer commentId = 56; // Integer | comment_id parameter
    String content = "+1"; // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a pull request review comment.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Reaction> result = apiInstance.reactionsListForPullRequestReviewComment(owner, repo, commentId, content, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsListForPullRequestReviewComment");
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
| **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a pull request review comment. | [optional] [enum: +1, -1, laugh, confused, heart, hooray, rocket, eyes] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Reaction&gt;**](Reaction.md)

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

<a id="reactionsListForTeamDiscussionCommentInOrg"></a>
# **reactionsListForTeamDiscussionCommentInOrg**
> List&lt;Reaction&gt; reactionsListForTeamDiscussionCommentInOrg(org, teamSlug, discussionNumber, commentNumber, content, perPage, page)

List reactions for a team discussion comment

List the reactions to a [team discussion comment](https://docs.github.com/enterprise-server@2.22/rest/reference/teams#discussion-comments/). OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String org = "org_example"; // String | 
    String teamSlug = "teamSlug_example"; // String | team_slug parameter
    Integer discussionNumber = 56; // Integer | 
    Integer commentNumber = 56; // Integer | 
    String content = "+1"; // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion comment.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Reaction> result = apiInstance.reactionsListForTeamDiscussionCommentInOrg(org, teamSlug, discussionNumber, commentNumber, content, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsListForTeamDiscussionCommentInOrg");
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
| **discussionNumber** | **Integer**|  | |
| **commentNumber** | **Integer**|  | |
| **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion comment. | [optional] [enum: +1, -1, laugh, confused, heart, hooray, rocket, eyes] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Reaction&gt;**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="reactionsListForTeamDiscussionCommentLegacy"></a>
# **reactionsListForTeamDiscussionCommentLegacy**
> List&lt;Reaction&gt; reactionsListForTeamDiscussionCommentLegacy(teamId, discussionNumber, commentNumber, content, perPage, page)

List reactions for a team discussion comment (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [&#x60;List reactions for a team discussion comment&#x60;](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#list-reactions-for-a-team-discussion-comment) endpoint.  List the reactions to a [team discussion comment](https://docs.github.com/enterprise-server@2.22/rest/reference/teams#discussion-comments). OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    Integer discussionNumber = 56; // Integer | 
    Integer commentNumber = 56; // Integer | 
    String content = "+1"; // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion comment.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Reaction> result = apiInstance.reactionsListForTeamDiscussionCommentLegacy(teamId, discussionNumber, commentNumber, content, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsListForTeamDiscussionCommentLegacy");
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
| **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion comment. | [optional] [enum: +1, -1, laugh, confused, heart, hooray, rocket, eyes] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Reaction&gt;**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="reactionsListForTeamDiscussionInOrg"></a>
# **reactionsListForTeamDiscussionInOrg**
> List&lt;Reaction&gt; reactionsListForTeamDiscussionInOrg(org, teamSlug, discussionNumber, content, perPage, page)

List reactions for a team discussion

List the reactions to a [team discussion](https://docs.github.com/enterprise-server@2.22/rest/reference/teams#discussions). OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).  **Note:** You can also specify a team by &#x60;org_id&#x60; and &#x60;team_id&#x60; using the route &#x60;GET /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    String org = "org_example"; // String | 
    String teamSlug = "teamSlug_example"; // String | team_slug parameter
    Integer discussionNumber = 56; // Integer | 
    String content = "+1"; // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Reaction> result = apiInstance.reactionsListForTeamDiscussionInOrg(org, teamSlug, discussionNumber, content, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsListForTeamDiscussionInOrg");
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
| **discussionNumber** | **Integer**|  | |
| **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion. | [optional] [enum: +1, -1, laugh, confused, heart, hooray, rocket, eyes] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Reaction&gt;**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="reactionsListForTeamDiscussionLegacy"></a>
# **reactionsListForTeamDiscussionLegacy**
> List&lt;Reaction&gt; reactionsListForTeamDiscussionLegacy(teamId, discussionNumber, content, perPage, page)

List reactions for a team discussion (Legacy)

**Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [&#x60;List reactions for a team discussion&#x60;](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#list-reactions-for-a-team-discussion) endpoint.  List the reactions to a [team discussion](https://docs.github.com/enterprise-server@2.22/rest/reference/teams#discussions). OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.22/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    ReactionsApi apiInstance = new ReactionsApi(defaultClient);
    Integer teamId = 56; // Integer | 
    Integer discussionNumber = 56; // Integer | 
    String content = "+1"; // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Reaction> result = apiInstance.reactionsListForTeamDiscussionLegacy(teamId, discussionNumber, content, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsListForTeamDiscussionLegacy");
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
| **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.22/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion. | [optional] [enum: +1, -1, laugh, confused, heart, hooray, rocket, eyes] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Reaction&gt;**](Reaction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

