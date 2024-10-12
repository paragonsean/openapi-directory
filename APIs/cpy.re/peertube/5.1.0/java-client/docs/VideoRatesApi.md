# VideoRatesApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1UsersMeVideosVideoIdRatingGet_0**](VideoRatesApi.md#apiV1UsersMeVideosVideoIdRatingGet_0) | **GET** /api/v1/users/me/videos/{videoId}/rating | Get rate of my user for a video |
| [**apiV1VideosIdRatePut**](VideoRatesApi.md#apiV1VideosIdRatePut) | **PUT** /api/v1/videos/{id}/rate | Like/dislike a video |


<a id="apiV1UsersMeVideosVideoIdRatingGet_0"></a>
# **apiV1UsersMeVideosVideoIdRatingGet_0**
> GetMeVideoRating apiV1UsersMeVideosVideoIdRatingGet_0(videoId)

Get rate of my user for a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoRatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoRatesApi apiInstance = new VideoRatesApi(defaultClient);
    Integer videoId = 56; // Integer | The video id
    try {
      GetMeVideoRating result = apiInstance.apiV1UsersMeVideosVideoIdRatingGet_0(videoId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoRatesApi#apiV1UsersMeVideosVideoIdRatingGet_0");
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
| **videoId** | **Integer**| The video id | |

### Return type

[**GetMeVideoRating**](GetMeVideoRating.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="apiV1VideosIdRatePut"></a>
# **apiV1VideosIdRatePut**
> apiV1VideosIdRatePut(id, apiV1VideosIdRatePutRequest)

Like/dislike a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoRatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoRatesApi apiInstance = new VideoRatesApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    ApiV1VideosIdRatePutRequest apiV1VideosIdRatePutRequest = new ApiV1VideosIdRatePutRequest(); // ApiV1VideosIdRatePutRequest | 
    try {
      apiInstance.apiV1VideosIdRatePut(id, apiV1VideosIdRatePutRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoRatesApi#apiV1VideosIdRatePut");
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
| **apiV1VideosIdRatePutRequest** | [**ApiV1VideosIdRatePutRequest**](ApiV1VideosIdRatePutRequest.md)|  | [optional] |

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

