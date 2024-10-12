# TaskrouterV1ReservationApi

All URIs are relative to *https://taskrouter.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchTaskReservation**](TaskrouterV1ReservationApi.md#fetchTaskReservation) | **GET** /v1/Workspaces/{WorkspaceSid}/Tasks/{TaskSid}/Reservations/{Sid} |  |
| [**fetchWorkerReservation**](TaskrouterV1ReservationApi.md#fetchWorkerReservation) | **GET** /v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Reservations/{Sid} |  |
| [**listTaskReservation**](TaskrouterV1ReservationApi.md#listTaskReservation) | **GET** /v1/Workspaces/{WorkspaceSid}/Tasks/{TaskSid}/Reservations |  |
| [**listWorkerReservation**](TaskrouterV1ReservationApi.md#listWorkerReservation) | **GET** /v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Reservations |  |
| [**updateTaskReservation**](TaskrouterV1ReservationApi.md#updateTaskReservation) | **POST** /v1/Workspaces/{WorkspaceSid}/Tasks/{TaskSid}/Reservations/{Sid} |  |
| [**updateWorkerReservation**](TaskrouterV1ReservationApi.md#updateWorkerReservation) | **POST** /v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Reservations/{Sid} |  |


<a id="fetchTaskReservation"></a>
# **fetchTaskReservation**
> TaskrouterV1WorkspaceTaskTaskReservation fetchTaskReservation(workspaceSid, taskSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1ReservationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1ReservationApi apiInstance = new TaskrouterV1ReservationApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskReservation resource to fetch.
    String taskSid = "taskSid_example"; // String | The SID of the reserved Task resource with the TaskReservation resource to fetch.
    String sid = "sid_example"; // String | The SID of the TaskReservation resource to fetch.
    try {
      TaskrouterV1WorkspaceTaskTaskReservation result = apiInstance.fetchTaskReservation(workspaceSid, taskSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1ReservationApi#fetchTaskReservation");
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
| **workspaceSid** | **String**| The SID of the Workspace with the TaskReservation resource to fetch. | |
| **taskSid** | **String**| The SID of the reserved Task resource with the TaskReservation resource to fetch. | |
| **sid** | **String**| The SID of the TaskReservation resource to fetch. | |

### Return type

[**TaskrouterV1WorkspaceTaskTaskReservation**](TaskrouterV1WorkspaceTaskTaskReservation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="fetchWorkerReservation"></a>
# **fetchWorkerReservation**
> TaskrouterV1WorkspaceWorkerWorkerReservation fetchWorkerReservation(workspaceSid, workerSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1ReservationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1ReservationApi apiInstance = new TaskrouterV1ReservationApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the WorkerReservation resource to fetch.
    String workerSid = "workerSid_example"; // String | The SID of the reserved Worker resource with the WorkerReservation resource to fetch.
    String sid = "sid_example"; // String | The SID of the WorkerReservation resource to fetch.
    try {
      TaskrouterV1WorkspaceWorkerWorkerReservation result = apiInstance.fetchWorkerReservation(workspaceSid, workerSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1ReservationApi#fetchWorkerReservation");
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
| **workspaceSid** | **String**| The SID of the Workspace with the WorkerReservation resource to fetch. | |
| **workerSid** | **String**| The SID of the reserved Worker resource with the WorkerReservation resource to fetch. | |
| **sid** | **String**| The SID of the WorkerReservation resource to fetch. | |

### Return type

[**TaskrouterV1WorkspaceWorkerWorkerReservation**](TaskrouterV1WorkspaceWorkerWorkerReservation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listTaskReservation"></a>
# **listTaskReservation**
> ListTaskReservationResponse listTaskReservation(workspaceSid, taskSid, reservationStatus, workerSid, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1ReservationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1ReservationApi apiInstance = new TaskrouterV1ReservationApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskReservation resources to read.
    String taskSid = "taskSid_example"; // String | The SID of the reserved Task resource with the TaskReservation resources to read.
    TaskReservationEnumStatus reservationStatus = TaskReservationEnumStatus.fromValue("pending"); // TaskReservationEnumStatus | Returns the list of reservations for a task with a specified ReservationStatus.  Can be: `pending`, `accepted`, `rejected`, or `timeout`.
    String workerSid = "workerSid_example"; // String | The SID of the reserved Worker resource to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListTaskReservationResponse result = apiInstance.listTaskReservation(workspaceSid, taskSid, reservationStatus, workerSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1ReservationApi#listTaskReservation");
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
| **workspaceSid** | **String**| The SID of the Workspace with the TaskReservation resources to read. | |
| **taskSid** | **String**| The SID of the reserved Task resource with the TaskReservation resources to read. | |
| **reservationStatus** | **TaskReservationEnumStatus**| Returns the list of reservations for a task with a specified ReservationStatus.  Can be: &#x60;pending&#x60;, &#x60;accepted&#x60;, &#x60;rejected&#x60;, or &#x60;timeout&#x60;. | [optional] [enum: pending, accepted, rejected, timeout, canceled, rescinded, wrapping, completed] |
| **workerSid** | **String**| The SID of the reserved Worker resource to read. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListTaskReservationResponse**](ListTaskReservationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listWorkerReservation"></a>
# **listWorkerReservation**
> ListWorkerReservationResponse listWorkerReservation(workspaceSid, workerSid, reservationStatus, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1ReservationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1ReservationApi apiInstance = new TaskrouterV1ReservationApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the WorkerReservation resources to read.
    String workerSid = "workerSid_example"; // String | The SID of the reserved Worker resource with the WorkerReservation resources to read.
    WorkerReservationEnumStatus reservationStatus = WorkerReservationEnumStatus.fromValue("pending"); // WorkerReservationEnumStatus | Returns the list of reservations for a worker with a specified ReservationStatus. Can be: `pending`, `accepted`, `rejected`, `timeout`, `canceled`, or `rescinded`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListWorkerReservationResponse result = apiInstance.listWorkerReservation(workspaceSid, workerSid, reservationStatus, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1ReservationApi#listWorkerReservation");
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
| **workspaceSid** | **String**| The SID of the Workspace with the WorkerReservation resources to read. | |
| **workerSid** | **String**| The SID of the reserved Worker resource with the WorkerReservation resources to read. | |
| **reservationStatus** | **WorkerReservationEnumStatus**| Returns the list of reservations for a worker with a specified ReservationStatus. Can be: &#x60;pending&#x60;, &#x60;accepted&#x60;, &#x60;rejected&#x60;, &#x60;timeout&#x60;, &#x60;canceled&#x60;, or &#x60;rescinded&#x60;. | [optional] [enum: pending, accepted, rejected, timeout, canceled, rescinded, wrapping, completed] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListWorkerReservationResponse**](ListWorkerReservationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateTaskReservation"></a>
# **updateTaskReservation**
> TaskrouterV1WorkspaceTaskTaskReservation updateTaskReservation(workspaceSid, taskSid, sid, ifMatch, beep, beepOnCustomerEntrance, callAccept, callFrom, callRecord, callStatusCallbackUrl, callTimeout, callTo, callUrl, conferenceRecord, conferenceRecordingStatusCallback, conferenceRecordingStatusCallbackMethod, conferenceStatusCallback, conferenceStatusCallbackEvent, conferenceStatusCallbackMethod, conferenceTrim, dequeueFrom, dequeuePostWorkActivitySid, dequeueRecord, dequeueStatusCallbackEvent, dequeueStatusCallbackUrl, dequeueTimeout, dequeueTo, earlyMedia, endConferenceOnCustomerExit, endConferenceOnExit, from, instruction, jitterBufferSize, maxParticipants, muted, postWorkActivitySid, record, recordingChannels, recordingStatusCallback, recordingStatusCallbackMethod, redirectAccept, redirectCallSid, redirectUrl, region, reservationStatus, sipAuthPassword, sipAuthUsername, startConferenceOnEnter, statusCallback, statusCallbackEvent, statusCallbackMethod, supervisor, supervisorMode, timeout, to, waitMethod, waitUrl, workerActivitySid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1ReservationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1ReservationApi apiInstance = new TaskrouterV1ReservationApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskReservation resources to update.
    String taskSid = "taskSid_example"; // String | The SID of the reserved Task resource with the TaskReservation resources to update.
    String sid = "sid_example"; // String | The SID of the TaskReservation resource to update.
    String ifMatch = "ifMatch_example"; // String | The If-Match HTTP request header
    String beep = "beep_example"; // String | Whether to play a notification beep when the participant joins or when to play a beep. Can be: `true`, `false`, `onEnter`, or `onExit`. The default value is `true`.
    Boolean beepOnCustomerEntrance = true; // Boolean | Whether to play a notification beep when the customer joins.
    Boolean callAccept = true; // Boolean | Whether to accept a reservation when executing a Call instruction.
    String callFrom = "callFrom_example"; // String | The Caller ID of the outbound call when executing a Call instruction.
    String callRecord = "callRecord_example"; // String | Whether to record both legs of a call when executing a Call instruction or which leg to record.
    URI callStatusCallbackUrl = new URI(); // URI | The URL to call  for the completed call event when executing a Call instruction.
    Integer callTimeout = 56; // Integer | Timeout for call when executing a Call instruction.
    String callTo = "callTo_example"; // String | The Contact URI of the worker when executing a Call instruction.  Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination.
    URI callUrl = new URI(); // URI | TwiML URI executed on answering the worker's leg as a result of the Call instruction.
    String conferenceRecord = "conferenceRecord_example"; // String | Whether to record the conference the participant is joining or when to record the conference. Can be: `true`, `false`, `record-from-start`, and `do-not-record`. The default value is `false`.
    URI conferenceRecordingStatusCallback = new URI(); // URI | The URL we should call using the `conference_recording_status_callback_method` when the conference recording is available.
    String conferenceRecordingStatusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `conference_recording_status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
    URI conferenceStatusCallback = new URI(); // URI | The URL we should call using the `conference_status_callback_method` when the conference events in `conference_status_callback_event` occur. Only the value set by the first participant to join the conference is used. Subsequent `conference_status_callback` values are ignored.
    List<TaskReservationEnumConferenceEvent> conferenceStatusCallbackEvent = Arrays.asList(); // List<TaskReservationEnumConferenceEvent> | The conference status events that we will send to `conference_status_callback`. Can be: `start`, `end`, `join`, `leave`, `mute`, `hold`, `speaker`.
    String conferenceStatusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `conference_status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
    String conferenceTrim = "conferenceTrim_example"; // String | How to trim the leading and trailing silence from your recorded conference audio files. Can be: `trim-silence` or `do-not-trim` and defaults to `trim-silence`.
    String dequeueFrom = "dequeueFrom_example"; // String | The Caller ID of the call to the worker when executing a Dequeue instruction.
    String dequeuePostWorkActivitySid = "dequeuePostWorkActivitySid_example"; // String | The SID of the Activity resource to start after executing a Dequeue instruction.
    String dequeueRecord = "dequeueRecord_example"; // String | Whether to record both legs of a call when executing a Dequeue instruction or which leg to record.
    List<String> dequeueStatusCallbackEvent = Arrays.asList(); // List<String> | The Call progress events sent via webhooks as a result of a Dequeue instruction.
    URI dequeueStatusCallbackUrl = new URI(); // URI | The Callback URL for completed call event when executing a Dequeue instruction.
    Integer dequeueTimeout = 56; // Integer | Timeout for call when executing a Dequeue instruction.
    String dequeueTo = "dequeueTo_example"; // String | The Contact URI of the worker when executing a Dequeue instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination.
    Boolean earlyMedia = true; // Boolean | Whether to allow an agent to hear the state of the outbound call, including ringing or disconnect messages. The default is `true`.
    Boolean endConferenceOnCustomerExit = true; // Boolean | Whether to end the conference when the customer leaves.
    Boolean endConferenceOnExit = true; // Boolean | Whether to end the conference when the agent leaves.
    String from = "from_example"; // String | The Caller ID of the call to the worker when executing a Conference instruction.
    String instruction = "instruction_example"; // String | The assignment instruction for reservation.
    String jitterBufferSize = "jitterBufferSize_example"; // String | The jitter buffer size for conference. Can be: `small`, `medium`, `large`, `off`.
    Integer maxParticipants = 56; // Integer | The maximum number of participants in the conference. Can be a positive integer from `2` to `250`. The default value is `250`.
    Boolean muted = true; // Boolean | Whether the agent is muted in the conference. The default is `false`.
    String postWorkActivitySid = "postWorkActivitySid_example"; // String | The new worker activity SID after executing a Conference instruction.
    Boolean record = true; // Boolean | Whether to record the participant and their conferences, including the time between conferences. The default is `false`.
    String recordingChannels = "recordingChannels_example"; // String | The recording channels for the final recording. Can be: `mono` or `dual` and the default is `mono`.
    URI recordingStatusCallback = new URI(); // URI | The URL that we should call using the `recording_status_callback_method` when the recording status changes.
    String recordingStatusCallbackMethod = "HEAD"; // String | The HTTP method we should use when we call `recording_status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
    Boolean redirectAccept = true; // Boolean | Whether the reservation should be accepted when executing a Redirect instruction.
    String redirectCallSid = "redirectCallSid_example"; // String | The Call SID of the call parked in the queue when executing a Redirect instruction.
    URI redirectUrl = new URI(); // URI | TwiML URI to redirect the call to when executing the Redirect instruction.
    String region = "region_example"; // String | The [region](https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls) where we should mix the recorded audio. Can be:`us1`, `ie1`, `de1`, `sg1`, `br1`, `au1`, or `jp1`.
    TaskReservationEnumStatus reservationStatus = TaskReservationEnumStatus.fromValue("pending"); // TaskReservationEnumStatus | 
    String sipAuthPassword = "sipAuthPassword_example"; // String | The SIP password for authentication.
    String sipAuthUsername = "sipAuthUsername_example"; // String | The SIP username used for authentication.
    Boolean startConferenceOnEnter = true; // Boolean | Whether to start the conference when the participant joins, if it has not already started. The default is `true`. If `false` and the conference has not started, the participant is muted and hears background music until another participant starts the conference.
    URI statusCallback = new URI(); // URI | The URL we should call using the `status_callback_method` to send status information to your application.
    List<TaskReservationEnumCallStatus> statusCallbackEvent = Arrays.asList(); // List<TaskReservationEnumCallStatus> | The call progress events that we will send to `status_callback`. Can be: `initiated`, `ringing`, `answered`, or `completed`.
    String statusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `status_callback`. Can be: `POST` or `GET` and the default is `POST`.
    String supervisor = "supervisor_example"; // String | The Supervisor SID/URI when executing the Supervise instruction.
    TaskReservationEnumSupervisorMode supervisorMode = TaskReservationEnumSupervisorMode.fromValue("monitor"); // TaskReservationEnumSupervisorMode | 
    Integer timeout = 56; // Integer | Timeout for call when executing a Conference instruction.
    String to = "to_example"; // String | The Contact URI of the worker when executing a Conference instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination.
    String waitMethod = "HEAD"; // String | The HTTP method we should use to call `wait_url`. Can be `GET` or `POST` and the default is `POST`. When using a static audio file, this should be `GET` so that we can cache the file.
    URI waitUrl = new URI(); // URI | The URL we should call using the `wait_method` for the music to play while participants are waiting for the conference to start. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic).
    String workerActivitySid = "workerActivitySid_example"; // String | The new worker activity SID if rejecting a reservation.
    try {
      TaskrouterV1WorkspaceTaskTaskReservation result = apiInstance.updateTaskReservation(workspaceSid, taskSid, sid, ifMatch, beep, beepOnCustomerEntrance, callAccept, callFrom, callRecord, callStatusCallbackUrl, callTimeout, callTo, callUrl, conferenceRecord, conferenceRecordingStatusCallback, conferenceRecordingStatusCallbackMethod, conferenceStatusCallback, conferenceStatusCallbackEvent, conferenceStatusCallbackMethod, conferenceTrim, dequeueFrom, dequeuePostWorkActivitySid, dequeueRecord, dequeueStatusCallbackEvent, dequeueStatusCallbackUrl, dequeueTimeout, dequeueTo, earlyMedia, endConferenceOnCustomerExit, endConferenceOnExit, from, instruction, jitterBufferSize, maxParticipants, muted, postWorkActivitySid, record, recordingChannels, recordingStatusCallback, recordingStatusCallbackMethod, redirectAccept, redirectCallSid, redirectUrl, region, reservationStatus, sipAuthPassword, sipAuthUsername, startConferenceOnEnter, statusCallback, statusCallbackEvent, statusCallbackMethod, supervisor, supervisorMode, timeout, to, waitMethod, waitUrl, workerActivitySid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1ReservationApi#updateTaskReservation");
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
| **workspaceSid** | **String**| The SID of the Workspace with the TaskReservation resources to update. | |
| **taskSid** | **String**| The SID of the reserved Task resource with the TaskReservation resources to update. | |
| **sid** | **String**| The SID of the TaskReservation resource to update. | |
| **ifMatch** | **String**| The If-Match HTTP request header | [optional] |
| **beep** | **String**| Whether to play a notification beep when the participant joins or when to play a beep. Can be: &#x60;true&#x60;, &#x60;false&#x60;, &#x60;onEnter&#x60;, or &#x60;onExit&#x60;. The default value is &#x60;true&#x60;. | [optional] |
| **beepOnCustomerEntrance** | **Boolean**| Whether to play a notification beep when the customer joins. | [optional] |
| **callAccept** | **Boolean**| Whether to accept a reservation when executing a Call instruction. | [optional] |
| **callFrom** | **String**| The Caller ID of the outbound call when executing a Call instruction. | [optional] |
| **callRecord** | **String**| Whether to record both legs of a call when executing a Call instruction or which leg to record. | [optional] |
| **callStatusCallbackUrl** | **URI**| The URL to call  for the completed call event when executing a Call instruction. | [optional] |
| **callTimeout** | **Integer**| Timeout for call when executing a Call instruction. | [optional] |
| **callTo** | **String**| The Contact URI of the worker when executing a Call instruction.  Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination. | [optional] |
| **callUrl** | **URI**| TwiML URI executed on answering the worker&#39;s leg as a result of the Call instruction. | [optional] |
| **conferenceRecord** | **String**| Whether to record the conference the participant is joining or when to record the conference. Can be: &#x60;true&#x60;, &#x60;false&#x60;, &#x60;record-from-start&#x60;, and &#x60;do-not-record&#x60;. The default value is &#x60;false&#x60;. | [optional] |
| **conferenceRecordingStatusCallback** | **URI**| The URL we should call using the &#x60;conference_recording_status_callback_method&#x60; when the conference recording is available. | [optional] |
| **conferenceRecordingStatusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;conference_recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **conferenceStatusCallback** | **URI**| The URL we should call using the &#x60;conference_status_callback_method&#x60; when the conference events in &#x60;conference_status_callback_event&#x60; occur. Only the value set by the first participant to join the conference is used. Subsequent &#x60;conference_status_callback&#x60; values are ignored. | [optional] |
| **conferenceStatusCallbackEvent** | [**List&lt;TaskReservationEnumConferenceEvent&gt;**](TaskReservationEnumConferenceEvent.md)| The conference status events that we will send to &#x60;conference_status_callback&#x60;. Can be: &#x60;start&#x60;, &#x60;end&#x60;, &#x60;join&#x60;, &#x60;leave&#x60;, &#x60;mute&#x60;, &#x60;hold&#x60;, &#x60;speaker&#x60;. | [optional] |
| **conferenceStatusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;conference_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **conferenceTrim** | **String**| How to trim the leading and trailing silence from your recorded conference audio files. Can be: &#x60;trim-silence&#x60; or &#x60;do-not-trim&#x60; and defaults to &#x60;trim-silence&#x60;. | [optional] |
| **dequeueFrom** | **String**| The Caller ID of the call to the worker when executing a Dequeue instruction. | [optional] |
| **dequeuePostWorkActivitySid** | **String**| The SID of the Activity resource to start after executing a Dequeue instruction. | [optional] |
| **dequeueRecord** | **String**| Whether to record both legs of a call when executing a Dequeue instruction or which leg to record. | [optional] |
| **dequeueStatusCallbackEvent** | [**List&lt;String&gt;**](String.md)| The Call progress events sent via webhooks as a result of a Dequeue instruction. | [optional] |
| **dequeueStatusCallbackUrl** | **URI**| The Callback URL for completed call event when executing a Dequeue instruction. | [optional] |
| **dequeueTimeout** | **Integer**| Timeout for call when executing a Dequeue instruction. | [optional] |
| **dequeueTo** | **String**| The Contact URI of the worker when executing a Dequeue instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination. | [optional] |
| **earlyMedia** | **Boolean**| Whether to allow an agent to hear the state of the outbound call, including ringing or disconnect messages. The default is &#x60;true&#x60;. | [optional] |
| **endConferenceOnCustomerExit** | **Boolean**| Whether to end the conference when the customer leaves. | [optional] |
| **endConferenceOnExit** | **Boolean**| Whether to end the conference when the agent leaves. | [optional] |
| **from** | **String**| The Caller ID of the call to the worker when executing a Conference instruction. | [optional] |
| **instruction** | **String**| The assignment instruction for reservation. | [optional] |
| **jitterBufferSize** | **String**| The jitter buffer size for conference. Can be: &#x60;small&#x60;, &#x60;medium&#x60;, &#x60;large&#x60;, &#x60;off&#x60;. | [optional] |
| **maxParticipants** | **Integer**| The maximum number of participants in the conference. Can be a positive integer from &#x60;2&#x60; to &#x60;250&#x60;. The default value is &#x60;250&#x60;. | [optional] |
| **muted** | **Boolean**| Whether the agent is muted in the conference. The default is &#x60;false&#x60;. | [optional] |
| **postWorkActivitySid** | **String**| The new worker activity SID after executing a Conference instruction. | [optional] |
| **record** | **Boolean**| Whether to record the participant and their conferences, including the time between conferences. The default is &#x60;false&#x60;. | [optional] |
| **recordingChannels** | **String**| The recording channels for the final recording. Can be: &#x60;mono&#x60; or &#x60;dual&#x60; and the default is &#x60;mono&#x60;. | [optional] |
| **recordingStatusCallback** | **URI**| The URL that we should call using the &#x60;recording_status_callback_method&#x60; when the recording status changes. | [optional] |
| **recordingStatusCallbackMethod** | **String**| The HTTP method we should use when we call &#x60;recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **redirectAccept** | **Boolean**| Whether the reservation should be accepted when executing a Redirect instruction. | [optional] |
| **redirectCallSid** | **String**| The Call SID of the call parked in the queue when executing a Redirect instruction. | [optional] |
| **redirectUrl** | **URI**| TwiML URI to redirect the call to when executing the Redirect instruction. | [optional] |
| **region** | **String**| The [region](https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls) where we should mix the recorded audio. Can be:&#x60;us1&#x60;, &#x60;ie1&#x60;, &#x60;de1&#x60;, &#x60;sg1&#x60;, &#x60;br1&#x60;, &#x60;au1&#x60;, or &#x60;jp1&#x60;. | [optional] |
| **reservationStatus** | **TaskReservationEnumStatus**|  | [optional] [enum: pending, accepted, rejected, timeout, canceled, rescinded, wrapping, completed] |
| **sipAuthPassword** | **String**| The SIP password for authentication. | [optional] |
| **sipAuthUsername** | **String**| The SIP username used for authentication. | [optional] |
| **startConferenceOnEnter** | **Boolean**| Whether to start the conference when the participant joins, if it has not already started. The default is &#x60;true&#x60;. If &#x60;false&#x60; and the conference has not started, the participant is muted and hears background music until another participant starts the conference. | [optional] |
| **statusCallback** | **URI**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional] |
| **statusCallbackEvent** | [**List&lt;TaskReservationEnumCallStatus&gt;**](TaskReservationEnumCallStatus.md)| The call progress events that we will send to &#x60;status_callback&#x60;. Can be: &#x60;initiated&#x60;, &#x60;ringing&#x60;, &#x60;answered&#x60;, or &#x60;completed&#x60;. | [optional] |
| **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **supervisor** | **String**| The Supervisor SID/URI when executing the Supervise instruction. | [optional] |
| **supervisorMode** | **TaskReservationEnumSupervisorMode**|  | [optional] [enum: monitor, whisper, barge] |
| **timeout** | **Integer**| Timeout for call when executing a Conference instruction. | [optional] |
| **to** | **String**| The Contact URI of the worker when executing a Conference instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination. | [optional] |
| **waitMethod** | **String**| The HTTP method we should use to call &#x60;wait_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. When using a static audio file, this should be &#x60;GET&#x60; so that we can cache the file. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **waitUrl** | **URI**| The URL we should call using the &#x60;wait_method&#x60; for the music to play while participants are waiting for the conference to start. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic). | [optional] |
| **workerActivitySid** | **String**| The new worker activity SID if rejecting a reservation. | [optional] |

### Return type

[**TaskrouterV1WorkspaceTaskTaskReservation**](TaskrouterV1WorkspaceTaskTaskReservation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateWorkerReservation"></a>
# **updateWorkerReservation**
> TaskrouterV1WorkspaceWorkerWorkerReservation updateWorkerReservation(workspaceSid, workerSid, sid, ifMatch, beep, beepOnCustomerEntrance, callAccept, callFrom, callRecord, callStatusCallbackUrl, callTimeout, callTo, callUrl, conferenceRecord, conferenceRecordingStatusCallback, conferenceRecordingStatusCallbackMethod, conferenceStatusCallback, conferenceStatusCallbackEvent, conferenceStatusCallbackMethod, conferenceTrim, dequeueFrom, dequeuePostWorkActivitySid, dequeueRecord, dequeueStatusCallbackEvent, dequeueStatusCallbackUrl, dequeueTimeout, dequeueTo, earlyMedia, endConferenceOnCustomerExit, endConferenceOnExit, from, instruction, jitterBufferSize, maxParticipants, muted, postWorkActivitySid, record, recordingChannels, recordingStatusCallback, recordingStatusCallbackMethod, redirectAccept, redirectCallSid, redirectUrl, region, reservationStatus, sipAuthPassword, sipAuthUsername, startConferenceOnEnter, statusCallback, statusCallbackEvent, statusCallbackMethod, timeout, to, waitMethod, waitUrl, workerActivitySid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaskrouterV1ReservationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://taskrouter.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TaskrouterV1ReservationApi apiInstance = new TaskrouterV1ReservationApi(defaultClient);
    String workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the WorkerReservation resources to update.
    String workerSid = "workerSid_example"; // String | The SID of the reserved Worker resource with the WorkerReservation resources to update.
    String sid = "sid_example"; // String | The SID of the WorkerReservation resource to update.
    String ifMatch = "ifMatch_example"; // String | The If-Match HTTP request header
    String beep = "beep_example"; // String | Whether to play a notification beep when the participant joins or when to play a beep. Can be: `true`, `false`, `onEnter`, or `onExit`. The default value is `true`.
    Boolean beepOnCustomerEntrance = true; // Boolean | Whether to play a notification beep when the customer joins.
    Boolean callAccept = true; // Boolean | Whether to accept a reservation when executing a Call instruction.
    String callFrom = "callFrom_example"; // String | The Caller ID of the outbound call when executing a Call instruction.
    String callRecord = "callRecord_example"; // String | Whether to record both legs of a call when executing a Call instruction.
    URI callStatusCallbackUrl = new URI(); // URI | The URL to call for the completed call event when executing a Call instruction.
    Integer callTimeout = 56; // Integer | The timeout for a call when executing a Call instruction.
    String callTo = "callTo_example"; // String | The contact URI of the worker when executing a Call instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination.
    URI callUrl = new URI(); // URI | TwiML URI executed on answering the worker's leg as a result of the Call instruction.
    String conferenceRecord = "conferenceRecord_example"; // String | Whether to record the conference the participant is joining or when to record the conference. Can be: `true`, `false`, `record-from-start`, and `do-not-record`. The default value is `false`.
    URI conferenceRecordingStatusCallback = new URI(); // URI | The URL we should call using the `conference_recording_status_callback_method` when the conference recording is available.
    String conferenceRecordingStatusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `conference_recording_status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
    URI conferenceStatusCallback = new URI(); // URI | The URL we should call using the `conference_status_callback_method` when the conference events in `conference_status_callback_event` occur. Only the value set by the first participant to join the conference is used. Subsequent `conference_status_callback` values are ignored.
    List<WorkerReservationEnumConferenceEvent> conferenceStatusCallbackEvent = Arrays.asList(); // List<WorkerReservationEnumConferenceEvent> | The conference status events that we will send to `conference_status_callback`. Can be: `start`, `end`, `join`, `leave`, `mute`, `hold`, `speaker`.
    String conferenceStatusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `conference_status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
    String conferenceTrim = "conferenceTrim_example"; // String | Whether to trim leading and trailing silence from your recorded conference audio files. Can be: `trim-silence` or `do-not-trim` and defaults to `trim-silence`.
    String dequeueFrom = "dequeueFrom_example"; // String | The caller ID of the call to the worker when executing a Dequeue instruction.
    String dequeuePostWorkActivitySid = "dequeuePostWorkActivitySid_example"; // String | The SID of the Activity resource to start after executing a Dequeue instruction.
    String dequeueRecord = "dequeueRecord_example"; // String | Whether to record both legs of a call when executing a Dequeue instruction or which leg to record.
    List<String> dequeueStatusCallbackEvent = Arrays.asList(); // List<String> | The call progress events sent via webhooks as a result of a Dequeue instruction.
    URI dequeueStatusCallbackUrl = new URI(); // URI | The callback URL for completed call event when executing a Dequeue instruction.
    Integer dequeueTimeout = 56; // Integer | The timeout for call when executing a Dequeue instruction.
    String dequeueTo = "dequeueTo_example"; // String | The contact URI of the worker when executing a Dequeue instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination.
    Boolean earlyMedia = true; // Boolean | Whether to allow an agent to hear the state of the outbound call, including ringing or disconnect messages. The default is `true`.
    Boolean endConferenceOnCustomerExit = true; // Boolean | Whether to end the conference when the customer leaves.
    Boolean endConferenceOnExit = true; // Boolean | Whether to end the conference when the agent leaves.
    String from = "from_example"; // String | The caller ID of the call to the worker when executing a Conference instruction.
    String instruction = "instruction_example"; // String | The assignment instruction for the reservation.
    String jitterBufferSize = "jitterBufferSize_example"; // String | The jitter buffer size for conference. Can be: `small`, `medium`, `large`, `off`.
    Integer maxParticipants = 56; // Integer | The maximum number of participants allowed in the conference. Can be a positive integer from `2` to `250`. The default value is `250`.
    Boolean muted = true; // Boolean | Whether the agent is muted in the conference. Defaults to `false`.
    String postWorkActivitySid = "postWorkActivitySid_example"; // String | The new worker activity SID after executing a Conference instruction.
    Boolean record = true; // Boolean | Whether to record the participant and their conferences, including the time between conferences. Can be `true` or `false` and the default is `false`.
    String recordingChannels = "recordingChannels_example"; // String | The recording channels for the final recording. Can be: `mono` or `dual` and the default is `mono`.
    URI recordingStatusCallback = new URI(); // URI | The URL that we should call using the `recording_status_callback_method` when the recording status changes.
    String recordingStatusCallbackMethod = "HEAD"; // String | The HTTP method we should use when we call `recording_status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
    Boolean redirectAccept = true; // Boolean | Whether the reservation should be accepted when executing a Redirect instruction.
    String redirectCallSid = "redirectCallSid_example"; // String | The Call SID of the call parked in the queue when executing a Redirect instruction.
    URI redirectUrl = new URI(); // URI | TwiML URI to redirect the call to when executing the Redirect instruction.
    String region = "region_example"; // String | The [region](https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls) where we should mix the recorded audio. Can be:`us1`, `ie1`, `de1`, `sg1`, `br1`, `au1`, or `jp1`.
    WorkerReservationEnumStatus reservationStatus = WorkerReservationEnumStatus.fromValue("pending"); // WorkerReservationEnumStatus | 
    String sipAuthPassword = "sipAuthPassword_example"; // String | The SIP password for authentication.
    String sipAuthUsername = "sipAuthUsername_example"; // String | The SIP username used for authentication.
    Boolean startConferenceOnEnter = true; // Boolean | Whether to start the conference when the participant joins, if it has not already started. Can be: `true` or `false` and the default is `true`. If `false` and the conference has not started, the participant is muted and hears background music until another participant starts the conference.
    URI statusCallback = new URI(); // URI | The URL we should call using the `status_callback_method` to send status information to your application.
    List<WorkerReservationEnumCallStatus> statusCallbackEvent = Arrays.asList(); // List<WorkerReservationEnumCallStatus> | The call progress events that we will send to `status_callback`. Can be: `initiated`, `ringing`, `answered`, or `completed`.
    String statusCallbackMethod = "HEAD"; // String | The HTTP method we should use to call `status_callback`. Can be: `POST` or `GET` and the default is `POST`.
    Integer timeout = 56; // Integer | The timeout for a call when executing a Conference instruction.
    String to = "to_example"; // String | The Contact URI of the worker when executing a Conference instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination.
    String waitMethod = "HEAD"; // String | The HTTP method we should use to call `wait_url`. Can be `GET` or `POST` and the default is `POST`. When using a static audio file, this should be `GET` so that we can cache the file.
    URI waitUrl = new URI(); // URI | The URL we should call using the `wait_method` for the music to play while participants are waiting for the conference to start. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic).
    String workerActivitySid = "workerActivitySid_example"; // String | The new worker activity SID if rejecting a reservation.
    try {
      TaskrouterV1WorkspaceWorkerWorkerReservation result = apiInstance.updateWorkerReservation(workspaceSid, workerSid, sid, ifMatch, beep, beepOnCustomerEntrance, callAccept, callFrom, callRecord, callStatusCallbackUrl, callTimeout, callTo, callUrl, conferenceRecord, conferenceRecordingStatusCallback, conferenceRecordingStatusCallbackMethod, conferenceStatusCallback, conferenceStatusCallbackEvent, conferenceStatusCallbackMethod, conferenceTrim, dequeueFrom, dequeuePostWorkActivitySid, dequeueRecord, dequeueStatusCallbackEvent, dequeueStatusCallbackUrl, dequeueTimeout, dequeueTo, earlyMedia, endConferenceOnCustomerExit, endConferenceOnExit, from, instruction, jitterBufferSize, maxParticipants, muted, postWorkActivitySid, record, recordingChannels, recordingStatusCallback, recordingStatusCallbackMethod, redirectAccept, redirectCallSid, redirectUrl, region, reservationStatus, sipAuthPassword, sipAuthUsername, startConferenceOnEnter, statusCallback, statusCallbackEvent, statusCallbackMethod, timeout, to, waitMethod, waitUrl, workerActivitySid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaskrouterV1ReservationApi#updateWorkerReservation");
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
| **workspaceSid** | **String**| The SID of the Workspace with the WorkerReservation resources to update. | |
| **workerSid** | **String**| The SID of the reserved Worker resource with the WorkerReservation resources to update. | |
| **sid** | **String**| The SID of the WorkerReservation resource to update. | |
| **ifMatch** | **String**| The If-Match HTTP request header | [optional] |
| **beep** | **String**| Whether to play a notification beep when the participant joins or when to play a beep. Can be: &#x60;true&#x60;, &#x60;false&#x60;, &#x60;onEnter&#x60;, or &#x60;onExit&#x60;. The default value is &#x60;true&#x60;. | [optional] |
| **beepOnCustomerEntrance** | **Boolean**| Whether to play a notification beep when the customer joins. | [optional] |
| **callAccept** | **Boolean**| Whether to accept a reservation when executing a Call instruction. | [optional] |
| **callFrom** | **String**| The Caller ID of the outbound call when executing a Call instruction. | [optional] |
| **callRecord** | **String**| Whether to record both legs of a call when executing a Call instruction. | [optional] |
| **callStatusCallbackUrl** | **URI**| The URL to call for the completed call event when executing a Call instruction. | [optional] |
| **callTimeout** | **Integer**| The timeout for a call when executing a Call instruction. | [optional] |
| **callTo** | **String**| The contact URI of the worker when executing a Call instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination. | [optional] |
| **callUrl** | **URI**| TwiML URI executed on answering the worker&#39;s leg as a result of the Call instruction. | [optional] |
| **conferenceRecord** | **String**| Whether to record the conference the participant is joining or when to record the conference. Can be: &#x60;true&#x60;, &#x60;false&#x60;, &#x60;record-from-start&#x60;, and &#x60;do-not-record&#x60;. The default value is &#x60;false&#x60;. | [optional] |
| **conferenceRecordingStatusCallback** | **URI**| The URL we should call using the &#x60;conference_recording_status_callback_method&#x60; when the conference recording is available. | [optional] |
| **conferenceRecordingStatusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;conference_recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **conferenceStatusCallback** | **URI**| The URL we should call using the &#x60;conference_status_callback_method&#x60; when the conference events in &#x60;conference_status_callback_event&#x60; occur. Only the value set by the first participant to join the conference is used. Subsequent &#x60;conference_status_callback&#x60; values are ignored. | [optional] |
| **conferenceStatusCallbackEvent** | [**List&lt;WorkerReservationEnumConferenceEvent&gt;**](WorkerReservationEnumConferenceEvent.md)| The conference status events that we will send to &#x60;conference_status_callback&#x60;. Can be: &#x60;start&#x60;, &#x60;end&#x60;, &#x60;join&#x60;, &#x60;leave&#x60;, &#x60;mute&#x60;, &#x60;hold&#x60;, &#x60;speaker&#x60;. | [optional] |
| **conferenceStatusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;conference_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **conferenceTrim** | **String**| Whether to trim leading and trailing silence from your recorded conference audio files. Can be: &#x60;trim-silence&#x60; or &#x60;do-not-trim&#x60; and defaults to &#x60;trim-silence&#x60;. | [optional] |
| **dequeueFrom** | **String**| The caller ID of the call to the worker when executing a Dequeue instruction. | [optional] |
| **dequeuePostWorkActivitySid** | **String**| The SID of the Activity resource to start after executing a Dequeue instruction. | [optional] |
| **dequeueRecord** | **String**| Whether to record both legs of a call when executing a Dequeue instruction or which leg to record. | [optional] |
| **dequeueStatusCallbackEvent** | [**List&lt;String&gt;**](String.md)| The call progress events sent via webhooks as a result of a Dequeue instruction. | [optional] |
| **dequeueStatusCallbackUrl** | **URI**| The callback URL for completed call event when executing a Dequeue instruction. | [optional] |
| **dequeueTimeout** | **Integer**| The timeout for call when executing a Dequeue instruction. | [optional] |
| **dequeueTo** | **String**| The contact URI of the worker when executing a Dequeue instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination. | [optional] |
| **earlyMedia** | **Boolean**| Whether to allow an agent to hear the state of the outbound call, including ringing or disconnect messages. The default is &#x60;true&#x60;. | [optional] |
| **endConferenceOnCustomerExit** | **Boolean**| Whether to end the conference when the customer leaves. | [optional] |
| **endConferenceOnExit** | **Boolean**| Whether to end the conference when the agent leaves. | [optional] |
| **from** | **String**| The caller ID of the call to the worker when executing a Conference instruction. | [optional] |
| **instruction** | **String**| The assignment instruction for the reservation. | [optional] |
| **jitterBufferSize** | **String**| The jitter buffer size for conference. Can be: &#x60;small&#x60;, &#x60;medium&#x60;, &#x60;large&#x60;, &#x60;off&#x60;. | [optional] |
| **maxParticipants** | **Integer**| The maximum number of participants allowed in the conference. Can be a positive integer from &#x60;2&#x60; to &#x60;250&#x60;. The default value is &#x60;250&#x60;. | [optional] |
| **muted** | **Boolean**| Whether the agent is muted in the conference. Defaults to &#x60;false&#x60;. | [optional] |
| **postWorkActivitySid** | **String**| The new worker activity SID after executing a Conference instruction. | [optional] |
| **record** | **Boolean**| Whether to record the participant and their conferences, including the time between conferences. Can be &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional] |
| **recordingChannels** | **String**| The recording channels for the final recording. Can be: &#x60;mono&#x60; or &#x60;dual&#x60; and the default is &#x60;mono&#x60;. | [optional] |
| **recordingStatusCallback** | **URI**| The URL that we should call using the &#x60;recording_status_callback_method&#x60; when the recording status changes. | [optional] |
| **recordingStatusCallbackMethod** | **String**| The HTTP method we should use when we call &#x60;recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **redirectAccept** | **Boolean**| Whether the reservation should be accepted when executing a Redirect instruction. | [optional] |
| **redirectCallSid** | **String**| The Call SID of the call parked in the queue when executing a Redirect instruction. | [optional] |
| **redirectUrl** | **URI**| TwiML URI to redirect the call to when executing the Redirect instruction. | [optional] |
| **region** | **String**| The [region](https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls) where we should mix the recorded audio. Can be:&#x60;us1&#x60;, &#x60;ie1&#x60;, &#x60;de1&#x60;, &#x60;sg1&#x60;, &#x60;br1&#x60;, &#x60;au1&#x60;, or &#x60;jp1&#x60;. | [optional] |
| **reservationStatus** | **WorkerReservationEnumStatus**|  | [optional] [enum: pending, accepted, rejected, timeout, canceled, rescinded, wrapping, completed] |
| **sipAuthPassword** | **String**| The SIP password for authentication. | [optional] |
| **sipAuthUsername** | **String**| The SIP username used for authentication. | [optional] |
| **startConferenceOnEnter** | **Boolean**| Whether to start the conference when the participant joins, if it has not already started. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. If &#x60;false&#x60; and the conference has not started, the participant is muted and hears background music until another participant starts the conference. | [optional] |
| **statusCallback** | **URI**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional] |
| **statusCallbackEvent** | [**List&lt;WorkerReservationEnumCallStatus&gt;**](WorkerReservationEnumCallStatus.md)| The call progress events that we will send to &#x60;status_callback&#x60;. Can be: &#x60;initiated&#x60;, &#x60;ringing&#x60;, &#x60;answered&#x60;, or &#x60;completed&#x60;. | [optional] |
| **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **timeout** | **Integer**| The timeout for a call when executing a Conference instruction. | [optional] |
| **to** | **String**| The Contact URI of the worker when executing a Conference instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination. | [optional] |
| **waitMethod** | **String**| The HTTP method we should use to call &#x60;wait_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. When using a static audio file, this should be &#x60;GET&#x60; so that we can cache the file. | [optional] [enum: HEAD, GET, POST, PATCH, PUT, DELETE] |
| **waitUrl** | **URI**| The URL we should call using the &#x60;wait_method&#x60; for the music to play while participants are waiting for the conference to start. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic). | [optional] |
| **workerActivitySid** | **String**| The new worker activity SID if rejecting a reservation. | [optional] |

### Return type

[**TaskrouterV1WorkspaceWorkerWorkerReservation**](TaskrouterV1WorkspaceWorkerWorkerReservation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

