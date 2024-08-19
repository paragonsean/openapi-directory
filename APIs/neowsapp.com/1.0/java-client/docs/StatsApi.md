# StatsApi

All URIs are relative to *http://www.neowsapp.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**retrieveCurrentNeoStatistics**](StatsApi.md#retrieveCurrentNeoStatistics) | **GET** /rest/v1/stats | Get the Near Earth Object data set totals |


<a id="retrieveCurrentNeoStatistics"></a>
# **retrieveCurrentNeoStatistics**
> Statistics retrieveCurrentNeoStatistics()

Get the Near Earth Object data set totals

retrieveCurrentNeoStatistics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.neowsapp.com");

    StatsApi apiInstance = new StatsApi(defaultClient);
    try {
      Statistics result = apiInstance.retrieveCurrentNeoStatistics();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#retrieveCurrentNeoStatistics");
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

[**Statistics**](Statistics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

