# TaskrouterV1WorkflowRealTimeStatisticsApi

All URIs are relative to *https://taskrouter.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchWorkflowRealTimeStatistics**](TaskrouterV1WorkflowRealTimeStatisticsApi.md#fetchWorkflowRealTimeStatistics) | **GET** /v1/Workspaces/{WorkspaceSid}/Workflows/{WorkflowSid}/RealTimeStatistics |  |


<a id="fetchWorkflowRealTimeStatistics"></a>
# **fetchWorkflowRealTimeStatistics**
> TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics fetchWorkflowRealTimeStatistics(workspaceSid, workflowSid, taskChannel)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1WorkflowRealTimeStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1WorkflowRealTimeStatisticsApi apiInstance = new TaskrouterV1WorkflowRealTimeStatisticsApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Workflow to fetch.
    String workflowSid = "workflowSid_example"; // String | Returns the list of Tasks that are being controlled by the Workflow with the specified SID value.
    String taskChannel = "taskChannel_example"; // String | Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel's SID or its `unique_name`, such as `voice`, `sms`, or `default`.
    try {
      TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics result = apiInstance.fetchWorkflowRealTimeStatistics(workspaceSid, workflowSid, taskChannel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1WorkflowRealTimeStatisticsApi#fetchWorkflowRealTimeStatistics");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Workflow to fetch. | |
| **workflowSid** | **String**| Returns the list of Tasks that are being controlled by the Workflow with the specified SID value. | |
| **taskChannel** | **String**| Only calculate real-time statistics on this TaskChannel. Can be the TaskChannel&#39;s SID or its &#x60;unique_name&#x60;, such as &#x60;voice&#x60;, &#x60;sms&#x60;, or &#x60;default&#x60;. | [optional] |

### Return type

[**TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics**](TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

