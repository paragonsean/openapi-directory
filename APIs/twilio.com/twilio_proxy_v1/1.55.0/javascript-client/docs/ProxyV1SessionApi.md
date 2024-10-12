# TwilioProxy.ProxyV1SessionApi

All URIs are relative to *https://proxy.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSession**](ProxyV1SessionApi.md#createSession) | **POST** /v1/Services/{ServiceSid}/Sessions | 
[**deleteSession**](ProxyV1SessionApi.md#deleteSession) | **DELETE** /v1/Services/{ServiceSid}/Sessions/{Sid} | 
[**fetchSession**](ProxyV1SessionApi.md#fetchSession) | **GET** /v1/Services/{ServiceSid}/Sessions/{Sid} | 
[**listSession**](ProxyV1SessionApi.md#listSession) | **GET** /v1/Services/{ServiceSid}/Sessions | 
[**updateSession**](ProxyV1SessionApi.md#updateSession) | **POST** /v1/Services/{ServiceSid}/Sessions/{Sid} | 



## createSession

> ProxyV1ServiceSession createSession(serviceSid, opts)



Create a new Session

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1SessionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource.
let opts = {
  'dateExpiry': new Date("2013-10-20T19:20:30+01:00"), // Date | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session should expire. If this is value is present, it overrides the `ttl` value.
  'mode': "mode_example", // SessionEnumMode | 
  'participants': [null], // [Object] | The Participant objects to include in the new session.
  'status': "status_example", // SessionEnumStatus | 
  'ttl': 56, // Number | The time, in seconds, when the session will expire. The time is measured from the last Session create or the Session's last Interaction.
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
};
apiInstance.createSession(serviceSid, opts, (error, data, response) => {
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
 **dateExpiry** | **Date**| The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session should expire. If this is value is present, it overrides the &#x60;ttl&#x60; value. | [optional] 
 **mode** | **SessionEnumMode**|  | [optional] 
 **participants** | [**[Object]**](Object.md)| The Participant objects to include in the new session. | [optional] 
 **status** | **SessionEnumStatus**|  | [optional] 
 **ttl** | **Number**| The time, in seconds, when the session will expire. The time is measured from the last Session create or the Session&#39;s last Interaction. | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.** | [optional] 

### Return type

[**ProxyV1ServiceSession**](ProxyV1ServiceSession.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSession

> deleteSession(serviceSid, sid)



Delete a specific Session.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1SessionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to delete.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Session resource to delete.
apiInstance.deleteSession(serviceSid, sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Session resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSession

> ProxyV1ServiceSession fetchSession(serviceSid, sid)



Fetch a specific Session.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1SessionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Session resource to fetch.
apiInstance.fetchSession(serviceSid, sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Session resource to fetch. | 

### Return type

[**ProxyV1ServiceSession**](ProxyV1ServiceSession.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSession

> ListSessionResponse listSession(serviceSid, opts)



Retrieve a list of all Sessions for the Service. A maximum of 100 records will be returned per page.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1SessionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSession(serviceSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSessionResponse**](ListSessionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSession

> ProxyV1ServiceSession updateSession(serviceSid, sid, opts)



Update a specific Session.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1SessionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to update.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Session resource to update.
let opts = {
  'dateExpiry': new Date("2013-10-20T19:20:30+01:00"), // Date | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session should expire. If this is value is present, it overrides the `ttl` value.
  'status': "status_example", // SessionEnumStatus | 
  'ttl': 56 // Number | The time, in seconds, when the session will expire. The time is measured from the last Session create or the Session's last Interaction.
};
apiInstance.updateSession(serviceSid, sid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to update. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Session resource to update. | 
 **dateExpiry** | **Date**| The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date when the Session should expire. If this is value is present, it overrides the &#x60;ttl&#x60; value. | [optional] 
 **status** | **SessionEnumStatus**|  | [optional] 
 **ttl** | **Number**| The time, in seconds, when the session will expire. The time is measured from the last Session create or the Session&#39;s last Interaction. | [optional] 

### Return type

[**ProxyV1ServiceSession**](ProxyV1ServiceSession.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

