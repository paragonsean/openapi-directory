# LikesApi

All URIs are relative to *https://api.instagram.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mediaMediaIdLikesDelete**](LikesApi.md#mediaMediaIdLikesDelete) | **DELETE** /media/{media-id}/likes | Remove a like on this media by the current user. |
| [**mediaMediaIdLikesGet**](LikesApi.md#mediaMediaIdLikesGet) | **GET** /media/{media-id}/likes | Get a list of users who have liked this media. |
| [**mediaMediaIdLikesPost**](LikesApi.md#mediaMediaIdLikesPost) | **POST** /media/{media-id}/likes | Set a like on this media by the current user. |


<a id="mediaMediaIdLikesDelete"></a>
# **mediaMediaIdLikesDelete**
> StatusResponse mediaMediaIdLikesDelete(mediaId)

Remove a like on this media by the current user.

Remove a like on this media by the currently authenticated user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LikesApi;

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

    LikesApi apiInstance = new LikesApi(defaultClient);
    String mediaId = "mediaId_example"; // String | The ID of the media resource.
    try {
      StatusResponse result = apiInstance.mediaMediaIdLikesDelete(mediaId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LikesApi#mediaMediaIdLikesDelete");
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

[**StatusResponse**](StatusResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of removing a like. |  -  |

<a id="mediaMediaIdLikesGet"></a>
# **mediaMediaIdLikesGet**
> UsersInfoResponse mediaMediaIdLikesGet(mediaId)

Get a list of users who have liked this media.

Get a list of users who have liked this media.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LikesApi;

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

    LikesApi apiInstance = new LikesApi(defaultClient);
    String mediaId = "mediaId_example"; // String | The ID of the media resource.
    try {
      UsersInfoResponse result = apiInstance.mediaMediaIdLikesGet(mediaId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LikesApi#mediaMediaIdLikesGet");
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

[**UsersInfoResponse**](UsersInfoResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of users who liked the media resource. |  -  |

<a id="mediaMediaIdLikesPost"></a>
# **mediaMediaIdLikesPost**
> StatusResponse mediaMediaIdLikesPost(mediaId)

Set a like on this media by the current user.

Set a like on this media by the currently authenticated user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LikesApi;

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

    LikesApi apiInstance = new LikesApi(defaultClient);
    String mediaId = "mediaId_example"; // String | The ID of the media resource.
    try {
      StatusResponse result = apiInstance.mediaMediaIdLikesPost(mediaId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LikesApi#mediaMediaIdLikesPost");
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

[**StatusResponse**](StatusResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of setting a like. |  -  |

