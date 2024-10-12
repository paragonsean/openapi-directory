# SevenIoApi.SmsApi

All URIs are relative to *https://gateway.seven.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sms**](SmsApi.md#sms) | **POST** /sms | 



## sms

> Sms200Response sms(text, to, opts)



### Example

```javascript
import SevenIoApi from 'seven_io_api';
let defaultClient = SevenIoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SevenIoApi.SmsApi();
let text = "text_example"; // String | The actual text message to send.
let to = "to_example"; // String | The recipient number or group name.
let opts = {
  'from': "from_example", // String | Set a custom sender name.
  'foreignId': "foreignId_example", // String | Identifier to return in callbacks.
  'label': "label_example", // String | A custom label.
  'udh': "udh_example", // String | A custom User Data Header.
  'delay': "delay_example", // String | Date/Time for delayed dispatch.
  'debug': 0, // Number | Disable message sending.
  'noReload': 0, // Number | Enable sending of duplicated messages within 180 seconds.
  'unicode': 0, // Number | Force unicode encoding. Reduces sms length to 70 chars.
  'flash': 0, // Number | Send as flash.
  'utf8': 0, // Number | Force UTF8 encoding.
  'details': 0, // Number | Attach message details to response.
  'returnMsgId': 0, // Number | Attach message ID to second row in a text response.
  'json': 0, // Number | Return a detailed JSON response.
  'performanceTracking': 0 // Number | Enable performance tracking for found URLs.
};
apiInstance.sms(text, to, opts, (error, data, response) => {
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
 **text** | **String**| The actual text message to send. | 
 **to** | **String**| The recipient number or group name. | 
 **from** | **String**| Set a custom sender name. | [optional] 
 **foreignId** | **String**| Identifier to return in callbacks. | [optional] 
 **label** | **String**| A custom label. | [optional] 
 **udh** | **String**| A custom User Data Header. | [optional] 
 **delay** | **String**| Date/Time for delayed dispatch. | [optional] 
 **debug** | **Number**| Disable message sending. | [optional] [default to 0]
 **noReload** | **Number**| Enable sending of duplicated messages within 180 seconds. | [optional] [default to 0]
 **unicode** | **Number**| Force unicode encoding. Reduces sms length to 70 chars. | [optional] [default to 0]
 **flash** | **Number**| Send as flash. | [optional] [default to 0]
 **utf8** | **Number**| Force UTF8 encoding. | [optional] [default to 0]
 **details** | **Number**| Attach message details to response. | [optional] [default to 0]
 **returnMsgId** | **Number**| Attach message ID to second row in a text response. | [optional] [default to 0]
 **json** | **Number**| Return a detailed JSON response. | [optional] [default to 0]
 **performanceTracking** | **Number**| Enable performance tracking for found URLs. | [optional] [default to 0]

### Return type

[**Sms200Response**](Sms200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/plain

