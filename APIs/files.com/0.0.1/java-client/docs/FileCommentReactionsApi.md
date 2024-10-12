# FileCommentReactionsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteFileCommentReactionsId**](FileCommentReactionsApi.md#deleteFileCommentReactionsId) | **DELETE** /file_comment_reactions/{id} | Delete File Comment Reaction |
| [**postFileCommentReactions**](FileCommentReactionsApi.md#postFileCommentReactions) | **POST** /file_comment_reactions | Create File Comment Reaction |


<a id="deleteFileCommentReactionsId"></a>
# **deleteFileCommentReactionsId**
> deleteFileCommentReactionsId(id)

Delete File Comment Reaction

Delete File Comment Reaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileCommentReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    FileCommentReactionsApi apiInstance = new FileCommentReactionsApi(defaultClient);
    Integer id = 56; // Integer | File Comment Reaction ID.
    try {
      apiInstance.deleteFileCommentReactionsId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileCommentReactionsApi#deleteFileCommentReactionsId");
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
| **id** | **Integer**| File Comment Reaction ID. | |

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
| **204** | No body. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="postFileCommentReactions"></a>
# **postFileCommentReactions**
> FileCommentReactionEntity postFileCommentReactions(emoji, fileCommentId, userId)

Create File Comment Reaction

Create File Comment Reaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileCommentReactionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    FileCommentReactionsApi apiInstance = new FileCommentReactionsApi(defaultClient);
    String emoji = "emoji_example"; // String | Emoji to react with.
    Integer fileCommentId = 56; // Integer | ID of file comment to attach reaction to.
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    try {
      FileCommentReactionEntity result = apiInstance.postFileCommentReactions(emoji, fileCommentId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileCommentReactionsApi#postFileCommentReactions");
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
| **emoji** | **String**| Emoji to react with. | |
| **fileCommentId** | **Integer**| ID of file comment to attach reaction to. | |
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] |

### Return type

[**FileCommentReactionEntity**](FileCommentReactionEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The FileCommentReactions object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

