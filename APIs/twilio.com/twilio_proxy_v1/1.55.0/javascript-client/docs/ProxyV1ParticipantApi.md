# TwilioProxy.ProxyV1ParticipantApi

All URIs are relative to *https://proxy.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createParticipant**](ProxyV1ParticipantApi.md#createParticipant) | **POST** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants | 
[**deleteParticipant**](ProxyV1ParticipantApi.md#deleteParticipant) | **DELETE** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{Sid} | 
[**fetchParticipant**](ProxyV1ParticipantApi.md#fetchParticipant) | **GET** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants/{Sid} | 
[**listParticipant**](ProxyV1ParticipantApi.md#listParticipant) | **GET** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Participants | 



## createParticipant

> ProxyV1ServiceSessionParticipant createParticipant(serviceSid, sessionSid, identifier, opts)



Add a new Participant to the Session

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1ParticipantApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource.
let sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) resource.
let identifier = "identifier_example"; // String | The phone number of the Participant.
let opts = {
  'friendlyName': "friendlyName_example", // String | The string that you assigned to describe the participant. This value must be 255 characters or fewer. **This value should not have PII.**
  'proxyIdentifier': "proxyIdentifier_example", // String | The proxy phone number to use for the Participant. If not specified, Proxy will select a number from the pool.
  'proxyIdentifierSid': "proxyIdentifierSid_example" // String | The SID of the Proxy Identifier to assign to the Participant.
};
apiInstance.createParticipant(serviceSid, sessionSid, identifier, opts, (error, data, response) => {
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
 **identifier** | **String**| The phone number of the Participant. | 
 **friendlyName** | **String**| The string that you assigned to describe the participant. This value must be 255 characters or fewer. **This value should not have PII.** | [optional] 
 **proxyIdentifier** | **String**| The proxy phone number to use for the Participant. If not specified, Proxy will select a number from the pool. | [optional] 
 **proxyIdentifierSid** | **String**| The SID of the Proxy Identifier to assign to the Participant. | [optional] 

### Return type

[**ProxyV1ServiceSessionParticipant**](ProxyV1ServiceSessionParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteParticipant

> deleteParticipant(serviceSid, sessionSid, sid)



Delete a specific Participant. This is a soft-delete. The participant remains associated with the session and cannot be re-added. Participants are only permanently deleted when the [Session](https://www.twilio.com/docs/proxy/api/session) is deleted.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1ParticipantApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to delete.
let sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to delete.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Participant resource to delete.
apiInstance.deleteParticipant(serviceSid, sessionSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to delete. | 
 **sessionSid** | **String**| The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to delete. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Participant resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchParticipant

> ProxyV1ServiceSessionParticipant fetchParticipant(serviceSid, sessionSid, sid)



Fetch a specific Participant.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1ParticipantApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to fetch.
let sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Participant resource to fetch.
apiInstance.fetchParticipant(serviceSid, sessionSid, sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Participant resource to fetch. | 

### Return type

[**ProxyV1ServiceSessionParticipant**](ProxyV1ServiceSessionParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listParticipant

> ListParticipantResponse listParticipant(serviceSid, sessionSid, opts)



Retrieve a list of all Participants in a Session.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1ParticipantApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resources to read.
let sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resources to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listParticipant(serviceSid, sessionSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resources to read. | 
 **sessionSid** | **String**| The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resources to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListParticipantResponse**](ListParticipantResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

