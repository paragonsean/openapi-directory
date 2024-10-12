# TwilioTaskrouter.TaskrouterV1ReservationApi

All URIs are relative to *https://taskrouter.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchTaskReservation**](TaskrouterV1ReservationApi.md#fetchTaskReservation) | **GET** /v1/Workspaces/{WorkspaceSid}/Tasks/{TaskSid}/Reservations/{Sid} | 
[**fetchWorkerReservation**](TaskrouterV1ReservationApi.md#fetchWorkerReservation) | **GET** /v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Reservations/{Sid} | 
[**listTaskReservation**](TaskrouterV1ReservationApi.md#listTaskReservation) | **GET** /v1/Workspaces/{WorkspaceSid}/Tasks/{TaskSid}/Reservations | 
[**listWorkerReservation**](TaskrouterV1ReservationApi.md#listWorkerReservation) | **GET** /v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Reservations | 
[**updateTaskReservation**](TaskrouterV1ReservationApi.md#updateTaskReservation) | **POST** /v1/Workspaces/{WorkspaceSid}/Tasks/{TaskSid}/Reservations/{Sid} | 
[**updateWorkerReservation**](TaskrouterV1ReservationApi.md#updateWorkerReservation) | **POST** /v1/Workspaces/{WorkspaceSid}/Workers/{WorkerSid}/Reservations/{Sid} | 



## fetchTaskReservation

> TaskrouterV1WorkspaceTaskTaskReservation fetchTaskReservation(workspaceSid, taskSid, sid)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1ReservationApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskReservation resource to fetch.
let taskSid = "taskSid_example"; // String | The SID of the reserved Task resource with the TaskReservation resource to fetch.
let sid = "sid_example"; // String | The SID of the TaskReservation resource to fetch.
apiInstance.fetchTaskReservation(workspaceSid, taskSid, sid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspaceSid** | **String**| The SID of the Workspace with the TaskReservation resource to fetch. | 
 **taskSid** | **String**| The SID of the reserved Task resource with the TaskReservation resource to fetch. | 
 **sid** | **String**| The SID of the TaskReservation resource to fetch. | 

### Return type

[**TaskrouterV1WorkspaceTaskTaskReservation**](TaskrouterV1WorkspaceTaskTaskReservation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchWorkerReservation

> TaskrouterV1WorkspaceWorkerWorkerReservation fetchWorkerReservation(workspaceSid, workerSid, sid)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1ReservationApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the WorkerReservation resource to fetch.
let workerSid = "workerSid_example"; // String | The SID of the reserved Worker resource with the WorkerReservation resource to fetch.
let sid = "sid_example"; // String | The SID of the WorkerReservation resource to fetch.
apiInstance.fetchWorkerReservation(workspaceSid, workerSid, sid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspaceSid** | **String**| The SID of the Workspace with the WorkerReservation resource to fetch. | 
 **workerSid** | **String**| The SID of the reserved Worker resource with the WorkerReservation resource to fetch. | 
 **sid** | **String**| The SID of the WorkerReservation resource to fetch. | 

### Return type

[**TaskrouterV1WorkspaceWorkerWorkerReservation**](TaskrouterV1WorkspaceWorkerWorkerReservation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTaskReservation

> ListTaskReservationResponse listTaskReservation(workspaceSid, taskSid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1ReservationApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskReservation resources to read.
let taskSid = "taskSid_example"; // String | The SID of the reserved Task resource with the TaskReservation resources to read.
let opts = {
  'reservationStatus': "reservationStatus_example", // TaskReservationEnumStatus | Returns the list of reservations for a task with a specified ReservationStatus.  Can be: `pending`, `accepted`, `rejected`, or `timeout`.
  'workerSid': "workerSid_example", // String | The SID of the reserved Worker resource to read.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listTaskReservation(workspaceSid, taskSid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspaceSid** | **String**| The SID of the Workspace with the TaskReservation resources to read. | 
 **taskSid** | **String**| The SID of the reserved Task resource with the TaskReservation resources to read. | 
 **reservationStatus** | **TaskReservationEnumStatus**| Returns the list of reservations for a task with a specified ReservationStatus.  Can be: &#x60;pending&#x60;, &#x60;accepted&#x60;, &#x60;rejected&#x60;, or &#x60;timeout&#x60;. | [optional] 
 **workerSid** | **String**| The SID of the reserved Worker resource to read. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListTaskReservationResponse**](ListTaskReservationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWorkerReservation

> ListWorkerReservationResponse listWorkerReservation(workspaceSid, workerSid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1ReservationApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the WorkerReservation resources to read.
let workerSid = "workerSid_example"; // String | The SID of the reserved Worker resource with the WorkerReservation resources to read.
let opts = {
  'reservationStatus': "reservationStatus_example", // WorkerReservationEnumStatus | Returns the list of reservations for a worker with a specified ReservationStatus. Can be: `pending`, `accepted`, `rejected`, `timeout`, `canceled`, or `rescinded`.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listWorkerReservation(workspaceSid, workerSid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspaceSid** | **String**| The SID of the Workspace with the WorkerReservation resources to read. | 
 **workerSid** | **String**| The SID of the reserved Worker resource with the WorkerReservation resources to read. | 
 **reservationStatus** | **WorkerReservationEnumStatus**| Returns the list of reservations for a worker with a specified ReservationStatus. Can be: &#x60;pending&#x60;, &#x60;accepted&#x60;, &#x60;rejected&#x60;, &#x60;timeout&#x60;, &#x60;canceled&#x60;, or &#x60;rescinded&#x60;. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListWorkerReservationResponse**](ListWorkerReservationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTaskReservation

> TaskrouterV1WorkspaceTaskTaskReservation updateTaskReservation(workspaceSid, taskSid, sid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1ReservationApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the TaskReservation resources to update.
let taskSid = "taskSid_example"; // String | The SID of the reserved Task resource with the TaskReservation resources to update.
let sid = "sid_example"; // String | The SID of the TaskReservation resource to update.
let opts = {
  'ifMatch': "ifMatch_example", // String | The If-Match HTTP request header
  'beep': "beep_example", // String | Whether to play a notification beep when the participant joins or when to play a beep. Can be: `true`, `false`, `onEnter`, or `onExit`. The default value is `true`.
  'beepOnCustomerEntrance': true, // Boolean | Whether to play a notification beep when the customer joins.
  'callAccept': true, // Boolean | Whether to accept a reservation when executing a Call instruction.
  'callFrom': "callFrom_example", // String | The Caller ID of the outbound call when executing a Call instruction.
  'callRecord': "callRecord_example", // String | Whether to record both legs of a call when executing a Call instruction or which leg to record.
  'callStatusCallbackUrl': "callStatusCallbackUrl_example", // String | The URL to call  for the completed call event when executing a Call instruction.
  'callTimeout': 56, // Number | Timeout for call when executing a Call instruction.
  'callTo': "callTo_example", // String | The Contact URI of the worker when executing a Call instruction.  Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination.
  'callUrl': "callUrl_example", // String | TwiML URI executed on answering the worker's leg as a result of the Call instruction.
  'conferenceRecord': "conferenceRecord_example", // String | Whether to record the conference the participant is joining or when to record the conference. Can be: `true`, `false`, `record-from-start`, and `do-not-record`. The default value is `false`.
  'conferenceRecordingStatusCallback': "conferenceRecordingStatusCallback_example", // String | The URL we should call using the `conference_recording_status_callback_method` when the conference recording is available.
  'conferenceRecordingStatusCallbackMethod': "conferenceRecordingStatusCallbackMethod_example", // String | The HTTP method we should use to call `conference_recording_status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
  'conferenceStatusCallback': "conferenceStatusCallback_example", // String | The URL we should call using the `conference_status_callback_method` when the conference events in `conference_status_callback_event` occur. Only the value set by the first participant to join the conference is used. Subsequent `conference_status_callback` values are ignored.
  'conferenceStatusCallbackEvent': ["null"], // [TaskReservationEnumConferenceEvent] | The conference status events that we will send to `conference_status_callback`. Can be: `start`, `end`, `join`, `leave`, `mute`, `hold`, `speaker`.
  'conferenceStatusCallbackMethod': "conferenceStatusCallbackMethod_example", // String | The HTTP method we should use to call `conference_status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
  'conferenceTrim': "conferenceTrim_example", // String | How to trim the leading and trailing silence from your recorded conference audio files. Can be: `trim-silence` or `do-not-trim` and defaults to `trim-silence`.
  'dequeueFrom': "dequeueFrom_example", // String | The Caller ID of the call to the worker when executing a Dequeue instruction.
  'dequeuePostWorkActivitySid': "dequeuePostWorkActivitySid_example", // String | The SID of the Activity resource to start after executing a Dequeue instruction.
  'dequeueRecord': "dequeueRecord_example", // String | Whether to record both legs of a call when executing a Dequeue instruction or which leg to record.
  'dequeueStatusCallbackEvent': ["null"], // [String] | The Call progress events sent via webhooks as a result of a Dequeue instruction.
  'dequeueStatusCallbackUrl': "dequeueStatusCallbackUrl_example", // String | The Callback URL for completed call event when executing a Dequeue instruction.
  'dequeueTimeout': 56, // Number | Timeout for call when executing a Dequeue instruction.
  'dequeueTo': "dequeueTo_example", // String | The Contact URI of the worker when executing a Dequeue instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination.
  'earlyMedia': true, // Boolean | Whether to allow an agent to hear the state of the outbound call, including ringing or disconnect messages. The default is `true`.
  'endConferenceOnCustomerExit': true, // Boolean | Whether to end the conference when the customer leaves.
  'endConferenceOnExit': true, // Boolean | Whether to end the conference when the agent leaves.
  'from': "from_example", // String | The Caller ID of the call to the worker when executing a Conference instruction.
  'instruction': "instruction_example", // String | The assignment instruction for reservation.
  'jitterBufferSize': "jitterBufferSize_example", // String | The jitter buffer size for conference. Can be: `small`, `medium`, `large`, `off`.
  'maxParticipants': 56, // Number | The maximum number of participants in the conference. Can be a positive integer from `2` to `250`. The default value is `250`.
  'muted': true, // Boolean | Whether the agent is muted in the conference. The default is `false`.
  'postWorkActivitySid': "postWorkActivitySid_example", // String | The new worker activity SID after executing a Conference instruction.
  'record': true, // Boolean | Whether to record the participant and their conferences, including the time between conferences. The default is `false`.
  'recordingChannels': "recordingChannels_example", // String | The recording channels for the final recording. Can be: `mono` or `dual` and the default is `mono`.
  'recordingStatusCallback': "recordingStatusCallback_example", // String | The URL that we should call using the `recording_status_callback_method` when the recording status changes.
  'recordingStatusCallbackMethod': "recordingStatusCallbackMethod_example", // String | The HTTP method we should use when we call `recording_status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
  'redirectAccept': true, // Boolean | Whether the reservation should be accepted when executing a Redirect instruction.
  'redirectCallSid': "redirectCallSid_example", // String | The Call SID of the call parked in the queue when executing a Redirect instruction.
  'redirectUrl': "redirectUrl_example", // String | TwiML URI to redirect the call to when executing the Redirect instruction.
  'region': "region_example", // String | The [region](https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls) where we should mix the recorded audio. Can be:`us1`, `ie1`, `de1`, `sg1`, `br1`, `au1`, or `jp1`.
  'reservationStatus': "reservationStatus_example", // TaskReservationEnumStatus | 
  'sipAuthPassword': "sipAuthPassword_example", // String | The SIP password for authentication.
  'sipAuthUsername': "sipAuthUsername_example", // String | The SIP username used for authentication.
  'startConferenceOnEnter': true, // Boolean | Whether to start the conference when the participant joins, if it has not already started. The default is `true`. If `false` and the conference has not started, the participant is muted and hears background music until another participant starts the conference.
  'statusCallback': "statusCallback_example", // String | The URL we should call using the `status_callback_method` to send status information to your application.
  'statusCallbackEvent': ["null"], // [TaskReservationEnumCallStatus] | The call progress events that we will send to `status_callback`. Can be: `initiated`, `ringing`, `answered`, or `completed`.
  'statusCallbackMethod': "statusCallbackMethod_example", // String | The HTTP method we should use to call `status_callback`. Can be: `POST` or `GET` and the default is `POST`.
  'supervisor': "supervisor_example", // String | The Supervisor SID/URI when executing the Supervise instruction.
  'supervisorMode': "supervisorMode_example", // TaskReservationEnumSupervisorMode | 
  'timeout': 56, // Number | Timeout for call when executing a Conference instruction.
  'to': "to_example", // String | The Contact URI of the worker when executing a Conference instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination.
  'waitMethod': "waitMethod_example", // String | The HTTP method we should use to call `wait_url`. Can be `GET` or `POST` and the default is `POST`. When using a static audio file, this should be `GET` so that we can cache the file.
  'waitUrl': "waitUrl_example", // String | The URL we should call using the `wait_method` for the music to play while participants are waiting for the conference to start. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic).
  'workerActivitySid': "workerActivitySid_example" // String | The new worker activity SID if rejecting a reservation.
};
apiInstance.updateTaskReservation(workspaceSid, taskSid, sid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspaceSid** | **String**| The SID of the Workspace with the TaskReservation resources to update. | 
 **taskSid** | **String**| The SID of the reserved Task resource with the TaskReservation resources to update. | 
 **sid** | **String**| The SID of the TaskReservation resource to update. | 
 **ifMatch** | **String**| The If-Match HTTP request header | [optional] 
 **beep** | **String**| Whether to play a notification beep when the participant joins or when to play a beep. Can be: &#x60;true&#x60;, &#x60;false&#x60;, &#x60;onEnter&#x60;, or &#x60;onExit&#x60;. The default value is &#x60;true&#x60;. | [optional] 
 **beepOnCustomerEntrance** | **Boolean**| Whether to play a notification beep when the customer joins. | [optional] 
 **callAccept** | **Boolean**| Whether to accept a reservation when executing a Call instruction. | [optional] 
 **callFrom** | **String**| The Caller ID of the outbound call when executing a Call instruction. | [optional] 
 **callRecord** | **String**| Whether to record both legs of a call when executing a Call instruction or which leg to record. | [optional] 
 **callStatusCallbackUrl** | **String**| The URL to call  for the completed call event when executing a Call instruction. | [optional] 
 **callTimeout** | **Number**| Timeout for call when executing a Call instruction. | [optional] 
 **callTo** | **String**| The Contact URI of the worker when executing a Call instruction.  Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination. | [optional] 
 **callUrl** | **String**| TwiML URI executed on answering the worker&#39;s leg as a result of the Call instruction. | [optional] 
 **conferenceRecord** | **String**| Whether to record the conference the participant is joining or when to record the conference. Can be: &#x60;true&#x60;, &#x60;false&#x60;, &#x60;record-from-start&#x60;, and &#x60;do-not-record&#x60;. The default value is &#x60;false&#x60;. | [optional] 
 **conferenceRecordingStatusCallback** | **String**| The URL we should call using the &#x60;conference_recording_status_callback_method&#x60; when the conference recording is available. | [optional] 
 **conferenceRecordingStatusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;conference_recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] 
 **conferenceStatusCallback** | **String**| The URL we should call using the &#x60;conference_status_callback_method&#x60; when the conference events in &#x60;conference_status_callback_event&#x60; occur. Only the value set by the first participant to join the conference is used. Subsequent &#x60;conference_status_callback&#x60; values are ignored. | [optional] 
 **conferenceStatusCallbackEvent** | [**[TaskReservationEnumConferenceEvent]**](TaskReservationEnumConferenceEvent.md)| The conference status events that we will send to &#x60;conference_status_callback&#x60;. Can be: &#x60;start&#x60;, &#x60;end&#x60;, &#x60;join&#x60;, &#x60;leave&#x60;, &#x60;mute&#x60;, &#x60;hold&#x60;, &#x60;speaker&#x60;. | [optional] 
 **conferenceStatusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;conference_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] 
 **conferenceTrim** | **String**| How to trim the leading and trailing silence from your recorded conference audio files. Can be: &#x60;trim-silence&#x60; or &#x60;do-not-trim&#x60; and defaults to &#x60;trim-silence&#x60;. | [optional] 
 **dequeueFrom** | **String**| The Caller ID of the call to the worker when executing a Dequeue instruction. | [optional] 
 **dequeuePostWorkActivitySid** | **String**| The SID of the Activity resource to start after executing a Dequeue instruction. | [optional] 
 **dequeueRecord** | **String**| Whether to record both legs of a call when executing a Dequeue instruction or which leg to record. | [optional] 
 **dequeueStatusCallbackEvent** | [**[String]**](String.md)| The Call progress events sent via webhooks as a result of a Dequeue instruction. | [optional] 
 **dequeueStatusCallbackUrl** | **String**| The Callback URL for completed call event when executing a Dequeue instruction. | [optional] 
 **dequeueTimeout** | **Number**| Timeout for call when executing a Dequeue instruction. | [optional] 
 **dequeueTo** | **String**| The Contact URI of the worker when executing a Dequeue instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination. | [optional] 
 **earlyMedia** | **Boolean**| Whether to allow an agent to hear the state of the outbound call, including ringing or disconnect messages. The default is &#x60;true&#x60;. | [optional] 
 **endConferenceOnCustomerExit** | **Boolean**| Whether to end the conference when the customer leaves. | [optional] 
 **endConferenceOnExit** | **Boolean**| Whether to end the conference when the agent leaves. | [optional] 
 **from** | **String**| The Caller ID of the call to the worker when executing a Conference instruction. | [optional] 
 **instruction** | **String**| The assignment instruction for reservation. | [optional] 
 **jitterBufferSize** | **String**| The jitter buffer size for conference. Can be: &#x60;small&#x60;, &#x60;medium&#x60;, &#x60;large&#x60;, &#x60;off&#x60;. | [optional] 
 **maxParticipants** | **Number**| The maximum number of participants in the conference. Can be a positive integer from &#x60;2&#x60; to &#x60;250&#x60;. The default value is &#x60;250&#x60;. | [optional] 
 **muted** | **Boolean**| Whether the agent is muted in the conference. The default is &#x60;false&#x60;. | [optional] 
 **postWorkActivitySid** | **String**| The new worker activity SID after executing a Conference instruction. | [optional] 
 **record** | **Boolean**| Whether to record the participant and their conferences, including the time between conferences. The default is &#x60;false&#x60;. | [optional] 
 **recordingChannels** | **String**| The recording channels for the final recording. Can be: &#x60;mono&#x60; or &#x60;dual&#x60; and the default is &#x60;mono&#x60;. | [optional] 
 **recordingStatusCallback** | **String**| The URL that we should call using the &#x60;recording_status_callback_method&#x60; when the recording status changes. | [optional] 
 **recordingStatusCallbackMethod** | **String**| The HTTP method we should use when we call &#x60;recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] 
 **redirectAccept** | **Boolean**| Whether the reservation should be accepted when executing a Redirect instruction. | [optional] 
 **redirectCallSid** | **String**| The Call SID of the call parked in the queue when executing a Redirect instruction. | [optional] 
 **redirectUrl** | **String**| TwiML URI to redirect the call to when executing the Redirect instruction. | [optional] 
 **region** | **String**| The [region](https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls) where we should mix the recorded audio. Can be:&#x60;us1&#x60;, &#x60;ie1&#x60;, &#x60;de1&#x60;, &#x60;sg1&#x60;, &#x60;br1&#x60;, &#x60;au1&#x60;, or &#x60;jp1&#x60;. | [optional] 
 **reservationStatus** | **TaskReservationEnumStatus**|  | [optional] 
 **sipAuthPassword** | **String**| The SIP password for authentication. | [optional] 
 **sipAuthUsername** | **String**| The SIP username used for authentication. | [optional] 
 **startConferenceOnEnter** | **Boolean**| Whether to start the conference when the participant joins, if it has not already started. The default is &#x60;true&#x60;. If &#x60;false&#x60; and the conference has not started, the participant is muted and hears background music until another participant starts the conference. | [optional] 
 **statusCallback** | **String**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional] 
 **statusCallbackEvent** | [**[TaskReservationEnumCallStatus]**](TaskReservationEnumCallStatus.md)| The call progress events that we will send to &#x60;status_callback&#x60;. Can be: &#x60;initiated&#x60;, &#x60;ringing&#x60;, &#x60;answered&#x60;, or &#x60;completed&#x60;. | [optional] 
 **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. | [optional] 
 **supervisor** | **String**| The Supervisor SID/URI when executing the Supervise instruction. | [optional] 
 **supervisorMode** | **TaskReservationEnumSupervisorMode**|  | [optional] 
 **timeout** | **Number**| Timeout for call when executing a Conference instruction. | [optional] 
 **to** | **String**| The Contact URI of the worker when executing a Conference instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination. | [optional] 
 **waitMethod** | **String**| The HTTP method we should use to call &#x60;wait_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. When using a static audio file, this should be &#x60;GET&#x60; so that we can cache the file. | [optional] 
 **waitUrl** | **String**| The URL we should call using the &#x60;wait_method&#x60; for the music to play while participants are waiting for the conference to start. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic). | [optional] 
 **workerActivitySid** | **String**| The new worker activity SID if rejecting a reservation. | [optional] 

### Return type

[**TaskrouterV1WorkspaceTaskTaskReservation**](TaskrouterV1WorkspaceTaskTaskReservation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## updateWorkerReservation

> TaskrouterV1WorkspaceWorkerWorkerReservation updateWorkerReservation(workspaceSid, workerSid, sid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1ReservationApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the WorkerReservation resources to update.
let workerSid = "workerSid_example"; // String | The SID of the reserved Worker resource with the WorkerReservation resources to update.
let sid = "sid_example"; // String | The SID of the WorkerReservation resource to update.
let opts = {
  'ifMatch': "ifMatch_example", // String | The If-Match HTTP request header
  'beep': "beep_example", // String | Whether to play a notification beep when the participant joins or when to play a beep. Can be: `true`, `false`, `onEnter`, or `onExit`. The default value is `true`.
  'beepOnCustomerEntrance': true, // Boolean | Whether to play a notification beep when the customer joins.
  'callAccept': true, // Boolean | Whether to accept a reservation when executing a Call instruction.
  'callFrom': "callFrom_example", // String | The Caller ID of the outbound call when executing a Call instruction.
  'callRecord': "callRecord_example", // String | Whether to record both legs of a call when executing a Call instruction.
  'callStatusCallbackUrl': "callStatusCallbackUrl_example", // String | The URL to call for the completed call event when executing a Call instruction.
  'callTimeout': 56, // Number | The timeout for a call when executing a Call instruction.
  'callTo': "callTo_example", // String | The contact URI of the worker when executing a Call instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination.
  'callUrl': "callUrl_example", // String | TwiML URI executed on answering the worker's leg as a result of the Call instruction.
  'conferenceRecord': "conferenceRecord_example", // String | Whether to record the conference the participant is joining or when to record the conference. Can be: `true`, `false`, `record-from-start`, and `do-not-record`. The default value is `false`.
  'conferenceRecordingStatusCallback': "conferenceRecordingStatusCallback_example", // String | The URL we should call using the `conference_recording_status_callback_method` when the conference recording is available.
  'conferenceRecordingStatusCallbackMethod': "conferenceRecordingStatusCallbackMethod_example", // String | The HTTP method we should use to call `conference_recording_status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
  'conferenceStatusCallback': "conferenceStatusCallback_example", // String | The URL we should call using the `conference_status_callback_method` when the conference events in `conference_status_callback_event` occur. Only the value set by the first participant to join the conference is used. Subsequent `conference_status_callback` values are ignored.
  'conferenceStatusCallbackEvent': ["null"], // [WorkerReservationEnumConferenceEvent] | The conference status events that we will send to `conference_status_callback`. Can be: `start`, `end`, `join`, `leave`, `mute`, `hold`, `speaker`.
  'conferenceStatusCallbackMethod': "conferenceStatusCallbackMethod_example", // String | The HTTP method we should use to call `conference_status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
  'conferenceTrim': "conferenceTrim_example", // String | Whether to trim leading and trailing silence from your recorded conference audio files. Can be: `trim-silence` or `do-not-trim` and defaults to `trim-silence`.
  'dequeueFrom': "dequeueFrom_example", // String | The caller ID of the call to the worker when executing a Dequeue instruction.
  'dequeuePostWorkActivitySid': "dequeuePostWorkActivitySid_example", // String | The SID of the Activity resource to start after executing a Dequeue instruction.
  'dequeueRecord': "dequeueRecord_example", // String | Whether to record both legs of a call when executing a Dequeue instruction or which leg to record.
  'dequeueStatusCallbackEvent': ["null"], // [String] | The call progress events sent via webhooks as a result of a Dequeue instruction.
  'dequeueStatusCallbackUrl': "dequeueStatusCallbackUrl_example", // String | The callback URL for completed call event when executing a Dequeue instruction.
  'dequeueTimeout': 56, // Number | The timeout for call when executing a Dequeue instruction.
  'dequeueTo': "dequeueTo_example", // String | The contact URI of the worker when executing a Dequeue instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination.
  'earlyMedia': true, // Boolean | Whether to allow an agent to hear the state of the outbound call, including ringing or disconnect messages. The default is `true`.
  'endConferenceOnCustomerExit': true, // Boolean | Whether to end the conference when the customer leaves.
  'endConferenceOnExit': true, // Boolean | Whether to end the conference when the agent leaves.
  'from': "from_example", // String | The caller ID of the call to the worker when executing a Conference instruction.
  'instruction': "instruction_example", // String | The assignment instruction for the reservation.
  'jitterBufferSize': "jitterBufferSize_example", // String | The jitter buffer size for conference. Can be: `small`, `medium`, `large`, `off`.
  'maxParticipants': 56, // Number | The maximum number of participants allowed in the conference. Can be a positive integer from `2` to `250`. The default value is `250`.
  'muted': true, // Boolean | Whether the agent is muted in the conference. Defaults to `false`.
  'postWorkActivitySid': "postWorkActivitySid_example", // String | The new worker activity SID after executing a Conference instruction.
  'record': true, // Boolean | Whether to record the participant and their conferences, including the time between conferences. Can be `true` or `false` and the default is `false`.
  'recordingChannels': "recordingChannels_example", // String | The recording channels for the final recording. Can be: `mono` or `dual` and the default is `mono`.
  'recordingStatusCallback': "recordingStatusCallback_example", // String | The URL that we should call using the `recording_status_callback_method` when the recording status changes.
  'recordingStatusCallbackMethod': "recordingStatusCallbackMethod_example", // String | The HTTP method we should use when we call `recording_status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
  'redirectAccept': true, // Boolean | Whether the reservation should be accepted when executing a Redirect instruction.
  'redirectCallSid': "redirectCallSid_example", // String | The Call SID of the call parked in the queue when executing a Redirect instruction.
  'redirectUrl': "redirectUrl_example", // String | TwiML URI to redirect the call to when executing the Redirect instruction.
  'region': "region_example", // String | The [region](https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls) where we should mix the recorded audio. Can be:`us1`, `ie1`, `de1`, `sg1`, `br1`, `au1`, or `jp1`.
  'reservationStatus': "reservationStatus_example", // WorkerReservationEnumStatus | 
  'sipAuthPassword': "sipAuthPassword_example", // String | The SIP password for authentication.
  'sipAuthUsername': "sipAuthUsername_example", // String | The SIP username used for authentication.
  'startConferenceOnEnter': true, // Boolean | Whether to start the conference when the participant joins, if it has not already started. Can be: `true` or `false` and the default is `true`. If `false` and the conference has not started, the participant is muted and hears background music until another participant starts the conference.
  'statusCallback': "statusCallback_example", // String | The URL we should call using the `status_callback_method` to send status information to your application.
  'statusCallbackEvent': ["null"], // [WorkerReservationEnumCallStatus] | The call progress events that we will send to `status_callback`. Can be: `initiated`, `ringing`, `answered`, or `completed`.
  'statusCallbackMethod': "statusCallbackMethod_example", // String | The HTTP method we should use to call `status_callback`. Can be: `POST` or `GET` and the default is `POST`.
  'timeout': 56, // Number | The timeout for a call when executing a Conference instruction.
  'to': "to_example", // String | The Contact URI of the worker when executing a Conference instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination.
  'waitMethod': "waitMethod_example", // String | The HTTP method we should use to call `wait_url`. Can be `GET` or `POST` and the default is `POST`. When using a static audio file, this should be `GET` so that we can cache the file.
  'waitUrl': "waitUrl_example", // String | The URL we should call using the `wait_method` for the music to play while participants are waiting for the conference to start. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic).
  'workerActivitySid': "workerActivitySid_example" // String | The new worker activity SID if rejecting a reservation.
};
apiInstance.updateWorkerReservation(workspaceSid, workerSid, sid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspaceSid** | **String**| The SID of the Workspace with the WorkerReservation resources to update. | 
 **workerSid** | **String**| The SID of the reserved Worker resource with the WorkerReservation resources to update. | 
 **sid** | **String**| The SID of the WorkerReservation resource to update. | 
 **ifMatch** | **String**| The If-Match HTTP request header | [optional] 
 **beep** | **String**| Whether to play a notification beep when the participant joins or when to play a beep. Can be: &#x60;true&#x60;, &#x60;false&#x60;, &#x60;onEnter&#x60;, or &#x60;onExit&#x60;. The default value is &#x60;true&#x60;. | [optional] 
 **beepOnCustomerEntrance** | **Boolean**| Whether to play a notification beep when the customer joins. | [optional] 
 **callAccept** | **Boolean**| Whether to accept a reservation when executing a Call instruction. | [optional] 
 **callFrom** | **String**| The Caller ID of the outbound call when executing a Call instruction. | [optional] 
 **callRecord** | **String**| Whether to record both legs of a call when executing a Call instruction. | [optional] 
 **callStatusCallbackUrl** | **String**| The URL to call for the completed call event when executing a Call instruction. | [optional] 
 **callTimeout** | **Number**| The timeout for a call when executing a Call instruction. | [optional] 
 **callTo** | **String**| The contact URI of the worker when executing a Call instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination. | [optional] 
 **callUrl** | **String**| TwiML URI executed on answering the worker&#39;s leg as a result of the Call instruction. | [optional] 
 **conferenceRecord** | **String**| Whether to record the conference the participant is joining or when to record the conference. Can be: &#x60;true&#x60;, &#x60;false&#x60;, &#x60;record-from-start&#x60;, and &#x60;do-not-record&#x60;. The default value is &#x60;false&#x60;. | [optional] 
 **conferenceRecordingStatusCallback** | **String**| The URL we should call using the &#x60;conference_recording_status_callback_method&#x60; when the conference recording is available. | [optional] 
 **conferenceRecordingStatusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;conference_recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] 
 **conferenceStatusCallback** | **String**| The URL we should call using the &#x60;conference_status_callback_method&#x60; when the conference events in &#x60;conference_status_callback_event&#x60; occur. Only the value set by the first participant to join the conference is used. Subsequent &#x60;conference_status_callback&#x60; values are ignored. | [optional] 
 **conferenceStatusCallbackEvent** | [**[WorkerReservationEnumConferenceEvent]**](WorkerReservationEnumConferenceEvent.md)| The conference status events that we will send to &#x60;conference_status_callback&#x60;. Can be: &#x60;start&#x60;, &#x60;end&#x60;, &#x60;join&#x60;, &#x60;leave&#x60;, &#x60;mute&#x60;, &#x60;hold&#x60;, &#x60;speaker&#x60;. | [optional] 
 **conferenceStatusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;conference_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] 
 **conferenceTrim** | **String**| Whether to trim leading and trailing silence from your recorded conference audio files. Can be: &#x60;trim-silence&#x60; or &#x60;do-not-trim&#x60; and defaults to &#x60;trim-silence&#x60;. | [optional] 
 **dequeueFrom** | **String**| The caller ID of the call to the worker when executing a Dequeue instruction. | [optional] 
 **dequeuePostWorkActivitySid** | **String**| The SID of the Activity resource to start after executing a Dequeue instruction. | [optional] 
 **dequeueRecord** | **String**| Whether to record both legs of a call when executing a Dequeue instruction or which leg to record. | [optional] 
 **dequeueStatusCallbackEvent** | [**[String]**](String.md)| The call progress events sent via webhooks as a result of a Dequeue instruction. | [optional] 
 **dequeueStatusCallbackUrl** | **String**| The callback URL for completed call event when executing a Dequeue instruction. | [optional] 
 **dequeueTimeout** | **Number**| The timeout for call when executing a Dequeue instruction. | [optional] 
 **dequeueTo** | **String**| The contact URI of the worker when executing a Dequeue instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination. | [optional] 
 **earlyMedia** | **Boolean**| Whether to allow an agent to hear the state of the outbound call, including ringing or disconnect messages. The default is &#x60;true&#x60;. | [optional] 
 **endConferenceOnCustomerExit** | **Boolean**| Whether to end the conference when the customer leaves. | [optional] 
 **endConferenceOnExit** | **Boolean**| Whether to end the conference when the agent leaves. | [optional] 
 **from** | **String**| The caller ID of the call to the worker when executing a Conference instruction. | [optional] 
 **instruction** | **String**| The assignment instruction for the reservation. | [optional] 
 **jitterBufferSize** | **String**| The jitter buffer size for conference. Can be: &#x60;small&#x60;, &#x60;medium&#x60;, &#x60;large&#x60;, &#x60;off&#x60;. | [optional] 
 **maxParticipants** | **Number**| The maximum number of participants allowed in the conference. Can be a positive integer from &#x60;2&#x60; to &#x60;250&#x60;. The default value is &#x60;250&#x60;. | [optional] 
 **muted** | **Boolean**| Whether the agent is muted in the conference. Defaults to &#x60;false&#x60;. | [optional] 
 **postWorkActivitySid** | **String**| The new worker activity SID after executing a Conference instruction. | [optional] 
 **record** | **Boolean**| Whether to record the participant and their conferences, including the time between conferences. Can be &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional] 
 **recordingChannels** | **String**| The recording channels for the final recording. Can be: &#x60;mono&#x60; or &#x60;dual&#x60; and the default is &#x60;mono&#x60;. | [optional] 
 **recordingStatusCallback** | **String**| The URL that we should call using the &#x60;recording_status_callback_method&#x60; when the recording status changes. | [optional] 
 **recordingStatusCallbackMethod** | **String**| The HTTP method we should use when we call &#x60;recording_status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] 
 **redirectAccept** | **Boolean**| Whether the reservation should be accepted when executing a Redirect instruction. | [optional] 
 **redirectCallSid** | **String**| The Call SID of the call parked in the queue when executing a Redirect instruction. | [optional] 
 **redirectUrl** | **String**| TwiML URI to redirect the call to when executing the Redirect instruction. | [optional] 
 **region** | **String**| The [region](https://support.twilio.com/hc/en-us/articles/223132167-How-global-low-latency-routing-and-region-selection-work-for-conferences-and-Client-calls) where we should mix the recorded audio. Can be:&#x60;us1&#x60;, &#x60;ie1&#x60;, &#x60;de1&#x60;, &#x60;sg1&#x60;, &#x60;br1&#x60;, &#x60;au1&#x60;, or &#x60;jp1&#x60;. | [optional] 
 **reservationStatus** | **WorkerReservationEnumStatus**|  | [optional] 
 **sipAuthPassword** | **String**| The SIP password for authentication. | [optional] 
 **sipAuthUsername** | **String**| The SIP username used for authentication. | [optional] 
 **startConferenceOnEnter** | **Boolean**| Whether to start the conference when the participant joins, if it has not already started. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. If &#x60;false&#x60; and the conference has not started, the participant is muted and hears background music until another participant starts the conference. | [optional] 
 **statusCallback** | **String**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional] 
 **statusCallbackEvent** | [**[WorkerReservationEnumCallStatus]**](WorkerReservationEnumCallStatus.md)| The call progress events that we will send to &#x60;status_callback&#x60;. Can be: &#x60;initiated&#x60;, &#x60;ringing&#x60;, &#x60;answered&#x60;, or &#x60;completed&#x60;. | [optional] 
 **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. | [optional] 
 **timeout** | **Number**| The timeout for a call when executing a Conference instruction. | [optional] 
 **to** | **String**| The Contact URI of the worker when executing a Conference instruction. Can be the URI of the Twilio Client, the SIP URI for Programmable SIP, or the [E.164](https://www.twilio.com/docs/glossary/what-e164) formatted phone number, depending on the destination. | [optional] 
 **waitMethod** | **String**| The HTTP method we should use to call &#x60;wait_url&#x60;. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. When using a static audio file, this should be &#x60;GET&#x60; so that we can cache the file. | [optional] 
 **waitUrl** | **String**| The URL we should call using the &#x60;wait_method&#x60; for the music to play while participants are waiting for the conference to start. The default value is the URL of our standard hold music. [Learn more about hold music](https://www.twilio.com/labs/twimlets/holdmusic). | [optional] 
 **workerActivitySid** | **String**| The new worker activity SID if rejecting a reservation. | [optional] 

### Return type

[**TaskrouterV1WorkspaceWorkerWorkerReservation**](TaskrouterV1WorkspaceWorkerWorkerReservation.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

