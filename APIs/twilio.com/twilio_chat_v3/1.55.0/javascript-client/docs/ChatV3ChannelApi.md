# TwilioChat.ChatV3ChannelApi

All URIs are relative to *https://chat.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateChannel**](ChatV3ChannelApi.md#updateChannel) | **POST** /v3/Services/{ServiceSid}/Channels/{Sid} | 



## updateChannel

> ChatV3Channel updateChannel(serviceSid, sid, opts)



Update a specific Channel.

### Example

```javascript
import TwilioChat from 'twilio_chat';
let defaultClient = TwilioChat.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioChat.ChatV3ChannelApi();
let serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Service.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this Channel.
let opts = {
  'xTwilioWebhookEnabled': "xTwilioWebhookEnabled_example", // ChannelEnumWebhookEnabledType | The X-Twilio-Webhook-Enabled HTTP request header
  'messagingServiceSid': "messagingServiceSid_example", // String | The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this channel belongs to.
  'type': "type_example" // ChannelEnumChannelType | 
};
apiInstance.updateChannel(serviceSid, sid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The unique SID identifier of the Service. | 
 **sid** | **String**| A 34 character string that uniquely identifies this Channel. | 
 **xTwilioWebhookEnabled** | **ChannelEnumWebhookEnabledType**| The X-Twilio-Webhook-Enabled HTTP request header | [optional] 
 **messagingServiceSid** | **String**| The unique ID of the [Messaging Service](https://www.twilio.com/docs/messaging/api/service-resource) this channel belongs to. | [optional] 
 **type** | **ChannelEnumChannelType**|  | [optional] 

### Return type

[**ChatV3Channel**](ChatV3Channel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

