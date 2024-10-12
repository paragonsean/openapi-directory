# TwilioProxy.ProxyV1ServiceApi

All URIs are relative to *https://proxy.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createService**](ProxyV1ServiceApi.md#createService) | **POST** /v1/Services | 
[**deleteService**](ProxyV1ServiceApi.md#deleteService) | **DELETE** /v1/Services/{Sid} | 
[**fetchService**](ProxyV1ServiceApi.md#fetchService) | **GET** /v1/Services/{Sid} | 
[**listService**](ProxyV1ServiceApi.md#listService) | **GET** /v1/Services | 
[**updateService**](ProxyV1ServiceApi.md#updateService) | **POST** /v1/Services/{Sid} | 



## createService

> ProxyV1Service createService(uniqueName, opts)



Create a new Service for Twilio Proxy

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1ServiceApi();
let uniqueName = "uniqueName_example"; // String | An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
let opts = {
  'callbackUrl': "callbackUrl_example", // String | The URL we should call when the interaction status changes.
  'chatInstanceSid': "chatInstanceSid_example", // String | The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.
  'defaultTtl': 56, // Number | The default `ttl` value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session's last create or last Interaction. The default value of `0` indicates an unlimited Session length. You can override a Session's default TTL value by setting its `ttl` value.
  'geoMatchLevel': "geoMatchLevel_example", // ServiceEnumGeoMatchLevel | 
  'interceptCallbackUrl': "interceptCallbackUrl_example", // String | The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues.
  'numberSelectionBehavior': "numberSelectionBehavior_example", // ServiceEnumNumberSelectionBehavior | 
  'outOfSessionCallbackUrl': "outOfSessionCallbackUrl_example" // String | The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/en-us/serverless/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information.
};
apiInstance.createService(uniqueName, opts, (error, data, response) => {
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
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.** | 
 **callbackUrl** | **String**| The URL we should call when the interaction status changes. | [optional] 
 **chatInstanceSid** | **String**| The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship. | [optional] 
 **defaultTtl** | **Number**| The default &#x60;ttl&#x60; value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session&#39;s last create or last Interaction. The default value of &#x60;0&#x60; indicates an unlimited Session length. You can override a Session&#39;s default TTL value by setting its &#x60;ttl&#x60; value. | [optional] 
 **geoMatchLevel** | **ServiceEnumGeoMatchLevel**|  | [optional] 
 **interceptCallbackUrl** | **String**| The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues. | [optional] 
 **numberSelectionBehavior** | **ServiceEnumNumberSelectionBehavior**|  | [optional] 
 **outOfSessionCallbackUrl** | **String**| The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/en-us/serverless/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information. | [optional] 

### Return type

[**ProxyV1Service**](ProxyV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteService

> deleteService(sid)



Delete a specific Service.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1ServiceApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to delete.
apiInstance.deleteService(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchService

> ProxyV1Service fetchService(sid)



Fetch a specific Service.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1ServiceApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to fetch.
apiInstance.fetchService(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to fetch. | 

### Return type

[**ProxyV1Service**](ProxyV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listService

> ListServiceResponse listService(opts)



Retrieve a list of all Services for Twilio Proxy. A maximum of 100 records will be returned per page.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1ServiceApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listService(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListServiceResponse**](ListServiceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateService

> ProxyV1Service updateService(sid, opts)



Update a specific Service.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1ServiceApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Service resource to update.
let opts = {
  'callbackUrl': "callbackUrl_example", // String | The URL we should call when the interaction status changes.
  'chatInstanceSid': "chatInstanceSid_example", // String | The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship.
  'defaultTtl': 56, // Number | The default `ttl` value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session's last create or last Interaction. The default value of `0` indicates an unlimited Session length. You can override a Session's default TTL value by setting its `ttl` value.
  'geoMatchLevel': "geoMatchLevel_example", // ServiceEnumGeoMatchLevel | 
  'interceptCallbackUrl': "interceptCallbackUrl_example", // String | The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues.
  'numberSelectionBehavior': "numberSelectionBehavior_example", // ServiceEnumNumberSelectionBehavior | 
  'outOfSessionCallbackUrl': "outOfSessionCallbackUrl_example", // String | The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/en-us/serverless/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information.
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.**
};
apiInstance.updateService(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Service resource to update. | 
 **callbackUrl** | **String**| The URL we should call when the interaction status changes. | [optional] 
 **chatInstanceSid** | **String**| The SID of the Chat Service Instance managed by Proxy Service. The Chat Service enables Proxy to forward SMS and channel messages to this chat instance. This is a one-to-one relationship. | [optional] 
 **defaultTtl** | **Number**| The default &#x60;ttl&#x60; value to set for Sessions created in the Service. The TTL (time to live) is measured in seconds after the Session&#39;s last create or last Interaction. The default value of &#x60;0&#x60; indicates an unlimited Session length. You can override a Session&#39;s default TTL value by setting its &#x60;ttl&#x60; value. | [optional] 
 **geoMatchLevel** | **ServiceEnumGeoMatchLevel**|  | [optional] 
 **interceptCallbackUrl** | **String**| The URL we call on each interaction. If we receive a 403 status, we block the interaction; otherwise the interaction continues. | [optional] 
 **numberSelectionBehavior** | **ServiceEnumNumberSelectionBehavior**|  | [optional] 
 **outOfSessionCallbackUrl** | **String**| The URL we should call when an inbound call or SMS action occurs on a closed or non-existent Session. If your server (or a Twilio [function](https://www.twilio.com/en-us/serverless/functions)) responds with valid [TwiML](https://www.twilio.com/docs/voice/twiml), we will process it. This means it is possible, for example, to play a message for a call, send an automated text message response, or redirect a call to another Phone Number. See [Out-of-Session Callback Response Guide](https://www.twilio.com/docs/proxy/out-session-callback-response-guide) for more information. | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. This value must be 191 characters or fewer in length and be unique. **This value should not have PII.** | [optional] 

### Return type

[**ProxyV1Service**](ProxyV1Service.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

