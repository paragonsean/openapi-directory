# TwilioSync.SyncV1StreamMessageApi

All URIs are relative to *https://sync.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createStreamMessage**](SyncV1StreamMessageApi.md#createStreamMessage) | **POST** /v1/Services/{ServiceSid}/Streams/{StreamSid}/Messages | 



## createStreamMessage

> SyncV1ServiceSyncStreamStreamMessage createStreamMessage(serviceSid, streamSid, data)



Create a new Stream Message.

### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1StreamMessageApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the new Stream Message in.
let streamSid = "streamSid_example"; // String | The SID of the Sync Stream to create the new Stream Message resource for.
let data = null; // Object | A JSON string that represents an arbitrary, schema-less object that makes up the Stream Message body. Can be up to 4 KiB in length.
apiInstance.createStreamMessage(serviceSid, streamSid, data, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the new Stream Message in. | 
 **streamSid** | **String**| The SID of the Sync Stream to create the new Stream Message resource for. | 
 **data** | [**Object**](Object.md)| A JSON string that represents an arbitrary, schema-less object that makes up the Stream Message body. Can be up to 4 KiB in length. | 

### Return type

[**SyncV1ServiceSyncStreamStreamMessage**](SyncV1ServiceSyncStreamStreamMessage.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

