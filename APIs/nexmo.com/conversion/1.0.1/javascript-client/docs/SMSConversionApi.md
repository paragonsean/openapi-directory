# NexmoConversionApi.SMSConversionApi

All URIs are relative to *https://api.nexmo.com/conversions*

Method | HTTP request | Description
------------- | ------------- | -------------
[**smsConversion**](SMSConversionApi.md#smsConversion) | **POST** /sms | Tell Nexmo if your SMS message was successful



## smsConversion

> smsConversion(messageId, delivered, timestamp)

Tell Nexmo if your SMS message was successful

Send a Conversion API request with information about the SMS message identified by &#x60;message-id&#x60;. Nexmo uses your conversion data and internal information about &#x60;message-id&#x60; to help improve our routing of messages in the future.

### Example

```javascript
import NexmoConversionApi from 'nexmo_conversion_api';
let defaultClient = NexmoConversionApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';
// Configure API key authorization: apiSig
let apiSig = defaultClient.authentications['apiSig'];
apiSig.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiSig.apiKeyPrefix = 'Token';
// Configure API key authorization: apiSecret
let apiSecret = defaultClient.authentications['apiSecret'];
apiSecret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiSecret.apiKeyPrefix = 'Token';

let apiInstance = new NexmoConversionApi.SMSConversionApi();
let messageId = "00A0B0C0"; // String | The ID you receive in the response to a request. * From the Verify API - use the `event_id` in the response to Verify Check. * From the SMS API - use the `message-id` * From the Text-To-Speech API - use the `call-id` * From the Text-To-Speech-Prompt API - use the `call-id`
let delivered = true; // Boolean | Set to _true_ if your user replied to the message you sent. Otherwise, set to _false_. **Note**: for curl, use 0 and 1.
let timestamp = "2020-01-01 12:00:00"; // String | When the user completed your call-to-action (e.g. visited your website, installed your app) in [UTC±00:00](https://en.wikipedia.org/wiki/UTC%C2%B100:00) format: _yyyy-MM-dd HH:mm:ss_. If you do not set this parameter, Nexmo uses the time it receives this request.
apiInstance.smsConversion(messageId, delivered, timestamp, (error, data, response) => {
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
 **messageId** | **String**| The ID you receive in the response to a request. * From the Verify API - use the &#x60;event_id&#x60; in the response to Verify Check. * From the SMS API - use the &#x60;message-id&#x60; * From the Text-To-Speech API - use the &#x60;call-id&#x60; * From the Text-To-Speech-Prompt API - use the &#x60;call-id&#x60; | 
 **delivered** | **Boolean**| Set to _true_ if your user replied to the message you sent. Otherwise, set to _false_. **Note**: for curl, use 0 and 1. | 
 **timestamp** | **String**| When the user completed your call-to-action (e.g. visited your website, installed your app) in [UTC±00:00](https://en.wikipedia.org/wiki/UTC%C2%B100:00) format: _yyyy-MM-dd HH:mm:ss_. If you do not set this parameter, Nexmo uses the time it receives this request. | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [apiSig](../README.md#apiSig), [apiSecret](../README.md#apiSecret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

