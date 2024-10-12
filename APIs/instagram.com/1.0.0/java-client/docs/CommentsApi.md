# CommentsApi

All URIs are relative to *https://api.instagram.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mediaMediaIdCommentsCommentIdDelete**](CommentsApi.md#mediaMediaIdCommentsCommentIdDelete) | **DELETE** /media/{media-id}/comments/{comment-id} | Remove a comment. |
| [**mediaMediaIdCommentsGet**](CommentsApi.md#mediaMediaIdCommentsGet) | **GET** /media/{media-id}/comments | Get a list of recent comments on a media object. |
| [**mediaMediaIdCommentsPost**](CommentsApi.md#mediaMediaIdCommentsPost) | **POST** /media/{media-id}/comments | Create a comment on a media object. |


<a id="mediaMediaIdCommentsCommentIdDelete"></a>
# **mediaMediaIdCommentsCommentIdDelete**
> StatusResponse mediaMediaIdCommentsCommentIdDelete(mediaId, commentId)

Remove a comment.

Remove a comment either on the authenticated user&#39;s media object or authored by the authenticated user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.instagram.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: instagram_auth
    OAuth instagram_auth = (OAuth) defaultClient.getAuthentication("instagram_auth");
    instagram_auth.setAccessToken("YOUR ACCESS TOKEN");

    CommentsApi apiInstance = new CommentsApi(defaultClient);
    String mediaId = "mediaId_example"; // String | The ID of the media resource.
    String commentId = "commentId_example"; // String | The ID of the comment entry.
    try {
      StatusResponse result = apiInstance.mediaMediaIdCommentsCommentIdDelete(mediaId, commentId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentsApi#mediaMediaIdCommentsCommentIdDelete");
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
| **mediaId** | **String**| The ID of the media resource. | |
| **commentId** | **String**| The ID of the comment entry. | |

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of deleting a comment. |  -  |

<a id="mediaMediaIdCommentsGet"></a>
# **mediaMediaIdCommentsGet**
> CommentsResponse mediaMediaIdCommentsGet(mediaId)

Get a list of recent comments on a media object.

Get a list of recent comments on a media object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.instagram.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: instagram_auth
    OAuth instagram_auth = (OAuth) defaultClient.getAuthentication("instagram_auth");
    instagram_auth.setAccessToken("YOUR ACCESS TOKEN");

    CommentsApi apiInstance = new CommentsApi(defaultClient);
    String mediaId = "mediaId_example"; // String | The ID of the media resource.
    try {
      CommentsResponse result = apiInstance.mediaMediaIdCommentsGet(mediaId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentsApi#mediaMediaIdCommentsGet");
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
| **mediaId** | **String**| The ID of the media resource. | |

### Return type

[**CommentsResponse**](CommentsResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of comments of the media resource. |  -  |

<a id="mediaMediaIdCommentsPost"></a>
# **mediaMediaIdCommentsPost**
> StatusResponse mediaMediaIdCommentsPost(mediaId, text)

Create a comment on a media object.

Create a comment on a media object with the following rules:    * The total length of the comment cannot exceed 300 characters.   * The comment cannot contain more than 4 hashtags.   * The comment cannot contain more than 1 URL.   * The comment cannot consist of all capital letters. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.instagram.com/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: instagram_auth
    OAuth instagram_auth = (OAuth) defaultClient.getAuthentication("instagram_auth");
    instagram_auth.setAccessToken("YOUR ACCESS TOKEN");

    CommentsApi apiInstance = new CommentsApi(defaultClient);
    String mediaId = "mediaId_example"; // String | The ID of the media resource.
    String text = "text_example"; // String | Text to post as a comment on the media object as specified in `media-id`.
    try {
      StatusResponse result = apiInstance.mediaMediaIdCommentsPost(mediaId, text);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentsApi#mediaMediaIdCommentsPost");
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
| **mediaId** | **String**| The ID of the media resource. | |
| **text** | **String**| Text to post as a comment on the media object as specified in &#x60;media-id&#x60;. | |

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of posting a comment. |  -  |

