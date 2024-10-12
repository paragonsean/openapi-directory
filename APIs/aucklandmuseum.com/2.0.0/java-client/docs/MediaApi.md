# MediaApi

All URIs are relative to *http://api.aucklandmuseum.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMedia**](MediaApi.md#getMedia) | **GET** /id/media/{path} | Retrieve media associated with Collections and Cenotaph subjects in Auckland Museum |


<a id="getMedia"></a>
# **getMedia**
> getMedia(path, rendering)

Retrieve media associated with Collections and Cenotaph subjects in Auckland Museum

Gets &#x60;media&#x60; at a given path 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.aucklandmuseum.com");

    MediaApi apiInstance = new MediaApi(defaultClient);
    String path = "path_example"; // String | The media `identifier` 
    String rendering = "rendering_example"; // String | The desired media `rendering`  Possible values: * `original.jpg` * `original.pdf` * `thumbnail.jpg` (fixed with 70px) * `standard.jpg` (fixed width 440px and height 440px) * `preview.jpg` (fixed height 100px) 
    try {
      apiInstance.getMedia(path, rendering);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaApi#getMedia");
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
| **path** | **String**| The media &#x60;identifier&#x60;  | |
| **rendering** | **String**| The desired media &#x60;rendering&#x60;  Possible values: * &#x60;original.jpg&#x60; * &#x60;original.pdf&#x60; * &#x60;thumbnail.jpg&#x60; (fixed with 70px) * &#x60;standard.jpg&#x60; (fixed width 440px and height 440px) * &#x60;preview.jpg&#x60; (fixed height 100px)  | [optional] |

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
| **200** | &#x60;media&#x60; found  |  -  |
| **404** | &#x60;media&#x60; not found  |  -  |

