# TwilioTaskrouter.TaskrouterV1EventApi

All URIs are relative to *https://taskrouter.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchEvent**](TaskrouterV1EventApi.md#fetchEvent) | **GET** /v1/Workspaces/{WorkspaceSid}/Events/{Sid} | 
[**listEvent**](TaskrouterV1EventApi.md#listEvent) | **GET** /v1/Workspaces/{WorkspaceSid}/Events | 



## fetchEvent

> TaskrouterV1WorkspaceEvent fetchEvent(workspaceSid, sid)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1EventApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Event to fetch.
let sid = "sid_example"; // String | The SID of the Event resource to fetch.
apiInstance.fetchEvent(workspaceSid, sid, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Event to fetch. | 
 **sid** | **String**| The SID of the Event resource to fetch. | 

### Return type

[**TaskrouterV1WorkspaceEvent**](TaskrouterV1WorkspaceEvent.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEvent

> ListEventResponse listEvent(workspaceSid, opts)





### Example

```javascript
import TwilioTaskrouter from 'twilio_taskrouter';
let defaultClient = TwilioTaskrouter.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioTaskrouter.TaskrouterV1EventApi();
let workspaceSid = "workspaceSid_example"; // String | The SID of the Workspace with the Events to read. Returns only the Events that pertain to the specified Workspace.
let opts = {
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Only include Events that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time.
  'eventType': "eventType_example", // String | The type of Events to read. Returns only Events of the type specified.
  'minutes': 56, // Number | The period of events to read in minutes. Returns only Events that occurred since this many minutes in the past. The default is `15` minutes. Task Attributes for Events occuring more 43,200 minutes ago will be redacted.
  'reservationSid': "reservationSid_example", // String | The SID of the Reservation with the Events to read. Returns only Events that pertain to the specified Reservation.
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Only include Events from on or after this date and time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Task Attributes for Events older than 30 days will be redacted.
  'taskQueueSid': "taskQueueSid_example", // String | The SID of the TaskQueue with the Events to read. Returns only the Events that pertain to the specified TaskQueue.
  'taskSid': "taskSid_example", // String | The SID of the Task with the Events to read. Returns only the Events that pertain to the specified Task.
  'workerSid': "workerSid_example", // String | The SID of the Worker with the Events to read. Returns only the Events that pertain to the specified Worker.
  'workflowSid': "workflowSid_example", // String | The SID of the Workflow with the Events to read. Returns only the Events that pertain to the specified Workflow.
  'taskChannel': "taskChannel_example", // String | The TaskChannel with the Events to read. Returns only the Events that pertain to the specified TaskChannel.
  'sid': "sid_example", // String | The SID of the Event resource to read.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listEvent(workspaceSid, opts, (error, data, response) => {
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
 **workspaceSid** | **String**| The SID of the Workspace with the Events to read. Returns only the Events that pertain to the specified Workspace. | 
 **endDate** | **Date**| Only include Events that occurred on or before this date, specified in GMT as an [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time. | [optional] 
 **eventType** | **String**| The type of Events to read. Returns only Events of the type specified. | [optional] 
 **minutes** | **Number**| The period of events to read in minutes. Returns only Events that occurred since this many minutes in the past. The default is &#x60;15&#x60; minutes. Task Attributes for Events occuring more 43,200 minutes ago will be redacted. | [optional] 
 **reservationSid** | **String**| The SID of the Reservation with the Events to read. Returns only Events that pertain to the specified Reservation. | [optional] 
 **startDate** | **Date**| Only include Events from on or after this date and time, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Task Attributes for Events older than 30 days will be redacted. | [optional] 
 **taskQueueSid** | **String**| The SID of the TaskQueue with the Events to read. Returns only the Events that pertain to the specified TaskQueue. | [optional] 
 **taskSid** | **String**| The SID of the Task with the Events to read. Returns only the Events that pertain to the specified Task. | [optional] 
 **workerSid** | **String**| The SID of the Worker with the Events to read. Returns only the Events that pertain to the specified Worker. | [optional] 
 **workflowSid** | **String**| The SID of the Workflow with the Events to read. Returns only the Events that pertain to the specified Workflow. | [optional] 
 **taskChannel** | **String**| The TaskChannel with the Events to read. Returns only the Events that pertain to the specified TaskChannel. | [optional] 
 **sid** | **String**| The SID of the Event resource to read. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListEventResponse**](ListEventResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

