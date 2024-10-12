# CallFireApiDocumentation.TextsApi

All URIs are relative to *https://api.callfire.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addTextBroadcastBatch**](TextsApi.md#addTextBroadcastBatch) | **POST** /texts/broadcasts/{id}/batches | Add batches to a text broadcast
[**addTextBroadcastRecipients**](TextsApi.md#addTextBroadcastRecipients) | **POST** /texts/broadcasts/{id}/recipients | Add recipients to a text broadcast
[**archiveTextBroadcast**](TextsApi.md#archiveTextBroadcast) | **POST** /texts/broadcasts/{id}/archive | Archive text broadcast
[**createTextAutoReply**](TextsApi.md#createTextAutoReply) | **POST** /texts/auto-replys | Create an auto reply
[**createTextBroadcast**](TextsApi.md#createTextBroadcast) | **POST** /texts/broadcasts | Create a text broadcast
[**deleteTextAutoReply**](TextsApi.md#deleteTextAutoReply) | **DELETE** /texts/auto-replys/{id} | Delete an auto reply
[**findTextAutoReplys**](TextsApi.md#findTextAutoReplys) | **GET** /texts/auto-replys | Find auto replies
[**findTextBroadcasts**](TextsApi.md#findTextBroadcasts) | **GET** /texts/broadcasts | Find text broadcasts
[**findTexts**](TextsApi.md#findTexts) | **GET** /texts | Find texts
[**getText**](TextsApi.md#getText) | **GET** /texts/{id} | Find a specific text
[**getTextAutoReply**](TextsApi.md#getTextAutoReply) | **GET** /texts/auto-replys/{id} | Find a specific auto reply
[**getTextBroadcast**](TextsApi.md#getTextBroadcast) | **GET** /texts/broadcasts/{id} | Find a specific text broadcast
[**getTextBroadcastBatches**](TextsApi.md#getTextBroadcastBatches) | **GET** /texts/broadcasts/{id}/batches | Find batches in a text broadcast
[**getTextBroadcastStats**](TextsApi.md#getTextBroadcastStats) | **GET** /texts/broadcasts/{id}/stats | Get statistics on text broadcast
[**getTextBroadcastTexts**](TextsApi.md#getTextBroadcastTexts) | **GET** /texts/broadcasts/{id}/texts | Find texts in a text broadcast
[**sendTexts**](TextsApi.md#sendTexts) | **POST** /texts | Send texts
[**startTextBroadcast**](TextsApi.md#startTextBroadcast) | **POST** /texts/broadcasts/{id}/start | Start text broadcast
[**stopTextBroadcast**](TextsApi.md#stopTextBroadcast) | **POST** /texts/broadcasts/{id}/stop | Stop text broadcast
[**toggleTextBroadcastRecipientsStatus**](TextsApi.md#toggleTextBroadcastRecipientsStatus) | **POST** /texts/broadcasts/{id}/toggleRecipientsStatus | Disable/enable undialed recipients in broadcast
[**updateTextBroadcast**](TextsApi.md#updateTextBroadcast) | **PUT** /texts/broadcasts/{id} | Update a text broadcast



## addTextBroadcastBatch

> ResourceId addTextBroadcastBatch(id, opts)

Add batches to a text broadcast

Allows adding an extra batches to an already created text broadcast campaign. The batches which being  added pass the CallFire validation process (unlike in the recipients version of this API). That is why using of a scrubDuplicates flag remove duplicates from your batch. Batches may be added as a contact list id, a list of contact ids, or a list of numbers

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let id = 789; // Number | An id of a text broadcast
let opts = {
  'strictValidation': true, // Boolean | Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
  'batchRequest': new CallFireApiDocumentation.BatchRequest() // BatchRequest | A request object
};
apiInstance.addTextBroadcastBatch(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a text broadcast | 
 **strictValidation** | **Boolean**| Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation | [optional] 
 **batchRequest** | [**BatchRequest**](BatchRequest.md)| A request object | [optional] 

### Return type

[**ResourceId**](ResourceId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addTextBroadcastRecipients

> TextList addTextBroadcastRecipients(id, opts)

Add recipients to a text broadcast

Use this API to add recipients to a text broadcast which is already created. Post a list of Recipient objects to be immediately added to the text broadcast campaign. These contacts will not go through validation process, and will be acted upon as they are added. Recipients may be added as a list of contact ids, or list of numbers

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let id = 789; // Number | An id of a text broadcast
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'strictValidation': true, // Boolean | Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
  'textRecipient': [new CallFireApiDocumentation.TextRecipient()] // [TextRecipient] | A list of the TextRecipient objects
};
apiInstance.addTextBroadcastRecipients(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a text broadcast | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **strictValidation** | **Boolean**| Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation | [optional] 
 **textRecipient** | [**[TextRecipient]**](TextRecipient.md)| A list of the TextRecipient objects | [optional] 

### Return type

[**TextList**](TextList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## archiveTextBroadcast

> archiveTextBroadcast(id)

Archive text broadcast

Archives a text broadcast (and hides it in the search results)

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let id = 789; // Number | An id of a text broadcast to archive
apiInstance.archiveTextBroadcast(id, (error, data, response) => {
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
 **id** | **Number**| An id of a text broadcast to archive | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createTextAutoReply

> ResourceId createTextAutoReply(opts)

Create an auto reply

CallFire gives you possibility to set up auto reply messages for your numbers and keywords. You can set a general auto reply for anyone who texts your number, keyword, and/or include a text to match, so that the auto reply would be sent only to those who text the matched text

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let opts = {
  'textAutoReply': new CallFireApiDocumentation.TextAutoReply() // TextAutoReply | TextAutoReply object, keyword or number should be specified with response message and text to match if needed
};
apiInstance.createTextAutoReply(opts, (error, data, response) => {
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
 **textAutoReply** | [**TextAutoReply**](TextAutoReply.md)| TextAutoReply object, keyword or number should be specified with response message and text to match if needed | [optional] 

### Return type

[**ResourceId**](ResourceId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTextBroadcast

> ResourceId createTextBroadcast(opts)

Create a text broadcast

Creates a text broadcast campaign using the Text Broadcast API. Send a TextBroadcast object in the message body to detail a text broadcast campaign. A campaign can be created without contacts and with bare minimum configuration, but contacts have to be added further on to use the campaign. It supports scheduling, retry logic, pattern-based messages.

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let opts = {
  'start': true, // Boolean | If true then starts the campaign immediately (not required).
  'strictValidation': true, // Boolean | Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
  'textBroadcast': new CallFireApiDocumentation.TextBroadcast() // TextBroadcast | A TextBroadcast object
};
apiInstance.createTextBroadcast(opts, (error, data, response) => {
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
 **start** | **Boolean**| If true then starts the campaign immediately (not required). | [optional] 
 **strictValidation** | **Boolean**| Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation | [optional] 
 **textBroadcast** | [**TextBroadcast**](TextBroadcast.md)| A TextBroadcast object | [optional] 

### Return type

[**ResourceId**](ResourceId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteTextAutoReply

> deleteTextAutoReply(id)

Delete an auto reply

Deletes a text auto reply and removes the configuration. Can not delete a TextAutoReply which is currently active for a campaign

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let id = 789; // Number | An id of a text auto reply
apiInstance.deleteTextAutoReply(id, (error, data, response) => {
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
 **id** | **Number**| An id of a text auto reply | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findTextAutoReplys

> TextAutoReplyPage findTextAutoReplys(opts)

Find auto replies

Find all text autoreplies created by user. Returns a paged list of TextAutoReply

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'number': "number_example" // String | Phone number in E.164 format (11-digit) which contains a TextAutoReply. Example: 12132000384. If number is empty then operator returns all autoreplies configured for the user's account
};
apiInstance.findTextAutoReplys(opts, (error, data, response) => {
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
 **number** | **String**| Phone number in E.164 format (11-digit) which contains a TextAutoReply. Example: 12132000384. If number is empty then operator returns all autoreplies configured for the user&#39;s account | [optional] 

### Return type

[**TextAutoReplyPage**](TextAutoReplyPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findTextBroadcasts

> TextBroadcastPage findTextBroadcasts(opts)

Find text broadcasts

Searches for all text broadcasts created by user. Can query on label, name, and the current running status of the campaign. Returns a paged list of text broadcasts

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let opts = {
  'name': "name_example", // String | A name of text broadcast
  'label': "label_example", // String | A label of a text broadcast
  'running': true, // Boolean | Returns broadcasts only in running state.
  'scheduled': true, // Boolean | Specify whether the campaigns should be scheduled or not
  'intervalBegin': 789, // Number | Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
  'intervalEnd': 789, // Number | End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
  'limit': 10, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.findTextBroadcasts(opts, (error, data, response) => {
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
 **name** | **String**| A name of text broadcast | [optional] 
 **label** | **String**| A label of a text broadcast | [optional] 
 **running** | **Boolean**| Returns broadcasts only in running state. | [optional] 
 **scheduled** | **Boolean**| Specify whether the campaigns should be scheduled or not | [optional] 
 **intervalBegin** | **Number**| Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] 
 **intervalEnd** | **Number**| End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] 
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 10]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**TextBroadcastPage**](TextBroadcastPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findTexts

> TextPage findTexts(opts)

Find texts

Searches for texts sent or received by user. Use \&quot;campaignId&#x3D;0\&quot; parameter to query for all texts sent through the POST /texts API. See [call states and results](https://developers.callfire.com/results-responses-errors.html)

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let opts = {
  'id': [null], // [Number] | List of Text ids to search for, if ids specified other query params ignored
  'campaignId': 789, // Number | An id of a campaign, queries for texts inside a particular campaign. Specify null to list texts of all campaigns or 0 for a default campaign
  'batchId': 789, // Number | An Id of a contact batch, queries for texts which are used in the particular contact batch
  'fromNumber': "fromNumber_example", // String | A phone number in E.164 format (11-digit). Example: 12132000384, 67076
  'toNumber': "toNumber_example", // String | A phone number in E.164 format (11-digit). Example: 12132000384, 67076
  'label': "label_example", // String | A label of a text message
  'states': "states_example", // String | Expected text statuses in comma separated string, available values: READY, SELECTED, CALLBACK, FINISHED, DISABLED, DNC, DUP, INVALID, TIMEOUT, PERIOD_LIMIT. See [call states and results](https://developers.callfire.com/results-responses-errors.html)
  'results': "results_example", // String | Expected text results in comma separated string, available values: SENT, RECEIVED, DNT, TOO_BIG, INTERNAL_ERROR, CARRIER_ERROR, CARRIER_TEMP_ERROR, UNDIALED. See [call states and results](https://developers.callfire.com/results-responses-errors.html)
  'inbound': true, // Boolean | Specify true for inbound or false for outbounds. Do not specify this parameter if you need to get both inbound and outbound texts listed in response
  'intervalBegin': 789, // Number | Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000
  'intervalEnd': 789, // Number | End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000
  'limit': 10, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0, // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.findTexts(opts, (error, data, response) => {
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
 **id** | [**[Number]**](Number.md)| List of Text ids to search for, if ids specified other query params ignored | [optional] 
 **campaignId** | **Number**| An id of a campaign, queries for texts inside a particular campaign. Specify null to list texts of all campaigns or 0 for a default campaign | [optional] 
 **batchId** | **Number**| An Id of a contact batch, queries for texts which are used in the particular contact batch | [optional] 
 **fromNumber** | **String**| A phone number in E.164 format (11-digit). Example: 12132000384, 67076 | [optional] 
 **toNumber** | **String**| A phone number in E.164 format (11-digit). Example: 12132000384, 67076 | [optional] 
 **label** | **String**| A label of a text message | [optional] 
 **states** | **String**| Expected text statuses in comma separated string, available values: READY, SELECTED, CALLBACK, FINISHED, DISABLED, DNC, DUP, INVALID, TIMEOUT, PERIOD_LIMIT. See [call states and results](https://developers.callfire.com/results-responses-errors.html) | [optional] 
 **results** | **String**| Expected text results in comma separated string, available values: SENT, RECEIVED, DNT, TOO_BIG, INTERNAL_ERROR, CARRIER_ERROR, CARRIER_TEMP_ERROR, UNDIALED. See [call states and results](https://developers.callfire.com/results-responses-errors.html) | [optional] 
 **inbound** | **Boolean**| Specify true for inbound or false for outbounds. Do not specify this parameter if you need to get both inbound and outbound texts listed in response | [optional] 
 **intervalBegin** | **Number**| Start of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 | [optional] 
 **intervalEnd** | **Number**| End of the find time interval, formatted in unix time milliseconds. Example: 1473781817000 | [optional] 
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 10]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**TextPage**](TextPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getText

> Text getText(id, opts)

Find a specific text

Returns a single Text instance for a given text id

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let id = 789; // Number | An id of a text
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getText(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a text | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**Text**](Text.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTextAutoReply

> TextAutoReply getTextAutoReply(id, opts)

Find a specific auto reply

Returns a single TextAutoReply instance for a given text auto reply id

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let id = 789; // Number | An id of a text auto reply
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getTextAutoReply(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a text auto reply | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**TextAutoReply**](TextAutoReply.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTextBroadcast

> TextBroadcast getTextBroadcast(id, opts)

Find a specific text broadcast

Returns a single TextBroadcast instance for a given text broadcast id

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let id = 789; // Number | An id of a text broadcast
let opts = {
  'fields': "fields_example" // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
};
apiInstance.getTextBroadcast(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a text broadcast | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 

### Return type

[**TextBroadcast**](TextBroadcast.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTextBroadcastBatches

> BatchPage getTextBroadcastBatches(id, opts)

Find batches in a text broadcast

This endpoint will enable the user to page through all of the batches for a particular text broadcast campaign

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let id = 789; // Number | An id of a text broadcast
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0 // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
};
apiInstance.getTextBroadcastBatches(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a text broadcast | 
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


## getTextBroadcastStats

> TextBroadcastStatsDto getTextBroadcastStats(id, opts)

Get statistics on text broadcast

Returns the broadcast statistics. Example: total number of the sent/received actions, total cost, number of remaining outbound actions, error count, etc

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let id = 789; // Number | An id of a text broadcast
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'begin': 789, // Number | Start of a search find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
  'end': 789 // Number | End of a search time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT
};
apiInstance.getTextBroadcastStats(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a text broadcast | 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **begin** | **Number**| Start of a search find time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] 
 **end** | **Number**| End of a search time interval, formatted in unix time milliseconds. Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] 

### Return type

[**TextBroadcastStatsDto**](TextBroadcastStatsDto.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTextBroadcastTexts

> TextPage getTextBroadcastTexts(id, opts)

Find texts in a text broadcast

This endpoint will enable the user to page through all of the texts for a particular text broadcast campaign

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let id = 789; // Number | An id of a text broadcast
let opts = {
  'batchId': 789, // Number | ~
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'limit': 100, // Number | To set the maximum number of records to return in a paged list response. The default is 100
  'offset': 0 // Number | Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
};
apiInstance.getTextBroadcastTexts(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a text broadcast | 
 **batchId** | **Number**| ~ | [optional] 
 **fields** | **String**| Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page. | [optional] 
 **limit** | **Number**| To set the maximum number of records to return in a paged list response. The default is 100 | [optional] [default to 100]
 **offset** | **Number**| Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API. | [optional] [default to 0]

### Return type

[**TextPage**](TextPage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendTexts

> TextList sendTexts(opts)

Send texts

Use the /texts API to send individual texts quickly. By default all texts are going out from CallFire&#39;s dedicated short code. Example: 67076, 818818 etc

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let opts = {
  'fields': "fields_example", // String | Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
  'campaignId': 789, // Number | Specifies a campaignId to send texts through a previously created campaign
  'defaultMessage': "defaultMessage_example", // String | Text message can be overridden by TextRecipient.message field. If multiple recipients have the same text message to a different recipients it is better to specify a single default message and do not duplicate it in each recipient.
  'strictValidation': true, // Boolean | Turns on strict validation for recipients
  'textRecipient': [new CallFireApiDocumentation.TextRecipient()] // [TextRecipient] | List of TextRecipient objects. By recipient we mean either phone number or contact with user-defined attributes added to action. Text messaging supports media files, provide a list of ids of media files for recipient to attach media to the message.
};
apiInstance.sendTexts(opts, (error, data, response) => {
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
 **campaignId** | **Number**| Specifies a campaignId to send texts through a previously created campaign | [optional] 
 **defaultMessage** | **String**| Text message can be overridden by TextRecipient.message field. If multiple recipients have the same text message to a different recipients it is better to specify a single default message and do not duplicate it in each recipient. | [optional] 
 **strictValidation** | **Boolean**| Turns on strict validation for recipients | [optional] 
 **textRecipient** | [**[TextRecipient]**](TextRecipient.md)| List of TextRecipient objects. By recipient we mean either phone number or contact with user-defined attributes added to action. Text messaging supports media files, provide a list of ids of media files for recipient to attach media to the message. | [optional] 

### Return type

[**TextList**](TextList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startTextBroadcast

> startTextBroadcast(id)

Start text broadcast

Starts a text broadcast

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let id = 789; // Number | An id of a text broadcast to start
apiInstance.startTextBroadcast(id, (error, data, response) => {
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
 **id** | **Number**| An id of a text broadcast to start | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopTextBroadcast

> stopTextBroadcast(id)

Stop text broadcast

Stops a text broadcast

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let id = 789; // Number | An Id of a text broadcast. To stop the broadcast
apiInstance.stopTextBroadcast(id, (error, data, response) => {
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
 **id** | **Number**| An Id of a text broadcast. To stop the broadcast | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## toggleTextBroadcastRecipientsStatus

> toggleTextBroadcastRecipientsStatus(id, opts)

Disable/enable undialed recipients in broadcast

This operation lets the user to disable/enable undialed contacts in created broadcast

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let id = 789; // Number | An id of a text broadcast
let opts = {
  'enable': false, // Boolean | Flag which indicate what to do with texts (true will enable texts in DISABLED status and vice versa)
  'recipient': [new CallFireApiDocumentation.Recipient()] // [Recipient] | List of Recipient objects. By recipient we mean either phone number or contact id.
};
apiInstance.toggleTextBroadcastRecipientsStatus(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a text broadcast | 
 **enable** | **Boolean**| Flag which indicate what to do with texts (true will enable texts in DISABLED status and vice versa) | [optional] [default to false]
 **recipient** | [**[Recipient]**](Recipient.md)| List of Recipient objects. By recipient we mean either phone number or contact id. | [optional] 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTextBroadcast

> TextBroadcastCreateResponse updateTextBroadcast(id, opts)

Update a text broadcast

Allows modifying the configuration of existing text broadcast campaign. See TextBroadcast for more information on what can/can&#39;t be updated on this API

### Example

```javascript
import CallFireApiDocumentation from 'call_fire_api_documentation';
let defaultClient = CallFireApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new CallFireApiDocumentation.TextsApi();
let id = 789; // Number | An id of a text broadcast
let opts = {
  'strictValidation': true, // Boolean | Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation = true and one of numbers didn't pass validation
  'textBroadcast': new CallFireApiDocumentation.TextBroadcast() // TextBroadcast | A TextBroadcast object
};
apiInstance.updateTextBroadcast(id, opts, (error, data, response) => {
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
 **id** | **Number**| An id of a text broadcast | 
 **strictValidation** | **Boolean**| Turns on strict validation for recipients. System will reply with BAD_REQUEST(400) if strictValidation &#x3D; true and one of numbers didn&#39;t pass validation | [optional] 
 **textBroadcast** | [**TextBroadcast**](TextBroadcast.md)| A TextBroadcast object | [optional] 

### Return type

[**TextBroadcastCreateResponse**](TextBroadcastCreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

