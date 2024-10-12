# TaskrouterV1WorkersStatisticsApi

All URIs are relative to *https://taskrouter.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchWorkerStatistics**](TaskrouterV1WorkersStatisticsApi.md#fetchWorkerStatistics) | **GET** /v1/Workspaces/{WorkspaceSid}/Workers/Statistics |  |


<a id="fetchWorkerStatistics"></a>
# **fetchWorkerStatistics**
> TaskrouterV1WorkspaceWorkerWorkerStatistics fetchWorkerStatistics(workspaceSid, minutes, startDate, endDate, taskQueueSid, taskQueueName, friendlyName, taskChannel)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1WorkersStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1WorkersStatisticsApi apiInstance = new TaskrouterV1WorkersStatisticsApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Worker to fetch.
    Integer minutes = 56; // Integer | Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
    String taskQueueSid = "taskQueueSid_example"; // String | The SID of the TaskQueue for which to fetch Worker statistics.
    String taskQueueName = "taskQueueName_example"; // String | The `friendly_name` of the TaskQueue for which to fetch Worker statistics.
    String friendlyName = "friendlyName_example"; // String | Only include Workers with `friendly_name` values that match this parameter.
    String taskChannel = "taskChannel_example"; // String | Only calculate statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
    try {
      TaskrouterV1WorkspaceWorkerWorkerStatistics result = apiInstance.fetchWorkerStatistics(workspaceSid, minutes, startDate, endDate, taskQueueSid, taskQueueName, friendlyName, taskChannel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1WorkersStatisticsApi#fetchWorkerStatistics");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Worker to fetch. | |
| **minutes** | **Integer**| Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends. | [optional] |
| **startDate** | **OffsetDateTime**| Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] |
| **endDate** | **OffsetDateTime**| Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time. | [optional] |
| **taskQueueSid** | **String**| The SID of the TaskQueue for which to fetch Worker statistics. | [optional] |
| **taskQueueName** | **String**| The &#x60;friendly_name&#x60; of the TaskQueue for which to fetch Worker statistics. | [optional] |
| **friendlyName** | **String**| Only include Workers with &#x60;friendly_name&#x60; values that match this parameter. | [optional] |
| **taskChannel** | **String**| Only calculate statistics on this TaskChannel. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;. | [optional] |

### Return type

[**TaskrouterV1WorkspaceWorkerWorkerStatistics**](TaskrouterV1WorkspaceWorkerWorkerStatistics.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

