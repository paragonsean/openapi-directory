# HomeApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**homeGet**](HomeApi.md#homeGet) | **GET** / | Get top level links for this PI System Web API instance. |


<a id="homeGet"></a>
# **homeGet**
> Landing homeGet()

Get top level links for this PI System Web API instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HomeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://devdata.osisoft.com/piwebapi");

    HomeApi apiInstance = new HomeApi(defaultClient);
    try {
      Landing result = apiInstance.homeGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HomeApi#homeGet");
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

[**Landing**](Landing.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/html, application/x-ms-application

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Links to top level collections and system information. |  -  |

