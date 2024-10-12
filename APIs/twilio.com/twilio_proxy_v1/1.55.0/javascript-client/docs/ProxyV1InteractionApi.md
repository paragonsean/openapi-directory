# TwilioProxy.ProxyV1InteractionApi

All URIs are relative to *https://proxy.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteInteraction**](ProxyV1InteractionApi.md#deleteInteraction) | **DELETE** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Interactions/{Sid} | 
[**fetchInteraction**](ProxyV1InteractionApi.md#fetchInteraction) | **GET** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Interactions/{Sid} | 
[**listInteraction**](ProxyV1InteractionApi.md#listInteraction) | **GET** /v1/Services/{ServiceSid}/Sessions/{SessionSid}/Interactions | 



## deleteInteraction

> deleteInteraction(serviceSid, sessionSid, sid)



Delete a specific Interaction.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1InteractionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to delete.
let sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to delete.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Interaction resource to delete.
apiInstance.deleteInteraction(serviceSid, sessionSid, sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Interaction resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchInteraction

> ProxyV1ServiceSessionInteraction fetchInteraction(serviceSid, sessionSid, sid)



Retrieve a list of Interactions for a given [Session](https://www.twilio.com/docs/proxy/api/session).

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1InteractionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to fetch.
let sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) of the resource to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Interaction resource to fetch.
apiInstance.fetchInteraction(serviceSid, sessionSid, sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Interaction resource to fetch. | 

### Return type

[**ProxyV1ServiceSessionInteraction**](ProxyV1ServiceSessionInteraction.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInteraction

> ListInteractionResponse listInteraction(serviceSid, sessionSid, opts)



Retrieve a list of all Interactions for a Session. A maximum of 100 records will be returned per page.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1InteractionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) to read the resources from.
let sessionSid = "sessionSid_example"; // String | The SID of the parent [Session](https://www.twilio.com/docs/proxy/api/session) to read the resources from.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listInteraction(serviceSid, sessionSid, opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListInteractionResponse**](ListInteractionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

