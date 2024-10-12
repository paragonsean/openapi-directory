# DefaultApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rootPost**](DefaultApi.md#rootPost) | **POST** / |  |


<a id="rootPost"></a>
# **rootPost**
> PackResponse rootPost(pack)



a pure-JSON endpoint for packing requests. 

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
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Pack pack = new Pack(); // Pack | complete set of items, boxes, and parameters to pack.
    try {
      PackResponse result = apiInstance.rootPost(pack);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#rootPost");
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
| **pack** | [**Pack**](Pack.md)| complete set of items, boxes, and parameters to pack. | [optional] |

### Return type

[**PackResponse**](PackResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful pack. |  -  |
| **400** | Bad request. Malformed or some other problem occurred processing the request. |  -  |
| **422** | Invalid input. The request was well-formed, but the parameters were contradictory, invalid, or otherwise somehow unable to be processed. More information will be contained in the error details. |  -  |
| **429** | Rate limited. Without an API key, only 10 unique requests are allowed per day for testing or demonstration purposes. Note that a randomized pack repeated is only a single unique request. |  -  |
| **500** | Unexpected error. |  -  |

