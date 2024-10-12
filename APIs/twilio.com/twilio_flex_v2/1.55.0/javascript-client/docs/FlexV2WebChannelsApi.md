# TwilioFlex.FlexV2WebChannelsApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createWebChannel**](FlexV2WebChannelsApi.md#createWebChannel) | **POST** /v2/WebChats | 



## createWebChannel

> FlexV2WebChannel createWebChannel(addressSid, opts)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV2WebChannelsApi();
let addressSid = "addressSid_example"; // String | The SID of the Conversations Address. See [Address Configuration Resource](https://www.twilio.com/docs/conversations/api/address-configuration-resource) for configuration details. When a conversation is created on the Flex backend, the callback URL will be set to the corresponding Studio Flow SID or webhook URL in your address configuration.
let opts = {
  'chatFriendlyName': "chatFriendlyName_example", // String | The Conversation's friendly name. See the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource) for an example.
  'customerFriendlyName': "customerFriendlyName_example", // String | The Conversation participant's friendly name. See the [Conversation Participant Resource](https://www.twilio.com/docs/conversations/api/conversation-participant-resource) for an example.
  'preEngagementData': "preEngagementData_example" // String | The pre-engagement data.
};
apiInstance.createWebChannel(addressSid, opts, (error, data, response) => {
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
 **addressSid** | **String**| The SID of the Conversations Address. See [Address Configuration Resource](https://www.twilio.com/docs/conversations/api/address-configuration-resource) for configuration details. When a conversation is created on the Flex backend, the callback URL will be set to the corresponding Studio Flow SID or webhook URL in your address configuration. | 
 **chatFriendlyName** | **String**| The Conversation&#39;s friendly name. See the [Conversation resource](https://www.twilio.com/docs/conversations/api/conversation-resource) for an example. | [optional] 
 **customerFriendlyName** | **String**| The Conversation participant&#39;s friendly name. See the [Conversation Participant Resource](https://www.twilio.com/docs/conversations/api/conversation-participant-resource) for an example. | [optional] 
 **preEngagementData** | **String**| The pre-engagement data. | [optional] 

### Return type

[**FlexV2WebChannel**](FlexV2WebChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

