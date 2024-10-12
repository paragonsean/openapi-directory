# MediaTypesApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resourcesMediaTypesFormatGet**](MediaTypesApi.md#resourcesMediaTypesFormatGet) | **GET** /resources/mediaTypes.{format} | Get MediaTypes |


<a id="resourcesMediaTypesFormatGet"></a>
# **resourcesMediaTypesFormatGet**
> List&lt;MediaTypeHolderWrapped&gt; resourcesMediaTypesFormatGet(format)

Get MediaTypes

Information about media types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MediaTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    MediaTypesApi apiInstance = new MediaTypesApi(defaultClient);
    String format = "format_example"; // String | Automatically added
    try {
      List<MediaTypeHolderWrapped> result = apiInstance.resourcesMediaTypesFormatGet(format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MediaTypesApi#resourcesMediaTypesFormatGet");
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
| **format** | **String**| Automatically added | |

### Return type

[**List&lt;MediaTypeHolderWrapped&gt;**](MediaTypeHolderWrapped.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of available MediaTypes. |  -  |
| **400** | Invalid ID |  -  |
| **500** | Internal Server Error |  -  |

