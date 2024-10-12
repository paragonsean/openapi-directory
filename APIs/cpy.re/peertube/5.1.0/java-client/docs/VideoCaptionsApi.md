# VideoCaptionsApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVideoCaption**](VideoCaptionsApi.md#addVideoCaption) | **PUT** /api/v1/videos/{id}/captions/{captionLanguage} | Add or replace a video caption |
| [**delVideoCaption**](VideoCaptionsApi.md#delVideoCaption) | **DELETE** /api/v1/videos/{id}/captions/{captionLanguage} | Delete a video caption |
| [**getVideoCaptions**](VideoCaptionsApi.md#getVideoCaptions) | **GET** /api/v1/videos/{id}/captions | List captions of a video |


<a id="addVideoCaption"></a>
# **addVideoCaption**
> addVideoCaption(id, captionLanguage, captionfile)

Add or replace a video caption

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoCaptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoCaptionsApi apiInstance = new VideoCaptionsApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    String captionLanguage = "captionLanguage_example"; // String | The caption language
    File captionfile = new File("/path/to/file"); // File | The file to upload.
    try {
      apiInstance.addVideoCaption(id, captionLanguage, captionfile);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoCaptionsApi#addVideoCaption");
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
| **captionLanguage** | **String**| The caption language | |
| **captionfile** | **File**| The file to upload. | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **404** | video or language not found |  -  |

<a id="delVideoCaption"></a>
# **delVideoCaption**
> delVideoCaption(id, captionLanguage)

Delete a video caption

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoCaptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    VideoCaptionsApi apiInstance = new VideoCaptionsApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    String captionLanguage = "captionLanguage_example"; // String | The caption language
    try {
      apiInstance.delVideoCaption(id, captionLanguage);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoCaptionsApi#delVideoCaption");
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
| **captionLanguage** | **String**| The caption language | |

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
| **404** | video or language or caption for that language not found |  -  |

<a id="getVideoCaptions"></a>
# **getVideoCaptions**
> GetVideoCaptions200Response getVideoCaptions(id)

List captions of a video

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VideoCaptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    VideoCaptionsApi apiInstance = new VideoCaptionsApi(defaultClient);
    GetLiveIdIdParameter id = new GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
    try {
      GetVideoCaptions200Response result = apiInstance.getVideoCaptions(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VideoCaptionsApi#getVideoCaptions");
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

[**GetVideoCaptions200Response**](GetVideoCaptions200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

