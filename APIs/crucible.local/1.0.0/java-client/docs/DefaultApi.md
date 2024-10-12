# DefaultApi

All URIs are relative to *http://crucible.local/context*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addChangesetToReview**](DefaultApi.md#addChangesetToReview) | **POST** /rest-service/reviews-v1/{id}/addChangeset |  |
| [**addFile**](DefaultApi.md#addFile) | **POST** /rest-service/reviews-v1/{id}/addFile |  |
| [**addFisheyeReviewItem**](DefaultApi.md#addFisheyeReviewItem) | **POST** /rest-service/reviews-v1/{id}/reviewitems |  |
| [**addGeneralComment**](DefaultApi.md#addGeneralComment) | **POST** /rest-service/reviews-v1/{id}/comments |  |
| [**addPatchReview0**](DefaultApi.md#addPatchReview0) | **POST** /rest-service/reviews-v1/{id}/addPatch |  |
| [**addPatchToReview**](DefaultApi.md#addPatchToReview) | **POST** /rest-service/reviews-v1/{id}/patch |  |
| [**addReply**](DefaultApi.md#addReply) | **POST** /rest-service/reviews-v1/{id}/comments/{cId}/replies |  |
| [**addReviewItem**](DefaultApi.md#addReviewItem) | **POST** /rest-service/reviews-v1/{id}/reviewitems/details |  |
| [**addReviewItemRevisions**](DefaultApi.md#addReviewItemRevisions) | **POST** /rest-service/reviews-v1/{id}/reviewitems/{riId}/revisions |  |
| [**addReviewItems**](DefaultApi.md#addReviewItems) | **POST** /rest-service/reviews-v1/{id}/reviewitems/revisions |  |
| [**addReviewers**](DefaultApi.md#addReviewers) | **POST** /rest-service/reviews-v1/{id}/reviewers |  |
| [**addVersionedComment**](DefaultApi.md#addVersionedComment) | **POST** /rest-service/reviews-v1/{id}/reviewitems/{riId}/comments |  |
| [**browse**](DefaultApi.md#browse) | **GET** /rest-service/repositories-v1/browse/{repository}/{path} |  |
| [**change**](DefaultApi.md#change) | **GET** /rest-service/repositories-v1/change/{repository}/{revision} |  |
| [**changeState**](DefaultApi.md#changeState) | **POST** /rest-service/reviews-v1/{id}/transition |  |
| [**changes**](DefaultApi.md#changes) | **GET** /rest-service/repositories-v1/changes/{repository}/{path} |  |
| [**closeReviewWithComment**](DefaultApi.md#closeReviewWithComment) | **POST** /rest-service/reviews-v1/{id}/close |  |
| [**completeReview**](DefaultApi.md#completeReview) | **POST** /rest-service/reviews-v1/{id}/complete |  |
| [**createReview**](DefaultApi.md#createReview) | **POST** /rest-service/reviews-v1 |  |
| [**deleteReview**](DefaultApi.md#deleteReview) | **DELETE** /rest-service/reviews-v1/{id} |  |
| [**details**](DefaultApi.md#details) | **GET** /rest-service/repositories-v1/{repository}/{revision}/{path} |  |
| [**getAllComments**](DefaultApi.md#getAllComments) | **GET** /rest-service/reviews-v1/{id}/comments |  |
| [**getAllDetailedReviews**](DefaultApi.md#getAllDetailedReviews) | **GET** /rest-service/reviews-v1/details |  |
| [**getAllProjects**](DefaultApi.md#getAllProjects) | **GET** /rest-service/projects-v1 |  |
| [**getAllRepositories**](DefaultApi.md#getAllRepositories) | **GET** /rest-service/repositories-v1 |  |
| [**getAllReviews**](DefaultApi.md#getAllReviews) | **GET** /rest-service/reviews-v1 |  |
| [**getAvailableActions**](DefaultApi.md#getAvailableActions) | **GET** /rest-service/reviews-v1/{id}/actions |  |
| [**getAvailableTransitions**](DefaultApi.md#getAvailableTransitions) | **GET** /rest-service/reviews-v1/{id}/transitions |  |
| [**getComment**](DefaultApi.md#getComment) | **GET** /rest-service/reviews-v1/{id}/comments/{cId} |  |
| [**getCompletedReviewers**](DefaultApi.md#getCompletedReviewers) | **GET** /rest-service/reviews-v1/{id}/reviewers/completed |  |
| [**getContents**](DefaultApi.md#getContents) | **GET** /rest-service/repositories-v1/content/{repository}/{revision}/{path} |  |
| [**getCustomFilterReviews**](DefaultApi.md#getCustomFilterReviews) | **GET** /rest-service/reviews-v1/filter |  |
| [**getDetailedCustomFilterReviews**](DefaultApi.md#getDetailedCustomFilterReviews) | **GET** /rest-service/reviews-v1/filter/details |  |
| [**getDetailedFilteredReviewsForUser**](DefaultApi.md#getDetailedFilteredReviewsForUser) | **GET** /rest-service/reviews-v1/filter/{filter}/details |  |
| [**getDetailedReview**](DefaultApi.md#getDetailedReview) | **GET** /rest-service/reviews-v1/{id}/details |  |
| [**getFilteredReviewsForUser**](DefaultApi.md#getFilteredReviewsForUser) | **GET** /rest-service/reviews-v1/filter/{filter} |  |
| [**getGeneralComments**](DefaultApi.md#getGeneralComments) | **GET** /rest-service/reviews-v1/{id}/comments/general |  |
| [**getMappedUser**](DefaultApi.md#getMappedUser) | **GET** /rest-service/users-v1/{repository}/{username} |  |
| [**getMetrics**](DefaultApi.md#getMetrics) | **GET** /rest-service/reviews-v1/metrics/{version} |  |
| [**getProject**](DefaultApi.md#getProject) | **GET** /rest-service/projects-v1/{key} |  |
| [**getReplies**](DefaultApi.md#getReplies) | **GET** /rest-service/reviews-v1/{id}/comments/{cId}/replies |  |
| [**getRepositoryDetails**](DefaultApi.md#getRepositoryDetails) | **GET** /rest-service/repositories-v1/{repository} |  |
| [**getReview**](DefaultApi.md#getReview) | **GET** /rest-service/reviews-v1/{id} |  |
| [**getReviewItem**](DefaultApi.md#getReviewItem) | **GET** /rest-service/reviews-v1/{id}/reviewitems/{riId} |  |
| [**getReviewItemsComments**](DefaultApi.md#getReviewItemsComments) | **GET** /rest-service/reviews-v1/{id}/reviewitems/{riId}/comments |  |
| [**getReviewItemsForReview**](DefaultApi.md#getReviewItemsForReview) | **GET** /rest-service/reviews-v1/{id}/reviewitems |  |
| [**getReviewPatches**](DefaultApi.md#getReviewPatches) | **GET** /rest-service/reviews-v1/{id}/patch |  |
| [**getReviewers**](DefaultApi.md#getReviewers) | **GET** /rest-service/reviews-v1/{id}/reviewers |  |
| [**getReviewsDetailsForPath**](DefaultApi.md#getReviewsDetailsForPath) | **GET** /rest-service/reviews-v1/search/{repository}/details |  |
| [**getReviewsForIssueKey**](DefaultApi.md#getReviewsForIssueKey) | **GET** /rest-service/search-v1/reviewsForIssue |  |
| [**getReviewsForPath**](DefaultApi.md#getReviewsForPath) | **GET** /rest-service/reviews-v1/search/{repository} |  |
| [**getReviewsForTerm**](DefaultApi.md#getReviewsForTerm) | **GET** /rest-service/search-v1/reviews |  |
| [**getSvnRepositoryDetails**](DefaultApi.md#getSvnRepositoryDetails) | **GET** /rest-service/repositories-v1/{repository}/svn |  |
| [**getUncompletedReviewers**](DefaultApi.md#getUncompletedReviewers) | **GET** /rest-service/reviews-v1/{id}/reviewers/uncompleted |  |
| [**getUserProfile**](DefaultApi.md#getUserProfile) | **GET** /rest-service/users-v1/{username} |  |
| [**getUsers**](DefaultApi.md#getUsers) | **GET** /rest-service/users-v1 |  |
| [**getVersionInfo**](DefaultApi.md#getVersionInfo) | **GET** /rest-service/reviews-v1/versionInfo |  |
| [**getVersionedComments**](DefaultApi.md#getVersionedComments) | **GET** /rest-service/reviews-v1/{id}/comments/versioned |  |
| [**history**](DefaultApi.md#history) | **GET** /rest-service/repositories-v1/history/{repository}/{revision}/{path} |  |
| [**login**](DefaultApi.md#login) | **GET** /rest-service/auth-v1/login |  |
| [**loginPost**](DefaultApi.md#loginPost) | **POST** /rest-service/auth-v1/login |  |
| [**markAllCommentsAsRead**](DefaultApi.md#markAllCommentsAsRead) | **POST** /rest-service/reviews-v1/{id}/comments/markAllAsRead |  |
| [**markCommentAsLeaveUnread**](DefaultApi.md#markCommentAsLeaveUnread) | **POST** /rest-service/reviews-v1/{id}/comments/{cId}/markAsLeaveUnread |  |
| [**markCommentAsRead**](DefaultApi.md#markCommentAsRead) | **POST** /rest-service/reviews-v1/{id}/comments/{cId}/markAsRead |  |
| [**postCustomFilterReviews**](DefaultApi.md#postCustomFilterReviews) | **POST** /rest-service/reviews-v1/filter |  |
| [**postDetailedCustomFilterReviews**](DefaultApi.md#postDetailedCustomFilterReviews) | **POST** /rest-service/reviews-v1/filter/details |  |
| [**publishAllComments**](DefaultApi.md#publishAllComments) | **POST** /rest-service/reviews-v1/{id}/publish |  |
| [**publishComment**](DefaultApi.md#publishComment) | **POST** /rest-service/reviews-v1/{id}/publish/{cId} |  |
| [**remindIncompleteReviewers**](DefaultApi.md#remindIncompleteReviewers) | **POST** /rest-service/reviews-v1/{id}/remind |  |
| [**removeComment**](DefaultApi.md#removeComment) | **DELETE** /rest-service/reviews-v1/{id}/comments/{cId} |  |
| [**removePatch**](DefaultApi.md#removePatch) | **DELETE** /rest-service/reviews-v1/{id}/patch/{patchId} |  |
| [**removeReply**](DefaultApi.md#removeReply) | **DELETE** /rest-service/reviews-v1/{id}/comments/{cId}/replies/{rId} |  |
| [**removeReviewItem**](DefaultApi.md#removeReviewItem) | **DELETE** /rest-service/reviews-v1/{id}/reviewitems/{riId} |  |
| [**removeReviewItemRevisions**](DefaultApi.md#removeReviewItemRevisions) | **DELETE** /rest-service/reviews-v1/{id}/reviewitems/{riId}/revisions |  |
| [**removeReviewer**](DefaultApi.md#removeReviewer) | **DELETE** /rest-service/reviews-v1/{id}/reviewers/{username} |  |
| [**setReviewItem**](DefaultApi.md#setReviewItem) | **PUT** /rest-service/reviews-v1/{id}/reviewitems/{riId}/details |  |
| [**uncompleteReview**](DefaultApi.md#uncompleteReview) | **POST** /rest-service/reviews-v1/{id}/uncomplete |  |
| [**updateComment**](DefaultApi.md#updateComment) | **POST** /rest-service/reviews-v1/{id}/comments/{cId} |  |
| [**updateReply**](DefaultApi.md#updateReply) | **POST** /rest-service/reviews-v1/{id}/comments/{cId}/replies/{rId} |  |


<a id="addChangesetToReview"></a>
# **addChangesetToReview**
> addChangesetToReview(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the perm id of the review to add the changeset to
    try {
      apiInstance.addChangesetToReview(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addChangesetToReview");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the perm id of the review to add the changeset to | |

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
| **200** | Successful Response |  -  |

<a id="addFile"></a>
# **addFile**
> addFile(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review perma id to add the file
    try {
      apiInstance.addFile(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addFile");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review perma id to add the file | |

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
| **200** | Successful Response |  -  |

<a id="addFisheyeReviewItem"></a>
# **addFisheyeReviewItem**
> addFisheyeReviewItem(id)



Add the changes between two files in a fisheye repository to the review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the id of the review (e.g. \"CR-362\").
    try {
      apiInstance.addFisheyeReviewItem(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addFisheyeReviewItem");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the review (e.g. \&quot;CR-362\&quot;). | |

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
| **200** | Successful Response |  -  |

<a id="addGeneralComment"></a>
# **addGeneralComment**
> addGeneralComment(id)



Add a general comment to the review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review perma-id
    try {
      apiInstance.addGeneralComment(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addGeneralComment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review perma-id | |

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
| **200** | Successful Response |  -  |

<a id="addPatchReview0"></a>
# **addPatchReview0**
> addPatchReview0(id)



Old, non-restful name. Kept for backwards compatibility. Exactly the same as POSTing to /{id}/patch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.addPatchReview0(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addPatchReview0");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**|  | |

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
| **200** | Successful Response |  -  |

<a id="addPatchToReview"></a>
# **addPatchToReview**
> addPatchToReview(id)



Add the revisions in a patch to an existing review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review id to get the patches for
    try {
      apiInstance.addPatchToReview(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addPatchToReview");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review id to get the patches for | |

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
| **200** | Successful Response |  -  |

<a id="addReply"></a>
# **addReply**
> addReply(id, cId)



Adds a reply to the given comment. This call includes the  repsonse header that  contains the URL of the newly created entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review perma-id (e.g. \"CR-45\").
    String cId = "cId_example"; // String | the comment to reply to
    try {
      apiInstance.addReply(id, cId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addReply");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review perma-id (e.g. \&quot;CR-45\&quot;). | |
| **cId** | **String**| the comment to reply to | |

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
| **200** | Successful Response |  -  |

<a id="addReviewItem"></a>
# **addReviewItem**
> addReviewItem(id)



Adds the given review item to the review. This will always create a new review item, even if there is an existing  one with the same data in the review (in which case the existing item will be replaced).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the id of the review (e.g. \"CR-362\").
    try {
      apiInstance.addReviewItem(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addReviewItem");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the review (e.g. \&quot;CR-362\&quot;). | |

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
| **200** | Successful Response |  -  |

<a id="addReviewItemRevisions"></a>
# **addReviewItemRevisions**
> addReviewItemRevisions(riId, id, rev)



Adds the given list of revisions to the supplied review item, merging if required. For example, if the review  item for  contains revisions 3 to 6, and if:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String riId = "riId_example"; // String | the id of the review item (e.g. \"CFR-5622\").
    String id = "id_example"; // String | the id of the review (e.g. \"CR-345\").
    String rev = "rev_example"; // String | a list of revisions to add to the review item, merging if required. If a revision already exists  in the given review item, then the given revision is ignored.
    try {
      apiInstance.addReviewItemRevisions(riId, id, rev);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addReviewItemRevisions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **riId** | **String**| the id of the review item (e.g. \&quot;CFR-5622\&quot;). | |
| **id** | **String**| the id of the review (e.g. \&quot;CR-345\&quot;). | |
| **rev** | **String**| a list of revisions to add to the review item, merging if required. If a revision already exists  in the given review item, then the given revision is ignored. | [optional] |

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
| **200** | Successful Response |  -  |

<a id="addReviewItems"></a>
# **addReviewItems**
> addReviewItems(id)



Adds a review item for each of the supplied crucibleRevisionData elements.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the id of the review (e.g. \"CR-362\").
    try {
      apiInstance.addReviewItems(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addReviewItems");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the review (e.g. \&quot;CR-362\&quot;). | |

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
| **200** | Successful Response |  -  |

<a id="addReviewers"></a>
# **addReviewers**
> addReviewers(id)



Adds the given list of reviewers to the review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the id of the review to add to
    try {
      apiInstance.addReviewers(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addReviewers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the review to add to | |

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
| **200** | Successful Response |  -  |

<a id="addVersionedComment"></a>
# **addVersionedComment**
> addVersionedComment(riId, id)



This call includes the  repsonse header that contains the URL of the newly created entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String riId = "riId_example"; // String | the review item id.
    String id = "id_example"; // String | the review perma id
    try {
      apiInstance.addVersionedComment(riId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addVersionedComment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **riId** | **String**| the review item id. | |
| **id** | **String**| the review perma id | |

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
| **200** | Successful Response |  -  |

<a id="browse"></a>
# **browse**
> browse(path, repository)



Lists the contents of the specified directory.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String path = "path_example"; // String | path to a directory. When path represents a file name, the result is unspecified.
    String repository = "repository_example"; // String | the key of the Crucible SCM plugin repository.
    try {
      apiInstance.browse(path, repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#browse");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **path** | **String**| path to a directory. When path represents a file name, the result is unspecified. | |
| **repository** | **String**| the key of the Crucible SCM plugin repository. | |

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
| **200** | Successful Response |  -  |

<a id="change"></a>
# **change**
> change(repository, revision)



Represents a particular changeset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the Crucible SCM plugin repository.
    String revision = "revision_example"; // String | the SCM revision string.
    try {
      apiInstance.change(repository, revision);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#change");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **repository** | **String**| the key of the Crucible SCM plugin repository. | |
| **revision** | **String**| the SCM revision string. | |

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
| **200** | Successful Response |  -  |

<a id="changeState"></a>
# **changeState**
> changeState(id, action, ignoreWarnings)



Change the state of a review by performing an action on it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review perma-id (e.g. \"CR-45\").
    String action = "action_example"; // String | the string representation of the action to perform. Valid actions are:    Note:
    Boolean ignoreWarnings = true; // Boolean | if  then condition failure warnings will be ignored
    try {
      apiInstance.changeState(id, action, ignoreWarnings);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#changeState");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review perma-id (e.g. \&quot;CR-45\&quot;). | |
| **action** | **String**| the string representation of the action to perform. Valid actions are:    Note: | [optional] |
| **ignoreWarnings** | **Boolean**| if  then condition failure warnings will be ignored | [optional] [default to true] |

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
| **200** | Successful Response |  -  |

<a id="changes"></a>
# **changes**
> changes(path, repository, oldestCsid, includeOldest, newestCsid, includeNewest, max)



Represents a sorted list of changesets, newest first.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String path = "path_example"; // String | only show change sets which contain at least one revision with a path under this path.  Changesets with some revisions outside this path still include all revisions.  i.e. Revisions outside the path are *not* excluded from the change set.
    String repository = "repository_example"; // String | the key of the Crucible SCM plugin repository.
    String oldestCsid = "oldestCsid_example"; // String | only return change sets after this change set. If omitted there is no restriction.
    Boolean includeOldest = true; // Boolean | include the change set with id \"from\" in the change sets returned.
    String newestCsid = "newestCsid_example"; // String | only return change sets before this change set. If omitted there is no restriction.
    Boolean includeNewest = true; // Boolean | include the change set with id \"to\" in the change sets returned.
    Integer max = 56; // Integer | return only the newest change sets, to a maximum of maxChangesets.
    try {
      apiInstance.changes(path, repository, oldestCsid, includeOldest, newestCsid, includeNewest, max);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#changes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **path** | **String**| only show change sets which contain at least one revision with a path under this path.  Changesets with some revisions outside this path still include all revisions.  i.e. Revisions outside the path are *not* excluded from the change set. | |
| **repository** | **String**| the key of the Crucible SCM plugin repository. | |
| **oldestCsid** | **String**| only return change sets after this change set. If omitted there is no restriction. | [optional] |
| **includeOldest** | **Boolean**| include the change set with id \&quot;from\&quot; in the change sets returned. | [optional] |
| **newestCsid** | **String**| only return change sets before this change set. If omitted there is no restriction. | [optional] |
| **includeNewest** | **Boolean**| include the change set with id \&quot;to\&quot; in the change sets returned. | [optional] |
| **max** | **Integer**| return only the newest change sets, to a maximum of maxChangesets. | [optional] |

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
| **200** | Successful Response |  -  |

<a id="closeReviewWithComment"></a>
# **closeReviewWithComment**
> closeReviewWithComment(id)



Closes the given review with the summary given.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review perma id to close. it should be in the open state.
    try {
      apiInstance.closeReviewWithComment(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#closeReviewWithComment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review perma id to close. it should be in the open state. | |

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
| **200** | Successful Response |  -  |

<a id="completeReview"></a>
# **completeReview**
> completeReview(id, ignoreWarnings)



Completes the review for the current user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review perma id
    Boolean ignoreWarnings = true; // Boolean | if {@code ignoreWarnings==true} then condition failure warnings will be ignored
    try {
      apiInstance.completeReview(id, ignoreWarnings);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#completeReview");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review perma id | |
| **ignoreWarnings** | **Boolean**| if {@code ignoreWarnings&#x3D;&#x3D;true} then condition failure warnings will be ignored | [optional] [default to true] |

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
| **200** | Successful Response |  -  |

<a id="createReview"></a>
# **createReview**
> createReview()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.createReview();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#createReview");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **200** | Successful Response |  -  |

<a id="deleteReview"></a>
# **deleteReview**
> deleteReview(id)



Permanently deletes the specified review.  The review must have been abandoned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the permId of the review to delete (e.g. \"CR-45\").
    try {
      apiInstance.deleteReview(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteReview");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the permId of the review to delete (e.g. \&quot;CR-45\&quot;). | |

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
| **200** | Successful Response |  -  |

<a id="details"></a>
# **details**
> details(path, repository, revision)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String path = "path_example"; // String | the path of a file or versioned directory (note that  versioned directories are not supported by all SCM plugins).
    String repository = "repository_example"; // String | the key of the Crucible SCM plugin repository.
    String revision = "revision_example"; // String | the SCM revision string.
    try {
      apiInstance.details(path, repository, revision);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#details");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **path** | **String**| the path of a file or versioned directory (note that  versioned directories are not supported by all SCM plugins). | |
| **repository** | **String**| the key of the Crucible SCM plugin repository. | |
| **revision** | **String**| the SCM revision string. | |

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
| **200** | Successful Response |  -  |

<a id="getAllComments"></a>
# **getAllComments**
> getAllComments(id, render)



Return all the comments visible to the requesting user for the review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review perma-id
    Boolean render = false; // Boolean | indicate whether to render the wiki text in the returned comments. If set to \"true\", the comments will contain a  <messageAsHtml> element containing the wiki rendered html.
    try {
      apiInstance.getAllComments(id, render);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAllComments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review perma-id | |
| **render** | **Boolean**| indicate whether to render the wiki text in the returned comments. If set to \&quot;true\&quot;, the comments will contain a  &lt;messageAsHtml&gt; element containing the wiki rendered html. | [optional] [default to false] |

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
| **200** | Successful Response |  -  |

<a id="getAllDetailedReviews"></a>
# **getAllDetailedReviews**
> getAllDetailedReviews(state)



Retrieves all reviews that are in one of the the specified states. For each review all details are included (review items + comments). The  wiki rendered comments will be available via the &lt;messageAsHtml&gt; element

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String state = "state_example"; // String | the review states to match.
    try {
      apiInstance.getAllDetailedReviews(state);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAllDetailedReviews");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **state** | **String**| the review states to match. | [optional] |

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
| **200** | Successful Response |  -  |

<a id="getAllProjects"></a>
# **getAllProjects**
> getAllProjects(excludeAllowedReviewers)



Get the list of projects that the authenticated user is entitled to access.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Boolean excludeAllowedReviewers = false; // Boolean | if set to true, user data (e.g. allowedReviewers) which is expensive  to compute, will not be included in the response data. Defaults to false so allowedReviewers are included in the response.
    try {
      apiInstance.getAllProjects(excludeAllowedReviewers);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAllProjects");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **excludeAllowedReviewers** | **Boolean**| if set to true, user data (e.g. allowedReviewers) which is expensive  to compute, will not be included in the response data. Defaults to false so allowedReviewers are included in the response. | [optional] [default to false] |

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
| **200** | Successful Response |  -  |

<a id="getAllRepositories"></a>
# **getAllRepositories**
> getAllRepositories(name, enabled, available, type, limit)



Returns a list of all repositories. This includes plugin provided repositories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | filter repositories by the repository key, only repositories of keys containing this value  would be returned if value was provided.  Case insensitive.
    Boolean enabled = true; // Boolean | filter repositories by enabled flag.  Only enabled/disabled repositories would be returned  accordingly if value was provided.
    Boolean available = true; // Boolean | filter repositories by its availability.  Only available/unavailable repositories would be returned  accordingly if value was provided.
    String type = "type_example"; // String | filter repositories by type.  Allowed values: cvs, svn, p4, git, hg, plugin (for light SCM repositories).  Parameter can be specified more than once.
    Integer limit = 10000; // Integer | maximum number of repositories to be returned.
    try {
      apiInstance.getAllRepositories(name, enabled, available, type, limit);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAllRepositories");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| filter repositories by the repository key, only repositories of keys containing this value  would be returned if value was provided.  Case insensitive. | [optional] |
| **enabled** | **Boolean**| filter repositories by enabled flag.  Only enabled/disabled repositories would be returned  accordingly if value was provided. | [optional] |
| **available** | **Boolean**| filter repositories by its availability.  Only available/unavailable repositories would be returned  accordingly if value was provided. | [optional] |
| **type** | **String**| filter repositories by type.  Allowed values: cvs, svn, p4, git, hg, plugin (for light SCM repositories).  Parameter can be specified more than once. | [optional] |
| **limit** | **Integer**| maximum number of repositories to be returned. | [optional] [default to 10000] |

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
| **200** | Successful Response |  -  |

<a id="getAllReviews"></a>
# **getAllReviews**
> getAllReviews(state)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String state = "state_example"; // String | only return reviews that are in these states.
    try {
      apiInstance.getAllReviews(state);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAllReviews");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **state** | **String**| only return reviews that are in these states. | [optional] |

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
| **200** | Successful Response |  -  |

<a id="getAvailableActions"></a>
# **getAvailableActions**
> getAvailableActions(id)



Get a list of the actions which the current user is allowed to perform  on the review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the permId of the a review (e.g. \"CR-45\").
    try {
      apiInstance.getAvailableActions(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAvailableActions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the permId of the a review (e.g. \&quot;CR-45\&quot;). | |

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
| **200** | Successful Response |  -  |

<a id="getAvailableTransitions"></a>
# **getAvailableTransitions**
> getAvailableTransitions(id)



Get a list of the actions which the current user can perform on this  review, given its current state and the user&#39;s permissions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the permId of the a review (e.g. \"CR-45\").
    try {
      apiInstance.getAvailableTransitions(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAvailableTransitions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the permId of the a review (e.g. \&quot;CR-45\&quot;). | |

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
| **200** | Successful Response |  -  |

<a id="getComment"></a>
# **getComment**
> getComment(id, cId, render)



Gets the given comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the perma id of the review
    String cId = "cId_example"; // String | the id of the comment
    Boolean render = false; // Boolean | true if the wiki text should be rendered into html, into the field <messageAsHtml>.
    try {
      apiInstance.getComment(id, cId, render);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getComment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the perma id of the review | |
| **cId** | **String**| the id of the comment | |
| **render** | **Boolean**| true if the wiki text should be rendered into html, into the field &lt;messageAsHtml&gt;. | [optional] [default to false] |

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
| **200** | Successful Response |  -  |

<a id="getCompletedReviewers"></a>
# **getCompletedReviewers**
> getCompletedReviewers(id)



Gets a list of completed reviewers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review perma id to retrieve reviewers
    try {
      apiInstance.getCompletedReviewers(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getCompletedReviewers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review perma id to retrieve reviewers | |

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
| **200** | Successful Response |  -  |

<a id="getContents"></a>
# **getContents**
> getContents(path, repository, revision)



Returns the raw content of the specified file revision as a binary  stream. No attempt is made to identify the content type and no mime  type is provided.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String path = "path_example"; // String | the path of a file.
    String repository = "repository_example"; // String | the key of the Crucible SCM plugin repository.
    String revision = "revision_example"; // String | the SCM revision string.
    try {
      apiInstance.getContents(path, repository, revision);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getContents");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **path** | **String**| the path of a file. | |
| **repository** | **String**| the key of the Crucible SCM plugin repository. | |
| **revision** | **String**| the SCM revision string. | |

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
| **200** | Successful Response |  -  |

<a id="getCustomFilterReviews"></a>
# **getCustomFilterReviews**
> getCustomFilterReviews(title, author, moderator, creator, states, reviewer, orRoles, complete, allReviewersComplete, project, fromDate, toDate)



To ignore a property, omit it from the query string.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String title = "title_example"; // String | a string that will be searched for in review titles.
    String author = "author_example"; // String | reviews authored by this user.
    String moderator = "moderator_example"; // String | reviews moderated by this user.
    String creator = "creator_example"; // String | reviews created by this user.
    String states = "states_example"; // String | comma-separated list of amy of the following strings: (Draft,  Approval, Review, Summarize, Closed, Dead, Rejected, Unknown).
    String reviewer = "reviewer_example"; // String | reviews reviewed by this user.
    Boolean orRoles = true; // Boolean | whether the value of , ,   and  should be OR'd  () or AND'd ()  together.
    Boolean complete = true; // Boolean | reviews that the specified reviewer has completed.
    Boolean allReviewersComplete = true; // Boolean | Reviews that all reviewers have completed.
    String project = "project_example"; // String | reviews for the specified project.
    Long fromDate = 56L; // Long | reviews with last activity date after the specified timestamp, in milliseconds. Inclusive.
    Long toDate = 56L; // Long | reviews with last activity date before the specified timestamp, in milliseconds. Inclusive.
    try {
      apiInstance.getCustomFilterReviews(title, author, moderator, creator, states, reviewer, orRoles, complete, allReviewersComplete, project, fromDate, toDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getCustomFilterReviews");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **title** | **String**| a string that will be searched for in review titles. | [optional] |
| **author** | **String**| reviews authored by this user. | [optional] |
| **moderator** | **String**| reviews moderated by this user. | [optional] |
| **creator** | **String**| reviews created by this user. | [optional] |
| **states** | **String**| comma-separated list of amy of the following strings: (Draft,  Approval, Review, Summarize, Closed, Dead, Rejected, Unknown). | [optional] |
| **reviewer** | **String**| reviews reviewed by this user. | [optional] |
| **orRoles** | **Boolean**| whether the value of , ,   and  should be OR&#39;d  () or AND&#39;d ()  together. | [optional] |
| **complete** | **Boolean**| reviews that the specified reviewer has completed. | [optional] |
| **allReviewersComplete** | **Boolean**| Reviews that all reviewers have completed. | [optional] |
| **project** | **String**| reviews for the specified project. | [optional] |
| **fromDate** | **Long**| reviews with last activity date after the specified timestamp, in milliseconds. Inclusive. | [optional] |
| **toDate** | **Long**| reviews with last activity date before the specified timestamp, in milliseconds. Inclusive. | [optional] |

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
| **200** | Successful Response |  -  |

<a id="getDetailedCustomFilterReviews"></a>
# **getDetailedCustomFilterReviews**
> getDetailedCustomFilterReviews(title, author, moderator, creator, states, reviewer, orRoles, complete, allReviewersComplete, project, fromDate, toDate)



To ignore a property, omit it from the query string.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String title = "title_example"; // String | a string that will be searched for in review titles.
    String author = "author_example"; // String | reviews authored by this user.
    String moderator = "moderator_example"; // String | reviews moderated by this user.
    String creator = "creator_example"; // String | reviews created by this user.
    String states = "states_example"; // String | comma-separated list of amy of the following strings: (Draft,  Approval, Review, Summarize, Closed, Dead, Rejected, Unknown).
    String reviewer = "reviewer_example"; // String | reviews reviewed by this user.
    Boolean orRoles = true; // Boolean | whether the value of , ,   and  should be OR'd  () or AND'd ()  together.
    Boolean complete = true; // Boolean | reviews that the specified reviewer has completed.
    Boolean allReviewersComplete = true; // Boolean | Reviews that all reviewers have completed.
    String project = "project_example"; // String | reviews for the specified project.
    Long fromDate = 56L; // Long | reviews with last activity date after the specified timestamp, in milliseconds. Inclusive.
    Long toDate = 56L; // Long | reviews with last activity date before the specified timestamp, in milliseconds. Inclusive.
    try {
      apiInstance.getDetailedCustomFilterReviews(title, author, moderator, creator, states, reviewer, orRoles, complete, allReviewersComplete, project, fromDate, toDate);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDetailedCustomFilterReviews");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **title** | **String**| a string that will be searched for in review titles. | [optional] |
| **author** | **String**| reviews authored by this user. | [optional] |
| **moderator** | **String**| reviews moderated by this user. | [optional] |
| **creator** | **String**| reviews created by this user. | [optional] |
| **states** | **String**| comma-separated list of amy of the following strings: (Draft,  Approval, Review, Summarize, Closed, Dead, Rejected, Unknown). | [optional] |
| **reviewer** | **String**| reviews reviewed by this user. | [optional] |
| **orRoles** | **Boolean**| whether the value of , ,   and  should be OR&#39;d  () or AND&#39;d ()  together. | [optional] |
| **complete** | **Boolean**| reviews that the specified reviewer has completed. | [optional] |
| **allReviewersComplete** | **Boolean**| Reviews that all reviewers have completed. | [optional] |
| **project** | **String**| reviews for the specified project. | [optional] |
| **fromDate** | **Long**| reviews with last activity date after the specified timestamp, in milliseconds. Inclusive. | [optional] |
| **toDate** | **Long**| reviews with last activity date before the specified timestamp, in milliseconds. Inclusive. | [optional] |

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
| **200** | Successful Response |  -  |

<a id="getDetailedFilteredReviewsForUser"></a>
# **getDetailedFilteredReviewsForUser**
> getDetailedFilteredReviewsForUser(filter)



Gets a list of all the reviews that match the specified filter criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String filter = "filter_example"; // String | a predefined filter type.
    try {
      apiInstance.getDetailedFilteredReviewsForUser(filter);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDetailedFilteredReviewsForUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **filter** | **String**| a predefined filter type. | |

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
| **200** | Successful Response |  -  |

<a id="getDetailedReview"></a>
# **getDetailedReview**
> getDetailedReview(id)



Returns the specified review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the permId of the review (e.g. \"CR-45\").
    try {
      apiInstance.getDetailedReview(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getDetailedReview");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the permId of the review (e.g. \&quot;CR-45\&quot;). | |

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
| **200** | Successful Response |  -  |

<a id="getFilteredReviewsForUser"></a>
# **getFilteredReviewsForUser**
> getFilteredReviewsForUser(filter)



Get all the reviews which match the given filter, for the current user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String filter = "filter_example"; // String | a predefined filter type.
    try {
      apiInstance.getFilteredReviewsForUser(filter);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getFilteredReviewsForUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **filter** | **String**| a predefined filter type. | |

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
| **200** | Successful Response |  -  |

<a id="getGeneralComments"></a>
# **getGeneralComments**
> getGeneralComments(id, render)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | review perma-id
    Boolean render = false; // Boolean | indicate whether to render the wiki text in the returned comments. If set to \"true\", the comments will contain a  <messageAsHtml> element containing the wiki rendered html.
    try {
      apiInstance.getGeneralComments(id, render);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getGeneralComments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| review perma-id | |
| **render** | **Boolean**| indicate whether to render the wiki text in the returned comments. If set to \&quot;true\&quot;, the comments will contain a  &lt;messageAsHtml&gt; element containing the wiki rendered html. | [optional] [default to false] |

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
| **200** | Successful Response |  -  |

<a id="getMappedUser"></a>
# **getMappedUser**
> getMappedUser(repository, username)



Returns the user details of the user mapped to a committer in a repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository
    String username = "username_example"; // String | the name of the committer
    try {
      apiInstance.getMappedUser(repository, username);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMappedUser");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **repository** | **String**| the key of the repository | |
| **username** | **String**| the name of the committer | |

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
| **200** | Successful Response |  -  |

<a id="getMetrics"></a>
# **getMetrics**
> getMetrics(version)



Get comment metrics metadata for the specified metrics version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String version = "version_example"; // String | a metrics version.
    try {
      apiInstance.getMetrics(version);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getMetrics");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **version** | **String**| a metrics version. | |

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
| **200** | Successful Response |  -  |

<a id="getProject"></a>
# **getProject**
> getProject(key, excludeAllowedReviewers)



Returns a project description.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | the key of a Crucible project.
    Boolean excludeAllowedReviewers = false; // Boolean | 
    try {
      apiInstance.getProject(key, excludeAllowedReviewers);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getProject");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **key** | **String**| the key of a Crucible project. | |
| **excludeAllowedReviewers** | **Boolean**|  | [optional] [default to false] |

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
| **200** | Successful Response |  -  |

<a id="getReplies"></a>
# **getReplies**
> getReplies(id, cId, render)



Gets the replies to the given comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review perma-id (e.g. \"CR-45\").
    String cId = "cId_example"; // String | the comment to reply to
    Boolean render = false; // Boolean | true if the comments should also be rendered into html, into the element <messageAsHtml>
    try {
      apiInstance.getReplies(id, cId, render);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReplies");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review perma-id (e.g. \&quot;CR-45\&quot;). | |
| **cId** | **String**| the comment to reply to | |
| **render** | **Boolean**| true if the comments should also be rendered into html, into the element &lt;messageAsHtml&gt; | [optional] [default to false] |

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
| **200** | Successful Response |  -  |

<a id="getRepositoryDetails"></a>
# **getRepositoryDetails**
> getRepositoryDetails(repository)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the Crucible SCM plugin repository.
    try {
      apiInstance.getRepositoryDetails(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRepositoryDetails");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **repository** | **String**| the key of the Crucible SCM plugin repository. | |

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
| **200** | Successful Response |  -  |

<a id="getReview"></a>
# **getReview**
> getReview(id)



Get a single review by its permId (e.g. \&quot;CR-45\&quot;).  If the review does not exist, a 404 is returned.    The moderator element may not exist if the review does not have a Moderator.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the permId of the review to delete (e.g. \"CR-45\").
    try {
      apiInstance.getReview(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReview");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the permId of the review to delete (e.g. \&quot;CR-45\&quot;). | |

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
| **200** | Successful Response |  -  |

<a id="getReviewItem"></a>
# **getReviewItem**
> getReviewItem(riId, id)



Returns detailed information for a specific review item.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String riId = "riId_example"; // String | review item id (e.g. \"CFR-6312\").
    String id = "id_example"; // String | review id (e.g. \"CR-345\").
    try {
      apiInstance.getReviewItem(riId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReviewItem");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **riId** | **String**| review item id (e.g. \&quot;CFR-6312\&quot;). | |
| **id** | **String**| review id (e.g. \&quot;CR-345\&quot;). | |

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
| **200** | Successful Response |  -  |

<a id="getReviewItemsComments"></a>
# **getReviewItemsComments**
> getReviewItemsComments(riId, id, render)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String riId = "riId_example"; // String | the review item id.
    String id = "id_example"; // String | the review perma id
    Boolean render = false; // Boolean | indicate whether to render the wiki text in the returned comments. If set to \"true\", the comments will contain a  <messageAsHtml> element containing the wiki rendered html.
    try {
      apiInstance.getReviewItemsComments(riId, id, render);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReviewItemsComments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **riId** | **String**| the review item id. | |
| **id** | **String**| the review perma id | |
| **render** | **Boolean**| indicate whether to render the wiki text in the returned comments. If set to \&quot;true\&quot;, the comments will contain a  &lt;messageAsHtml&gt; element containing the wiki rendered html. | [optional] [default to false] |

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
| **200** | Successful Response |  -  |

<a id="getReviewItemsForReview"></a>
# **getReviewItemsForReview**
> getReviewItemsForReview(id)



Returns a list of all the items in a review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the id of the review (e.g. \"CR-362\").
    try {
      apiInstance.getReviewItemsForReview(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReviewItemsForReview");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the review (e.g. \&quot;CR-362\&quot;). | |

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
| **200** | Successful Response |  -  |

<a id="getReviewPatches"></a>
# **getReviewPatches**
> getReviewPatches(id)



Get a list of patches and their details for the given review

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review id to get the patches for
    try {
      apiInstance.getReviewPatches(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReviewPatches");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review id to get the patches for | |

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
| **200** | Successful Response |  -  |

<a id="getReviewers"></a>
# **getReviewers**
> getReviewers(id)



Get a list of reviewers in the review given by the permaid id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the id of the review to add to
    try {
      apiInstance.getReviewers(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReviewers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the review to add to | |

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
| **200** | Successful Response |  -  |

<a id="getReviewsDetailsForPath"></a>
# **getReviewsDetailsForPath**
> getReviewsDetailsForPath(repository, path)



Return a list of Reviews which include a particular file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to search for file.
    String path = "path_example"; // String | path to find in reviews.
    try {
      apiInstance.getReviewsDetailsForPath(repository, path);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReviewsDetailsForPath");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **repository** | **String**| the key of the repository to search for file. | |
| **path** | **String**| path to find in reviews. | [optional] |

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
| **200** | Successful Response |  -  |

<a id="getReviewsForIssueKey"></a>
# **getReviewsForIssueKey**
> getReviewsForIssueKey(jiraKey, maxReturn)



Get a list of all reviews that have been linked to the specified JIRA issue key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String jiraKey = "jiraKey_example"; // String | a Jira issue key (e.g. \"FOO-3453\")
    String maxReturn = "maxReturn_example"; // String | the maximum number of reviews to return.
    try {
      apiInstance.getReviewsForIssueKey(jiraKey, maxReturn);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReviewsForIssueKey");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **jiraKey** | **String**| a Jira issue key (e.g. \&quot;FOO-3453\&quot;) | [optional] |
| **maxReturn** | **String**| the maximum number of reviews to return. | [optional] |

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
| **200** | Successful Response |  -  |

<a id="getReviewsForPath"></a>
# **getReviewsForPath**
> getReviewsForPath(repository, path)



Return a list of Reviews which include a particular file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to search for file
    String path = "path_example"; // String | path to find in reviews
    try {
      apiInstance.getReviewsForPath(repository, path);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReviewsForPath");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **repository** | **String**| the key of the repository to search for file | |
| **path** | **String**| path to find in reviews | [optional] |

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
| **200** | Successful Response |  -  |

<a id="getReviewsForTerm"></a>
# **getReviewsForTerm**
> getReviewsForTerm(term, maxReturn)



Search for reviews where the name, description, state or permaId contain the specified term.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String term = "term_example"; // String | a search term.
    String maxReturn = "maxReturn_example"; // String | the maximum number of reviews to return.
    try {
      apiInstance.getReviewsForTerm(term, maxReturn);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getReviewsForTerm");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **term** | **String**| a search term. | [optional] |
| **maxReturn** | **String**| the maximum number of reviews to return. | [optional] |

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
| **200** | Successful Response |  -  |

<a id="getSvnRepositoryDetails"></a>
# **getSvnRepositoryDetails**
> getSvnRepositoryDetails(repository)



For backward compatibility we provide this method, but repositories should be referred to just by their key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of a FishEye or Crucible SCM plugin repository
    try {
      apiInstance.getSvnRepositoryDetails(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSvnRepositoryDetails");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **repository** | **String**| the key of a FishEye or Crucible SCM plugin repository | |

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
| **200** | Successful Response |  -  |

<a id="getUncompletedReviewers"></a>
# **getUncompletedReviewers**
> getUncompletedReviewers(id)



Gets a list of reviewers that have not completed the review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review perma id to retrieve reviewers
    try {
      apiInstance.getUncompletedReviewers(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getUncompletedReviewers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review perma id to retrieve reviewers | |

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
| **200** | Successful Response |  -  |

<a id="getUserProfile"></a>
# **getUserProfile**
> getUserProfile(username)



Returns the user&#39;s profile details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | the username of the user
    try {
      apiInstance.getUserProfile(username);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getUserProfile");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**| the username of the user | |

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
| **200** | Successful Response |  -  |

<a id="getUsers"></a>
# **getUsers**
> getUsers(username)



Get a list of all the users. You can also ask for a set of users.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String username = "username_example"; // String | a username (or a few) to limit the number of returned entries. It will return only existing users.
    try {
      apiInstance.getUsers(username);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getUsers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **username** | **String**| a username (or a few) to limit the number of returned entries. It will return only existing users. | [optional] |

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
| **200** | Successful Response |  -  |

<a id="getVersionInfo"></a>
# **getVersionInfo**
> getVersionInfo()



Returns Crucible version information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getVersionInfo();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getVersionInfo");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **200** | Successful Response |  -  |

<a id="getVersionedComments"></a>
# **getVersionedComments**
> getVersionedComments(id, render)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | review perma-id
    Boolean render = false; // Boolean | indicate whether to render the wiki text in the returned comments. If set to \"true\", the comments will contain a  <messageAsHtml> element containing the wiki rendered html.
    try {
      apiInstance.getVersionedComments(id, render);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getVersionedComments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| review perma-id | |
| **render** | **Boolean**| indicate whether to render the wiki text in the returned comments. If set to \&quot;true\&quot;, the comments will contain a  &lt;messageAsHtml&gt; element containing the wiki rendered html. | [optional] [default to false] |

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
| **200** | Successful Response |  -  |

<a id="history"></a>
# **history**
> history(path, repository, revision)



Represents the history of a versioned entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String path = "path_example"; // String | the path of a file or versioned directory (note that  versioned directories are not supported by all SCM plugins).
    String repository = "repository_example"; // String | the key of the Crucible SCM plugin repository.
    String revision = "revision_example"; // String | the SCM revision string.
    try {
      apiInstance.history(path, repository, revision);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#history");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **path** | **String**| the path of a file or versioned directory (note that  versioned directories are not supported by all SCM plugins). | |
| **repository** | **String**| the key of the Crucible SCM plugin repository. | |
| **revision** | **String**| the SCM revision string. | |

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
| **200** | Successful Response |  -  |

<a id="login"></a>
# **login**
> login(userName, password)



Get the user authentication token.    This is a legacy version of the login request. Using GET is deprecated as your password is likely to appear in logs which record request URLs.  Use the POST version instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String userName = "userName_example"; // String | the username of the user to get the token for
    String password = "password_example"; // String | the password for the user to get the token for
    try {
      apiInstance.login(userName, password);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#login");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **userName** | **String**| the username of the user to get the token for | [optional] |
| **password** | **String**| the password for the user to get the token for | [optional] |

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
| **200** | Successful Response |  -  |

<a id="loginPost"></a>
# **loginPost**
> loginPost()



Get the user authentication token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.loginPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#loginPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **200** | Successful Response |  -  |

<a id="markAllCommentsAsRead"></a>
# **markAllCommentsAsRead**
> markAllCommentsAsRead(id)



For the effective user, mark all comments in a review as read (except  those marked as leave unread).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review perma-id (e.g. \"CR-45\").
    try {
      apiInstance.markAllCommentsAsRead(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#markAllCommentsAsRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review perma-id (e.g. \&quot;CR-45\&quot;). | |

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
| **200** | Successful Response |  -  |

<a id="markCommentAsLeaveUnread"></a>
# **markCommentAsLeaveUnread**
> markCommentAsLeaveUnread(id, cId)



Marks the comment as leave unread to the current user - it will not automatically be marked as read by crucible.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review perma id for the comment
    String cId = "cId_example"; // String | the comment perma id
    try {
      apiInstance.markCommentAsLeaveUnread(id, cId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#markCommentAsLeaveUnread");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review perma id for the comment | |
| **cId** | **String**| the comment perma id | |

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
| **200** | Successful Response |  -  |

<a id="markCommentAsRead"></a>
# **markCommentAsRead**
> markCommentAsRead(id, cId)



Mark the given comment as read for the user used to make this POST.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review perma id
    String cId = "cId_example"; // String | the comment perma id.
    try {
      apiInstance.markCommentAsRead(id, cId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#markCommentAsRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review perma id | |
| **cId** | **String**| the comment perma id. | |

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
| **200** | Successful Response |  -  |

<a id="postCustomFilterReviews"></a>
# **postCustomFilterReviews**
> postCustomFilterReviews()



This method should no longer be used, as it uses a POST for a read-only  retrieval operation and is provided for backward compatibility only.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.postCustomFilterReviews();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#postCustomFilterReviews");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **200** | Successful Response |  -  |

<a id="postDetailedCustomFilterReviews"></a>
# **postDetailedCustomFilterReviews**
> postDetailedCustomFilterReviews()



This method should no longer be used, as it uses a POST for a read-only  retrieval operation and is provided for backward compatibility only.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.postDetailedCustomFilterReviews();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#postDetailedCustomFilterReviews");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **200** | Successful Response |  -  |

<a id="publishAllComments"></a>
# **publishAllComments**
> publishAllComments(id)



Publishes all the draft comments of the current user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review perma id to look for draft comments
    try {
      apiInstance.publishAllComments(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#publishAllComments");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review perma id to look for draft comments | |

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
| **200** | Successful Response |  -  |

<a id="publishComment"></a>
# **publishComment**
> publishComment(id, cId)



publishes the given draft comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review perma id
    String cId = "cId_example"; // String | the comment perma id
    try {
      apiInstance.publishComment(id, cId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#publishComment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review perma id | |
| **cId** | **String**| the comment perma id | |

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
| **200** | Successful Response |  -  |

<a id="remindIncompleteReviewers"></a>
# **remindIncompleteReviewers**
> remindIncompleteReviewers(id)



Immediately send a reminder to incomplete reviewers about the given review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review perma id to remind about. it should be in the open state.
    try {
      apiInstance.remindIncompleteReviewers(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#remindIncompleteReviewers");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review perma id to remind about. it should be in the open state. | |

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
| **200** | Successful Response |  -  |

<a id="removeComment"></a>
# **removeComment**
> removeComment(id, cId)



Deletes the given comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the perma id of the review
    String cId = "cId_example"; // String | the id of the comment
    try {
      apiInstance.removeComment(id, cId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeComment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the perma id of the review | |
| **cId** | **String**| the id of the comment | |

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
| **200** | Successful Response |  -  |

<a id="removePatch"></a>
# **removePatch**
> removePatch(patchId, id)



Removes the patch with the given id from the review. All of the revisions provided by the patch will be removed as well.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer patchId = 56; // Integer | the id of the patch (as returned by the '{id}/patch' resource)
    String id = "id_example"; // String | the permaId of the review
    try {
      apiInstance.removePatch(patchId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removePatch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **patchId** | **Integer**| the id of the patch (as returned by the &#39;{id}/patch&#39; resource) | |
| **id** | **String**| the permaId of the review | |

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
| **200** | Successful Response |  -  |

<a id="removeReply"></a>
# **removeReply**
> removeReply(id, rId, cId)



Deletes the reply.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The review perma id
    String rId = "rId_example"; // String | the perma id of the reply to delete
    String cId = "cId_example"; // String | the reply's parent comment perma id
    try {
      apiInstance.removeReply(id, rId, cId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeReply");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The review perma id | |
| **rId** | **String**| the perma id of the reply to delete | |
| **cId** | **String**| the reply&#39;s parent comment perma id | |

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
| **200** | Successful Response |  -  |

<a id="removeReviewItem"></a>
# **removeReviewItem**
> removeReviewItem(riId, id)



Removes an item from a review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String riId = "riId_example"; // String | review item id (e.g. \"CFR-6312\").
    String id = "id_example"; // String | review id (e.g. \"CR-345\").
    try {
      apiInstance.removeReviewItem(riId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeReviewItem");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **riId** | **String**| review item id (e.g. \&quot;CFR-6312\&quot;). | |
| **id** | **String**| review id (e.g. \&quot;CR-345\&quot;). | |

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
| **200** | Successful Response |  -  |

<a id="removeReviewItemRevisions"></a>
# **removeReviewItemRevisions**
> removeReviewItemRevisions(riId, id, rev)



Removes the revisions given from the review item in the review specified by the id. If the review item has no  more revisions left, it is automatically deleted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String riId = "riId_example"; // String | the id of the review item (e.g. \"CFR-5622\").
    String id = "id_example"; // String | the id of the review (e.g. \"CR-345\").
    String rev = "rev_example"; // String | a list of revisions to add to the review item, merging if required. If a revision already exists  in the given review item, then the given revision is ignored.
    try {
      apiInstance.removeReviewItemRevisions(riId, id, rev);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeReviewItemRevisions");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **riId** | **String**| the id of the review item (e.g. \&quot;CFR-5622\&quot;). | |
| **id** | **String**| the id of the review (e.g. \&quot;CR-345\&quot;). | |
| **rev** | **String**| a list of revisions to add to the review item, merging if required. If a revision already exists  in the given review item, then the given revision is ignored. | [optional] |

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
| **200** | Successful Response |  -  |

<a id="removeReviewer"></a>
# **removeReviewer**
> removeReviewer(id, username)



Removes the reviewer from the review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the perma id of the review
    String username = "username_example"; // String | the name of the reviewer.
    try {
      apiInstance.removeReviewer(id, username);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeReviewer");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the perma id of the review | |
| **username** | **String**| the name of the reviewer. | |

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
| **200** | Successful Response |  -  |

<a id="setReviewItem"></a>
# **setReviewItem**
> setReviewItem(riId, id)



Sets the review item specified by itemId with the given reviewItem. The old review item is discarded. Can only  perform this operation if the old review item specified by itemId can be deleted. The old review item&#39;s permId is  not changed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String riId = "riId_example"; // String | a valid review item id (e.g. \"CFR-5622\").
    String id = "id_example"; // String | a valid review id (e.g. \"CR-345\").
    try {
      apiInstance.setReviewItem(riId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#setReviewItem");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **riId** | **String**| a valid review item id (e.g. \&quot;CFR-5622\&quot;). | |
| **id** | **String**| a valid review id (e.g. \&quot;CR-345\&quot;). | |

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
| **200** | Successful Response |  -  |

<a id="uncompleteReview"></a>
# **uncompleteReview**
> uncompleteReview(id, ignoreWarnings)



Uncompletes the review for the current user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the review perma id
    Boolean ignoreWarnings = true; // Boolean | if {@code ignoreWarnings==true} then condition failure warnings will be ignored
    try {
      apiInstance.uncompleteReview(id, ignoreWarnings);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#uncompleteReview");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the review perma id | |
| **ignoreWarnings** | **Boolean**| if {@code ignoreWarnings&#x3D;&#x3D;true} then condition failure warnings will be ignored | [optional] [default to true] |

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
| **200** | Successful Response |  -  |

<a id="updateComment"></a>
# **updateComment**
> updateComment(id, cId)



Updates the comment given by the perma id to the new comment posted.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | the perma id of the review
    String cId = "cId_example"; // String | the id of the comment
    try {
      apiInstance.updateComment(id, cId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateComment");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the perma id of the review | |
| **cId** | **String**| the id of the comment | |

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
| **200** | Successful Response |  -  |

<a id="updateReply"></a>
# **updateReply**
> updateReply(id, rId, cId)



Updates a reply with the given newComment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://crucible.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | The review perma id
    String rId = "rId_example"; // String | the perma id of the reply to delete
    String cId = "cId_example"; // String | the reply's parent comment perma id
    try {
      apiInstance.updateReply(id, rId, cId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateReply");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| The review perma id | |
| **rId** | **String**| the perma id of the reply to delete | |
| **cId** | **String**| the reply&#39;s parent comment perma id | |

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
| **200** | Successful Response |  -  |

