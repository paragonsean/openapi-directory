# TwilioFlex.FlexV1InteractionChannelParticipantApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInteractionChannelParticipant**](FlexV1InteractionChannelParticipantApi.md#createInteractionChannelParticipant) | **POST** /v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Participants | 
[**listInteractionChannelParticipant**](FlexV1InteractionChannelParticipantApi.md#listInteractionChannelParticipant) | **GET** /v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Participants | 
[**updateInteractionChannelParticipant**](FlexV1InteractionChannelParticipantApi.md#updateInteractionChannelParticipant) | **POST** /v1/Interactions/{InteractionSid}/Channels/{ChannelSid}/Participants/{Sid} | 



## createInteractionChannelParticipant

> FlexV1InteractionInteractionChannelInteractionChannelParticipant createInteractionChannelParticipant(interactionSid, channelSid, mediaProperties, type, opts)



Add a Participant to a Channel.

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InteractionChannelParticipantApi();
let interactionSid = "interactionSid_example"; // String | The Interaction Sid for the new Channel Participant.
let channelSid = "channelSid_example"; // String | The Channel Sid for the new Channel Participant.
let mediaProperties = null; // Object | JSON representing the Media Properties for the new Participant.
let type = "type_example"; // InteractionChannelParticipantEnumType | 
let opts = {
  'routingProperties': null // Object | Object representing the Routing Properties for the new Participant.
};
apiInstance.createInteractionChannelParticipant(interactionSid, channelSid, mediaProperties, type, opts, (error, data, response) => {
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
 **interactionSid** | **String**| The Interaction Sid for the new Channel Participant. | 
 **channelSid** | **String**| The Channel Sid for the new Channel Participant. | 
 **mediaProperties** | [**Object**](Object.md)| JSON representing the Media Properties for the new Participant. | 
 **type** | **InteractionChannelParticipantEnumType**|  | 
 **routingProperties** | [**Object**](Object.md)| Object representing the Routing Properties for the new Participant. | [optional] 

### Return type

[**FlexV1InteractionInteractionChannelInteractionChannelParticipant**](FlexV1InteractionInteractionChannelInteractionChannelParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## listInteractionChannelParticipant

> ListInteractionChannelParticipantResponse listInteractionChannelParticipant(interactionSid, channelSid, opts)



List all Participants for a Channel.

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InteractionChannelParticipantApi();
let interactionSid = "interactionSid_example"; // String | The Interaction Sid for this channel.
let channelSid = "channelSid_example"; // String | The Channel Sid for this Participant.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listInteractionChannelParticipant(interactionSid, channelSid, opts, (error, data, response) => {
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
 **interactionSid** | **String**| The Interaction Sid for this channel. | 
 **channelSid** | **String**| The Channel Sid for this Participant. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListInteractionChannelParticipantResponse**](ListInteractionChannelParticipantResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateInteractionChannelParticipant

> FlexV1InteractionInteractionChannelInteractionChannelParticipant updateInteractionChannelParticipant(interactionSid, channelSid, sid, status)



Update an existing Channel Participant.

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InteractionChannelParticipantApi();
let interactionSid = "interactionSid_example"; // String | The Interaction Sid for this channel.
let channelSid = "channelSid_example"; // String | The Channel Sid for this Participant.
let sid = "sid_example"; // String | The unique string created by Twilio to identify an Interaction Channel resource.
let status = "status_example"; // InteractionChannelParticipantEnumStatus | 
apiInstance.updateInteractionChannelParticipant(interactionSid, channelSid, sid, status, (error, data, response) => {
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
 **interactionSid** | **String**| The Interaction Sid for this channel. | 
 **channelSid** | **String**| The Channel Sid for this Participant. | 
 **sid** | **String**| The unique string created by Twilio to identify an Interaction Channel resource. | 
 **status** | **InteractionChannelParticipantEnumStatus**|  | 

### Return type

[**FlexV1InteractionInteractionChannelInteractionChannelParticipant**](FlexV1InteractionInteractionChannelInteractionChannelParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

