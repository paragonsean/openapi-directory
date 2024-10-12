# TwilioFlex.FlexV1InteractionChannelInviteApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInteractionChannelInvite**](FlexV1InteractionChannelInviteApi.md#createInteractionChannelInvite) | **POST** /v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Invites | 
[**listInteractionChannelInvite**](FlexV1InteractionChannelInviteApi.md#listInteractionChannelInvite) | **GET** /v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Invites | 



## createInteractionChannelInvite

> FlexV1InteractionInteractionChannelInteractionChannelInvite createInteractionChannelInvite(interactionSid, channelSid, routing)



Invite an Agent or a TaskQueue to a Channel.

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InteractionChannelInviteApi();
let interactionSid = "interactionSid_example"; // String | The Interaction SID for this Channel.
let channelSid = "channelSid_example"; // String | The Channel SID for this Invite.
let routing = null; // Object | The Interaction's routing logic.
apiInstance.createInteractionChannelInvite(interactionSid, channelSid, routing, (error, data, response) => {
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
 **interactionSid** | **String**| The Interaction SID for this Channel. | 
 **channelSid** | **String**| The Channel SID for this Invite. | 
 **routing** | [**Object**](Object.md)| The Interaction&#39;s routing logic. | 

### Return type

[**FlexV1InteractionInteractionChannelInteractionChannelInvite**](FlexV1InteractionInteractionChannelInteractionChannelInvite.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## listInteractionChannelInvite

> ListInteractionChannelInviteResponse listInteractionChannelInvite(interactionSid, channelSid, opts)



List all Invites for a Channel.

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InteractionChannelInviteApi();
let interactionSid = "interactionSid_example"; // String | The Interaction SID for this Channel.
let channelSid = "channelSid_example"; // String | The Channel SID for this Participant.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listInteractionChannelInvite(interactionSid, channelSid, opts, (error, data, response) => {
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
 **interactionSid** | **String**| The Interaction SID for this Channel. | 
 **channelSid** | **String**| The Channel SID for this Participant. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListInteractionChannelInviteResponse**](ListInteractionChannelInviteResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

