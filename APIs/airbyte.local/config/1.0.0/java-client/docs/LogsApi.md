# LogsApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLogs**](LogsApi.md#getLogs) | **POST** /v1/logs/get | Get logs |


<a id="getLogs"></a>
# **getLogs**
> File getLogs(logsRequestBody)

Get logs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    LogsApi apiInstance = new LogsApi(defaultClient);
    LogsRequestBody logsRequestBody = new LogsRequestBody(); // LogsRequestBody | 
    try {
      File result = apiInstance.getLogs(logsRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#getLogs");
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
| **logsRequestBody** | [**LogsRequestBody**](LogsRequestBody.md)|  | |

### Return type

[**File**](File.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the log file |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

