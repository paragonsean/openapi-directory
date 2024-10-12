# TaskrouterV1TaskChannelApi

All URIs are relative to *https://taskrouter.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTaskChannel**](TaskrouterV1TaskChannelApi.md#createTaskChannel) | **POST** /v1/Workspaces/{WorkspaceSid}/TaskChannels |  |
| [**deleteTaskChannel**](TaskrouterV1TaskChannelApi.md#deleteTaskChannel) | **DELETE** /v1/Workspaces/{WorkspaceSid}/TaskChannels/{Sid} |  |
| [**fetchTaskChannel**](TaskrouterV1TaskChannelApi.md#fetchTaskChannel) | **GET** /v1/Workspaces/{WorkspaceSid}/TaskChannels/{Sid} |  |
| [**listTaskChannel**](TaskrouterV1TaskChannelApi.md#listTaskChannel) | **GET** /v1/Workspaces/{WorkspaceSid}/TaskChannels |  |
| [**updateTaskChannel**](TaskrouterV1TaskChannelApi.md#updateTaskChannel) | **POST** /v1/Workspaces/{WorkspaceSid}/TaskChannels/{Sid} |  |


<a id="createTaskChannel"></a>
# **createTaskChannel**
> TaskrouterV1WorkspaceTaskChannel createTaskChannel(workspaceSid, friendlyName, uniqueName, channelOptimizedRouting)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1TaskChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1TaskChannelApi apiInstance = new TaskrouterV1TaskChannelApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace that the new Task Channel belongs to.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Task Channel. It can be up to 64 characters long.
    String uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the Task Channel, such as `voice` or `sms`.
    Boolean channelOptimizedRouting = true; // Boolean | Whether the Task Channel should prioritize Workers that have been idle. If `true`, Workers that have been idle the longest are prioritized.
    try {
      TaskrouterV1WorkspaceTaskChannel result = apiInstance.createTaskChannel(workspaceSid, friendlyName, uniqueName, channelOptimizedRouting);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1TaskChannelApi#createTaskChannel");
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
| **workspaceSid** | **String**| The SID of the Workspace that the new Task Channel belongs to. | |
| **friendlyName** | **String**| A descriptive string that you create to describe the Task Channel. It can be up to 64 characters long. | |
| **uniqueName** | **String**| An application-defined string that uniquely identifies the Task Channel, such as &#x60;voice&#x60; or &#x60;sms&#x60;. | |
| **channelOptimizedRouting** | **Boolean**| Whether the Task Channel should prioritize Workers that have been idle. If &#x60;true&#x60;, Workers that have been idle the longest are prioritized. | [optional] |

### Return type

[**TaskrouterV1WorkspaceTaskChannel**](TaskrouterV1WorkspaceTaskChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteTaskChannel"></a>
# **deleteTaskChannel**
> deleteTaskChannel(workspaceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1TaskChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1TaskChannelApi apiInstance = new TaskrouterV1TaskChannelApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Task Channel to delete.
    String sid = "sid_example"; // String | The SID of the Task Channel resource to delete.
    try {
      apiInstance.deleteTaskChannel(workspaceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1TaskChannelApi#deleteTaskChannel");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Task Channel to delete. | |
| **sid** | **String**| The SID of the Task Channel resource to delete. | |

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

<a id="fetchTaskChannel"></a>
# **fetchTaskChannel**
> TaskrouterV1WorkspaceTaskChannel fetchTaskChannel(workspaceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1TaskChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1TaskChannelApi apiInstance = new TaskrouterV1TaskChannelApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Task Channel to fetch.
    String sid = "sid_example"; // String | The SID of the Task Channel resource to fetch.
    try {
      TaskrouterV1WorkspaceTaskChannel result = apiInstance.fetchTaskChannel(workspaceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1TaskChannelApi#fetchTaskChannel");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Task Channel to fetch. | |
| **sid** | **String**| The SID of the Task Channel resource to fetch. | |

### Return type

[**TaskrouterV1WorkspaceTaskChannel**](TaskrouterV1WorkspaceTaskChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listTaskChannel"></a>
# **listTaskChannel**
> ListTaskChannelResponse listTaskChannel(workspaceSid, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1TaskChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1TaskChannelApi apiInstance = new TaskrouterV1TaskChannelApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Task Channel to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListTaskChannelResponse result = apiInstance.listTaskChannel(workspaceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1TaskChannelApi#listTaskChannel");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Task Channel to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListTaskChannelResponse**](ListTaskChannelResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateTaskChannel"></a>
# **updateTaskChannel**
> TaskrouterV1WorkspaceTaskChannel updateTaskChannel(workspaceSid, sid, channelOptimizedRouting, friendlyName)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1TaskChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1TaskChannelApi apiInstance = new TaskrouterV1TaskChannelApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Task Channel to update.
    String sid = "sid_example"; // String | The SID of the Task Channel resource to update.
    Boolean channelOptimizedRouting = true; // Boolean | Whether the TaskChannel should prioritize Workers that have been idle. If `true`, Workers that have been idle the longest are prioritized.
    String friendlyName = "friendlyName_example"; // String | A descriptive string that you create to describe the Task Channel. It can be up to 64 characters long.
    try {
      TaskrouterV1WorkspaceTaskChannel result = apiInstance.updateTaskChannel(workspaceSid, sid, channelOptimizedRouting, friendlyName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1TaskChannelApi#updateTaskChannel");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Task Channel to update. | |
| **sid** | **String**| The SID of the Task Channel resource to update. | |
| **channelOptimizedRouting** | **Boolean**| Whether the TaskChannel should prioritize Workers that have been idle. If &#x60;true&#x60;, Workers that have been idle the longest are prioritized. | [optional] |
| **friendlyName** | **String**| A descriptive string that you create to describe the Task Channel. It can be up to 64 characters long. | [optional] |

### Return type

[**TaskrouterV1WorkspaceTaskChannel**](TaskrouterV1WorkspaceTaskChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

