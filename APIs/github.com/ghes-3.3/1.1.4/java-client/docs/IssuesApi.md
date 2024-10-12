# IssuesApi

All URIs are relative to *https://github.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**issuesAddAssignees**](IssuesApi.md#issuesAddAssignees) | **POST** /repos/{owner}/{repo}/issues/{issue_number}/assignees | Add assignees to an issue |
| [**issuesAddLabels**](IssuesApi.md#issuesAddLabels) | **POST** /repos/{owner}/{repo}/issues/{issue_number}/labels | Add labels to an issue |
| [**issuesCheckUserCanBeAssigned**](IssuesApi.md#issuesCheckUserCanBeAssigned) | **GET** /repos/{owner}/{repo}/assignees/{assignee} | Check if a user can be assigned |
| [**issuesCheckUserCanBeAssignedToIssue**](IssuesApi.md#issuesCheckUserCanBeAssignedToIssue) | **GET** /repos/{owner}/{repo}/issues/{issue_number}/assignees/{assignee} | Check if a user can be assigned to a issue |
| [**issuesCreate**](IssuesApi.md#issuesCreate) | **POST** /repos/{owner}/{repo}/issues | Create an issue |
| [**issuesCreateComment**](IssuesApi.md#issuesCreateComment) | **POST** /repos/{owner}/{repo}/issues/{issue_number}/comments | Create an issue comment |
| [**issuesCreateLabel**](IssuesApi.md#issuesCreateLabel) | **POST** /repos/{owner}/{repo}/labels | Create a label |
| [**issuesCreateMilestone**](IssuesApi.md#issuesCreateMilestone) | **POST** /repos/{owner}/{repo}/milestones | Create a milestone |
| [**issuesDeleteComment**](IssuesApi.md#issuesDeleteComment) | **DELETE** /repos/{owner}/{repo}/issues/comments/{comment_id} | Delete an issue comment |
| [**issuesDeleteLabel**](IssuesApi.md#issuesDeleteLabel) | **DELETE** /repos/{owner}/{repo}/labels/{name} | Delete a label |
| [**issuesDeleteMilestone**](IssuesApi.md#issuesDeleteMilestone) | **DELETE** /repos/{owner}/{repo}/milestones/{milestone_number} | Delete a milestone |
| [**issuesGet**](IssuesApi.md#issuesGet) | **GET** /repos/{owner}/{repo}/issues/{issue_number} | Get an issue |
| [**issuesGetComment**](IssuesApi.md#issuesGetComment) | **GET** /repos/{owner}/{repo}/issues/comments/{comment_id} | Get an issue comment |
| [**issuesGetEvent**](IssuesApi.md#issuesGetEvent) | **GET** /repos/{owner}/{repo}/issues/events/{event_id} | Get an issue event |
| [**issuesGetLabel**](IssuesApi.md#issuesGetLabel) | **GET** /repos/{owner}/{repo}/labels/{name} | Get a label |
| [**issuesGetMilestone**](IssuesApi.md#issuesGetMilestone) | **GET** /repos/{owner}/{repo}/milestones/{milestone_number} | Get a milestone |
| [**issuesList**](IssuesApi.md#issuesList) | **GET** /issues | List issues assigned to the authenticated user |
| [**issuesListAssignees**](IssuesApi.md#issuesListAssignees) | **GET** /repos/{owner}/{repo}/assignees | List assignees |
| [**issuesListComments**](IssuesApi.md#issuesListComments) | **GET** /repos/{owner}/{repo}/issues/{issue_number}/comments | List issue comments |
| [**issuesListCommentsForRepo**](IssuesApi.md#issuesListCommentsForRepo) | **GET** /repos/{owner}/{repo}/issues/comments | List issue comments for a repository |
| [**issuesListEvents**](IssuesApi.md#issuesListEvents) | **GET** /repos/{owner}/{repo}/issues/{issue_number}/events | List issue events |
| [**issuesListEventsForRepo**](IssuesApi.md#issuesListEventsForRepo) | **GET** /repos/{owner}/{repo}/issues/events | List issue events for a repository |
| [**issuesListEventsForTimeline**](IssuesApi.md#issuesListEventsForTimeline) | **GET** /repos/{owner}/{repo}/issues/{issue_number}/timeline | List timeline events for an issue |
| [**issuesListForAuthenticatedUser**](IssuesApi.md#issuesListForAuthenticatedUser) | **GET** /user/issues | List user account issues assigned to the authenticated user |
| [**issuesListForOrg**](IssuesApi.md#issuesListForOrg) | **GET** /orgs/{org}/issues | List organization issues assigned to the authenticated user |
| [**issuesListForRepo**](IssuesApi.md#issuesListForRepo) | **GET** /repos/{owner}/{repo}/issues | List repository issues |
| [**issuesListLabelsForMilestone**](IssuesApi.md#issuesListLabelsForMilestone) | **GET** /repos/{owner}/{repo}/milestones/{milestone_number}/labels | List labels for issues in a milestone |
| [**issuesListLabelsForRepo**](IssuesApi.md#issuesListLabelsForRepo) | **GET** /repos/{owner}/{repo}/labels | List labels for a repository |
| [**issuesListLabelsOnIssue**](IssuesApi.md#issuesListLabelsOnIssue) | **GET** /repos/{owner}/{repo}/issues/{issue_number}/labels | List labels for an issue |
| [**issuesListMilestones**](IssuesApi.md#issuesListMilestones) | **GET** /repos/{owner}/{repo}/milestones | List milestones |
| [**issuesLock**](IssuesApi.md#issuesLock) | **PUT** /repos/{owner}/{repo}/issues/{issue_number}/lock | Lock an issue |
| [**issuesRemoveAllLabels**](IssuesApi.md#issuesRemoveAllLabels) | **DELETE** /repos/{owner}/{repo}/issues/{issue_number}/labels | Remove all labels from an issue |
| [**issuesRemoveAssignees**](IssuesApi.md#issuesRemoveAssignees) | **DELETE** /repos/{owner}/{repo}/issues/{issue_number}/assignees | Remove assignees from an issue |
| [**issuesRemoveLabel**](IssuesApi.md#issuesRemoveLabel) | **DELETE** /repos/{owner}/{repo}/issues/{issue_number}/labels/{name} | Remove a label from an issue |
| [**issuesSetLabels**](IssuesApi.md#issuesSetLabels) | **PUT** /repos/{owner}/{repo}/issues/{issue_number}/labels | Set labels for an issue |
| [**issuesUnlock**](IssuesApi.md#issuesUnlock) | **DELETE** /repos/{owner}/{repo}/issues/{issue_number}/lock | Unlock an issue |
| [**issuesUpdate**](IssuesApi.md#issuesUpdate) | **PATCH** /repos/{owner}/{repo}/issues/{issue_number} | Update an issue |
| [**issuesUpdateComment**](IssuesApi.md#issuesUpdateComment) | **PATCH** /repos/{owner}/{repo}/issues/comments/{comment_id} | Update an issue comment |
| [**issuesUpdateLabel**](IssuesApi.md#issuesUpdateLabel) | **PATCH** /repos/{owner}/{repo}/labels/{name} | Update a label |
| [**issuesUpdateMilestone**](IssuesApi.md#issuesUpdateMilestone) | **PATCH** /repos/{owner}/{repo}/milestones/{milestone_number} | Update a milestone |


<a id="issuesAddAssignees"></a>
# **issuesAddAssignees**
> Issue issuesAddAssignees(owner, repo, issueNumber, issuesAddAssigneesRequest)

Add assignees to an issue

Adds up to 10 assignees to an issue. Users already assigned to an issue are not replaced.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer issueNumber = 56; // Integer | The number that identifies the issue.
    IssuesAddAssigneesRequest issuesAddAssigneesRequest = new IssuesAddAssigneesRequest(); // IssuesAddAssigneesRequest | 
    try {
      Issue result = apiInstance.issuesAddAssignees(owner, repo, issueNumber, issuesAddAssigneesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesAddAssignees");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issueNumber** | **Integer**| The number that identifies the issue. | |
| **issuesAddAssigneesRequest** | [**IssuesAddAssigneesRequest**](IssuesAddAssigneesRequest.md)|  | [optional] |

### Return type

[**Issue**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  -  |

<a id="issuesAddLabels"></a>
# **issuesAddLabels**
> List&lt;Label&gt; issuesAddLabels(owner, repo, issueNumber, issuesAddLabelsRequest)

Add labels to an issue



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer issueNumber = 56; // Integer | The number that identifies the issue.
    IssuesAddLabelsRequest issuesAddLabelsRequest = new IssuesAddLabelsRequest(); // IssuesAddLabelsRequest | 
    try {
      List<Label> result = apiInstance.issuesAddLabels(owner, repo, issueNumber, issuesAddLabelsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesAddLabels");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issueNumber** | **Integer**| The number that identifies the issue. | |
| **issuesAddLabelsRequest** | [**IssuesAddLabelsRequest**](IssuesAddLabelsRequest.md)|  | [optional] |

### Return type

[**List&lt;Label&gt;**](Label.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **301** | Moved permanently |  -  |
| **404** | Resource not found |  -  |
| **410** | Gone |  -  |
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

<a id="issuesCheckUserCanBeAssigned"></a>
# **issuesCheckUserCanBeAssigned**
> issuesCheckUserCanBeAssigned(owner, repo, assignee)

Check if a user can be assigned

Checks if a user has permission to be assigned to an issue in this repository.  If the &#x60;assignee&#x60; can be assigned to issues in the repository, a &#x60;204&#x60; header with no content is returned.  Otherwise a &#x60;404&#x60; status code is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    String assignee = "assignee_example"; // String | 
    try {
      apiInstance.issuesCheckUserCanBeAssigned(owner, repo, assignee);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesCheckUserCanBeAssigned");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **assignee** | **String**|  | |

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
| **204** | If the &#x60;assignee&#x60; can be assigned to issues in the repository, a &#x60;204&#x60; header with no content is returned. |  -  |
| **404** | Otherwise a &#x60;404&#x60; status code is returned. |  -  |

<a id="issuesCheckUserCanBeAssignedToIssue"></a>
# **issuesCheckUserCanBeAssignedToIssue**
> issuesCheckUserCanBeAssignedToIssue(owner, repo, issueNumber, assignee)

Check if a user can be assigned to a issue

Checks if a user has permission to be assigned to a specific issue.  If the &#x60;assignee&#x60; can be assigned to this issue, a &#x60;204&#x60; status code with no content is returned.  Otherwise a &#x60;404&#x60; status code is returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer issueNumber = 56; // Integer | The number that identifies the issue.
    String assignee = "assignee_example"; // String | 
    try {
      apiInstance.issuesCheckUserCanBeAssignedToIssue(owner, repo, issueNumber, assignee);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesCheckUserCanBeAssignedToIssue");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issueNumber** | **Integer**| The number that identifies the issue. | |
| **assignee** | **String**|  | |

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
| **204** | Response if &#x60;assignee&#x60; can be assigned to &#x60;issue_number&#x60; |  -  |
| **404** | Response if &#x60;assignee&#x60; can not be assigned to &#x60;issue_number&#x60; |  -  |

<a id="issuesCreate"></a>
# **issuesCreate**
> Issue issuesCreate(owner, repo, issuesCreateRequest)

Create an issue

Any user with pull access to a repository can create an issue. If [issues are disabled in the repository](https://docs.github.com/enterprise-server@3.3/articles/disabling-issues/), the API returns a &#x60;410 Gone&#x60; status.  This endpoint triggers [notifications](https://docs.github.com/enterprise-server@3.3/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    IssuesCreateRequest issuesCreateRequest = new IssuesCreateRequest(); // IssuesCreateRequest | 
    try {
      Issue result = apiInstance.issuesCreate(owner, repo, issuesCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesCreate");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issuesCreateRequest** | [**IssuesCreateRequest**](IssuesCreateRequest.md)|  | |

### Return type

[**Issue**](Issue.md)

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
| **410** | Gone |  -  |
| **422** | Validation failed, or the endpoint has been spammed. |  -  |
| **503** | Service unavailable |  -  |

<a id="issuesCreateComment"></a>
# **issuesCreateComment**
> IssueComment issuesCreateComment(owner, repo, issueNumber, issuesUpdateCommentRequest)

Create an issue comment

This endpoint triggers [notifications](https://docs.github.com/enterprise-server@3.3/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See \&quot;[Secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#secondary-rate-limits)\&quot; and \&quot;[Dealing with secondary rate limits](https://docs.github.com/enterprise-server@3.3/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)\&quot; for details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer issueNumber = 56; // Integer | The number that identifies the issue.
    IssuesUpdateCommentRequest issuesUpdateCommentRequest = new IssuesUpdateCommentRequest(); // IssuesUpdateCommentRequest | 
    try {
      IssueComment result = apiInstance.issuesCreateComment(owner, repo, issueNumber, issuesUpdateCommentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesCreateComment");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issueNumber** | **Integer**| The number that identifies the issue. | |
| **issuesUpdateCommentRequest** | [**IssuesUpdateCommentRequest**](IssuesUpdateCommentRequest.md)|  | |

### Return type

[**IssueComment**](IssueComment.md)

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
| **410** | Gone |  -  |
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

<a id="issuesCreateLabel"></a>
# **issuesCreateLabel**
> Label issuesCreateLabel(owner, repo, issuesCreateLabelRequest)

Create a label



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    IssuesCreateLabelRequest issuesCreateLabelRequest = new IssuesCreateLabelRequest(); // IssuesCreateLabelRequest | 
    try {
      Label result = apiInstance.issuesCreateLabel(owner, repo, issuesCreateLabelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesCreateLabel");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issuesCreateLabelRequest** | [**IssuesCreateLabelRequest**](IssuesCreateLabelRequest.md)|  | |

### Return type

[**Label**](Label.md)

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
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

<a id="issuesCreateMilestone"></a>
# **issuesCreateMilestone**
> Milestone issuesCreateMilestone(owner, repo, issuesCreateMilestoneRequest)

Create a milestone



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    IssuesCreateMilestoneRequest issuesCreateMilestoneRequest = new IssuesCreateMilestoneRequest(); // IssuesCreateMilestoneRequest | 
    try {
      Milestone result = apiInstance.issuesCreateMilestone(owner, repo, issuesCreateMilestoneRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesCreateMilestone");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issuesCreateMilestoneRequest** | [**IssuesCreateMilestoneRequest**](IssuesCreateMilestoneRequest.md)|  | |

### Return type

[**Milestone**](Milestone.md)

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
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

<a id="issuesDeleteComment"></a>
# **issuesDeleteComment**
> issuesDeleteComment(owner, repo, commentId)

Delete an issue comment



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer commentId = 56; // Integer | The unique identifier of the comment.
    try {
      apiInstance.issuesDeleteComment(owner, repo, commentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesDeleteComment");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **commentId** | **Integer**| The unique identifier of the comment. | |

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

<a id="issuesDeleteLabel"></a>
# **issuesDeleteLabel**
> issuesDeleteLabel(owner, repo, name)

Delete a label



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    String name = "name_example"; // String | 
    try {
      apiInstance.issuesDeleteLabel(owner, repo, name);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesDeleteLabel");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **name** | **String**|  | |

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

<a id="issuesDeleteMilestone"></a>
# **issuesDeleteMilestone**
> issuesDeleteMilestone(owner, repo, milestoneNumber)

Delete a milestone



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer milestoneNumber = 56; // Integer | The number that identifies the milestone.
    try {
      apiInstance.issuesDeleteMilestone(owner, repo, milestoneNumber);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesDeleteMilestone");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **milestoneNumber** | **Integer**| The number that identifies the milestone. | |

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

<a id="issuesGet"></a>
# **issuesGet**
> Issue issuesGet(owner, repo, issueNumber)

Get an issue

The API returns a [&#x60;301 Moved Permanently&#x60; status](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#http-redirects-redirects) if the issue was [transferred](https://docs.github.com/enterprise-server@3.3/articles/transferring-an-issue-to-another-repository/) to another repository. If the issue was transferred to or deleted from a repository where the authenticated user lacks read access, the API returns a &#x60;404 Not Found&#x60; status. If the issue was deleted from a repository where the authenticated user has read access, the API returns a &#x60;410 Gone&#x60; status. To receive webhook events for transferred and deleted issues, subscribe to the [&#x60;issues&#x60;](https://docs.github.com/enterprise-server@3.3/webhooks/event-payloads/#issues) webhook.  **Note**: GitHub&#39;s REST API considers every pull request an issue, but not every issue is a pull request. For this reason, \&quot;Issues\&quot; endpoints may return both issues and pull requests in the response. You can identify pull requests by the &#x60;pull_request&#x60; key. Be aware that the &#x60;id&#x60; of a pull request returned from \&quot;Issues\&quot; endpoints will be an _issue id_. To find out the pull request id, use the \&quot;[List pull requests](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-pull-requests)\&quot; endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer issueNumber = 56; // Integer | The number that identifies the issue.
    try {
      Issue result = apiInstance.issuesGet(owner, repo, issueNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesGet");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issueNumber** | **Integer**| The number that identifies the issue. | |

### Return type

[**Issue**](Issue.md)

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
| **304** | Not modified |  -  |
| **404** | Resource not found |  -  |
| **410** | Gone |  -  |

<a id="issuesGetComment"></a>
# **issuesGetComment**
> IssueComment issuesGetComment(owner, repo, commentId)

Get an issue comment



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer commentId = 56; // Integer | The unique identifier of the comment.
    try {
      IssueComment result = apiInstance.issuesGetComment(owner, repo, commentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesGetComment");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **commentId** | **Integer**| The unique identifier of the comment. | |

### Return type

[**IssueComment**](IssueComment.md)

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

<a id="issuesGetEvent"></a>
# **issuesGetEvent**
> IssueEvent issuesGetEvent(owner, repo, eventId)

Get an issue event



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer eventId = 56; // Integer | 
    try {
      IssueEvent result = apiInstance.issuesGetEvent(owner, repo, eventId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesGetEvent");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **eventId** | **Integer**|  | |

### Return type

[**IssueEvent**](IssueEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **410** | Gone |  -  |

<a id="issuesGetLabel"></a>
# **issuesGetLabel**
> Label issuesGetLabel(owner, repo, name)

Get a label



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    String name = "name_example"; // String | 
    try {
      Label result = apiInstance.issuesGetLabel(owner, repo, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesGetLabel");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **name** | **String**|  | |

### Return type

[**Label**](Label.md)

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

<a id="issuesGetMilestone"></a>
# **issuesGetMilestone**
> Milestone issuesGetMilestone(owner, repo, milestoneNumber)

Get a milestone



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer milestoneNumber = 56; // Integer | The number that identifies the milestone.
    try {
      Milestone result = apiInstance.issuesGetMilestone(owner, repo, milestoneNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesGetMilestone");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **milestoneNumber** | **Integer**| The number that identifies the milestone. | |

### Return type

[**Milestone**](Milestone.md)

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

<a id="issuesList"></a>
# **issuesList**
> List&lt;Issue&gt; issuesList(filter, state, labels, sort, direction, since, collab, orgs, owned, pulls, perPage, page)

List issues assigned to the authenticated user

List issues assigned to the authenticated user across all visible repositories including owned repositories, member repositories, and organization repositories. You can use the &#x60;filter&#x60; query parameter to fetch issues that are not necessarily assigned to you.   **Note**: GitHub&#39;s REST API considers every pull request an issue, but not every issue is a pull request. For this reason, \&quot;Issues\&quot; endpoints may return both issues and pull requests in the response. You can identify pull requests by the &#x60;pull_request&#x60; key. Be aware that the &#x60;id&#x60; of a pull request returned from \&quot;Issues\&quot; endpoints will be an _issue id_. To find out the pull request id, use the \&quot;[List pull requests](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-pull-requests)\&quot; endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String filter = "assigned"; // String | Indicates which sorts of issues to return. `assigned` means issues assigned to you. `created` means issues created by you. `mentioned` means issues mentioning you. `subscribed` means issues you're subscribed to updates for. `all` or `repos` means all issues you can see, regardless of participation or creation.
    String state = "open"; // String | Indicates the state of the issues to return.
    String labels = "labels_example"; // String | A list of comma separated label names. Example: `bug,ui,@high`
    String sort = "created"; // String | What to sort results by.
    String direction = "asc"; // String | The direction to sort the results by.
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    Boolean collab = true; // Boolean | 
    Boolean orgs = true; // Boolean | 
    Boolean owned = true; // Boolean | 
    Boolean pulls = true; // Boolean | 
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Issue> result = apiInstance.issuesList(filter, state, labels, sort, direction, since, collab, orgs, owned, pulls, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesList");
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
| **filter** | **String**| Indicates which sorts of issues to return. &#x60;assigned&#x60; means issues assigned to you. &#x60;created&#x60; means issues created by you. &#x60;mentioned&#x60; means issues mentioning you. &#x60;subscribed&#x60; means issues you&#39;re subscribed to updates for. &#x60;all&#x60; or &#x60;repos&#x60; means all issues you can see, regardless of participation or creation. | [optional] [default to assigned] [enum: assigned, created, mentioned, subscribed, repos, all] |
| **state** | **String**| Indicates the state of the issues to return. | [optional] [default to open] [enum: open, closed, all] |
| **labels** | **String**| A list of comma separated label names. Example: &#x60;bug,ui,@high&#x60; | [optional] |
| **sort** | **String**| What to sort results by. | [optional] [default to created] [enum: created, updated, comments] |
| **direction** | **String**| The direction to sort the results by. | [optional] [default to desc] [enum: asc, desc] |
| **since** | **OffsetDateTime**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **collab** | **Boolean**|  | [optional] |
| **orgs** | **Boolean**|  | [optional] |
| **owned** | **Boolean**|  | [optional] |
| **pulls** | **Boolean**|  | [optional] |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Issue&gt;**](Issue.md)

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
| **404** | Resource not found |  -  |
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

<a id="issuesListAssignees"></a>
# **issuesListAssignees**
> List&lt;SimpleUser&gt; issuesListAssignees(owner, repo, perPage, page)

List assignees

Lists the [available assignees](https://docs.github.com/enterprise-server@3.3/articles/assigning-issues-and-pull-requests-to-other-github-users/) for issues in a repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<SimpleUser> result = apiInstance.issuesListAssignees(owner, repo, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesListAssignees");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
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
| **404** | Resource not found |  -  |

<a id="issuesListComments"></a>
# **issuesListComments**
> List&lt;IssueComment&gt; issuesListComments(owner, repo, issueNumber, since, perPage, page)

List issue comments

Issue Comments are ordered by ascending ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer issueNumber = 56; // Integer | The number that identifies the issue.
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<IssueComment> result = apiInstance.issuesListComments(owner, repo, issueNumber, since, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesListComments");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issueNumber** | **Integer**| The number that identifies the issue. | |
| **since** | **OffsetDateTime**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;IssueComment&gt;**](IssueComment.md)

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

<a id="issuesListCommentsForRepo"></a>
# **issuesListCommentsForRepo**
> List&lt;IssueComment&gt; issuesListCommentsForRepo(owner, repo, sort, direction, since, perPage, page)

List issue comments for a repository

By default, Issue Comments are ordered by ascending ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    String sort = "created"; // String | The property to sort the results by. `created` means when the repository was starred. `updated` means when the repository was last pushed to.
    String direction = "asc"; // String | Either `asc` or `desc`. Ignored without the `sort` parameter.
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<IssueComment> result = apiInstance.issuesListCommentsForRepo(owner, repo, sort, direction, since, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesListCommentsForRepo");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **sort** | **String**| The property to sort the results by. &#x60;created&#x60; means when the repository was starred. &#x60;updated&#x60; means when the repository was last pushed to. | [optional] [default to created] [enum: created, updated] |
| **direction** | **String**| Either &#x60;asc&#x60; or &#x60;desc&#x60;. Ignored without the &#x60;sort&#x60; parameter. | [optional] [enum: asc, desc] |
| **since** | **OffsetDateTime**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;IssueComment&gt;**](IssueComment.md)

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
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

<a id="issuesListEvents"></a>
# **issuesListEvents**
> List&lt;IssueEventForIssue&gt; issuesListEvents(owner, repo, issueNumber, perPage, page)

List issue events



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer issueNumber = 56; // Integer | The number that identifies the issue.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<IssueEventForIssue> result = apiInstance.issuesListEvents(owner, repo, issueNumber, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesListEvents");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issueNumber** | **Integer**| The number that identifies the issue. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;IssueEventForIssue&gt;**](IssueEventForIssue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **410** | Gone |  -  |

<a id="issuesListEventsForRepo"></a>
# **issuesListEventsForRepo**
> List&lt;IssueEvent&gt; issuesListEventsForRepo(owner, repo, perPage, page)

List issue events for a repository



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<IssueEvent> result = apiInstance.issuesListEventsForRepo(owner, repo, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesListEventsForRepo");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;IssueEvent&gt;**](IssueEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

<a id="issuesListEventsForTimeline"></a>
# **issuesListEventsForTimeline**
> List&lt;TimelineIssueEvents&gt; issuesListEventsForTimeline(owner, repo, issueNumber, perPage, page)

List timeline events for an issue



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer issueNumber = 56; // Integer | The number that identifies the issue.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<TimelineIssueEvents> result = apiInstance.issuesListEventsForTimeline(owner, repo, issueNumber, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesListEventsForTimeline");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issueNumber** | **Integer**| The number that identifies the issue. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;TimelineIssueEvents&gt;**](TimelineIssueEvents.md)

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

<a id="issuesListForAuthenticatedUser"></a>
# **issuesListForAuthenticatedUser**
> List&lt;Issue&gt; issuesListForAuthenticatedUser(filter, state, labels, sort, direction, since, perPage, page)

List user account issues assigned to the authenticated user

List issues across owned and member repositories assigned to the authenticated user.  **Note**: GitHub&#39;s REST API considers every pull request an issue, but not every issue is a pull request. For this reason, \&quot;Issues\&quot; endpoints may return both issues and pull requests in the response. You can identify pull requests by the &#x60;pull_request&#x60; key. Be aware that the &#x60;id&#x60; of a pull request returned from \&quot;Issues\&quot; endpoints will be an _issue id_. To find out the pull request id, use the \&quot;[List pull requests](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-pull-requests)\&quot; endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String filter = "assigned"; // String | Indicates which sorts of issues to return. `assigned` means issues assigned to you. `created` means issues created by you. `mentioned` means issues mentioning you. `subscribed` means issues you're subscribed to updates for. `all` or `repos` means all issues you can see, regardless of participation or creation.
    String state = "open"; // String | Indicates the state of the issues to return.
    String labels = "labels_example"; // String | A list of comma separated label names. Example: `bug,ui,@high`
    String sort = "created"; // String | What to sort results by.
    String direction = "asc"; // String | The direction to sort the results by.
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Issue> result = apiInstance.issuesListForAuthenticatedUser(filter, state, labels, sort, direction, since, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesListForAuthenticatedUser");
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
| **filter** | **String**| Indicates which sorts of issues to return. &#x60;assigned&#x60; means issues assigned to you. &#x60;created&#x60; means issues created by you. &#x60;mentioned&#x60; means issues mentioning you. &#x60;subscribed&#x60; means issues you&#39;re subscribed to updates for. &#x60;all&#x60; or &#x60;repos&#x60; means all issues you can see, regardless of participation or creation. | [optional] [default to assigned] [enum: assigned, created, mentioned, subscribed, repos, all] |
| **state** | **String**| Indicates the state of the issues to return. | [optional] [default to open] [enum: open, closed, all] |
| **labels** | **String**| A list of comma separated label names. Example: &#x60;bug,ui,@high&#x60; | [optional] |
| **sort** | **String**| What to sort results by. | [optional] [default to created] [enum: created, updated, comments] |
| **direction** | **String**| The direction to sort the results by. | [optional] [default to desc] [enum: asc, desc] |
| **since** | **OffsetDateTime**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Issue&gt;**](Issue.md)

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
| **404** | Resource not found |  -  |

<a id="issuesListForOrg"></a>
# **issuesListForOrg**
> List&lt;Issue&gt; issuesListForOrg(org, filter, state, labels, sort, direction, since, perPage, page)

List organization issues assigned to the authenticated user

List issues in an organization assigned to the authenticated user.  **Note**: GitHub&#39;s REST API considers every pull request an issue, but not every issue is a pull request. For this reason, \&quot;Issues\&quot; endpoints may return both issues and pull requests in the response. You can identify pull requests by the &#x60;pull_request&#x60; key. Be aware that the &#x60;id&#x60; of a pull request returned from \&quot;Issues\&quot; endpoints will be an _issue id_. To find out the pull request id, use the \&quot;[List pull requests](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-pull-requests)\&quot; endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    String filter = "assigned"; // String | Indicates which sorts of issues to return. `assigned` means issues assigned to you. `created` means issues created by you. `mentioned` means issues mentioning you. `subscribed` means issues you're subscribed to updates for. `all` or `repos` means all issues you can see, regardless of participation or creation.
    String state = "open"; // String | Indicates the state of the issues to return.
    String labels = "labels_example"; // String | A list of comma separated label names. Example: `bug,ui,@high`
    String sort = "created"; // String | What to sort results by.
    String direction = "asc"; // String | The direction to sort the results by.
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Issue> result = apiInstance.issuesListForOrg(org, filter, state, labels, sort, direction, since, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesListForOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **filter** | **String**| Indicates which sorts of issues to return. &#x60;assigned&#x60; means issues assigned to you. &#x60;created&#x60; means issues created by you. &#x60;mentioned&#x60; means issues mentioning you. &#x60;subscribed&#x60; means issues you&#39;re subscribed to updates for. &#x60;all&#x60; or &#x60;repos&#x60; means all issues you can see, regardless of participation or creation. | [optional] [default to assigned] [enum: assigned, created, mentioned, subscribed, repos, all] |
| **state** | **String**| Indicates the state of the issues to return. | [optional] [default to open] [enum: open, closed, all] |
| **labels** | **String**| A list of comma separated label names. Example: &#x60;bug,ui,@high&#x60; | [optional] |
| **sort** | **String**| What to sort results by. | [optional] [default to created] [enum: created, updated, comments] |
| **direction** | **String**| The direction to sort the results by. | [optional] [default to desc] [enum: asc, desc] |
| **since** | **OffsetDateTime**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Issue&gt;**](Issue.md)

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

<a id="issuesListForRepo"></a>
# **issuesListForRepo**
> List&lt;Issue&gt; issuesListForRepo(owner, repo, milestone, state, assignee, creator, mentioned, labels, sort, direction, since, perPage, page)

List repository issues

List issues in a repository. Only open issues will be listed.  **Note**: GitHub&#39;s REST API considers every pull request an issue, but not every issue is a pull request. For this reason, \&quot;Issues\&quot; endpoints may return both issues and pull requests in the response. You can identify pull requests by the &#x60;pull_request&#x60; key. Be aware that the &#x60;id&#x60; of a pull request returned from \&quot;Issues\&quot; endpoints will be an _issue id_. To find out the pull request id, use the \&quot;[List pull requests](https://docs.github.com/enterprise-server@3.3/rest/reference/pulls#list-pull-requests)\&quot; endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    String milestone = "milestone_example"; // String | If an `integer` is passed, it should refer to a milestone by its `number` field. If the string `*` is passed, issues with any milestone are accepted. If the string `none` is passed, issues without milestones are returned.
    String state = "open"; // String | Indicates the state of the issues to return.
    String assignee = "assignee_example"; // String | Can be the name of a user. Pass in `none` for issues with no assigned user, and `*` for issues assigned to any user.
    String creator = "creator_example"; // String | The user that created the issue.
    String mentioned = "mentioned_example"; // String | A user that's mentioned in the issue.
    String labels = "labels_example"; // String | A list of comma separated label names. Example: `bug,ui,@high`
    String sort = "created"; // String | What to sort results by.
    String direction = "asc"; // String | The direction to sort the results by.
    OffsetDateTime since = OffsetDateTime.now(); // OffsetDateTime | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Issue> result = apiInstance.issuesListForRepo(owner, repo, milestone, state, assignee, creator, mentioned, labels, sort, direction, since, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesListForRepo");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **milestone** | **String**| If an &#x60;integer&#x60; is passed, it should refer to a milestone by its &#x60;number&#x60; field. If the string &#x60;*&#x60; is passed, issues with any milestone are accepted. If the string &#x60;none&#x60; is passed, issues without milestones are returned. | [optional] |
| **state** | **String**| Indicates the state of the issues to return. | [optional] [default to open] [enum: open, closed, all] |
| **assignee** | **String**| Can be the name of a user. Pass in &#x60;none&#x60; for issues with no assigned user, and &#x60;*&#x60; for issues assigned to any user. | [optional] |
| **creator** | **String**| The user that created the issue. | [optional] |
| **mentioned** | **String**| A user that&#39;s mentioned in the issue. | [optional] |
| **labels** | **String**| A list of comma separated label names. Example: &#x60;bug,ui,@high&#x60; | [optional] |
| **sort** | **String**| What to sort results by. | [optional] [default to created] [enum: created, updated, comments] |
| **direction** | **String**| The direction to sort the results by. | [optional] [default to desc] [enum: asc, desc] |
| **since** | **OffsetDateTime**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Issue&gt;**](Issue.md)

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
| **404** | Resource not found |  -  |
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

<a id="issuesListLabelsForMilestone"></a>
# **issuesListLabelsForMilestone**
> List&lt;Label&gt; issuesListLabelsForMilestone(owner, repo, milestoneNumber, perPage, page)

List labels for issues in a milestone



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer milestoneNumber = 56; // Integer | The number that identifies the milestone.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Label> result = apiInstance.issuesListLabelsForMilestone(owner, repo, milestoneNumber, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesListLabelsForMilestone");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **milestoneNumber** | **Integer**| The number that identifies the milestone. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Label&gt;**](Label.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |

<a id="issuesListLabelsForRepo"></a>
# **issuesListLabelsForRepo**
> List&lt;Label&gt; issuesListLabelsForRepo(owner, repo, perPage, page)

List labels for a repository



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Label> result = apiInstance.issuesListLabelsForRepo(owner, repo, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesListLabelsForRepo");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Label&gt;**](Label.md)

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

<a id="issuesListLabelsOnIssue"></a>
# **issuesListLabelsOnIssue**
> List&lt;Label&gt; issuesListLabelsOnIssue(owner, repo, issueNumber, perPage, page)

List labels for an issue



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer issueNumber = 56; // Integer | The number that identifies the issue.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Label> result = apiInstance.issuesListLabelsOnIssue(owner, repo, issueNumber, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesListLabelsOnIssue");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issueNumber** | **Integer**| The number that identifies the issue. | |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Label&gt;**](Label.md)

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
| **404** | Resource not found |  -  |
| **410** | Gone |  -  |

<a id="issuesListMilestones"></a>
# **issuesListMilestones**
> List&lt;Milestone&gt; issuesListMilestones(owner, repo, state, sort, direction, perPage, page)

List milestones



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    String state = "open"; // String | The state of the milestone. Either `open`, `closed`, or `all`.
    String sort = "due_on"; // String | What to sort results by. Either `due_on` or `completeness`.
    String direction = "asc"; // String | The direction of the sort. Either `asc` or `desc`.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    try {
      List<Milestone> result = apiInstance.issuesListMilestones(owner, repo, state, sort, direction, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesListMilestones");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **state** | **String**| The state of the milestone. Either &#x60;open&#x60;, &#x60;closed&#x60;, or &#x60;all&#x60;. | [optional] [default to open] [enum: open, closed, all] |
| **sort** | **String**| What to sort results by. Either &#x60;due_on&#x60; or &#x60;completeness&#x60;. | [optional] [default to due_on] [enum: due_on, completeness] |
| **direction** | **String**| The direction of the sort. Either &#x60;asc&#x60; or &#x60;desc&#x60;. | [optional] [default to asc] [enum: asc, desc] |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |

### Return type

[**List&lt;Milestone&gt;**](Milestone.md)

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

<a id="issuesLock"></a>
# **issuesLock**
> issuesLock(owner, repo, issueNumber, issuesLockRequest)

Lock an issue

Users with push access can lock an issue or pull request&#39;s conversation.  Note that, if you choose not to pass any parameters, you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer issueNumber = 56; // Integer | The number that identifies the issue.
    IssuesLockRequest issuesLockRequest = new IssuesLockRequest(); // IssuesLockRequest | 
    try {
      apiInstance.issuesLock(owner, repo, issueNumber, issuesLockRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesLock");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issueNumber** | **Integer**| The number that identifies the issue. | |
| **issuesLockRequest** | [**IssuesLockRequest**](IssuesLockRequest.md)|  | [optional] |

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
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **410** | Gone |  -  |
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

<a id="issuesRemoveAllLabels"></a>
# **issuesRemoveAllLabels**
> issuesRemoveAllLabels(owner, repo, issueNumber)

Remove all labels from an issue



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer issueNumber = 56; // Integer | The number that identifies the issue.
    try {
      apiInstance.issuesRemoveAllLabels(owner, repo, issueNumber);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesRemoveAllLabels");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issueNumber** | **Integer**| The number that identifies the issue. | |

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
| **301** | Moved permanently |  -  |
| **404** | Resource not found |  -  |
| **410** | Gone |  -  |

<a id="issuesRemoveAssignees"></a>
# **issuesRemoveAssignees**
> Issue issuesRemoveAssignees(owner, repo, issueNumber, issuesRemoveAssigneesRequest)

Remove assignees from an issue

Removes one or more assignees from an issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer issueNumber = 56; // Integer | The number that identifies the issue.
    IssuesRemoveAssigneesRequest issuesRemoveAssigneesRequest = new IssuesRemoveAssigneesRequest(); // IssuesRemoveAssigneesRequest | 
    try {
      Issue result = apiInstance.issuesRemoveAssignees(owner, repo, issueNumber, issuesRemoveAssigneesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesRemoveAssignees");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issueNumber** | **Integer**| The number that identifies the issue. | |
| **issuesRemoveAssigneesRequest** | [**IssuesRemoveAssigneesRequest**](IssuesRemoveAssigneesRequest.md)|  | [optional] |

### Return type

[**Issue**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="issuesRemoveLabel"></a>
# **issuesRemoveLabel**
> List&lt;Label&gt; issuesRemoveLabel(owner, repo, issueNumber, name)

Remove a label from an issue

Removes the specified label from the issue, and returns the remaining labels on the issue. This endpoint returns a &#x60;404 Not Found&#x60; status if the label does not exist.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer issueNumber = 56; // Integer | The number that identifies the issue.
    String name = "name_example"; // String | 
    try {
      List<Label> result = apiInstance.issuesRemoveLabel(owner, repo, issueNumber, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesRemoveLabel");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issueNumber** | **Integer**| The number that identifies the issue. | |
| **name** | **String**|  | |

### Return type

[**List&lt;Label&gt;**](Label.md)

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
| **410** | Gone |  -  |

<a id="issuesSetLabels"></a>
# **issuesSetLabels**
> List&lt;Label&gt; issuesSetLabels(owner, repo, issueNumber, issuesSetLabelsRequest)

Set labels for an issue

Removes any previous labels and sets the new labels for an issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer issueNumber = 56; // Integer | The number that identifies the issue.
    IssuesSetLabelsRequest issuesSetLabelsRequest = new IssuesSetLabelsRequest(); // IssuesSetLabelsRequest | 
    try {
      List<Label> result = apiInstance.issuesSetLabels(owner, repo, issueNumber, issuesSetLabelsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesSetLabels");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issueNumber** | **Integer**| The number that identifies the issue. | |
| **issuesSetLabelsRequest** | [**IssuesSetLabelsRequest**](IssuesSetLabelsRequest.md)|  | [optional] |

### Return type

[**List&lt;Label&gt;**](Label.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **301** | Moved permanently |  -  |
| **404** | Resource not found |  -  |
| **410** | Gone |  -  |
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

<a id="issuesUnlock"></a>
# **issuesUnlock**
> issuesUnlock(owner, repo, issueNumber)

Unlock an issue

Users with push access can unlock an issue&#39;s conversation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer issueNumber = 56; // Integer | The number that identifies the issue.
    try {
      apiInstance.issuesUnlock(owner, repo, issueNumber);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesUnlock");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issueNumber** | **Integer**| The number that identifies the issue. | |

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
| **404** | Resource not found |  -  |

<a id="issuesUpdate"></a>
# **issuesUpdate**
> Issue issuesUpdate(owner, repo, issueNumber, issuesUpdateRequest)

Update an issue

Issue owners and users with push access can edit an issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer issueNumber = 56; // Integer | The number that identifies the issue.
    IssuesUpdateRequest issuesUpdateRequest = new IssuesUpdateRequest(); // IssuesUpdateRequest | 
    try {
      Issue result = apiInstance.issuesUpdate(owner, repo, issueNumber, issuesUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesUpdate");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **issueNumber** | **Integer**| The number that identifies the issue. | |
| **issuesUpdateRequest** | [**IssuesUpdateRequest**](IssuesUpdateRequest.md)|  | [optional] |

### Return type

[**Issue**](Issue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **301** | Moved permanently |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |
| **410** | Gone |  -  |
| **422** | Validation failed, or the endpoint has been spammed. |  -  |
| **503** | Service unavailable |  -  |

<a id="issuesUpdateComment"></a>
# **issuesUpdateComment**
> IssueComment issuesUpdateComment(owner, repo, commentId, issuesUpdateCommentRequest)

Update an issue comment



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer commentId = 56; // Integer | The unique identifier of the comment.
    IssuesUpdateCommentRequest issuesUpdateCommentRequest = new IssuesUpdateCommentRequest(); // IssuesUpdateCommentRequest | 
    try {
      IssueComment result = apiInstance.issuesUpdateComment(owner, repo, commentId, issuesUpdateCommentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesUpdateComment");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **commentId** | **Integer**| The unique identifier of the comment. | |
| **issuesUpdateCommentRequest** | [**IssuesUpdateCommentRequest**](IssuesUpdateCommentRequest.md)|  | |

### Return type

[**IssueComment**](IssueComment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

<a id="issuesUpdateLabel"></a>
# **issuesUpdateLabel**
> Label issuesUpdateLabel(owner, repo, name, issuesUpdateLabelRequest)

Update a label



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    String name = "name_example"; // String | 
    IssuesUpdateLabelRequest issuesUpdateLabelRequest = new IssuesUpdateLabelRequest(); // IssuesUpdateLabelRequest | 
    try {
      Label result = apiInstance.issuesUpdateLabel(owner, repo, name, issuesUpdateLabelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesUpdateLabel");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **name** | **String**|  | |
| **issuesUpdateLabelRequest** | [**IssuesUpdateLabelRequest**](IssuesUpdateLabelRequest.md)|  | [optional] |

### Return type

[**Label**](Label.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

<a id="issuesUpdateMilestone"></a>
# **issuesUpdateMilestone**
> Milestone issuesUpdateMilestone(owner, repo, milestoneNumber, issuesUpdateMilestoneRequest)

Update a milestone



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    IssuesApi apiInstance = new IssuesApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer milestoneNumber = 56; // Integer | The number that identifies the milestone.
    IssuesUpdateMilestoneRequest issuesUpdateMilestoneRequest = new IssuesUpdateMilestoneRequest(); // IssuesUpdateMilestoneRequest | 
    try {
      Milestone result = apiInstance.issuesUpdateMilestone(owner, repo, milestoneNumber, issuesUpdateMilestoneRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssuesApi#issuesUpdateMilestone");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **milestoneNumber** | **Integer**| The number that identifies the milestone. | |
| **issuesUpdateMilestoneRequest** | [**IssuesUpdateMilestoneRequest**](IssuesUpdateMilestoneRequest.md)|  | [optional] |

### Return type

[**Milestone**](Milestone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |

