# CallFireApiDocumentation.CallsApi

All URIs are relative to *https://api.callfire.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addCallBroadcastBatch**](CallsApi.md#addCallBroadcastBatch) | **POST** /calls/broadcasts/{id}/batches | Add batches to a call broadcast
[**addCallBroadcastRecipients**](CallsApi.md#addCallBroadcastRecipients) | **POST** /calls/broadcasts/{id}/recipients | Add recipients to a call broadcast
[**archiveVoiceBroadcast**](CallsApi.md#archiveVoiceBroadcast) | **POST** /calls/broadcasts/{id}/archive | Archive voice broadcast
[**createCallBroadcast**](CallsApi.md#createCallBroadcast) | **POST** /calls/broadcasts | Create a call broadcast
[**findCallBroadcasts**](CallsApi.md#findCallBroadcasts) | **GET** /calls/broadcasts | Find call broadcasts
[**findCalls**](CallsApi.md#findCalls) | **GET** /calls | Find calls
[**getCall**](CallsApi.md#getCall) | **GET** /calls/{id} | Find a specific call
[**getCallBroadcast**](CallsApi.md#getCallBroadcast) | **GET** /calls/broadcasts/{id} | Find a specific call broadcast
[**getCallBroadcastBatches**](CallsApi.md#getCallBroadcastBatches) | **GET** /calls/broadcasts/{id}/batches | Find batches in a call broadcast
[**getCallBroadcastCalls**](CallsApi.md#getCallBroadcastCalls) | **GET** /calls/broadcasts/{id}/calls | Find calls in a call broadcast
[**getCallBroadcastStats**](CallsApi.md#getCallBroadcastStats) | **GET** /calls/broadcasts/{id}/stats | Get statistics on call broadcast
[**getCallRecording**](CallsApi.md#getCallRecording) | **GET** /calls/recordings/{id} | Get call recording by id
[**getCallRecordingByName**](CallsApi.md#getCallRecordingByName) | **GET** /calls/{id}/recordings/{name} | Get call recording by name
[**getCallRecordingMp3**](CallsApi.md#getCallRecordingMp3) | **GET** /calls/recordings/{id}.mp3 | Get call recording in mp3 format
[**getCallRecordingMp3ByName**](CallsApi.md#getCallRecordingMp3ByName) | **GET** /calls/{id}/recordings/{name}.mp3 | Get call mp3 recording by name
[**getCallRecordings**](CallsApi.md#getCallRecordings) | **GET** /calls/{id}/recordings | Get call recordings for a call
[**sendCalls**](CallsApi.md#sendCalls) | **POST** /calls | Send calls
[**startVoiceBroadcast**](CallsApi.md#startVoiceBroadcast) | **POST** /calls/broadcasts/{id}/start | Start voice broadcast
[**stopVoiceBroadcast**](CallsApi.md#stopVoiceBroadcast) | **POST** /calls/broadcasts/{id}/stop | Stop voice broadcast
[**toggleCallBroadcastRecipientsStatus**](CallsApi.md#toggleCallBroadcastRecipientsStatus) | **POST** /calls/broadcasts/{id}/toggleRecipientsStatus | Disable/enable undialed recipients in broadcast
[**updateCallBroadcast**](CallsApi.md#updateCallBroadcast) | **PUT** /calls/broadcasts/{id} | Update a call broadcast



## addCallBroadcastBatch

> ResourceId addCallBroadcastBatch(id, opts)

Add batches to a call broadcast

The &#39;add batch&#39; API allows user to add additional batches to an already created voice broadcast campaign. The added batch will go through the CallFire validation process, unlike in the recipients version of this API. That is why you can use the scrubDuplicates flag to remove duplicates from your batch. Batches may be added as a contact list id, a list of contact ids, or a list of numbers

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let id = 789; // Number | An id of a call broadcast
let opts = {
  'strictValidation': true, // Boolean | Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
  'batchRequest': new CallFireApiDocumentation.BatchRequest() // BatchRequest | A request object
};
apiInstance.addCallBroadcastBatch(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a call broadcast | 
 **strictValidation** | **Boolean**| Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation | [optional] 
 **batchRequest** | [**BatchRequest**](BatchRequest.md)| A request object | [optional] 

### Return type

[**ResourceId**](ResourceId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addCallBroadcastRecipients

> CallList addCallBroadcastRecipients(id, opts)

Add recipients to a call broadcast

Use this API to add the recipients to an existing voice broadcast. Post a list of Recipient objects to be added to the voice broadcast campaign. These contacts will not go through validation process, and will be acted upon as they are added. Recipients may be added as a list of contact ids, or list of numbers

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let id = 789; // Number | An id of a call broadcast
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'strictValidation': true, // Boolean | Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
  'recipient': [new CallFireApiDocumentation.Recipient()] // [Recipient] | A list of CallRecipient objects
};
apiInstance.addCallBroadcastRecipients(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a call broadcast | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **strictValidation** | **Boolean**| Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation | [optional] 
 **recipient** | [**[Recipient]**](Recipient.md)| A list of CallRecipient objects | [optional] 

### Return type

[**CallList**](CallList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## archiveVoiceBroadcast

> archiveVoiceBroadcast(id)

Archive voice broadcast

Archives a voice broadcast (voice broadcast will be hidden in search results)

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let id = 789; // Number | An id of a voice broadcast to archive
apiInstance.archiveVoiceBroadcast(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| An id of a voice broadcast to archive | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createCallBroadcast

> ResourceId createCallBroadcast(opts)

Create a call broadcast

Creates a call broadcast campaign using the Call Broadcast API. Send a CallBroadcast in the message body to add details in a voice broadcast campaign. The campaign can be created without contacts and bare minimum configuration, but contacts will have to be added further on to use the campaign

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let opts = {
  'start': true, // Boolean | Specify whether to immediately start this campaign (not required)
  'strictValidation': true, // Boolean | Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
  'callBroadcast': new CallFireApiDocumentation.CallBroadcast() // CallBroadcast | A CallBroadcast object
};
apiInstance.createCallBroadcast(opts, (error, data, response) => {
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
 **start** | **Boolean**| Specify whether to immediately start this campaign (not required) | [optional] 
 **strictValidation** | **Boolean**| Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation | [optional] 
 **callBroadcast** | [**CallBroadcast**](CallBroadcast.md)| A CallBroadcast object | [optional] 

### Return type

[**ResourceId**](ResourceId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## findCallBroadcasts

> CallBroadcastPage findCallBroadcasts(opts)

Find call broadcasts

Searches for all voice broadcasts created by user. Can query on label, name, and the current running status of the campaign. Returns a paged list of voice broadcasts

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'limit': 10, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'label': "label_example", // String | A label of a voice broadcast
  'name': "name_example", // String | A name of voice broadcast
  'running': true, // Boolean | Specify whether the campaigns should be running or not
  'scheduled': true, // Boolean | Specify whether the campaigns should be scheduled or not
  'intervalBegin': 789, // Number | Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
  'intervalEnd': 789 // Number | End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
};
apiInstance.findCallBroadcasts(opts, (error, data, response) => {
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
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 10]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]
 **label** | **String**| A label of a voice broadcast | [optional] 
 **name** | **String**| A name of voice broadcast | [optional] 
 **running** | **Boolean**| Specify whether the campaigns should be running or not | [optional] 
 **scheduled** | **Boolean**| Specify whether the campaigns should be scheduled or not | [optional] 
 **intervalBegin** | **Number**| Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] 
 **intervalEnd** | **Number**| End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] 

### Return type

[**CallBroadcastPage**](CallBroadcastPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findCalls

> CallPage findCalls(opts)

Find calls

To search for all calls sent or received by the user. Use \&quot;id&#x3D;0\&quot; for the campaignId parameter to query for all calls sent through the POST /calls API. See [call states and results](https://developers.callfire.com/results-responses-errors.html)

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'id': [null], // [Number] | Lists the Call ids to search for. If calls ids are specified then other query parameters can be ignored
  'campaignId': 789, // Number | An id of a campaign, queries for calls included to a particular campaign. Specify null for all campaigns and 0 for default campaign
  'batchId': 789, // Number | An id of a contact batch, queries for calls of a particular contact batch
  'fromNumber': "fromNumber_example", // String | Phone number in E.164 format (11-digit) that call was from. Example: 12132000384
  'toNumber': "toNumber_example", // String | Phone number in E.164 format (11-digit) that call was sent to. Example: 12132000384
  'label': "label_example", // String | A label for a specific call
  'states': "states_example", // String | Searches for all calls which correspond to statuses listed in a comma separated string. Available values: READY, SELECTED, CALLBACK, FINISHED, DISABLED, DNC, DUP, INVALID, TIMEOUT, PERIOD_LIMIT. See [call states and results](https://developers.callfire.com/results-responses-errors.html)
  'results': "results_example", // String | Searches for all calls with statuses listed in a comma separated string. Available values: SENT, RECEIVED, DNT, TOO_BIG, INTERNAL_ERROR, CARRIER_ERROR, CARRIER_TEMP_ERROR, UNDIALED. See [call states and results](https://developers.callfire.com/results-responses-errors.html)
  'inbound': true, // Boolean | Filters inbound calls for \"true\" value and outbound calls for \"false\" value
  'intervalBegin': 789, // Number | Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
  'intervalEnd': 789 // Number | End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
};
apiInstance.findCalls(opts, (error, data, response) => {
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
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]
 **id** | [**[Number]**](Number.md)| Lists the Call ids to search for. If calls ids are specified then other query parameters can be ignored | [optional] 
 **campaignId** | **Number**| An id of a campaign, queries for calls included to a particular campaign. Specify null for all campaigns and 0 for default campaign | [optional] 
 **batchId** | **Number**| An id of a contact batch, queries for calls of a particular contact batch | [optional] 
 **fromNumber** | **String**| Phone number in E.164 format (11-digit) that call was from. Example: 12132000384 | [optional] 
 **toNumber** | **String**| Phone number in E.164 format (11-digit) that call was sent to. Example: 12132000384 | [optional] 
 **label** | **String**| A label for a specific call | [optional] 
 **states** | **String**| Searches for all calls which correspond to statuses listed in a comma separated string. Available values: READY, SELECTED, CALLBACK, FINISHED, DISABLED, DNC, DUP, INVALID, TIMEOUT, PERIOD_LIMIT. See [call states and results](https://developers.callfire.com/results-responses-errors.html) | [optional] 
 **results** | **String**| Searches for all calls with statuses listed in a comma separated string. Available values: SENT, RECEIVED, DNT, TOO_BIG, INTERNAL_ERROR, CARRIER_ERROR, CARRIER_TEMP_ERROR, UNDIALED. See [call states and results](https://developers.callfire.com/results-responses-errors.html) | [optional] 
 **inbound** | **Boolean**| Filters inbound calls for \&quot;true\&quot; value and outbound calls for \&quot;false\&quot; value | [optional] 
 **intervalBegin** | **Number**| Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] 
 **intervalEnd** | **Number**| End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] 

### Return type

[**CallPage**](CallPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCall

> Call getCall(id, opts)

Find a specific call

Returns a single Call instance for a given call id.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let id = 789; // Number | An id of a call
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getCall(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a call | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**Call**](Call.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCallBroadcast

> CallBroadcast getCallBroadcast(id, opts)

Find a specific call broadcast

Returns a single CallBroadcast instance for a given call broadcast campaign id

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let id = 789; // Number | An id of a CallBroadcast
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getCallBroadcast(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a CallBroadcast | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**CallBroadcast**](CallBroadcast.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCallBroadcastBatches

> BatchPage getCallBroadcastBatches(id, opts)

Find batches in a call broadcast

This endpoint will enable the user to page through all of the batches for a particular voice broadcast campaign

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let id = 789; // Number | An id of a call broadcast
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0 // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
};
apiInstance.getCallBroadcastBatches(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a call broadcast | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]

### Return type

[**BatchPage**](BatchPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCallBroadcastCalls

> CallPage getCallBroadcastCalls(id, opts)

Find calls in a call broadcast

This endpoint will enable the user to page through all calls for a particular call broadcast campaign

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let id = 789; // Number | An Id of a call broadcast
let opts = {
  'batchId': 789, // Number | An id of a particular batch associated with broadcast
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0 // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
};
apiInstance.getCallBroadcastCalls(id, opts, (error, data, response) => {
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
 **id** | **Number**| An Id of a call broadcast | 
 **batchId** | **Number**| An id of a particular batch associated with broadcast | [optional] 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]

### Return type

[**CallPage**](CallPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCallBroadcastStats

> CallBroadcastStats getCallBroadcastStats(id, opts)

Get statistics on call broadcast

Returns broadcast statistics like total number of sent/received actions, total cost, number of remaining outbound actions, error count, etc

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let id = 789; // Number | An id of a call broadcast
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'begin': 789, // Number | Start of the search time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
  'end': 789 // Number | End of the search time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
};
apiInstance.getCallBroadcastStats(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a call broadcast | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **begin** | **Number**| Start of the search time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] 
 **end** | **Number**| End of the search time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] 

### Return type

[**CallBroadcastStats**](CallBroadcastStats.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCallRecording

> CallRecording getCallRecording(id, opts)

Get call recording by id

Returns metadata of recording of a particular call. Metadata contains a link to a MP3 recording

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let id = 789; // Number | ~
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getCallRecording(id, opts, (error, data, response) => {
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
 **id** | **Number**| ~ | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**CallRecording**](CallRecording.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCallRecordingByName

> CallRecording getCallRecordingByName(id, name, opts)

Get call recording by name

Returns recording metadata of particular call. Metadata contains link to a MP3 recording

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let id = 789; // Number | An id of a call
let name = "name_example"; // String | A name of a recording
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getCallRecordingByName(id, name, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a call | 
 **name** | **String**| A name of a recording | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**CallRecording**](CallRecording.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCallRecordingMp3

> Object getCallRecordingMp3(id)

Get call recording in mp3 format

Returns an MP3 recording of particular call, response contains binary data, content type is &#39;audio/mpeg&#39;

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let id = 789; // Number | An id of a call
apiInstance.getCallRecordingMp3(id, (error, data, response) => {
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
 **id** | **Number**| An id of a call | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCallRecordingMp3ByName

> Object getCallRecordingMp3ByName(id, name)

Get call mp3 recording by name

Returns a MP3 recording of a particular call, response contains binary data, content type is &#39;audio/mpeg&#39;

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let id = 789; // Number | An id of a call
let name = "name_example"; // String | A name of a recording
apiInstance.getCallRecordingMp3ByName(id, name, (error, data, response) => {
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
 **id** | **Number**| An id of a call | 
 **name** | **String**| A name of a recording | 

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: audio/mpeg


## getCallRecordings

> CallRecordingList getCallRecordings(id, opts)

Get call recordings for a call

Returns a list of recordings metadata of particular call. Metadata contains link to a MP3 recording

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let id = 789; // Number | An id of a call
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getCallRecordings(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a call | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**CallRecordingList**](CallRecordingList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendCalls

> CallList sendCalls(opts)

Send calls

Use the /calls API to send individual calls quickly. A verified Caller ID and sufficient credits are required to make a call. CallRecipient represents a single recipient identified by phone number or contact id in CallFire system. You can attach user-defined attributes to a Call action via CallRecipient.attributes property, attributes are available in Call action response

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'campaignId': 789, // Number | Specifies a campaignId to send calls quickly on a previously created campaign
  'defaultLiveMessage': "defaultLiveMessage_example", // String | Text to be turned into a sound, this text will be played when the phone is answered. Parameter can be overridden for any particular CallRecipient
  'defaultMachineMessage': "defaultMachineMessage_example", // String | Text to be turned into a sound, this text will be played when answering machine is detected. Parameter can be overridden for any particular CallRecipient
  'defaultLiveMessageSoundId': 789, // Number | Id of sound file to play if phone is answered. Parameter can be overridden for any particular CallRecipient
  'defaultMachineMessageSoundId': 789, // Number | An id of a sound file to play if answering machine is detected. Parameter can be overridden for any particular CallRecipient
  'defaultVoice': "defaultVoice_example", // String | The voice set by default for all text-to-speech messages defined in CallRecipient objects or as default *Message properties
  'strictValidation': true, // Boolean | Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
  'callRecipient': [new CallFireApiDocumentation.CallRecipient()] // [CallRecipient] | An array of CallRecipient objects.  Limitations: 1. Max number of CallRecipient objects is 10 
};
apiInstance.sendCalls(opts, (error, data, response) => {
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
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **campaignId** | **Number**| Specifies a campaignId to send calls quickly on a previously created campaign | [optional] 
 **defaultLiveMessage** | **String**| Text to be turned into a sound, this text will be played when the phone is answered. Parameter can be overridden for any particular CallRecipient | [optional] 
 **defaultMachineMessage** | **String**| Text to be turned into a sound, this text will be played when answering machine is detected. Parameter can be overridden for any particular CallRecipient | [optional] 
 **defaultLiveMessageSoundId** | **Number**| Id of sound file to play if phone is answered. Parameter can be overridden for any particular CallRecipient | [optional] 
 **defaultMachineMessageSoundId** | **Number**| An id of a sound file to play if answering machine is detected. Parameter can be overridden for any particular CallRecipient | [optional] 
 **defaultVoice** | **String**| The voice set by default for all text-to-speech messages defined in CallRecipient objects or as default *Message properties | [optional] 
 **strictValidation** | **Boolean**| Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation | [optional] 
 **callRecipient** | [**[CallRecipient]**](CallRecipient.md)| An array of CallRecipient objects.  Limitations: 1. Max number of CallRecipient objects is 10  | [optional] 

### Return type

[**CallList**](CallList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startVoiceBroadcast

> startVoiceBroadcast(id)

Start voice broadcast

Start a voice broadcast

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let id = 789; // Number | An id of voice broadcast to start
apiInstance.startVoiceBroadcast(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| An id of voice broadcast to start | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopVoiceBroadcast

> stopVoiceBroadcast(id)

Stop voice broadcast

Stop a voice broadcast

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let id = 789; // Number | An id of voice broadcast to stop
apiInstance.stopVoiceBroadcast(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| An id of voice broadcast to stop | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## toggleCallBroadcastRecipientsStatus

> toggleCallBroadcastRecipientsStatus(id, opts)

Disable/enable undialed recipients in broadcast

This operation lets the user to disable/enable undialed recipients in created broadcast

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let id = 789; // Number | An id of a voice broadcast
let opts = {
  'enable': false, // Boolean | Flag which indicate what to do with calls (true will enable call in DISABLED status and vice versa)
  'recipient': [new CallFireApiDocumentation.Recipient()] // [Recipient] | List of Recipient objects. By recipient we mean either phone number or contact id.
};
apiInstance.toggleCallBroadcastRecipientsStatus(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| An id of a voice broadcast | 
 **enable** | **Boolean**| Flag which indicate what to do with calls (true will enable call in DISABLED status and vice versa) | [optional] [default to false]
 **recipient** | [**[Recipient]**](Recipient.md)| List of Recipient objects. By recipient we mean either phone number or contact id. | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCallBroadcast

> updateCallBroadcast(id, opts)

Update a call broadcast

This operation lets the user modify the configuration of a voice broadcast campaign after call broadcast campaign is created. See CallBroadcast for more information on what can/can&#39;t be updated on this API

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.CallsApi();
let id = 789; // Number | An id of a voice broadcast
let opts = {
  'strictValidation': true, // Boolean | Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
  'callBroadcast': new CallFireApiDocumentation.CallBroadcast() // CallBroadcast | A CallBroadcast object
};
apiInstance.updateCallBroadcast(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **Number**| An id of a voice broadcast | 
 **strictValidation** | **Boolean**| Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation | [optional] 
 **callBroadcast** | [**CallBroadcast**](CallBroadcast.md)| A CallBroadcast object | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

