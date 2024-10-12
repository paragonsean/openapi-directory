# VideoFilesApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**delVideoHLS**](VideoFilesApi.md#delVideoHLS) | **DELETE** /api/v1/videos/{id}/hls | Delete video HLS files |
| [**delVideoWebTorrent**](VideoFilesApi.md#delVideoWebTorrent) | **DELETE** /api/v1/videos/{id}/webtorrent | Delete video WebTorrent files |


<a id="delVideoHLS"></a>
# **delVideoHLS**
> delVideoHLS(id)

Delete video HLS files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoFilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoFilesApi apiInstance = new VideoFilesApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    try {
      apiInstance.delVideoHLS(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoFilesApi#delVideoHLS");
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **404** | video does not exist |  -  |

<a id="delVideoWebTorrent"></a>
# **delVideoWebTorrent**
> delVideoWebTorrent(id)

Delete video WebTorrent files

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoFilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoFilesApi apiInstance = new VideoFilesApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    try {
      apiInstance.delVideoWebTorrent(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoFilesApi#delVideoWebTorrent");
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **404** | video does not exist |  -  |

