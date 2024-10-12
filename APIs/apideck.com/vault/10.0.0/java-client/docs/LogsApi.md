# LogsApi

All URIs are relative to *https://unify.apideck.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**logsAll**](LogsApi.md#logsAll) | **GET** /vault/logs | Get all consumer request logs |


<a id="logsAll"></a>
# **logsAll**
> GetLogsResponse logsAll(xApideckAppId, xApideckConsumerId, filter, cursor, limit)

Get all consumer request logs

This endpoint includes all consumer request logs. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LogsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    LogsApi apiInstance = new LogsApi(defaultClient);
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    LogsFilter filter = new LogsFilter(); // LogsFilter | Filter results
    String cursor = "cursor_example"; // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    Integer limit = 20; // Integer | Number of results to return. Minimum 1, Maximum 200, Default 20
    try {
      GetLogsResponse result = apiInstance.logsAll(xApideckAppId, xApideckConsumerId, filter, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LogsApi#logsAll");
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
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **filter** | [**LogsFilter**](.md)| Filter results | [optional] |
| **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] |
| **limit** | **Integer**| Number of results to return. Minimum 1, Maximum 200, Default 20 | [optional] [default to 20] |

### Return type

[**GetLogsResponse**](GetLogsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Logs |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

