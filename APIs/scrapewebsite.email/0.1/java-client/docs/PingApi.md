# PingApi

All URIs are relative to *http://scrapewebsite.email*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gETV1PingFormat**](PingApi.md#gETV1PingFormat) | **GET** /v1/ping.json | Returns whether the system is up. |


<a id="gETV1PingFormat"></a>
# **gETV1PingFormat**
> gETV1PingFormat()

Returns whether the system is up.

&lt;p&gt;Returns ‘pong’ if the site is up&lt;/p&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://scrapewebsite.email");

    PingApi apiInstance = new PingApi(defaultClient);
    try {
      apiInstance.gETV1PingFormat();
    } catch (ApiException e) {
      System.err.println("Exception when calling PingApi#gETV1PingFormat");
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
| **200** | No response was specified |  -  |

