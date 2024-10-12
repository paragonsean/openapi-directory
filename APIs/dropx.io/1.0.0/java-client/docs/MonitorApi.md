# MonitorApi

All URIs are relative to *http://dropx.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersUsageGet**](MonitorApi.md#usersUsageGet) | **GET** /users/usage | Get API usuage details |


<a id="usersUsageGet"></a>
# **usersUsageGet**
> usersUsageGet()

Get API usuage details

Returns API request consumption details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonitorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://dropx.io/api/v1");

    MonitorApi apiInstance = new MonitorApi(defaultClient);
    try {
      apiInstance.usersUsageGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorApi#usersUsageGet");
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
| **200** | A list of usage details |  -  |
| **401** | Invalid authentication |  -  |
| **500** | internal server error |  -  |

