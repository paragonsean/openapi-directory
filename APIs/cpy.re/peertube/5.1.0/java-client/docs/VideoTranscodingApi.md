# VideoTranscodingApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1VideosIdStudioEditPost**](VideoTranscodingApi.md#apiV1VideosIdStudioEditPost) | **POST** /api/v1/videos/{id}/studio/edit | Create a studio task |
| [**createVideoTranscoding**](VideoTranscodingApi.md#createVideoTranscoding) | **POST** /api/v1/videos/{id}/transcoding | Create a transcoding job |


<a id="apiV1VideosIdStudioEditPost"></a>
# **apiV1VideosIdStudioEditPost**
> apiV1VideosIdStudioEditPost(id)

Create a studio task

Create a task to edit a video  (cut, add intro/outro etc)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoTranscodingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoTranscodingApi apiInstance = new VideoTranscodingApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    try {
      apiInstance.apiV1VideosIdStudioEditPost(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoTranscodingApi#apiV1VideosIdStudioEditPost");
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
| **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **400** | incorrect parameters |  -  |
| **404** | video not found |  -  |

<a id="createVideoTranscoding"></a>
# **createVideoTranscoding**
> createVideoTranscoding(id, createVideoTranscodingRequest)

Create a transcoding job

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoTranscodingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoTranscodingApi apiInstance = new VideoTranscodingApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    CreateVideoTranscodingRequest createVideoTranscodingRequest = new CreateVideoTranscodingRequest(); // CreateVideoTranscodingRequest | 
    try {
      apiInstance.createVideoTranscoding(id, createVideoTranscodingRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoTranscodingApi#createVideoTranscoding");
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
| **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | |
| **createVideoTranscodingRequest** | [**CreateVideoTranscodingRequest**](CreateVideoTranscodingRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **404** | video does not exist |  -  |

