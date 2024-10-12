# DefaultApi

All URIs are relative to *http://api.phila.gov/polling-places/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rootGet**](DefaultApi.md#rootGet) | **GET** / | Get Polling Places Data |


<a id="rootGet"></a>
# **rootGet**
> Features rootGet(ward, division, paramCallback)

Get Polling Places Data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.phila.gov/polling-places/v1");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer ward = 56; // Integer | Ward Number
    Integer division = 56; // Integer | Division Number
    String paramCallback = "paramCallback_example"; // String | Optional parameter for jsonp support.
    try {
      Features result = apiInstance.rootGet(ward, division, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#rootGet");
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
| **ward** | **Integer**| Ward Number | |
| **division** | **Integer**| Division Number | |
| **paramCallback** | **String**| Optional parameter for jsonp support. | [optional] |

### Return type

[**Features**](Features.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array containing the polling place |  -  |

