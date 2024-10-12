# TaskrouterV1WorkersCumulativeStatisticsApi

All URIs are relative to *https://taskrouter.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchWorkersCumulativeStatistics**](TaskrouterV1WorkersCumulativeStatisticsApi.md#fetchWorkersCumulativeStatistics) | **GET** /v1/Workspaces/{WorkspaceSid}/Workers/CumulativeStatistics |  |


<a id="fetchWorkersCumulativeStatistics"></a>
# **fetchWorkersCumulativeStatistics**
> TaskrouterV1WorkspaceWorkerWorkersCumulativeStatistics fetchWorkersCumulativeStatistics(workspaceSid, endDate, minutes, startDate, taskChannel)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1WorkersCumulativeStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1WorkersCumulativeStatisticsApi apiInstance = new TaskrouterV1WorkersCumulativeStatisticsApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the resource to fetch.
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Only calculate statistics from this date and time and earlier, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    Integer minutes = 56; // Integer | Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends.
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    String taskChannel = "taskChannel_example"; // String | Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
    try {
      TaskrouterV1WorkspaceWorkerWorkersCumulativeStatistics result = apiInstance.fetchWorkersCumulativeStatistics(workspaceSid, endDate, minutes, startDate, taskChannel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1WorkersCumulativeStatisticsApi#fetchWorkersCumulativeStatistics");
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
| **workspaceSid** | **String**| The SID of the Workspace with the resource to fetch. | |
| **endDate** | **OffsetDateTime**| Only calculate statistics from this date and time and earlier, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] |
| **minutes** | **Integer**| Only calculate statistics since this many minutes in the past. The default 15 minutes. This is helpful for displaying statistics for the last 15 minutes, 240 minutes (4 hours), and 480 minutes (8 hours) to see trends. | [optional] |
| **startDate** | **OffsetDateTime**| Only calculate statistics from this date and time and later, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] |
| **taskChannel** | **String**| Only calculate cumulative statistics on this TaskChannel. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;. | [optional] |

### Return type

[**TaskrouterV1WorkspaceWorkerWorkersCumulativeStatistics**](TaskrouterV1WorkspaceWorkerWorkersCumulativeStatistics.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

