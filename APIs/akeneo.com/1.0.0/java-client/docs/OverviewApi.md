# OverviewApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEndpoints**](OverviewApi.md#getEndpoints) | **GET** /api/rest/v1 | Get list of all endpoints |


<a id="getEndpoints"></a>
# **getEndpoints**
> GetEndpoints200Response getEndpoints()

Get list of all endpoints

This endpoint allows you to get the list of all the available endpoints. No need to be authenticated to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OverviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    OverviewApi apiInstance = new OverviewApi(defaultClient);
    try {
      GetEndpoints200Response result = apiInstance.getEndpoints();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OverviewApi#getEndpoints");
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

[**GetEndpoints200Response**](GetEndpoints200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, authentication, host, routes, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the list of all available endpoints |  -  |
| **406** | Not Acceptable |  -  |

