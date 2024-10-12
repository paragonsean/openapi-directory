# DumpsApi

All URIs are relative to *http://localhost:7700*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createADump**](DumpsApi.md#createADump) | **POST** /dumps | Create a dump |


<a id="createADump"></a>
# **createADump**
> createADump()

Create a dump

Create a dump

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DumpsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:7700");

    DumpsApi apiInstance = new DumpsApi(defaultClient);
    try {
      apiInstance.createADump();
    } catch (ApiException e) {
      System.err.println("Exception when calling DumpsApi#createADump");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

