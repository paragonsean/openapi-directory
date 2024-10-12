# TwilioVerify.VerifyV2RateLimitApi

All URIs are relative to *https://verify.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRateLimit**](VerifyV2RateLimitApi.md#createRateLimit) | **POST** /v2/Services/{ServiceSid}/RateLimits | 
[**deleteRateLimit**](VerifyV2RateLimitApi.md#deleteRateLimit) | **DELETE** /v2/Services/{ServiceSid}/RateLimits/{Sid} | 
[**fetchRateLimit**](VerifyV2RateLimitApi.md#fetchRateLimit) | **GET** /v2/Services/{ServiceSid}/RateLimits/{Sid} | 
[**listRateLimit**](VerifyV2RateLimitApi.md#listRateLimit) | **GET** /v2/Services/{ServiceSid}/RateLimits | 
[**updateRateLimit**](VerifyV2RateLimitApi.md#updateRateLimit) | **POST** /v2/Services/{ServiceSid}/RateLimits/{Sid} | 



## createRateLimit

> VerifyV2ServiceRateLimit createRateLimit(serviceSid, uniqueName, opts)



Create a new Rate Limit for a Service

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2RateLimitApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
let uniqueName = "uniqueName_example"; // String | Provides a unique and addressable name to be assigned to this Rate Limit, assigned by the developer, to be optionally used in addition to SID. **This value should not contain PII.**
let opts = {
  'description': "description_example" // String | Description of this Rate Limit
};
apiInstance.createRateLimit(serviceSid, uniqueName, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with. | 
 **uniqueName** | **String**| Provides a unique and addressable name to be assigned to this Rate Limit, assigned by the developer, to be optionally used in addition to SID. **This value should not contain PII.** | 
 **description** | **String**| Description of this Rate Limit | [optional] 

### Return type

[**VerifyV2ServiceRateLimit**](VerifyV2ServiceRateLimit.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteRateLimit

> deleteRateLimit(serviceSid, sid)



Delete a specific Rate Limit.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2RateLimitApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
apiInstance.deleteRateLimit(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchRateLimit

> VerifyV2ServiceRateLimit fetchRateLimit(serviceSid, sid)



Fetch a specific Rate Limit.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2RateLimitApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
apiInstance.fetchRateLimit(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch. | 

### Return type

[**VerifyV2ServiceRateLimit**](VerifyV2ServiceRateLimit.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRateLimit

> ListRateLimitResponse listRateLimit(serviceSid, opts)



Retrieve a list of all Rate Limits for a service.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2RateLimitApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listRateLimit(serviceSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListRateLimitResponse**](ListRateLimitResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRateLimit

> VerifyV2ServiceRateLimit updateRateLimit(serviceSid, sid, opts)



Update a specific Rate Limit.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2RateLimitApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch.
let opts = {
  'description': "description_example" // String | Description of this Rate Limit
};
apiInstance.updateRateLimit(serviceSid, sid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Rate Limit resource to fetch. | 
 **description** | **String**| Description of this Rate Limit | [optional] 

### Return type

[**VerifyV2ServiceRateLimit**](VerifyV2ServiceRateLimit.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

