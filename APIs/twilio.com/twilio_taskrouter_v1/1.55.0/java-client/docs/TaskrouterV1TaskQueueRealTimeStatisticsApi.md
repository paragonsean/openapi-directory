# TaskrouterV1TaskQueueRealTimeStatisticsApi

All URIs are relative to *https://taskrouter.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchTaskQueueRealTimeStatistics**](TaskrouterV1TaskQueueRealTimeStatisticsApi.md#fetchTaskQueueRealTimeStatistics) | **GET** /v1/Workspaces/{WorkspaceSid}/TaskQueues/{TaskQueueSid}/RealTimeStatistics |  |


<a id="fetchTaskQueueRealTimeStatistics"></a>
# **fetchTaskQueueRealTimeStatistics**
> TaskrouterV1WorkspaceTaskQueueTaskQueueRealTimeStatistics fetchTaskQueueRealTimeStatistics(workspaceSid, taskQueueSid, taskChannel)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1TaskQueueRealTimeStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1TaskQueueRealTimeStatisticsApi apiInstance = new TaskrouterV1TaskQueueRealTimeStatisticsApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskQueue to fetch.
    String taskQueueSid = "taskQueueSid_example"; // String | The SID of the TaskQueue for which to fetch statistics.
    String taskChannel = "taskChannel_example"; // String | The TaskChannel for which to fetch statistics. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
    try {
      TaskrouterV1WorkspaceTaskQueueTaskQueueRealTimeStatistics result = apiInstance.fetchTaskQueueRealTimeStatistics(workspaceSid, taskQueueSid, taskChannel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1TaskQueueRealTimeStatisticsApi#fetchTaskQueueRealTimeStatistics");
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
| **taskChannel** | **String**| The TaskChannel for which to fetch statistics. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;. | [optional] |

### Return type

[**TaskrouterV1WorkspaceTaskQueueTaskQueueRealTimeStatistics**](TaskrouterV1WorkspaceTaskQueueTaskQueueRealTimeStatistics.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

