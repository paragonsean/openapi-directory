# WwwZoomconnectCom.VoiceApi

All URIs are relative to *https://www.zoomconnect.com/app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiRestV1VoiceAllGet**](VoiceApi.md#apiRestV1VoiceAllGet) | **GET** /api/rest/v1/voice/all | all
[**apiRestV1VoiceMessageIdDelete**](VoiceApi.md#apiRestV1VoiceMessageIdDelete) | **DELETE** /api/rest/v1/voice/{messageId} | delete
[**apiRestV1VoiceMessageIdGet**](VoiceApi.md#apiRestV1VoiceMessageIdGet) | **GET** /api/rest/v1/voice/{messageId} | get
[**singleAudio**](VoiceApi.md#singleAudio) | **POST** /api/rest/v1/voice/single-audio | single-audio
[**singleText**](VoiceApi.md#singleText) | **POST** /api/rest/v1/voice/single-text | single-text



## apiRestV1VoiceAllGet

> WebServiceVoiceMessages apiRestV1VoiceAllGet(opts)

all

Returns all voice messages

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.VoiceApi();
let opts = {
  'pageSize': 100, // Number | number of elements to return at a time
  'page': 1, // Number | page number
  'status': "status_example", // String | filter by message status
  'fromDateTimeSent': new Date("2013-10-20T19:20:30+01:00"), // Date | date format: yyyyMMdd
  'toDateTimeSent': new Date("2013-10-20T19:20:30+01:00"), // Date | date format: yyyyMMdd
  'toNumber': "toNumber_example", // String | phone number the message was sent to
  'message': "message_example", // String | search matching message text
  'campaign': "campaign_example", // String | search by campaign
  'dataField': "dataField_example", // String | search by data field
  'deleted': true // Boolean | return only deleted / not deleted messages
};
apiInstance.apiRestV1VoiceAllGet(opts, (error, data, response) => {
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
 **status** | **String**| filter by message status | [optional] 
 **fromDateTimeSent** | **Date**| date format: yyyyMMdd | [optional] 
 **toDateTimeSent** | **Date**| date format: yyyyMMdd | [optional] 
 **toNumber** | **String**| phone number the message was sent to | [optional] 
 **message** | **String**| search matching message text | [optional] 
 **campaign** | **String**| search by campaign | [optional] 
 **dataField** | **String**| search by data field | [optional] 
 **deleted** | **Boolean**| return only deleted / not deleted messages | [optional] 

### Return type

[**WebServiceVoiceMessages**](WebServiceVoiceMessages.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## apiRestV1VoiceMessageIdDelete

> apiRestV1VoiceMessageIdDelete(messageId)

delete

Deletes a  message

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.VoiceApi();
let messageId = "messageId_example"; // String | messageId
apiInstance.apiRestV1VoiceMessageIdDelete(messageId, (error, data, response) => {
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


## apiRestV1VoiceMessageIdGet

> WebServiceVoiceMessage apiRestV1VoiceMessageIdGet(messageId)

get

Returns details for a single message

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.VoiceApi();
let messageId = "messageId_example"; // String | messageId
apiInstance.apiRestV1VoiceMessageIdGet(messageId, (error, data, response) => {
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

[**WebServiceVoiceMessage**](WebServiceVoiceMessage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## singleAudio

> WebServiceSendVoiceMessageResponse singleAudio(recipientNumber, file, opts)

single-audio

Send a single audio voice message to one recipient. Note, Content-Type header must be set to multipart/form-data for this request.

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.VoiceApi();
let recipientNumber = "recipientNumber_example"; // String | the phone number of the recipient to send to
let file = "/path/to/file"; // File | audio file to play, supports MP3 or WAV format
let opts = {
  'campaign': "campaign_example", // String | optional campaign name
  'dataField': "dataField_example", // String | optional extra data
  'retryCount': 56, // Number | optional number of times to retry unanswered call
  'retryMinimumInterval': 56, // Number | optional minimum interval in minutes between retry attempts
  'retryMaximumInterval': 56 // Number | optional maximum interval in minutes between retry attempts
};
apiInstance.singleAudio(recipientNumber, file, opts, (error, data, response) => {
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
 **recipientNumber** | **String**| the phone number of the recipient to send to | 
 **file** | **File**| audio file to play, supports MP3 or WAV format | 
 **campaign** | **String**| optional campaign name | [optional] 
 **dataField** | **String**| optional extra data | [optional] 
 **retryCount** | **Number**| optional number of times to retry unanswered call | [optional] 
 **retryMinimumInterval** | **Number**| optional minimum interval in minutes between retry attempts | [optional] 
 **retryMaximumInterval** | **Number**| optional maximum interval in minutes between retry attempts | [optional] 

### Return type

[**WebServiceSendVoiceMessageResponse**](WebServiceSendVoiceMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json, application/xml


## singleText

> WebServiceSendVoiceMessageResponse singleText(opts)

single-text

Send a single text voice message to one recipient

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.VoiceApi();
let opts = {
  'body': new WwwZoomconnectCom.WebServiceVoiceMessageSendSingleTextRequest() // WebServiceVoiceMessageSendSingleTextRequest | request
};
apiInstance.singleText(opts, (error, data, response) => {
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
 **body** | [**WebServiceVoiceMessageSendSingleTextRequest**](WebServiceVoiceMessageSendSingleTextRequest.md)| request | [optional] 

### Return type

[**WebServiceSendVoiceMessageResponse**](WebServiceSendVoiceMessageResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

