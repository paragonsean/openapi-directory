# ReactionsApi

All URIs are relative to *http://HOSTNAME/api/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reactionsCreateForCommitComment**](ReactionsApi.md#reactionsCreateForCommitComment) | **POST** /repos/{owner}/{repo}/comments/{comment_id}/reactions | Create reaction for a commit comment |
| [**reactionsCreateForIssue**](ReactionsApi.md#reactionsCreateForIssue) | **POST** /repos/{owner}/{repo}/issues/{issue_number}/reactions | Create reaction for an issue |
| [**reactionsCreateForIssueComment**](ReactionsApi.md#reactionsCreateForIssueComment) | **POST** /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions | Create reaction for an issue comment |
| [**reactionsCreateForPullRequestReviewComment**](ReactionsApi.md#reactionsCreateForPullRequestReviewComment) | **POST** /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions | Create reaction for a pull request review comment |
| [**reactionsCreateForTeamDiscussion**](ReactionsApi.md#reactionsCreateForTeamDiscussion) | **POST** /teams/{team_id}/discussions/{discussion_number}/reactions | Create reaction for a team discussion |
| [**reactionsCreateForTeamDiscussionComment**](ReactionsApi.md#reactionsCreateForTeamDiscussionComment) | **POST** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions | Create reaction for a team discussion comment |
| [**reactionsDelete**](ReactionsApi.md#reactionsDelete) | **DELETE** /reactions/{reaction_id} | Delete a reaction |
| [**reactionsListForCommitComment**](ReactionsApi.md#reactionsListForCommitComment) | **GET** /repos/{owner}/{repo}/comments/{comment_id}/reactions | List reactions for a commit comment |
| [**reactionsListForIssue**](ReactionsApi.md#reactionsListForIssue) | **GET** /repos/{owner}/{repo}/issues/{issue_number}/reactions | List reactions for an issue |
| [**reactionsListForIssueComment**](ReactionsApi.md#reactionsListForIssueComment) | **GET** /repos/{owner}/{repo}/issues/comments/{comment_id}/reactions | List reactions for an issue comment |
| [**reactionsListForPullRequestReviewComment**](ReactionsApi.md#reactionsListForPullRequestReviewComment) | **GET** /repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions | List reactions for a pull request review comment |
| [**reactionsListForTeamDiscussion**](ReactionsApi.md#reactionsListForTeamDiscussion) | **GET** /teams/{team_id}/discussions/{discussion_number}/reactions | List reactions for a team discussion |
| [**reactionsListForTeamDiscussionComment**](ReactionsApi.md#reactionsListForTeamDiscussionComment) | **GET** /teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions | List reactions for a team discussion comment |


<a id="reactionsCreateForCommitComment"></a>
# **reactionsCreateForCommitComment**
> Reaction reactionsCreateForCommitComment(owner, repo, commentId, reactionsCreateForCommitCommentRequest)

Create reaction for a commit comment

Create a reaction to a [commit comment](https://docs.github.com/enterprise-server@2.19/rest/reference/repos#comments). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this commit comment.

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

Create a reaction to an [issue](https://docs.github.com/enterprise-server@2.19/rest/reference/issues/). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this issue.

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
| **415** | Preview header missing |  -  |
| **422** | Validation failed |  -  |

<a id="reactionsCreateForIssueComment"></a>
# **reactionsCreateForIssueComment**
> Reaction reactionsCreateForIssueComment(owner, repo, commentId, reactionsCreateForIssueCommentRequest)

Create reaction for an issue comment

Create a reaction to an [issue comment](https://docs.github.com/enterprise-server@2.19/rest/reference/issues#comments). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this issue comment.

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
| **415** | Preview header missing |  -  |
| **422** | Validation failed |  -  |

<a id="reactionsCreateForPullRequestReviewComment"></a>
# **reactionsCreateForPullRequestReviewComment**
> Reaction reactionsCreateForPullRequestReviewComment(owner, repo, commentId, reactionsCreateForPullRequestReviewCommentRequest)

Create reaction for a pull request review comment

Create a reaction to a [pull request review comment](https://docs.github.com/enterprise-server@2.19/rest/reference/pulls#comments). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this pull request review comment.

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
| **415** | Preview header missing |  -  |
| **422** | Validation failed |  -  |

<a id="reactionsCreateForTeamDiscussion"></a>
# **reactionsCreateForTeamDiscussion**
> Reaction reactionsCreateForTeamDiscussion(accept, teamId, discussionNumber, reactionsCreateForTeamDiscussionRequest)

Create reaction for a team discussion

Create a reaction to a [team discussion](https://docs.github.com/enterprise-server@2.19/rest/reference/teams#discussions). OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.19/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this team discussion.

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
    String accept = "application/vnd.github.squirrel-girl-preview+json"; // String | This API is under preview and subject to change.
    Integer teamId = 56; // Integer | 
    Integer discussionNumber = 56; // Integer | 
    ReactionsCreateForTeamDiscussionRequest reactionsCreateForTeamDiscussionRequest = new ReactionsCreateForTeamDiscussionRequest(); // ReactionsCreateForTeamDiscussionRequest | 
    try {
      Reaction result = apiInstance.reactionsCreateForTeamDiscussion(accept, teamId, discussionNumber, reactionsCreateForTeamDiscussionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsCreateForTeamDiscussion");
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
| **accept** | **String**| This API is under preview and subject to change. | [default to application/vnd.github.squirrel-girl-preview+json] |
| **teamId** | **Integer**|  | |
| **discussionNumber** | **Integer**|  | |
| **reactionsCreateForTeamDiscussionRequest** | [**ReactionsCreateForTeamDiscussionRequest**](ReactionsCreateForTeamDiscussionRequest.md)|  | |

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

<a id="reactionsCreateForTeamDiscussionComment"></a>
# **reactionsCreateForTeamDiscussionComment**
> Reaction reactionsCreateForTeamDiscussionComment(accept, teamId, discussionNumber, commentNumber, reactionsCreateForTeamDiscussionCommentRequest)

Create reaction for a team discussion comment

Create a reaction to a [team discussion comment](https://docs.github.com/enterprise-server@2.19/rest/reference/teams#discussion-comments). OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.19/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). A response with an HTTP &#x60;200&#x60; status means that you already added the reaction type to this team discussion comment.

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
    String accept = "application/vnd.github.squirrel-girl-preview+json"; // String | This API is under preview and subject to change.
    Integer teamId = 56; // Integer | 
    Integer discussionNumber = 56; // Integer | 
    Integer commentNumber = 56; // Integer | 
    ReactionsCreateForTeamDiscussionCommentRequest reactionsCreateForTeamDiscussionCommentRequest = new ReactionsCreateForTeamDiscussionCommentRequest(); // ReactionsCreateForTeamDiscussionCommentRequest | 
    try {
      Reaction result = apiInstance.reactionsCreateForTeamDiscussionComment(accept, teamId, discussionNumber, commentNumber, reactionsCreateForTeamDiscussionCommentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsCreateForTeamDiscussionComment");
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
| **accept** | **String**| This API is under preview and subject to change. | [default to application/vnd.github.squirrel-girl-preview+json] |
| **teamId** | **Integer**|  | |
| **discussionNumber** | **Integer**|  | |
| **commentNumber** | **Integer**|  | |
| **reactionsCreateForTeamDiscussionCommentRequest** | [**ReactionsCreateForTeamDiscussionCommentRequest**](ReactionsCreateForTeamDiscussionCommentRequest.md)|  | |

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

<a id="reactionsDelete"></a>
# **reactionsDelete**
> reactionsDelete(accept, reactionId)

Delete a reaction

OAuth access tokens require the &#x60;write:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.19/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/), when deleting a [team discussion](https://docs.github.com/enterprise-server@2.19/rest/reference/teams#discussions) or [team discussion comment](https://docs.github.com/enterprise-server@2.19/rest/reference/teams#discussion-comments).

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
    String accept = "application/vnd.github.squirrel-girl-preview+json"; // String | This API is under preview and subject to change.
    Integer reactionId = 56; // Integer | 
    try {
      apiInstance.reactionsDelete(accept, reactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsDelete");
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
| **accept** | **String**| This API is under preview and subject to change. | [default to application/vnd.github.squirrel-girl-preview+json] |
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

<a id="reactionsListForCommitComment"></a>
# **reactionsListForCommitComment**
> List&lt;Reaction&gt; reactionsListForCommitComment(owner, repo, commentId, content, perPage, page)

List reactions for a commit comment

List the reactions to a [commit comment](https://docs.github.com/enterprise-server@2.19/rest/reference/repos#comments).

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
    String content = "+1"; // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.19/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a commit comment.
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
| **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.19/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a commit comment. | [optional] [enum: +1, -1, laugh, confused, heart, hooray, rocket, eyes] |
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
| **415** | Preview header missing |  -  |

<a id="reactionsListForIssue"></a>
# **reactionsListForIssue**
> List&lt;Reaction&gt; reactionsListForIssue(owner, repo, issueNumber, content, perPage, page)

List reactions for an issue

List the reactions to an [issue](https://docs.github.com/enterprise-server@2.19/rest/reference/issues).

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
    String content = "+1"; // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.19/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to an issue.
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
| **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.19/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to an issue. | [optional] [enum: +1, -1, laugh, confused, heart, hooray, rocket, eyes] |
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
| **415** | Preview header missing |  -  |

<a id="reactionsListForIssueComment"></a>
# **reactionsListForIssueComment**
> List&lt;Reaction&gt; reactionsListForIssueComment(owner, repo, commentId, content, perPage, page)

List reactions for an issue comment

List the reactions to an [issue comment](https://docs.github.com/enterprise-server@2.19/rest/reference/issues#comments).

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
    String content = "+1"; // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.19/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to an issue comment.
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
| **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.19/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to an issue comment. | [optional] [enum: +1, -1, laugh, confused, heart, hooray, rocket, eyes] |
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
| **415** | Preview header missing |  -  |

<a id="reactionsListForPullRequestReviewComment"></a>
# **reactionsListForPullRequestReviewComment**
> List&lt;Reaction&gt; reactionsListForPullRequestReviewComment(owner, repo, commentId, content, perPage, page)

List reactions for a pull request review comment

List the reactions to a [pull request review comment](https://docs.github.com/enterprise-server@2.19/rest/reference/pulls#review-comments).

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
    String content = "+1"; // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.19/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a pull request review comment.
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
| **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.19/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a pull request review comment. | [optional] [enum: +1, -1, laugh, confused, heart, hooray, rocket, eyes] |
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
| **415** | Preview header missing |  -  |

<a id="reactionsListForTeamDiscussion"></a>
# **reactionsListForTeamDiscussion**
> List&lt;Reaction&gt; reactionsListForTeamDiscussion(accept, teamId, discussionNumber, content, perPage, page)

List reactions for a team discussion

List the reactions to a [team discussion](https://docs.github.com/enterprise-server@2.19/rest/reference/teams#discussions). OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.19/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

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
    String accept = "application/vnd.github.squirrel-girl-preview+json"; // String | This API is under preview and subject to change.
    Integer teamId = 56; // Integer | 
    Integer discussionNumber = 56; // Integer | 
    String content = "+1"; // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.19/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Reaction> result = apiInstance.reactionsListForTeamDiscussion(accept, teamId, discussionNumber, content, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsListForTeamDiscussion");
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
| **accept** | **String**| This API is under preview and subject to change. | [default to application/vnd.github.squirrel-girl-preview+json] |
| **teamId** | **Integer**|  | |
| **discussionNumber** | **Integer**|  | |
| **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.19/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion. | [optional] [enum: +1, -1, laugh, confused, heart, hooray, rocket, eyes] |
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

<a id="reactionsListForTeamDiscussionComment"></a>
# **reactionsListForTeamDiscussionComment**
> List&lt;Reaction&gt; reactionsListForTeamDiscussionComment(accept, teamId, discussionNumber, commentNumber, content, perPage, page)

List reactions for a team discussion comment

List the reactions to a [team discussion comment](https://docs.github.com/enterprise-server@2.19/rest/reference/teams#discussion-comments). OAuth access tokens require the &#x60;read:discussion&#x60; [scope](https://docs.github.com/enterprise-server@2.19/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/).

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
    String accept = "application/vnd.github.squirrel-girl-preview+json"; // String | This API is under preview and subject to change.
    Integer teamId = 56; // Integer | 
    Integer discussionNumber = 56; // Integer | 
    Integer commentNumber = 56; // Integer | 
    String content = "+1"; // String | Returns a single [reaction type](https://docs.github.com/enterprise-server@2.19/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion comment.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Reaction> result = apiInstance.reactionsListForTeamDiscussionComment(accept, teamId, discussionNumber, commentNumber, content, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReactionsApi#reactionsListForTeamDiscussionComment");
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
| **accept** | **String**| This API is under preview and subject to change. | [default to application/vnd.github.squirrel-girl-preview+json] |
| **teamId** | **Integer**|  | |
| **discussionNumber** | **Integer**|  | |
| **commentNumber** | **Integer**|  | |
| **content** | **String**| Returns a single [reaction type](https://docs.github.com/enterprise-server@2.19/rest/reference/reactions#reaction-types). Omit this parameter to list all reactions to a team discussion comment. | [optional] [enum: +1, -1, laugh, confused, heart, hooray, rocket, eyes] |
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

