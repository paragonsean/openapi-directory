# TaskrouterV1WorkflowApi

All URIs are relative to *https://taskrouter.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWorkflow**](TaskrouterV1WorkflowApi.md#createWorkflow) | **POST** /v1/Workspaces/{WorkspaceSid}/Workflows |  |
| [**deleteWorkflow**](TaskrouterV1WorkflowApi.md#deleteWorkflow) | **DELETE** /v1/Workspaces/{WorkspaceSid}/Workflows/{Sid} |  |
| [**fetchWorkflow**](TaskrouterV1WorkflowApi.md#fetchWorkflow) | **GET** /v1/Workspaces/{WorkspaceSid}/Workflows/{Sid} |  |
| [**listWorkflow**](TaskrouterV1WorkflowApi.md#listWorkflow) | **GET** /v1/Workspaces/{WorkspaceSid}/Workflows |  |
| [**updateWorkflow**](TaskrouterV1WorkflowApi.md#updateWorkflow) | **POST** /v1/Workspaces/{WorkspaceSid}/Workflows/{Sid} |  |


<a id="createWorkflow"></a>
# **createWorkflow**
> TaskrouterV1WorkspaceWorkflow createWorkflow(workspaceSid, _configuration, friendlyName, assignmentCallbackUrl, fallbackAssignmentCallbackUrl, taskReservationTimeout)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1WorkflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1WorkflowApi apiInstance = new TaskrouterV1WorkflowApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace that the new Workflow to create belongs to.
    String _configuration = "_configuration_example"; // String | A JSON string that contains the rules to apply to the Workflow. See [Configuring Workflows](https://www.twilio.com/docs/taskrouter/workflow-configuration) for more information.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Workflow resource. For example, `Inbound Call Workflow` or `2014 Outbound Campaign`.
    URI assignmentCallbackUrl = new URI(); // URI | The URL from your application that will process task assignment events. See [Handling Task Assignment Callback](https://www.twilio.com/docs/taskrouter/handle-assignment-callbacks) for more details.
    URI fallbackAssignmentCallbackUrl = new URI(); // URI | The URL that we should call when a call to the `assignment_callback_url` fails.
    Integer taskReservationTimeout = 56; // Integer | How long TaskRouter will wait for a confirmation response from your application after it assigns a Task to a Worker. Can be up to `86,400` (24 hours) and the default is `120`.
    try {
      TaskrouterV1WorkspaceWorkflow result = apiInstance.createWorkflow(workspaceSid, _configuration, friendlyName, assignmentCallbackUrl, fallbackAssignmentCallbackUrl, taskReservationTimeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1WorkflowApi#createWorkflow");
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
| **workspaceSid** | **String**| The SID of the Workspace that the new Workflow to create belongs to. | |
| **_configuration** | **String**| A JSON string that contains the rules to apply to the Workflow. See [Configuring Workflows](https://www.twilio.com/docs/taskrouter/workflow-configuration) for more information. | |
| **friendlyName** | **String**| A descriptive string that you create to describe the Workflow resource. For example, &#x60;Inbound Call Workflow&#x60; or &#x60;2014 Outbound Campaign&#x60;. | |
| **assignmentCallbackUrl** | **URI**| The URL from your application that will process task assignment events. See [Handling Task Assignment Callback](https://www.twilio.com/docs/taskrouter/handle-assignment-callbacks) for more details. | [optional] |
| **fallbackAssignmentCallbackUrl** | **URI**| The URL that we should call when a call to the &#x60;assignment_callback_url&#x60; fails. | [optional] |
| **taskReservationTimeout** | **Integer**| How long TaskRouter will wait for a confirmation response from your application after it assigns a Task to a Worker. Can be up to &#x60;86,400&#x60; (24 hours) and the default is &#x60;120&#x60;. | [optional] |

### Return type

[**TaskrouterV1WorkspaceWorkflow**](TaskrouterV1WorkspaceWorkflow.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteWorkflow"></a>
# **deleteWorkflow**
> deleteWorkflow(workspaceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1WorkflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1WorkflowApi apiInstance = new TaskrouterV1WorkflowApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Workflow to delete.
    String sid = "sid_example"; // String | The SID of the Workflow resource to delete.
    try {
      apiInstance.deleteWorkflow(workspaceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1WorkflowApi#deleteWorkflow");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Workflow to delete. | |
| **sid** | **String**| The SID of the Workflow resource to delete. | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

<a id="fetchWorkflow"></a>
# **fetchWorkflow**
> TaskrouterV1WorkspaceWorkflow fetchWorkflow(workspaceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1WorkflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1WorkflowApi apiInstance = new TaskrouterV1WorkflowApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Workflow to fetch.
    String sid = "sid_example"; // String | The SID of the Workflow resource to fetch.
    try {
      TaskrouterV1WorkspaceWorkflow result = apiInstance.fetchWorkflow(workspaceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1WorkflowApi#fetchWorkflow");
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
| **sid** | **String**| The SID of the Workflow resource to fetch. | |

### Return type

[**TaskrouterV1WorkspaceWorkflow**](TaskrouterV1WorkspaceWorkflow.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listWorkflow"></a>
# **listWorkflow**
> ListWorkflowResponse listWorkflow(workspaceSid, friendlyName, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1WorkflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1WorkflowApi apiInstance = new TaskrouterV1WorkflowApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Workflow to read.
    String friendlyName = "friendlyName_example"; // String | The `friendly_name` of the Workflow resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListWorkflowResponse result = apiInstance.listWorkflow(workspaceSid, friendlyName, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1WorkflowApi#listWorkflow");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Workflow to read. | |
| **friendlyName** | **String**| The &#x60;friendly_name&#x60; of the Workflow resources to read. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListWorkflowResponse**](ListWorkflowResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateWorkflow"></a>
# **updateWorkflow**
> TaskrouterV1WorkspaceWorkflow updateWorkflow(workspaceSid, sid, assignmentCallbackUrl, _configuration, fallbackAssignmentCallbackUrl, friendlyName, reEvaluateTasks, taskReservationTimeout)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1WorkflowApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1WorkflowApi apiInstance = new TaskrouterV1WorkflowApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Workflow to update.
    String sid = "sid_example"; // String | The SID of the Workflow resource to update.
    URI assignmentCallbackUrl = new URI(); // URI | The URL from your application that will process task assignment events. See [Handling Task Assignment Callback](https://www.twilio.com/docs/taskrouter/handle-assignment-callbacks) for more details.
    String _configuration = "_configuration_example"; // String | A JSON string that contains the rules to apply to the Workflow. See [Configuring Workflows](https://www.twilio.com/docs/taskrouter/workflow-configuration) for more information.
    URI fallbackAssignmentCallbackUrl = new URI(); // URI | The URL that we should call when a call to the `assignment_callback_url` fails.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Workflow resource. For example, `Inbound Call Workflow` or `2014 Outbound Campaign`.
    String reEvaluateTasks = "reEvaluateTasks_example"; // String | Whether or not to re-evaluate Tasks. The default is `false`, which means Tasks in the Workflow will not be processed through the assignment loop again.
    Integer taskReservationTimeout = 56; // Integer | How long TaskRouter will wait for a confirmation response from your application after it assigns a Task to a Worker. Can be up to `86,400` (24 hours) and the default is `120`.
    try {
      TaskrouterV1WorkspaceWorkflow result = apiInstance.updateWorkflow(workspaceSid, sid, assignmentCallbackUrl, _configuration, fallbackAssignmentCallbackUrl, friendlyName, reEvaluateTasks, taskReservationTimeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1WorkflowApi#updateWorkflow");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Workflow to update. | |
| **sid** | **String**| The SID of the Workflow resource to update. | |
| **assignmentCallbackUrl** | **URI**| The URL from your application that will process task assignment events. See [Handling Task Assignment Callback](https://www.twilio.com/docs/taskrouter/handle-assignment-callbacks) for more details. | [optional] |
| **_configuration** | **String**| A JSON string that contains the rules to apply to the Workflow. See [Configuring Workflows](https://www.twilio.com/docs/taskrouter/workflow-configuration) for more information. | [optional] |
| **fallbackAssignmentCallbackUrl** | **URI**| The URL that we should call when a call to the &#x60;assignment_callback_url&#x60; fails. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the Workflow resource. For example, &#x60;Inbound Call Workflow&#x60; or &#x60;2014 Outbound Campaign&#x60;. | [optional] |
| **reEvaluateTasks** | **String**| Whether or not to re-evaluate Tasks. The default is &#x60;false&#x60;, which means Tasks in the Workflow will not be processed through the assignment loop again. | [optional] |
| **taskReservationTimeout** | **Integer**| How long TaskRouter will wait for a confirmation response from your application after it assigns a Task to a Worker. Can be up to &#x60;86,400&#x60; (24 hours) and the default is &#x60;120&#x60;. | [optional] |

### Return type

[**TaskrouterV1WorkspaceWorkflow**](TaskrouterV1WorkspaceWorkflow.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

