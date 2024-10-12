# CommentsApi

All URIs are relative to *https://api.test.osf.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**commentsDelete**](CommentsApi.md#commentsDelete) | **DELETE** /comments/{comment_id}/ | Delete a comment |
| [**commentsPut**](CommentsApi.md#commentsPut) | **PUT** /comments/{comment_id}/ | Update a comment |
| [**commentsRead**](CommentsApi.md#commentsRead) | **GET** /comments/{comment_id}/ | Retrieve a comment |


<a id="commentsDelete"></a>
# **commentsDelete**
> commentsDelete(commentId)

Delete a comment

Deletes a comment. This action can be undone by setting deleted to False in a comment update request. #### Returns If the request is successful, no content is returned.  If the request is unsuccessful, a JSON object with an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

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
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CommentsApi apiInstance = new CommentsApi(defaultClient);
    String commentId = "commentId_example"; // String | The unique identifier of the comment you wish to delete.
    try {
      apiInstance.commentsDelete(commentId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentsApi#commentsDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **commentId** | **String**| The unique identifier of the comment you wish to delete. | |

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
| **204** | No content |  -  |

<a id="commentsPut"></a>
# **commentsPut**
> commentsPut(commentId, body)

Update a comment

Updates the specified comment by setting the values of the parameters passed. Any parameters not provided will be left unchanged. #### Returns Returns JSON with a &#x60;data&#x60; key containing the new representation of the updated comment, if the request is successful.  If the request is unsuccessful, JSON with an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

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
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CommentsApi apiInstance = new CommentsApi(defaultClient);
    String commentId = "commentId_example"; // String | The unique identifier of the comment you wish to update.
    Object body = null; // Object | 
    try {
      apiInstance.commentsPut(commentId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentsApi#commentsPut");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **commentId** | **String**| The unique identifier of the comment you wish to update. | |
| **body** | **Object**|  | |

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
| **200** | OK |  -  |

<a id="commentsRead"></a>
# **commentsRead**
> Comment commentsRead(commentId)

Retrieve a comment

Retrieves the details of a comment #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested comment, if the request was successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

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
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    CommentsApi apiInstance = new CommentsApi(defaultClient);
    String commentId = "commentId_example"; // String | The unique identifier of the comment you wish to retrieve.
    try {
      Comment result = apiInstance.commentsRead(commentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentsApi#commentsRead");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **commentId** | **String**| The unique identifier of the comment you wish to retrieve. | |

### Return type

[**Comment**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

