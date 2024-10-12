# VideosVersionsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createVideoVersion**](VideosVersionsApi.md#createVideoVersion) | **POST** /videos/{video_id}/versions | Add a version to a video |


<a id="createVideoVersion"></a>
# **createVideoVersion**
> VideoVersions createVideoVersion(videoId, createVideoVersionRequest)

Add a version to a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideosVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    VideosVersionsApi apiInstance = new VideosVersionsApi(defaultClient);
    BigDecimal videoId = new BigDecimal("258684937"); // BigDecimal | The ID of the video.
    CreateVideoVersionRequest createVideoVersionRequest = new CreateVideoVersionRequest(); // CreateVideoVersionRequest | 
    try {
      VideoVersions result = apiInstance.createVideoVersion(videoId, createVideoVersionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideosVersionsApi#createVideoVersion");
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
| **videoId** | **BigDecimal**| The ID of the video. | |
| **createVideoVersionRequest** | [**CreateVideoVersionRequest**](CreateVideoVersionRequest.md)|  | |

### Return type

[**VideoVersions**](VideoVersions.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.video.version+json
 - **Accept**: application/vnd.vimeo.video.version+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Standard request. |  -  |
| **400** | * Error code 2204: If the request input contains invalid upload data. * Error code 2204: If the request input contains invalid versions data. |  -  |
| **403** | Error code 3427: If a user isn&#39;t permitted to edit the video |  -  |
| **404** | * Error code 5011: If an upload associated with the version isn&#39;t found. * Error code 5012: If a video associated with the upload isn&#39;t found. * Error code 5013: If the version of the API used is less than 3.4 and isn&#39;t of approach &#x60;tus&#x60;, the endpoint isn&#39;t available. |  -  |

