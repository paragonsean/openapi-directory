# TaskrouterV1TaskQueueStatisticsApi

All URIs are relative to *https://taskrouter.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchTaskQueueStatistics**](TaskrouterV1TaskQueueStatisticsApi.md#fetchTaskQueueStatistics) | **GET** /v1/Workspaces/{WorkspaceSid}/TaskQueues/{TaskQueueSid}/Statistics |  |


<a id="fetchTaskQueueStatistics"></a>
# **fetchTaskQueueStatistics**
> TaskrouterV1WorkspaceTaskQueueTaskQueueStatistics fetchTaskQueueStatistics(workspaceSid, taskQueueSid, endDate, minutes, startDate, taskChannel, splitByWaitTime)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1TaskQueueStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1TaskQueueStatisticsApi apiInstance = new TaskrouterV1TaskQueueStatisticsApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskQueue to fetch.
    String taskQueueSid = "taskQueueSid_example"; // String | The SID of the TaskQueue for which to fetch statistics.
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
    Integer minutes = 56; // Integer | Only calculate statistics since this many minutes in the past. The default is 15 minutes.
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    String taskChannel = "taskChannel_example"; // String | Only calculate real-time and cumulative statistics for the specified TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
    String splitByWaitTime = "splitByWaitTime_example"; // String | A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed.
    try {
      TaskrouterV1WorkspaceTaskQueueTaskQueueStatistics result = apiInstance.fetchTaskQueueStatistics(workspaceSid, taskQueueSid, endDate, minutes, startDate, taskChannel, splitByWaitTime);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1TaskQueueStatisticsApi#fetchTaskQueueStatistics");
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
| **workspaceSid** | **String**| The SID of the Workspace with the TaskQueue to fetch. | |
| **taskQueueSid** | **String**| The SID of the TaskQueue for which to fetch statistics. | |
| **endDate** | **OffsetDateTime**| Only calculate statistics from this date and time and earlier, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time. | [optional] |
| **minutes** | **Integer**| Only calculate statistics since this many minutes in the past. The default is 15 minutes. | [optional] |
| **startDate** | **OffsetDateTime**| Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] |
| **taskChannel** | **String**| Only calculate real-time and cumulative statistics for the specified TaskChannel. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;. | [optional] |
| **splitByWaitTime** | **String**| A comma separated list of values that describes the thresholds, in seconds, to calculate statistics on. For each threshold specified, the number of Tasks canceled and reservations accepted above and below the specified thresholds in seconds are computed. | [optional] |

### Return type

[**TaskrouterV1WorkspaceTaskQueueTaskQueueStatistics**](TaskrouterV1WorkspaceTaskQueueTaskQueueStatistics.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

