# TwilioFlex.FlexV1InteractionApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInteraction**](FlexV1InteractionApi.md#createInteraction) | **POST** /v1/Interactions | 
[**fetchInteraction**](FlexV1InteractionApi.md#fetchInteraction) | **GET** /v1/Interactions/{Sid} | 



## createInteraction

> FlexV1Interaction createInteraction(channel, routing, opts)



Create a new Interaction.

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InteractionApi();
let channel = null; // Object | The Interaction's channel.
let routing = null; // Object | The Interaction's routing logic.
let opts = {
  'interactionContextSid': "interactionContextSid_example" // String | The Interaction context sid is used for adding a context lookup sid
};
apiInstance.createInteraction(channel, routing, opts, (error, data, response) => {
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
 **channel** | [**Object**](Object.md)| The Interaction&#39;s channel. | 
 **routing** | [**Object**](Object.md)| The Interaction&#39;s routing logic. | 
 **interactionContextSid** | **String**| The Interaction context sid is used for adding a context lookup sid | [optional] 

### Return type

[**FlexV1Interaction**](FlexV1Interaction.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchInteraction

> FlexV1Interaction fetchInteraction(sid)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InteractionApi();
let sid = "sid_example"; // String | The SID of the Interaction resource to fetch.
apiInstance.fetchInteraction(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Interaction resource to fetch. | 

### Return type

[**FlexV1Interaction**](FlexV1Interaction.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

