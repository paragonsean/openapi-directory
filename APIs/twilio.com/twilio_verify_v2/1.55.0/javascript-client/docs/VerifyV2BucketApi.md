# TwilioVerify.VerifyV2BucketApi

All URIs are relative to *https://verify.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBucket**](VerifyV2BucketApi.md#createBucket) | **POST** /v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets | 
[**deleteBucket**](VerifyV2BucketApi.md#deleteBucket) | **DELETE** /v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets/{Sid} | 
[**fetchBucket**](VerifyV2BucketApi.md#fetchBucket) | **GET** /v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets/{Sid} | 
[**listBucket**](VerifyV2BucketApi.md#listBucket) | **GET** /v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets | 
[**updateBucket**](VerifyV2BucketApi.md#updateBucket) | **POST** /v2/Services/{ServiceSid}/RateLimits/{RateLimitSid}/Buckets/{Sid} | 



## createBucket

> VerifyV2ServiceRateLimitBucket createBucket(serviceSid, rateLimitSid, interval, max)



Create a new Bucket for a Rate Limit

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2BucketApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
let rateLimitSid = "rateLimitSid_example"; // String | The Twilio-provided string that uniquely identifies the Rate Limit resource.
let interval = 56; // Number | Number of seconds that the rate limit will be enforced over.
let max = 56; // Number | Maximum number of requests permitted in during the interval.
apiInstance.createBucket(serviceSid, rateLimitSid, interval, max, (error, data, response) => {
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
 **rateLimitSid** | **String**| The Twilio-provided string that uniquely identifies the Rate Limit resource. | 
 **interval** | **Number**| Number of seconds that the rate limit will be enforced over. | 
 **max** | **Number**| Maximum number of requests permitted in during the interval. | 

### Return type

[**VerifyV2ServiceRateLimitBucket**](VerifyV2ServiceRateLimitBucket.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteBucket

> deleteBucket(serviceSid, rateLimitSid, sid)



Delete a specific Bucket.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2BucketApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
let rateLimitSid = "rateLimitSid_example"; // String | The Twilio-provided string that uniquely identifies the Rate Limit resource.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this Bucket.
apiInstance.deleteBucket(serviceSid, rateLimitSid, sid, (error, data, response) => {
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
 **rateLimitSid** | **String**| The Twilio-provided string that uniquely identifies the Rate Limit resource. | 
 **sid** | **String**| A 34 character string that uniquely identifies this Bucket. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchBucket

> VerifyV2ServiceRateLimitBucket fetchBucket(serviceSid, rateLimitSid, sid)



Fetch a specific Bucket.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2BucketApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
let rateLimitSid = "rateLimitSid_example"; // String | The Twilio-provided string that uniquely identifies the Rate Limit resource.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this Bucket.
apiInstance.fetchBucket(serviceSid, rateLimitSid, sid, (error, data, response) => {
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
 **rateLimitSid** | **String**| The Twilio-provided string that uniquely identifies the Rate Limit resource. | 
 **sid** | **String**| A 34 character string that uniquely identifies this Bucket. | 

### Return type

[**VerifyV2ServiceRateLimitBucket**](VerifyV2ServiceRateLimitBucket.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBucket

> ListBucketResponse listBucket(serviceSid, rateLimitSid, opts)



Retrieve a list of all Buckets for a Rate Limit.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2BucketApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
let rateLimitSid = "rateLimitSid_example"; // String | The Twilio-provided string that uniquely identifies the Rate Limit resource.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listBucket(serviceSid, rateLimitSid, opts, (error, data, response) => {
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
 **rateLimitSid** | **String**| The Twilio-provided string that uniquely identifies the Rate Limit resource. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListBucketResponse**](ListBucketResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateBucket

> VerifyV2ServiceRateLimitBucket updateBucket(serviceSid, rateLimitSid, sid, opts)



Update a specific Bucket.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2BucketApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Service](https://www.twilio.com/docs/verify/api/service) the resource is associated with.
let rateLimitSid = "rateLimitSid_example"; // String | The Twilio-provided string that uniquely identifies the Rate Limit resource.
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this Bucket.
let opts = {
  'interval': 56, // Number | Number of seconds that the rate limit will be enforced over.
  'max': 56 // Number | Maximum number of requests permitted in during the interval.
};
apiInstance.updateBucket(serviceSid, rateLimitSid, sid, opts, (error, data, response) => {
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
 **rateLimitSid** | **String**| The Twilio-provided string that uniquely identifies the Rate Limit resource. | 
 **sid** | **String**| A 34 character string that uniquely identifies this Bucket. | 
 **interval** | **Number**| Number of seconds that the rate limit will be enforced over. | [optional] 
 **max** | **Number**| Maximum number of requests permitted in during the interval. | [optional] 

### Return type

[**VerifyV2ServiceRateLimitBucket**](VerifyV2ServiceRateLimitBucket.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

