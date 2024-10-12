# TaskrouterV1EventApi

All URIs are relative to *https://taskrouter.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchEvent**](TaskrouterV1EventApi.md#fetchEvent) | **GET** /v1/Workspaces/{WorkspaceSid}/Events/{Sid} |  |
| [**listEvent**](TaskrouterV1EventApi.md#listEvent) | **GET** /v1/Workspaces/{WorkspaceSid}/Events |  |


<a id="fetchEvent"></a>
# **fetchEvent**
> TaskrouterV1WorkspaceEvent fetchEvent(workspaceSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1EventApi apiInstance = new TaskrouterV1EventApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Event to fetch.
    String sid = "sid_example"; // String | The SID of the Event resource to fetch.
    try {
      TaskrouterV1WorkspaceEvent result = apiInstance.fetchEvent(workspaceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1EventApi#fetchEvent");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Event to fetch. | |
| **sid** | **String**| The SID of the Event resource to fetch. | |

### Return type

[**TaskrouterV1WorkspaceEvent**](TaskrouterV1WorkspaceEvent.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listEvent"></a>
# **listEvent**
> ListEventResponse listEvent(workspaceSid, endDate, eventType, minutes, reservationSid, startDate, taskQueueSid, taskSid, workerSid, workflowSid, taskChannel, sid, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1EventApi apiInstance = new TaskrouterV1EventApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Events to read. Returns only the Events that pertain to the specified Workspace.
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Only include Events that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
    String eventType = "eventType_example"; // String | The type of Events to read. Returns only Events of the type specified.
    Integer minutes = 56; // Integer | The period of events to read in minutes. Returns only Events that occurred since this many minutes in the past. The default is `15` minutes. Task Attributes for Events occuring more 43,200 minutes ago will be redacted.
    String reservationSid = "reservationSid_example"; // String | The SID of the Reservation with the Events to read. Returns only Events that pertain to the specified Reservation.
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Only include Events from on or after this date and time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Task Attributes for Events older than 30 days will be redacted.
    String taskQueueSid = "taskQueueSid_example"; // String | The SID of the TaskQueue with the Events to read. Returns only the Events that pertain to the specified TaskQueue.
    String taskSid = "taskSid_example"; // String | The SID of the Task with the Events to read. Returns only the Events that pertain to the specified Task.
    String workerSid = "workerSid_example"; // String | The SID of the Worker with the Events to read. Returns only the Events that pertain to the specified Worker.
    String workflowSid = "workflowSid_example"; // String | The SID of the Workflow with the Events to read. Returns only the Events that pertain to the specified Workflow.
    String taskChannel = "taskChannel_example"; // String | The TaskChannel with the Events to read. Returns only the Events that pertain to the specified TaskChannel.
    String sid = "sid_example"; // String | The SID of the Event resource to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListEventResponse result = apiInstance.listEvent(workspaceSid, endDate, eventType, minutes, reservationSid, startDate, taskQueueSid, taskSid, workerSid, workflowSid, taskChannel, sid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1EventApi#listEvent");
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
| **workspaceSid** | **String**| The SID of the Workspace with the Events to read. Returns only the Events that pertain to the specified Workspace. | |
| **endDate** | **OffsetDateTime**| Only include Events that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time. | [optional] |
| **eventType** | **String**| The type of Events to read. Returns only Events of the type specified. | [optional] |
| **minutes** | **Integer**| The period of events to read in minutes. Returns only Events that occurred since this many minutes in the past. The default is &#x60;15&#x60; minutes. Task Attributes for Events occuring more 43,200 minutes ago will be redacted. | [optional] |
| **reservationSid** | **String**| The SID of the Reservation with the Events to read. Returns only Events that pertain to the specified Reservation. | [optional] |
| **startDate** | **OffsetDateTime**| Only include Events from on or after this date and time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Task Attributes for Events older than 30 days will be redacted. | [optional] |
| **taskQueueSid** | **String**| The SID of the TaskQueue with the Events to read. Returns only the Events that pertain to the specified TaskQueue. | [optional] |
| **taskSid** | **String**| The SID of the Task with the Events to read. Returns only the Events that pertain to the specified Task. | [optional] |
| **workerSid** | **String**| The SID of the Worker with the Events to read. Returns only the Events that pertain to the specified Worker. | [optional] |
| **workflowSid** | **String**| The SID of the Workflow with the Events to read. Returns only the Events that pertain to the specified Workflow. | [optional] |
| **taskChannel** | **String**| The TaskChannel with the Events to read. Returns only the Events that pertain to the specified TaskChannel. | [optional] |
| **sid** | **String**| The SID of the Event resource to read. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListEventResponse**](ListEventResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

