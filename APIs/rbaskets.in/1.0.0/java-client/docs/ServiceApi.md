# ServiceApi

All URIs are relative to *https://rbaskets.in*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiVersionGet**](ServiceApi.md#apiVersionGet) | **GET** /api/version | Get service version |


<a id="apiVersionGet"></a>
# **apiVersionGet**
> Version apiVersionGet()

Get service version

Get service version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rbaskets.in");

    ServiceApi apiInstance = new ServiceApi(defaultClient);
    try {
      Version result = apiInstance.apiVersionGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServiceApi#apiVersionGet");
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

[**Version**](Version.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Returns service version. |  -  |

