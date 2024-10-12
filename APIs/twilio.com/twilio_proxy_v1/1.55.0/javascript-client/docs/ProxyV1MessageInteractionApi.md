# TwilioProxy.ProxyV1MessageInteractionApi

All URIs are relative to *https://proxy.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMessageInteraction**](ProxyV1MessageInteractionApi.md#createMessageInteraction) | **POST** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{ParticipantSid}/MessageInteractions | 
[**fetchMessageInteraction**](ProxyV1MessageInteractionApi.md#fetchMessageInteraction) | **GET** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{ParticipantSid}/MessageInteractions/{Sid} | 
[**listMessageInteraction**](ProxyV1MessageInteractionApi.md#listMessageInteraction) | **GET** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{ParticipantSid}/MessageInteractions | 



## createMessageInteraction

> ProxyV1ServiceSessionParticipantMessageInteraction createMessageInteraction(serviceSid, sessionSid, participantSid, opts)



Create a new message Interaction to send directly from your system to one [Participant](https://www.twilio.com/docs/proxy/api/participant).  The &#x60;inbound&#x60; properties for the Interaction will always be empty.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1MessageInteractionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource.
let sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) resource.
let participantSid = "participantSid_example"; // String | The SID of the [Participant](https://www.twilio.com/docs/proxy/api/participant) resource.
let opts = {
  'body': "body_example", // String | The message to send to the participant
  'mediaUrl': ["null"] // [String] | Reserved. Not currently supported.
};
apiInstance.createMessageInteraction(serviceSid, sessionSid, participantSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource. | 
 **sessionSid** | **String**| The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) resource. | 
 **participantSid** | **String**| The SID of the [Participant](https://www.twilio.com/docs/proxy/api/participant) resource. | 
 **body** | **String**| The message to send to the participant | [optional] 
 **mediaUrl** | [**[String]**](String.md)| Reserved. Not currently supported. | [optional] 

### Return type

[**ProxyV1ServiceSessionParticipantMessageInteraction**](ProxyV1ServiceSessionParticipantMessageInteraction.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchMessageInteraction

> ProxyV1ServiceSessionParticipantMessageInteraction fetchMessageInteraction(serviceSid, sessionSid, participantSid, sid)





### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1MessageInteractionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to fetch.
let sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to fetch.
let participantSid = "participantSid_example"; // String | The SID of the [Participant](https://www.twilio.com/docs/proxy/api/participant) resource.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the MessageInteraction resource to fetch.
apiInstance.fetchMessageInteraction(serviceSid, sessionSid, participantSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to fetch. | 
 **sessionSid** | **String**| The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to fetch. | 
 **participantSid** | **String**| The SID of the [Participant](https://www.twilio.com/docs/proxy/api/participant) resource. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the MessageInteraction resource to fetch. | 

### Return type

[**ProxyV1ServiceSessionParticipantMessageInteraction**](ProxyV1ServiceSessionParticipantMessageInteraction.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMessageInteraction

> ListMessageInteractionResponse listMessageInteraction(serviceSid, sessionSid, participantSid, opts)





### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1MessageInteractionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) to read the resources from.
let sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) to read the resources from.
let participantSid = "participantSid_example"; // String | The SID of the [Participant](https://www.twilio.com/docs/proxy/api/participant) to read the resources from.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listMessageInteraction(serviceSid, sessionSid, participantSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) to read the resources from. | 
 **sessionSid** | **String**| The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) to read the resources from. | 
 **participantSid** | **String**| The SID of the [Participant](https://www.twilio.com/docs/proxy/api/participant) to read the resources from. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListMessageInteractionResponse**](ListMessageInteractionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

