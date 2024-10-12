# StaticVideoFilesApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**staticStreamingPlaylistsHlsFilenameGet**](StaticVideoFilesApi.md#staticStreamingPlaylistsHlsFilenameGet) | **GET** /static/streaming-playlists/hls/{filename} | Get public HLS video file |
| [**staticStreamingPlaylistsHlsPrivateFilenameGet**](StaticVideoFilesApi.md#staticStreamingPlaylistsHlsPrivateFilenameGet) | **GET** /static/streaming-playlists/hls/private/{filename} | Get private HLS video file |
| [**staticWebseedFilenameGet**](StaticVideoFilesApi.md#staticWebseedFilenameGet) | **GET** /static/webseed/{filename} | Get public WebTorrent video file |
| [**staticWebseedPrivateFilenameGet**](StaticVideoFilesApi.md#staticWebseedPrivateFilenameGet) | **GET** /static/webseed/private/{filename} | Get private WebTorrent video file |


<a id="staticStreamingPlaylistsHlsFilenameGet"></a>
# **staticStreamingPlaylistsHlsFilenameGet**
> staticStreamingPlaylistsHlsFilenameGet(filename)

Get public HLS video file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StaticVideoFilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    StaticVideoFilesApi apiInstance = new StaticVideoFilesApi(defaultClient);
    String filename = "filename_example"; // String | Filename
    try {
      apiInstance.staticStreamingPlaylistsHlsFilenameGet(filename);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticVideoFilesApi#staticStreamingPlaylistsHlsFilenameGet");
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
| **filename** | **String**| Filename | |

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
| **200** | successful operation |  -  |
| **403** | invalid auth |  -  |
| **404** | not found |  -  |

<a id="staticStreamingPlaylistsHlsPrivateFilenameGet"></a>
# **staticStreamingPlaylistsHlsPrivateFilenameGet**
> staticStreamingPlaylistsHlsPrivateFilenameGet(filename, videoFileToken, reinjectVideoFileToken)

Get private HLS video file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StaticVideoFilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    StaticVideoFilesApi apiInstance = new StaticVideoFilesApi(defaultClient);
    String filename = "filename_example"; // String | Filename
    String videoFileToken = "videoFileToken_example"; // String | Video file token [generated](#operation/requestVideoToken) by PeerTube so you don't need to provide an OAuth token in the request header.
    Boolean reinjectVideoFileToken = true; // Boolean | Ask the server to reinject videoFileToken in URLs in m3u8 playlist
    try {
      apiInstance.staticStreamingPlaylistsHlsPrivateFilenameGet(filename, videoFileToken, reinjectVideoFileToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticVideoFilesApi#staticStreamingPlaylistsHlsPrivateFilenameGet");
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
| **filename** | **String**| Filename | |
| **videoFileToken** | **String**| Video file token [generated](#operation/requestVideoToken) by PeerTube so you don&#39;t need to provide an OAuth token in the request header. | [optional] |
| **reinjectVideoFileToken** | **Boolean**| Ask the server to reinject videoFileToken in URLs in m3u8 playlist | [optional] |

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
| **200** | successful operation |  -  |
| **403** | invalid auth |  -  |
| **404** | not found |  -  |

<a id="staticWebseedFilenameGet"></a>
# **staticWebseedFilenameGet**
> staticWebseedFilenameGet(filename)

Get public WebTorrent video file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StaticVideoFilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    StaticVideoFilesApi apiInstance = new StaticVideoFilesApi(defaultClient);
    String filename = "filename_example"; // String | Filename
    try {
      apiInstance.staticWebseedFilenameGet(filename);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticVideoFilesApi#staticWebseedFilenameGet");
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
| **filename** | **String**| Filename | |

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
| **200** | successful operation |  -  |
| **404** | not found |  -  |

<a id="staticWebseedPrivateFilenameGet"></a>
# **staticWebseedPrivateFilenameGet**
> staticWebseedPrivateFilenameGet(filename, videoFileToken)

Get private WebTorrent video file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StaticVideoFilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    StaticVideoFilesApi apiInstance = new StaticVideoFilesApi(defaultClient);
    String filename = "filename_example"; // String | Filename
    String videoFileToken = "videoFileToken_example"; // String | Video file token [generated](#operation/requestVideoToken) by PeerTube so you don't need to provide an OAuth token in the request header.
    try {
      apiInstance.staticWebseedPrivateFilenameGet(filename, videoFileToken);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticVideoFilesApi#staticWebseedPrivateFilenameGet");
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
| **filename** | **String**| Filename | |
| **videoFileToken** | **String**| Video file token [generated](#operation/requestVideoToken) by PeerTube so you don&#39;t need to provide an OAuth token in the request header. | [optional] |

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
| **200** | successful operation |  -  |
| **403** | invalid auth |  -  |
| **404** | not found |  -  |

