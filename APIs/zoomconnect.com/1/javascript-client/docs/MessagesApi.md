# WwwZoomconnectCom.MessagesApi

All URIs are relative to *https://www.zoomconnect.com/app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyse**](MessagesApi.md#analyse) | **POST** /api/rest/v1/messages/analyse/message-length-within-max-allowed | analyse-
[**analyseFull**](MessagesApi.md#analyseFull) | **POST** /api/rest/v1/messages/analyse/full | analyse-full
[**analyseMessageCreditCost**](MessagesApi.md#analyseMessageCreditCost) | **POST** /api/rest/v1/messages/analyse/message-credit-cost | analyse-message-credit-cost
[**analyseMessageEncoding**](MessagesApi.md#analyseMessageEncoding) | **POST** /api/rest/v1/messages/analyse/message-encoding | analyse-message-encoding
[**analyseMessageLength**](MessagesApi.md#analyseMessageLength) | **POST** /api/rest/v1/messages/analyse/message-length | analyse-message-length
[**analyseNumberOfMessages**](MessagesApi.md#analyseNumberOfMessages) | **POST** /api/rest/v1/messages/analyse/number-of-messages | analyse-number-of-messages
[**apiRestV1MessagesAllGet**](MessagesApi.md#apiRestV1MessagesAllGet) | **GET** /api/rest/v1/messages/all | all
[**apiRestV1MessagesMessageIdDelete**](MessagesApi.md#apiRestV1MessagesMessageIdDelete) | **DELETE** /api/rest/v1/messages/{messageId} | delete
[**apiRestV1MessagesMessageIdGet**](MessagesApi.md#apiRestV1MessagesMessageIdGet) | **GET** /api/rest/v1/messages/{messageId} | get
[**apiRestV1MessagesMessageIdMarkReadPost**](MessagesApi.md#apiRestV1MessagesMessageIdMarkReadPost) | **POST** /api/rest/v1/messages/{messageId}/markRead | markRead
[**apiRestV1MessagesMessageIdMarkReadPut**](MessagesApi.md#apiRestV1MessagesMessageIdMarkReadPut) | **PUT** /api/rest/v1/messages/{messageId}/markRead | markRead
[**apiRestV1MessagesMessageIdMarkUnreadPost**](MessagesApi.md#apiRestV1MessagesMessageIdMarkUnreadPost) | **POST** /api/rest/v1/messages/{messageId}/markUnread | markUnread
[**apiRestV1MessagesMessageIdMarkUnreadPut**](MessagesApi.md#apiRestV1MessagesMessageIdMarkUnreadPut) | **PUT** /api/rest/v1/messages/{messageId}/markUnread | markUnread



## analyse

> Boolean analyse(opts)

analyse-

Returns details for a single message

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.MessagesApi();
let opts = {
  'body': new WwwZoomconnectCom.WebServiceAnalyseMessageRequestMessageOnly() // WebServiceAnalyseMessageRequestMessageOnly | request
};
apiInstance.analyse(opts, (error, data, response) => {
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
 **body** | [**WebServiceAnalyseMessageRequestMessageOnly**](WebServiceAnalyseMessageRequestMessageOnly.md)| request | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## analyseFull

> WebServiceAnalyseMessageResponse analyseFull(opts)

analyse-full

Returns full analysis of message

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.MessagesApi();
let opts = {
  'body': new WwwZoomconnectCom.WebServiceAnalyseMessageRequestMessageAndRecipientNumber() // WebServiceAnalyseMessageRequestMessageAndRecipientNumber | request
};
apiInstance.analyseFull(opts, (error, data, response) => {
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
 **body** | [**WebServiceAnalyseMessageRequestMessageAndRecipientNumber**](WebServiceAnalyseMessageRequestMessageAndRecipientNumber.md)| request | [optional] 

### Return type

[**WebServiceAnalyseMessageResponse**](WebServiceAnalyseMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## analyseMessageCreditCost

> Number analyseMessageCreditCost(opts)

analyse-message-credit-cost

Returns the number of credit which would be required to send the request message to the requested recipient number

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.MessagesApi();
let opts = {
  'body': new WwwZoomconnectCom.WebServiceAnalyseMessageRequestMessageAndRecipientNumber() // WebServiceAnalyseMessageRequestMessageAndRecipientNumber | request
};
apiInstance.analyseMessageCreditCost(opts, (error, data, response) => {
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
 **body** | [**WebServiceAnalyseMessageRequestMessageAndRecipientNumber**](WebServiceAnalyseMessageRequestMessageAndRecipientNumber.md)| request | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## analyseMessageEncoding

> String analyseMessageEncoding(opts)

analyse-message-encoding

Returns the message encoding that would be required to send the requested message

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.MessagesApi();
let opts = {
  'body': new WwwZoomconnectCom.WebServiceAnalyseMessageRequestMessageOnly() // WebServiceAnalyseMessageRequestMessageOnly | request
};
apiInstance.analyseMessageEncoding(opts, (error, data, response) => {
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
 **body** | [**WebServiceAnalyseMessageRequestMessageOnly**](WebServiceAnalyseMessageRequestMessageOnly.md)| request | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## analyseMessageLength

> Number analyseMessageLength(opts)

analyse-message-length

Returns the number of characters the requested message consists of

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.MessagesApi();
let opts = {
  'body': new WwwZoomconnectCom.WebServiceAnalyseMessageRequestMessageOnly() // WebServiceAnalyseMessageRequestMessageOnly | request
};
apiInstance.analyseMessageLength(opts, (error, data, response) => {
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
 **body** | [**WebServiceAnalyseMessageRequestMessageOnly**](WebServiceAnalyseMessageRequestMessageOnly.md)| request | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## analyseNumberOfMessages

> Number analyseNumberOfMessages(opts)

analyse-number-of-messages

Returns the number of SMS parts which would be sent when sending the requested message

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.MessagesApi();
let opts = {
  'body': new WwwZoomconnectCom.WebServiceAnalyseMessageRequestMessageOnly() // WebServiceAnalyseMessageRequestMessageOnly | request
};
apiInstance.analyseNumberOfMessages(opts, (error, data, response) => {
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
 **body** | [**WebServiceAnalyseMessageRequestMessageOnly**](WebServiceAnalyseMessageRequestMessageOnly.md)| request | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## apiRestV1MessagesAllGet

> WebServiceMessages apiRestV1MessagesAllGet(opts)

all

Returns all messages

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.MessagesApi();
let opts = {
  'pageSize': 100, // Number | number of elements to return at a time
  'page': 1, // Number | page number
  'type': "type_example", // String | filter by message type
  'status': "status_example", // String | filter by message status
  'fromDateTimeSent': new Date("2013-10-20T19:20:30+01:00"), // Date | date format: yyyyMMdd
  'toDateTimeSent': new Date("2013-10-20T19:20:30+01:00"), // Date | date format: yyyyMMdd
  'fromDateTimeReceived': new Date("2013-10-20T19:20:30+01:00"), // Date | date format: yyyyMMdd
  'toDateTimeReceived': new Date("2013-10-20T19:20:30+01:00"), // Date | date format: yyyyMMdd
  'fromNumber': "fromNumber_example", // String | phone number the message was sent from
  'toNumber': "toNumber_example", // String | phone number the message was sent to
  'message': "message_example", // String | search matching message text
  'campaign': "campaign_example", // String | search by campaign
  'dataField': "dataField_example", // String | search by data field
  'deleted': true, // Boolean | return only deleted / not deleted messages
  'read': true, // Boolean | return only read / unread messages (inbox messages only)
  'repliesToMessageId': "repliesToMessageId_example" // String | return only inbox messages which are a reply to the message with the given message id
};
apiInstance.apiRestV1MessagesAllGet(opts, (error, data, response) => {
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
 **pageSize** | **Number**| number of elements to return at a time | [optional] [default to 100]
 **page** | **Number**| page number | [optional] [default to 1]
 **type** | **String**| filter by message type | [optional] 
 **status** | **String**| filter by message status | [optional] 
 **fromDateTimeSent** | **Date**| date format: yyyyMMdd | [optional] 
 **toDateTimeSent** | **Date**| date format: yyyyMMdd | [optional] 
 **fromDateTimeReceived** | **Date**| date format: yyyyMMdd | [optional] 
 **toDateTimeReceived** | **Date**| date format: yyyyMMdd | [optional] 
 **fromNumber** | **String**| phone number the message was sent from | [optional] 
 **toNumber** | **String**| phone number the message was sent to | [optional] 
 **message** | **String**| search matching message text | [optional] 
 **campaign** | **String**| search by campaign | [optional] 
 **dataField** | **String**| search by data field | [optional] 
 **deleted** | **Boolean**| return only deleted / not deleted messages | [optional] 
 **read** | **Boolean**| return only read / unread messages (inbox messages only) | [optional] 
 **repliesToMessageId** | **String**| return only inbox messages which are a reply to the message with the given message id | [optional] 

### Return type

[**WebServiceMessages**](WebServiceMessages.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## apiRestV1MessagesMessageIdDelete

> apiRestV1MessagesMessageIdDelete(messageId)

delete

Deletes a  message

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.MessagesApi();
let messageId = "messageId_example"; // String | messageId
apiInstance.apiRestV1MessagesMessageIdDelete(messageId, (error, data, response) => {
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
 **messageId** | **String**| messageId | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiRestV1MessagesMessageIdGet

> WebServiceMessage apiRestV1MessagesMessageIdGet(messageId)

get

Returns details for a single message

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.MessagesApi();
let messageId = "messageId_example"; // String | messageId
apiInstance.apiRestV1MessagesMessageIdGet(messageId, (error, data, response) => {
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
 **messageId** | **String**| messageId | 

### Return type

[**WebServiceMessage**](WebServiceMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## apiRestV1MessagesMessageIdMarkReadPost

> WebServiceMessage apiRestV1MessagesMessageIdMarkReadPost(messageId)

markRead

Marks a  message as read

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.MessagesApi();
let messageId = "messageId_example"; // String | messageId
apiInstance.apiRestV1MessagesMessageIdMarkReadPost(messageId, (error, data, response) => {
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
 **messageId** | **String**| messageId | 

### Return type

[**WebServiceMessage**](WebServiceMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## apiRestV1MessagesMessageIdMarkReadPut

> WebServiceMessage apiRestV1MessagesMessageIdMarkReadPut(messageId)

markRead

Marks a  message as read

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.MessagesApi();
let messageId = "messageId_example"; // String | messageId
apiInstance.apiRestV1MessagesMessageIdMarkReadPut(messageId, (error, data, response) => {
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
 **messageId** | **String**| messageId | 

### Return type

[**WebServiceMessage**](WebServiceMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## apiRestV1MessagesMessageIdMarkUnreadPost

> WebServiceMessage apiRestV1MessagesMessageIdMarkUnreadPost(messageId)

markUnread

Marks a  message as unread

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.MessagesApi();
let messageId = "messageId_example"; // String | messageId
apiInstance.apiRestV1MessagesMessageIdMarkUnreadPost(messageId, (error, data, response) => {
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
 **messageId** | **String**| messageId | 

### Return type

[**WebServiceMessage**](WebServiceMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## apiRestV1MessagesMessageIdMarkUnreadPut

> WebServiceMessage apiRestV1MessagesMessageIdMarkUnreadPut(messageId)

markUnread

Marks a  message as unread

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.MessagesApi();
let messageId = "messageId_example"; // String | messageId
apiInstance.apiRestV1MessagesMessageIdMarkUnreadPut(messageId, (error, data, response) => {
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
 **messageId** | **String**| messageId | 

### Return type

[**WebServiceMessage**](WebServiceMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

