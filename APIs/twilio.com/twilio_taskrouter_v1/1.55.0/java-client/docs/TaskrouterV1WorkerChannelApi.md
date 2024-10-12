# TaskrouterV1WorkerChannelApi

All URIs are relative to *https://taskrouter.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchWorkerChannel**](TaskrouterV1WorkerChannelApi.md#fetchWorkerChannel) | **GET** /v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Channels/{Sid} |  |
| [**listWorkerChannel**](TaskrouterV1WorkerChannelApi.md#listWorkerChannel) | **GET** /v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Channels |  |
| [**updateWorkerChannel**](TaskrouterV1WorkerChannelApi.md#updateWorkerChannel) | **POST** /v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Channels/{Sid} |  |


<a id="fetchWorkerChannel"></a>
# **fetchWorkerChannel**
> TaskrouterV1WorkspaceWorkerWorkerChannel fetchWorkerChannel(workspaceSid, workerSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1WorkerChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1WorkerChannelApi apiInstance = new TaskrouterV1WorkerChannelApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the WorkerChannel to fetch.
    String workerSid = "workerSid_example"; // String | The SID of the Worker with the WorkerChannel to fetch.
    String sid = "sid_example"; // String | The SID of the WorkerChannel to fetch.
    try {
      TaskrouterV1WorkspaceWorkerWorkerChannel result = apiInstance.fetchWorkerChannel(workspaceSid, workerSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1WorkerChannelApi#fetchWorkerChannel");
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
| **workspaceSid** | **String**| The SID of the Workspace with the WorkerChannel to fetch. | |
| **workerSid** | **String**| The SID of the Worker with the WorkerChannel to fetch. | |
| **sid** | **String**| The SID of the WorkerChannel to fetch. | |

### Return type

[**TaskrouterV1WorkspaceWorkerWorkerChannel**](TaskrouterV1WorkspaceWorkerWorkerChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listWorkerChannel"></a>
# **listWorkerChannel**
> ListWorkerChannelResponse listWorkerChannel(workspaceSid, workerSid, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1WorkerChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1WorkerChannelApi apiInstance = new TaskrouterV1WorkerChannelApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the WorkerChannels to read.
    String workerSid = "workerSid_example"; // String | The SID of the Worker with the WorkerChannels to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListWorkerChannelResponse result = apiInstance.listWorkerChannel(workspaceSid, workerSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1WorkerChannelApi#listWorkerChannel");
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
| **workspaceSid** | **String**| The SID of the Workspace with the WorkerChannels to read. | |
| **workerSid** | **String**| The SID of the Worker with the WorkerChannels to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListWorkerChannelResponse**](ListWorkerChannelResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateWorkerChannel"></a>
# **updateWorkerChannel**
> TaskrouterV1WorkspaceWorkerWorkerChannel updateWorkerChannel(workspaceSid, workerSid, sid, available, capacity)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1WorkerChannelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1WorkerChannelApi apiInstance = new TaskrouterV1WorkerChannelApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the WorkerChannel to update.
    String workerSid = "workerSid_example"; // String | The SID of the Worker with the WorkerChannel to update.
    String sid = "sid_example"; // String | The SID of the WorkerChannel to update.
    Boolean available = true; // Boolean | Whether the WorkerChannel is available. Set to `false` to prevent the Worker from receiving any new Tasks of this TaskChannel type.
    Integer capacity = 56; // Integer | The total number of Tasks that the Worker should handle for the TaskChannel type. TaskRouter creates reservations for Tasks of this TaskChannel type up to the specified capacity. If the capacity is 0, no new reservations will be created.
    try {
      TaskrouterV1WorkspaceWorkerWorkerChannel result = apiInstance.updateWorkerChannel(workspaceSid, workerSid, sid, available, capacity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1WorkerChannelApi#updateWorkerChannel");
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
| **workspaceSid** | **String**| The SID of the Workspace with the WorkerChannel to update. | |
| **workerSid** | **String**| The SID of the Worker with the WorkerChannel to update. | |
| **sid** | **String**| The SID of the WorkerChannel to update. | |
| **available** | **Boolean**| Whether the WorkerChannel is available. Set to &#x60;false&#x60; to prevent the Worker from receiving any new Tasks of this TaskChannel type. | [optional] |
| **capacity** | **Integer**| The total number of Tasks that the Worker should handle for the TaskChannel type. TaskRouter creates reservations for Tasks of this TaskChannel type up to the specified capacity. If the capacity is 0, no new reservations will be created. | [optional] |

### Return type

[**TaskrouterV1WorkspaceWorkerWorkerChannel**](TaskrouterV1WorkspaceWorkerWorkerChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

