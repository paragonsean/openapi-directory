# CommentsApi

All URIs are relative to *https://dev.to/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCommentById**](CommentsApi.md#getCommentById) | **GET** /api/comments/{id} | Comment by id |
| [**getCommentsByArticleId**](CommentsApi.md#getCommentsByArticleId) | **GET** /api/comments | Comments |


<a id="getCommentById"></a>
# **getCommentById**
> getCommentById(id)

Comment by id

This endpoint allows the client to retrieve a comment as well as his descendants comments.    It will return the required comment (the root) with its nested descendants as a thread.    See the format specification for further details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");

    CommentsApi apiInstance = new CommentsApi(defaultClient);
    Integer id = 321; // Integer | Comment identifier.
    try {
      apiInstance.getCommentById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentsApi#getCommentById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Comment identifier. | |

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
| **200** | A List of the Comments |  -  |
| **404** | Comment Not Found |  -  |

<a id="getCommentsByArticleId"></a>
# **getCommentsByArticleId**
> List&lt;Comment&gt; getCommentsByArticleId(aId, pId)

Comments

This endpoint allows the client to retrieve all comments belonging to an article or podcast episode as threaded conversations.  It will return the all top level comments with their nested comments as threads. See the format specification for further details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");

    CommentsApi apiInstance = new CommentsApi(defaultClient);
    String aId = "321"; // String | Article identifier.
    String pId = "321"; // String | Podcast Episode identifier.
    try {
      List<Comment> result = apiInstance.getCommentsByArticleId(aId, pId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentsApi#getCommentsByArticleId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **aId** | **String**| Article identifier. | [optional] |
| **pId** | **String**| Podcast Episode identifier. | [optional] |

### Return type

[**List&lt;Comment&gt;**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of Comments |  -  |
| **404** | Resource Not Found |  -  |

