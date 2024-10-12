# TwilioFlex.FlexV1InteractionChannelApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchInteractionChannel**](FlexV1InteractionChannelApi.md#fetchInteractionChannel) | **GET** /v1/Interactions/{InteractionSid}/Channels/{Sid} | 
[**listInteractionChannel**](FlexV1InteractionChannelApi.md#listInteractionChannel) | **GET** /v1/Interactions/{InteractionSid}/Channels | 
[**updateInteractionChannel**](FlexV1InteractionChannelApi.md#updateInteractionChannel) | **POST** /v1/Interactions/{InteractionSid}/Channels/{Sid} | 



## fetchInteractionChannel

> FlexV1InteractionInteractionChannel fetchInteractionChannel(interactionSid, sid)



Fetch a Channel for an Interaction.

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InteractionChannelApi();
let interactionSid = "interactionSid_example"; // String | The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
let sid = "sid_example"; // String | The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
apiInstance.fetchInteractionChannel(interactionSid, sid, (error, data, response) => {
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
 **interactionSid** | **String**| The unique string created by Twilio to identify an Interaction resource, prefixed with KD. | 
 **sid** | **String**| The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO. | 

### Return type

[**FlexV1InteractionInteractionChannel**](FlexV1InteractionInteractionChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInteractionChannel

> ListInteractionChannelResponse listInteractionChannel(interactionSid, opts)



List all Channels for an Interaction.

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InteractionChannelApi();
let interactionSid = "interactionSid_example"; // String | The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listInteractionChannel(interactionSid, opts, (error, data, response) => {
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
 **interactionSid** | **String**| The unique string created by Twilio to identify an Interaction resource, prefixed with KD. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListInteractionChannelResponse**](ListInteractionChannelResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateInteractionChannel

> FlexV1InteractionInteractionChannel updateInteractionChannel(interactionSid, sid, status, opts)



Update an existing Interaction Channel.

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InteractionChannelApi();
let interactionSid = "interactionSid_example"; // String | The unique string created by Twilio to identify an Interaction resource, prefixed with KD.
let sid = "sid_example"; // String | The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO.
let status = "status_example"; // InteractionChannelEnumUpdateChannelStatus | 
let opts = {
  'routing': null // Object | It changes the state of associated tasks. Routing status is required, When the channel status is set to `inactive`. Allowed Value for routing status is `closed`. Otherwise Optional, if not specified, all tasks will be set to `wrapping`.
};
apiInstance.updateInteractionChannel(interactionSid, sid, status, opts, (error, data, response) => {
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
 **interactionSid** | **String**| The unique string created by Twilio to identify an Interaction resource, prefixed with KD. | 
 **sid** | **String**| The unique string created by Twilio to identify an Interaction Channel resource, prefixed with UO. | 
 **status** | **InteractionChannelEnumUpdateChannelStatus**|  | 
 **routing** | [**Object**](Object.md)| It changes the state of associated tasks. Routing status is required, When the channel status is set to &#x60;inactive&#x60;. Allowed Value for routing status is &#x60;closed&#x60;. Otherwise Optional, if not specified, all tasks will be set to &#x60;wrapping&#x60;. | [optional] 

### Return type

[**FlexV1InteractionInteractionChannel**](FlexV1InteractionInteractionChannel.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

