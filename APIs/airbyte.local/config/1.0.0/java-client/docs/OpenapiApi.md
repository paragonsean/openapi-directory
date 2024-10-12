# OpenapiApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOpenApiSpec**](OpenapiApi.md#getOpenApiSpec) | **GET** /v1/openapi | Returns the openapi specification |


<a id="getOpenApiSpec"></a>
# **getOpenApiSpec**
> File getOpenApiSpec()

Returns the openapi specification

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenapiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    OpenapiApi apiInstance = new OpenapiApi(defaultClient);
    try {
      File result = apiInstance.getOpenApiSpec();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenapiApi#getOpenApiSpec");
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

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the openapi specification file |  -  |

