# LayingBodyApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLayingBodies**](LayingBodyApi.md#getLayingBodies) | **GET** /api/v1/LayingBody | Returns all laying bodies. |


<a id="getLayingBodies"></a>
# **getLayingBodies**
> LayingBodyResourceCollection getLayingBodies()

Returns all laying bodies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LayingBodyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    LayingBodyApi apiInstance = new LayingBodyApi(defaultClient);
    try {
      LayingBodyResourceCollection result = apiInstance.getLayingBodies();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LayingBodyApi#getLayingBodies");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LayingBodyResourceCollection**](LayingBodyResourceCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

