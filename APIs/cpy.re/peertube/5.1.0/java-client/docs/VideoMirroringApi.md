# VideoMirroringApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**delMirroredVideo**](VideoMirroringApi.md#delMirroredVideo) | **DELETE** /api/v1/server/redundancy/videos/{redundancyId} | Delete a mirror done on a video |
| [**getMirroredVideos**](VideoMirroringApi.md#getMirroredVideos) | **GET** /api/v1/server/redundancy/videos | List videos being mirrored |
| [**putMirroredVideo**](VideoMirroringApi.md#putMirroredVideo) | **POST** /api/v1/server/redundancy/videos | Mirror a video |


<a id="delMirroredVideo"></a>
# **delMirroredVideo**
> delMirroredVideo(redundancyId)

Delete a mirror done on a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoMirroringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoMirroringApi apiInstance = new VideoMirroringApi(defaultClient);
    String redundancyId = "redundancyId_example"; // String | id of an existing redundancy on a video
    try {
      apiInstance.delMirroredVideo(redundancyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoMirroringApi#delMirroredVideo");
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
| **redundancyId** | **String**| id of an existing redundancy on a video | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **404** | video redundancy not found |  -  |

<a id="getMirroredVideos"></a>
# **getMirroredVideos**
> List&lt;VideoRedundancy&gt; getMirroredVideos(target, start, count, sort)

List videos being mirrored

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoMirroringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoMirroringApi apiInstance = new VideoMirroringApi(defaultClient);
    String target = "my-videos"; // String | direction of the mirror
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "name"; // String | Sort abuses by criteria
    try {
      List<VideoRedundancy> result = apiInstance.getMirroredVideos(target, start, count, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoMirroringApi#getMirroredVideos");
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
| **target** | **String**| direction of the mirror | [enum: my-videos, remote-videos] |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort abuses by criteria | [optional] [enum: name] |

### Return type

[**List&lt;VideoRedundancy&gt;**](VideoRedundancy.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="putMirroredVideo"></a>
# **putMirroredVideo**
> putMirroredVideo(putMirroredVideoRequest)

Mirror a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoMirroringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoMirroringApi apiInstance = new VideoMirroringApi(defaultClient);
    PutMirroredVideoRequest putMirroredVideoRequest = new PutMirroredVideoRequest(); // PutMirroredVideoRequest | 
    try {
      apiInstance.putMirroredVideo(putMirroredVideoRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoMirroringApi#putMirroredVideo");
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
| **putMirroredVideoRequest** | [**PutMirroredVideoRequest**](PutMirroredVideoRequest.md)|  | [optional] |

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
| **400** | cannot mirror a local video |  -  |
| **404** | video does not exist |  -  |
| **409** | video is already mirrored |  -  |

