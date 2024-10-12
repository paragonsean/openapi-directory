# AutopilotV1TaskActionsApi

All URIs are relative to *https://autopilot.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchTaskActions**](AutopilotV1TaskActionsApi.md#fetchTaskActions) | **GET** /v1/Assistants/{AssistantSid}/Tasks/{TaskSid}/Actions |  |
| [**updateTaskActions**](AutopilotV1TaskActionsApi.md#updateTaskActions) | **POST** /v1/Assistants/{AssistantSid}/Tasks/{TaskSid}/Actions |  |


<a id="fetchTaskActions"></a>
# **fetchTaskActions**
> AutopilotV1AssistantTaskTaskActions fetchTaskActions(assistantSid, taskSid)



Returns JSON actions for the Task.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1TaskActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1TaskActionsApi apiInstance = new AutopilotV1TaskActionsApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task for which the task actions to fetch were defined.
    String taskSid = "taskSid_example"; // String | The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) for which the task actions to fetch were defined.
    try {
      AutopilotV1AssistantTaskTaskActions result = apiInstance.fetchTaskActions(assistantSid, taskSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1TaskActionsApi#fetchTaskActions");
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
| **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task for which the task actions to fetch were defined. | |
| **taskSid** | **String**| The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) for which the task actions to fetch were defined. | |

### Return type

[**AutopilotV1AssistantTaskTaskActions**](AutopilotV1AssistantTaskTaskActions.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateTaskActions"></a>
# **updateTaskActions**
> AutopilotV1AssistantTaskTaskActions updateTaskActions(assistantSid, taskSid, actions)



Updates the actions of an Task identified by {TaskSid} or {TaskUniqueName}.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutopilotV1TaskActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://autopilot.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AutopilotV1TaskActionsApi apiInstance = new AutopilotV1TaskActionsApi(defaultClient);
    String assistantSid = "assistantSid_example"; // String | The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task for which the task actions to update were defined.
    String taskSid = "taskSid_example"; // String | The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) for which the task actions to update were defined.
    Object actions = null; // Object | The JSON string that specifies the [actions](https://www.twilio.com/docs/autopilot/actions) that instruct the Assistant on how to perform the task.
    try {
      AutopilotV1AssistantTaskTaskActions result = apiInstance.updateTaskActions(assistantSid, taskSid, actions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutopilotV1TaskActionsApi#updateTaskActions");
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
| **assistantSid** | **String**| The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the Task for which the task actions to update were defined. | |
| **taskSid** | **String**| The SID of the [Task](https://www.twilio.com/docs/autopilot/api/task) for which the task actions to update were defined. | |
| **actions** | [**Object**](Object.md)| The JSON string that specifies the [actions](https://www.twilio.com/docs/autopilot/actions) that instruct the Assistant on how to perform the task. | [optional] |

### Return type

[**AutopilotV1AssistantTaskTaskActions**](AutopilotV1AssistantTaskTaskActions.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

