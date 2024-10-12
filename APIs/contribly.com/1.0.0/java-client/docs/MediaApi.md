# MediaApi

All URIs are relative to *https://api.contribly.com/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mediaPost**](MediaApi.md#mediaPost) | **POST** /media | Submit a new media file |


<a id="mediaPost"></a>
# **mediaPost**
> Media mediaPost(body)

Submit a new media file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    MediaApi apiInstance = new MediaApi(defaultClient);
    byte[] body = null; // byte[] | Binary media file
    try {
      Media result = apiInstance.mediaPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#mediaPost");
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
| **body** | **byte[]**| Binary media file | |

### Return type

[**Media**](Media.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Media created |  -  |

