# PullsApi

All URIs are relative to *http://HOSTNAME/api/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pullsCheckIfMerged**](PullsApi.md#pullsCheckIfMerged) | **GET** /repos/{owner}/{repo}/pulls/{pull_number}/merge | Check if a pull request has been merged |
| [**pullsCreate**](PullsApi.md#pullsCreate) | **POST** /repos/{owner}/{repo}/pulls | Create a pull request |
| [**pullsCreateReplyForReviewComment**](PullsApi.md#pullsCreateReplyForReviewComment) | **POST** /repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies | Create a reply for a review comment |
| [**pullsCreateReview**](PullsApi.md#pullsCreateReview) | **POST** /repos/{owner}/{repo}/pulls/{pull_number}/reviews | Create a review for a pull request |
| [**pullsCreateReviewCommentAlternative**](PullsApi.md#pullsCreateReviewCommentAlternative) | **POST** /repos/{owner}/{repo}/pulls/{pull_number}/comments | Create a review comment for a pull request (alternative) |
| [**pullsDeletePendingReview**](PullsApi.md#pullsDeletePendingReview) | **DELETE** /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id} | Delete a pending review for a pull request |
| [**pullsDeleteReviewComment**](PullsApi.md#pullsDeleteReviewComment) | **DELETE** /repos/{owner}/{repo}/pulls/comments/{comment_id} | Delete a review comment for a pull request |
| [**pullsDismissReview**](PullsApi.md#pullsDismissReview) | **PUT** /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/dismissals | Dismiss a review for a pull request |
| [**pullsGet**](PullsApi.md#pullsGet) | **GET** /repos/{owner}/{repo}/pulls/{pull_number} | Get a pull request |
| [**pullsGetReview**](PullsApi.md#pullsGetReview) | **GET** /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id} | Get a review for a pull request |
| [**pullsGetReviewComment**](PullsApi.md#pullsGetReviewComment) | **GET** /repos/{owner}/{repo}/pulls/comments/{comment_id} | Get a review comment for a pull request |
| [**pullsList**](PullsApi.md#pullsList) | **GET** /repos/{owner}/{repo}/pulls | List pull requests |
| [**pullsListCommentsForReview**](PullsApi.md#pullsListCommentsForReview) | **GET** /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/comments | List comments for a pull request review |
| [**pullsListCommits**](PullsApi.md#pullsListCommits) | **GET** /repos/{owner}/{repo}/pulls/{pull_number}/commits | List commits on a pull request |
| [**pullsListFiles**](PullsApi.md#pullsListFiles) | **GET** /repos/{owner}/{repo}/pulls/{pull_number}/files | List pull requests files |
| [**pullsListRequestedReviewers**](PullsApi.md#pullsListRequestedReviewers) | **GET** /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers | List requested reviewers for a pull request |
| [**pullsListReviewComments**](PullsApi.md#pullsListReviewComments) | **GET** /repos/{owner}/{repo}/pulls/{pull_number}/comments | List review comments on a pull request |
| [**pullsListReviewCommentsForRepo**](PullsApi.md#pullsListReviewCommentsForRepo) | **GET** /repos/{owner}/{repo}/pulls/comments | List review comments in a repository |
| [**pullsListReviews**](PullsApi.md#pullsListReviews) | **GET** /repos/{owner}/{repo}/pulls/{pull_number}/reviews | List reviews for a pull request |
| [**pullsMerge**](PullsApi.md#pullsMerge) | **PUT** /repos/{owner}/{repo}/pulls/{pull_number}/merge | Merge a pull request |
| [**pullsRemoveRequestedReviewers**](PullsApi.md#pullsRemoveRequestedReviewers) | **DELETE** /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers | Remove requested reviewers from a pull request |
| [**pullsRequestReviewers**](PullsApi.md#pullsRequestReviewers) | **POST** /repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers | Request reviewers for a pull request |
| [**pullsSubmitReview**](PullsApi.md#pullsSubmitReview) | **POST** /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/events | Submit a review for a pull request |
| [**pullsUpdate**](PullsApi.md#pullsUpdate) | **PATCH** /repos/{owner}/{repo}/pulls/{pull_number} | Update a pull request |
| [**pullsUpdateBranch**](PullsApi.md#pullsUpdateBranch) | **PUT** /repos/{owner}/{repo}/pulls/{pull_number}/update-branch | Update a pull request branch |
| [**pullsUpdateReview**](PullsApi.md#pullsUpdateReview) | **PUT** /repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id} | Update a review for a pull request |
| [**pullsUpdateReviewComment**](PullsApi.md#pullsUpdateReviewComment) | **PATCH** /repos/{owner}/{repo}/pulls/comments/{comment_id} | Update a review comment for a pull request |


<a id="pullsCheckIfMerged"></a>
# **pullsCheckIfMerged**
> pullsCheckIfMerged(owner, repo, pullNumber)

Check if a pull request has been merged



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    try {
      apiInstance.pullsCheckIfMerged(owner, repo, pullNumber);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsCheckIfMerged");
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
| **pullNumber** | **Integer**|  | |

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
| **204** | Response if pull request has been merged |  -  |
| **404** | Not Found if pull request has not been merged |  -  |

<a id="pullsCreate"></a>
# **pullsCreate**
> PullRequest pullsCreate(owner, repo, pullsCreateRequest)

Create a pull request

Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team, GitHub Enterprise Server 2.17+, and GitHub Enterprise Cloud. You can create a new pull request. This endpoint triggers [notifications](https://docs.github.com/articles/about-notifications/). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.19/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; for details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    PullsCreateRequest pullsCreateRequest = new PullsCreateRequest(); // PullsCreateRequest | 
    try {
      PullRequest result = apiInstance.pullsCreate(owner, repo, pullsCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsCreate");
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
| **pullsCreateRequest** | [**PullsCreateRequest**](PullsCreateRequest.md)|  | |

### Return type

[**PullRequest**](PullRequest.md)

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

<a id="pullsCreateReplyForReviewComment"></a>
# **pullsCreateReplyForReviewComment**
> PullRequestReviewComment pullsCreateReplyForReviewComment(owner, repo, pullNumber, commentId, pullsCreateReplyForReviewCommentRequest)

Create a reply for a review comment

Creates a reply to a review comment for a pull request. For the &#x60;comment_id&#x60;, provide the ID of the review comment you are replying to. This must be the ID of a _top-level review comment_, not a reply to that comment. Replies to replies are not supported.  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.19/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.19/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    Integer commentId = 56; // Integer | comment_id parameter
    PullsCreateReplyForReviewCommentRequest pullsCreateReplyForReviewCommentRequest = new PullsCreateReplyForReviewCommentRequest(); // PullsCreateReplyForReviewCommentRequest | 
    try {
      PullRequestReviewComment result = apiInstance.pullsCreateReplyForReviewComment(owner, repo, pullNumber, commentId, pullsCreateReplyForReviewCommentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsCreateReplyForReviewComment");
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
| **pullNumber** | **Integer**|  | |
| **commentId** | **Integer**| comment_id parameter | |
| **pullsCreateReplyForReviewCommentRequest** | [**PullsCreateReplyForReviewCommentRequest**](PullsCreateReplyForReviewCommentRequest.md)|  | |

### Return type

[**PullRequestReviewComment**](PullRequestReviewComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  * Location -  <br>  |
| **404** | Resource not found |  -  |

<a id="pullsCreateReview"></a>
# **pullsCreateReview**
> PullRequestReview pullsCreateReview(owner, repo, pullNumber, pullsCreateReviewRequest)

Create a review for a pull request

This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.19/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@2.19/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.  Pull request reviews created in the &#x60;PENDING&#x60; state do not include the &#x60;submitted_at&#x60; property in the response.  **Note:** To comment on a specific line in a file, you need to first determine the _position_ of that line in the diff. The GitHub REST API v3 offers the &#x60;application/vnd.github.v3.diff&#x60; [media type](https://docs.github.com/enterprise-server@2.19/rest/overview/media-types#commits-commit-comparison-and-pull-requests). To see a pull request diff, add this media type to the &#x60;Accept&#x60; header of a call to the [single pull request](https://docs.github.com/enterprise-server@2.19/rest/reference/pulls#get-a-pull-request) endpoint.  The &#x60;position&#x60; value equals the number of lines down from the first \&quot;@@\&quot; hunk header in the file you want to add a comment. The line just below the \&quot;@@\&quot; line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    PullsCreateReviewRequest pullsCreateReviewRequest = new PullsCreateReviewRequest(); // PullsCreateReviewRequest | 
    try {
      PullRequestReview result = apiInstance.pullsCreateReview(owner, repo, pullNumber, pullsCreateReviewRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsCreateReview");
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
| **pullNumber** | **Integer**|  | |
| **pullsCreateReviewRequest** | [**PullsCreateReviewRequest**](PullsCreateReviewRequest.md)|  | [optional] |

### Return type

[**PullRequestReview**](PullRequestReview.md)

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
| **422** | Validation failed |  -  |

<a id="pullsCreateReviewCommentAlternative"></a>
# **pullsCreateReviewCommentAlternative**
> LegacyReviewComment pullsCreateReviewCommentAlternative(owner, repo, pullNumber, pullsCreateReviewCommentAlternativeRequest)

Create a review comment for a pull request (alternative)

Creates a review comment in the pull request diff. To add a regular comment to a pull request timeline, see \&quot;[Create an issue comment](https://docs.github.com/enterprise-server@2.19/rest/reference/issues#create-an-issue-comment).\&quot;  **Note:** The position value equals the number of lines down from the first \&quot;@@\&quot; hunk header in the file you want to add a comment. The line just below the \&quot;@@\&quot; line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.  This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@2.19/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; for details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    PullsCreateReviewCommentAlternativeRequest pullsCreateReviewCommentAlternativeRequest = new PullsCreateReviewCommentAlternativeRequest(); // PullsCreateReviewCommentAlternativeRequest | 
    try {
      LegacyReviewComment result = apiInstance.pullsCreateReviewCommentAlternative(owner, repo, pullNumber, pullsCreateReviewCommentAlternativeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsCreateReviewCommentAlternative");
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
| **pullNumber** | **Integer**|  | |
| **pullsCreateReviewCommentAlternativeRequest** | [**PullsCreateReviewCommentAlternativeRequest**](PullsCreateReviewCommentAlternativeRequest.md)|  | |

### Return type

[**LegacyReviewComment**](LegacyReviewComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  * Location -  <br>  |

<a id="pullsDeletePendingReview"></a>
# **pullsDeletePendingReview**
> PullRequestReview pullsDeletePendingReview(owner, repo, pullNumber, reviewId)

Delete a pending review for a pull request



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    Integer reviewId = 56; // Integer | review_id parameter
    try {
      PullRequestReview result = apiInstance.pullsDeletePendingReview(owner, repo, pullNumber, reviewId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsDeletePendingReview");
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
| **pullNumber** | **Integer**|  | |
| **reviewId** | **Integer**| review_id parameter | |

### Return type

[**PullRequestReview**](PullRequestReview.md)

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

<a id="pullsDeleteReviewComment"></a>
# **pullsDeleteReviewComment**
> pullsDeleteReviewComment(owner, repo, commentId)

Delete a review comment for a pull request

Deletes a review comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer commentId = 56; // Integer | comment_id parameter
    try {
      apiInstance.pullsDeleteReviewComment(owner, repo, commentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsDeleteReviewComment");
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

<a id="pullsDismissReview"></a>
# **pullsDismissReview**
> PullRequestReview pullsDismissReview(owner, repo, pullNumber, reviewId, pullsDismissReviewRequest)

Dismiss a review for a pull request

**Note:** To dismiss a pull request review on a [protected branch](https://docs.github.com/enterprise-server@2.19/rest/reference/repos#branches), you must be a repository administrator or be included in the list of people or teams who can dismiss pull request reviews.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    Integer reviewId = 56; // Integer | review_id parameter
    PullsDismissReviewRequest pullsDismissReviewRequest = new PullsDismissReviewRequest(); // PullsDismissReviewRequest | 
    try {
      PullRequestReview result = apiInstance.pullsDismissReview(owner, repo, pullNumber, reviewId, pullsDismissReviewRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsDismissReview");
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
| **pullNumber** | **Integer**|  | |
| **reviewId** | **Integer**| review_id parameter | |
| **pullsDismissReviewRequest** | [**PullsDismissReviewRequest**](PullsDismissReviewRequest.md)|  | |

### Return type

[**PullRequestReview**](PullRequestReview.md)

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

<a id="pullsGet"></a>
# **pullsGet**
> PullRequest pullsGet(owner, repo, pullNumber)

Get a pull request

Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud. For more information, see [GitHub&#39;s products](https://help.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists details of a pull request by providing its number.  When you get, [create](https://docs.github.com/enterprise-server@2.19/rest/reference/pulls/#create-a-pull-request), or [edit](https://docs.github.com/enterprise-server@2.19/rest/reference/pulls#update-a-pull-request) a pull request, GitHub Enterprise Server creates a merge commit to test whether the pull request can be automatically merged into the base branch. This test commit is not added to the base branch or the head branch. You can review the status of the test commit using the &#x60;mergeable&#x60; key. For more information, see \&quot;[Checking mergeability of pull requests](https://docs.github.com/enterprise-server@2.19/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)\&quot;.  The value of the &#x60;mergeable&#x60; attribute can be &#x60;true&#x60;, &#x60;false&#x60;, or &#x60;null&#x60;. If the value is &#x60;null&#x60;, then GitHub Enterprise Server has started a background job to compute the mergeability. After giving the job time to complete, resubmit the request. When the job finishes, you will see a non-&#x60;null&#x60; value for the &#x60;mergeable&#x60; attribute in the response. If &#x60;mergeable&#x60; is &#x60;true&#x60;, then &#x60;merge_commit_sha&#x60; will be the SHA of the _test_ merge commit.  The value of the &#x60;merge_commit_sha&#x60; attribute changes depending on the state of the pull request. Before merging a pull request, the &#x60;merge_commit_sha&#x60; attribute holds the SHA of the _test_ merge commit. After merging a pull request, the &#x60;merge_commit_sha&#x60; attribute changes depending on how you merged the pull request:  *   If merged as a [merge commit](https://help.github.com/articles/about-merge-methods-on-github/), &#x60;merge_commit_sha&#x60; represents the SHA of the merge commit. *   If merged via a [squash](https://help.github.com/articles/about-merge-methods-on-github/#squashing-your-merge-commits), &#x60;merge_commit_sha&#x60; represents the SHA of the squashed commit on the base branch. *   If [rebased](https://help.github.com/articles/about-merge-methods-on-github/#rebasing-and-merging-your-commits), &#x60;merge_commit_sha&#x60; represents the commit that the base branch was updated to.  Pass the appropriate [media type](https://docs.github.com/enterprise-server@2.19/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) to fetch diff and patch formats.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    try {
      PullRequest result = apiInstance.pullsGet(owner, repo, pullNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsGet");
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
| **pullNumber** | **Integer**|  | |

### Return type

[**PullRequest**](PullRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Pass the appropriate [media type](https://docs.github.com/enterprise-server@2.19/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) to fetch diff and patch formats. |  -  |
| **304** | Not modified |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal Error |  -  |

<a id="pullsGetReview"></a>
# **pullsGetReview**
> PullRequestReview pullsGetReview(owner, repo, pullNumber, reviewId)

Get a review for a pull request



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    Integer reviewId = 56; // Integer | review_id parameter
    try {
      PullRequestReview result = apiInstance.pullsGetReview(owner, repo, pullNumber, reviewId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsGetReview");
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
| **pullNumber** | **Integer**|  | |
| **reviewId** | **Integer**| review_id parameter | |

### Return type

[**PullRequestReview**](PullRequestReview.md)

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

<a id="pullsGetReviewComment"></a>
# **pullsGetReviewComment**
> PullRequestReviewComment pullsGetReviewComment(owner, repo, commentId)

Get a review comment for a pull request

Provides details for a review comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer commentId = 56; // Integer | comment_id parameter
    try {
      PullRequestReviewComment result = apiInstance.pullsGetReviewComment(owner, repo, commentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsGetReviewComment");
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

[**PullRequestReviewComment**](PullRequestReviewComment.md)

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

<a id="pullsList"></a>
# **pullsList**
> List&lt;PullRequestSimple&gt; pullsList(owner, repo, state, head, base, sort, direction, perPage, page)

List pull requests

Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team, GitHub Enterprise Server 2.17+, and GitHub Enterprise Cloud.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String state = "open"; // String | Either `open`, `closed`, or `all` to filter by state.
    String head = "head_example"; // String | Filter pulls by head user or head organization and branch name in the format of `user:ref-name` or `organization:ref-name`. For example: `github:new-script-format` or `octocat:test-branch`.
    String base = "base_example"; // String | Filter pulls by base branch name. Example: `gh-pages`.
    String sort = "created"; // String | What to sort results by. Can be either `created`, `updated`, `popularity` (comment count) or `long-running` (age, filtering by pulls updated in the last month).
    String direction = "asc"; // String | The direction of the sort. Can be either `asc` or `desc`. Default: `desc` when sort is `created` or sort is not specified, otherwise `asc`.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<PullRequestSimple> result = apiInstance.pullsList(owner, repo, state, head, base, sort, direction, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsList");
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
| **state** | **String**| Either &#x60;open&#x60;, &#x60;closed&#x60;, or &#x60;all&#x60; to filter by state. | [optional] [default to open] [enum: open, closed, all] |
| **head** | **String**| Filter pulls by head user or head organization and branch name in the format of &#x60;user:ref-name&#x60; or &#x60;organization:ref-name&#x60;. For example: &#x60;github:new-script-format&#x60; or &#x60;octocat:test-branch&#x60;. | [optional] |
| **base** | **String**| Filter pulls by base branch name. Example: &#x60;gh-pages&#x60;. | [optional] |
| **sort** | **String**| What to sort results by. Can be either &#x60;created&#x60;, &#x60;updated&#x60;, &#x60;popularity&#x60; (comment count) or &#x60;long-running&#x60; (age, filtering by pulls updated in the last month). | [optional] [default to created] [enum: created, updated, popularity, long-running] |
| **direction** | **String**| The direction of the sort. Can be either &#x60;asc&#x60; or &#x60;desc&#x60;. Default: &#x60;desc&#x60; when sort is &#x60;created&#x60; or sort is not specified, otherwise &#x60;asc&#x60;. | [optional] [enum: asc, desc] |
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
| **304** | Not modified |  -  |
| **422** | Validation failed |  -  |

<a id="pullsListCommentsForReview"></a>
# **pullsListCommentsForReview**
> List&lt;ReviewComment&gt; pullsListCommentsForReview(owner, repo, pullNumber, reviewId, perPage, page)

List comments for a pull request review

List comments for a specific pull request review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    Integer reviewId = 56; // Integer | review_id parameter
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<ReviewComment> result = apiInstance.pullsListCommentsForReview(owner, repo, pullNumber, reviewId, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsListCommentsForReview");
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
| **pullNumber** | **Integer**|  | |
| **reviewId** | **Integer**| review_id parameter | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;ReviewComment&gt;**](ReviewComment.md)

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

<a id="pullsListCommits"></a>
# **pullsListCommits**
> List&lt;Commit&gt; pullsListCommits(owner, repo, pullNumber, perPage, page)

List commits on a pull request

Lists a maximum of 250 commits for a pull request. To receive a complete commit list for pull requests with more than 250 commits, use the [List commits](https://docs.github.com/enterprise-server@2.19/rest/reference/repos#list-commits) endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Commit> result = apiInstance.pullsListCommits(owner, repo, pullNumber, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsListCommits");
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
| **pullNumber** | **Integer**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Commit&gt;**](Commit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="pullsListFiles"></a>
# **pullsListFiles**
> List&lt;DiffEntry&gt; pullsListFiles(owner, repo, pullNumber, perPage, page)

List pull requests files

**Note:** Responses include a maximum of 3000 files. The paginated response returns 30 files per page by default.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<DiffEntry> result = apiInstance.pullsListFiles(owner, repo, pullNumber, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsListFiles");
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
| **pullNumber** | **Integer**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;DiffEntry&gt;**](DiffEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **422** | Validation failed |  -  |
| **500** | Internal Error |  -  |

<a id="pullsListRequestedReviewers"></a>
# **pullsListRequestedReviewers**
> PullRequestReviewRequest pullsListRequestedReviewers(owner, repo, pullNumber, perPage, page)

List requested reviewers for a pull request



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      PullRequestReviewRequest result = apiInstance.pullsListRequestedReviewers(owner, repo, pullNumber, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsListRequestedReviewers");
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
| **pullNumber** | **Integer**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**PullRequestReviewRequest**](PullRequestReviewRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="pullsListReviewComments"></a>
# **pullsListReviewComments**
> List&lt;PullRequestReviewComment&gt; pullsListReviewComments(owner, repo, pullNumber, sort, direction, since, perPage, page)

List review comments on a pull request

Lists all review comments for a pull request. By default, review comments are in ascending order by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    String sort = "created"; // String | One of `created` (when the repository was starred) or `updated` (when it was last pushed to).
    String direction = "asc"; // String | Can be either `asc` or `desc`. Ignored without `sort` parameter.
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<PullRequestReviewComment> result = apiInstance.pullsListReviewComments(owner, repo, pullNumber, sort, direction, since, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsListReviewComments");
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
| **pullNumber** | **Integer**|  | |
| **sort** | **String**| One of &#x60;created&#x60; (when the repository was starred) or &#x60;updated&#x60; (when it was last pushed to). | [optional] [default to created] [enum: created, updated] |
| **direction** | **String**| Can be either &#x60;asc&#x60; or &#x60;desc&#x60;. Ignored without &#x60;sort&#x60; parameter. | [optional] [enum: asc, desc] |
| **since** | **OffsetDateTime**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;PullRequestReviewComment&gt;**](PullRequestReviewComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="pullsListReviewCommentsForRepo"></a>
# **pullsListReviewCommentsForRepo**
> List&lt;PullRequestReviewComment&gt; pullsListReviewCommentsForRepo(owner, repo, sort, direction, since, perPage, page)

List review comments in a repository

Lists review comments for all pull requests in a repository. By default, review comments are in ascending order by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    String sort = "created"; // String | 
    String direction = "asc"; // String | Can be either `asc` or `desc`. Ignored without `sort` parameter.
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<PullRequestReviewComment> result = apiInstance.pullsListReviewCommentsForRepo(owner, repo, sort, direction, since, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsListReviewCommentsForRepo");
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
| **sort** | **String**|  | [optional] [enum: created, updated, created_at] |
| **direction** | **String**| Can be either &#x60;asc&#x60; or &#x60;desc&#x60;. Ignored without &#x60;sort&#x60; parameter. | [optional] [enum: asc, desc] |
| **since** | **OffsetDateTime**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;PullRequestReviewComment&gt;**](PullRequestReviewComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="pullsListReviews"></a>
# **pullsListReviews**
> List&lt;PullRequestReview&gt; pullsListReviews(owner, repo, pullNumber, perPage, page)

List reviews for a pull request

The list of reviews returns in chronological order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    Integer perPage = 30; // Integer | Results per page (max 100)
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<PullRequestReview> result = apiInstance.pullsListReviews(owner, repo, pullNumber, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsListReviews");
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
| **pullNumber** | **Integer**|  | |
| **perPage** | **Integer**| Results per page (max 100) | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;PullRequestReview&gt;**](PullRequestReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of reviews returns in chronological order. |  * Link -  <br>  |

<a id="pullsMerge"></a>
# **pullsMerge**
> PullRequestMergeResult pullsMerge(owner, repo, pullNumber, pullsMergeRequest)

Merge a pull request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    PullsMergeRequest pullsMergeRequest = new PullsMergeRequest(); // PullsMergeRequest | 
    try {
      PullRequestMergeResult result = apiInstance.pullsMerge(owner, repo, pullNumber, pullsMergeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsMerge");
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
| **pullNumber** | **Integer**|  | |
| **pullsMergeRequest** | [**PullsMergeRequest**](PullsMergeRequest.md)|  | [optional] |

### Return type

[**PullRequestMergeResult**](PullRequestMergeResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | if merge was successful |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **405** | Method Not Allowed if merge cannot be performed |  -  |
| **409** | Conflict if sha was provided and pull request head did not match |  -  |
| **422** | Validation failed |  -  |

<a id="pullsRemoveRequestedReviewers"></a>
# **pullsRemoveRequestedReviewers**
> PullRequestSimple pullsRemoveRequestedReviewers(owner, repo, pullNumber, pullsRemoveRequestedReviewersRequest)

Remove requested reviewers from a pull request



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    PullsRemoveRequestedReviewersRequest pullsRemoveRequestedReviewersRequest = new PullsRemoveRequestedReviewersRequest(); // PullsRemoveRequestedReviewersRequest | 
    try {
      PullRequestSimple result = apiInstance.pullsRemoveRequestedReviewers(owner, repo, pullNumber, pullsRemoveRequestedReviewersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsRemoveRequestedReviewers");
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
| **pullNumber** | **Integer**|  | |
| **pullsRemoveRequestedReviewersRequest** | [**PullsRemoveRequestedReviewersRequest**](PullsRemoveRequestedReviewersRequest.md)|  | |

### Return type

[**PullRequestSimple**](PullRequestSimple.md)

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

<a id="pullsRequestReviewers"></a>
# **pullsRequestReviewers**
> PullRequestSimple pullsRequestReviewers(owner, repo, pullNumber, pullsRequestReviewersRequest)

Request reviewers for a pull request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    PullsRequestReviewersRequest pullsRequestReviewersRequest = new PullsRequestReviewersRequest(); // PullsRequestReviewersRequest | 
    try {
      PullRequestSimple result = apiInstance.pullsRequestReviewers(owner, repo, pullNumber, pullsRequestReviewersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsRequestReviewers");
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
| **pullNumber** | **Integer**|  | |
| **pullsRequestReviewersRequest** | [**PullsRequestReviewersRequest**](PullsRequestReviewersRequest.md)|  | [optional] |

### Return type

[**PullRequestSimple**](PullRequestSimple.md)

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
| **422** | Unprocessable Entity if user is not a collaborator |  -  |

<a id="pullsSubmitReview"></a>
# **pullsSubmitReview**
> PullRequestReview pullsSubmitReview(owner, repo, pullNumber, reviewId, pullsSubmitReviewRequest)

Submit a review for a pull request



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    Integer reviewId = 56; // Integer | review_id parameter
    PullsSubmitReviewRequest pullsSubmitReviewRequest = new PullsSubmitReviewRequest(); // PullsSubmitReviewRequest | 
    try {
      PullRequestReview result = apiInstance.pullsSubmitReview(owner, repo, pullNumber, reviewId, pullsSubmitReviewRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsSubmitReview");
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
| **pullNumber** | **Integer**|  | |
| **reviewId** | **Integer**| review_id parameter | |
| **pullsSubmitReviewRequest** | [**PullsSubmitReviewRequest**](PullsSubmitReviewRequest.md)|  | |

### Return type

[**PullRequestReview**](PullRequestReview.md)

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

<a id="pullsUpdate"></a>
# **pullsUpdate**
> PullRequest pullsUpdate(owner, repo, pullNumber, pullsUpdateRequest)

Update a pull request

Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team, GitHub Enterprise Server 2.17+, and GitHub Enterprise Cloud.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    PullsUpdateRequest pullsUpdateRequest = new PullsUpdateRequest(); // PullsUpdateRequest | 
    try {
      PullRequest result = apiInstance.pullsUpdate(owner, repo, pullNumber, pullsUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsUpdate");
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
| **pullNumber** | **Integer**|  | |
| **pullsUpdateRequest** | [**PullsUpdateRequest**](PullsUpdateRequest.md)|  | [optional] |

### Return type

[**PullRequest**](PullRequest.md)

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
| **422** | Validation failed |  -  |

<a id="pullsUpdateBranch"></a>
# **pullsUpdateBranch**
> EnterpriseAdminUpdateOrgName202Response pullsUpdateBranch(owner, repo, pullNumber, pullsUpdateBranchRequest)

Update a pull request branch

Updates the pull request branch with the latest upstream changes by merging HEAD from the base branch into the pull request branch.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    PullsUpdateBranchRequest pullsUpdateBranchRequest = new PullsUpdateBranchRequest(); // PullsUpdateBranchRequest | 
    try {
      EnterpriseAdminUpdateOrgName202Response result = apiInstance.pullsUpdateBranch(owner, repo, pullNumber, pullsUpdateBranchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsUpdateBranch");
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
| **pullNumber** | **Integer**|  | |
| **pullsUpdateBranchRequest** | [**PullsUpdateBranchRequest**](PullsUpdateBranchRequest.md)|  | [optional] |

### Return type

[**EnterpriseAdminUpdateOrgName202Response**](EnterpriseAdminUpdateOrgName202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Response |  -  |
| **403** | Forbidden |  -  |
| **415** | Preview header missing |  -  |
| **422** | Validation failed |  -  |

<a id="pullsUpdateReview"></a>
# **pullsUpdateReview**
> PullRequestReview pullsUpdateReview(owner, repo, pullNumber, reviewId, pullsUpdateReviewRequest)

Update a review for a pull request

Update the review summary comment with new text.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer pullNumber = 56; // Integer | 
    Integer reviewId = 56; // Integer | review_id parameter
    PullsUpdateReviewRequest pullsUpdateReviewRequest = new PullsUpdateReviewRequest(); // PullsUpdateReviewRequest | 
    try {
      PullRequestReview result = apiInstance.pullsUpdateReview(owner, repo, pullNumber, reviewId, pullsUpdateReviewRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsUpdateReview");
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
| **pullNumber** | **Integer**|  | |
| **reviewId** | **Integer**| review_id parameter | |
| **pullsUpdateReviewRequest** | [**PullsUpdateReviewRequest**](PullsUpdateReviewRequest.md)|  | |

### Return type

[**PullRequestReview**](PullRequestReview.md)

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

<a id="pullsUpdateReviewComment"></a>
# **pullsUpdateReviewComment**
> PullRequestReviewComment pullsUpdateReviewComment(owner, repo, commentId, pullsUpdateReviewCommentRequest)

Update a review comment for a pull request

Enables you to edit a review comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PullsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://HOSTNAME/api/v3");

    PullsApi apiInstance = new PullsApi(defaultClient);
    String owner = "owner_example"; // String | 
    String repo = "repo_example"; // String | 
    Integer commentId = 56; // Integer | comment_id parameter
    PullsUpdateReviewCommentRequest pullsUpdateReviewCommentRequest = new PullsUpdateReviewCommentRequest(); // PullsUpdateReviewCommentRequest | 
    try {
      PullRequestReviewComment result = apiInstance.pullsUpdateReviewComment(owner, repo, commentId, pullsUpdateReviewCommentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PullsApi#pullsUpdateReviewComment");
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
| **pullsUpdateReviewCommentRequest** | [**PullsUpdateReviewCommentRequest**](PullsUpdateReviewCommentRequest.md)|  | |

### Return type

[**PullRequestReviewComment**](PullRequestReviewComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

