# TwilioVoice.VoiceV1ConnectionPolicyApi

All URIs are relative to *https://voice.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createConnectionPolicy**](VoiceV1ConnectionPolicyApi.md#createConnectionPolicy) | **POST** /v1/ConnectionPolicies | 
[**deleteConnectionPolicy**](VoiceV1ConnectionPolicyApi.md#deleteConnectionPolicy) | **DELETE** /v1/ConnectionPolicies/{Sid} | 
[**fetchConnectionPolicy**](VoiceV1ConnectionPolicyApi.md#fetchConnectionPolicy) | **GET** /v1/ConnectionPolicies/{Sid} | 
[**listConnectionPolicy**](VoiceV1ConnectionPolicyApi.md#listConnectionPolicy) | **GET** /v1/ConnectionPolicies | 
[**updateConnectionPolicy**](VoiceV1ConnectionPolicyApi.md#updateConnectionPolicy) | **POST** /v1/ConnectionPolicies/{Sid} | 



## createConnectionPolicy

> VoiceV1ConnectionPolicy createConnectionPolicy(opts)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1ConnectionPolicyApi();
let opts = {
  'friendlyName': "friendlyName_example" // String | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
};
apiInstance.createConnectionPolicy(opts, (error, data, response) => {
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
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long. | [optional] 

### Return type

[**VoiceV1ConnectionPolicy**](VoiceV1ConnectionPolicy.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteConnectionPolicy

> deleteConnectionPolicy(sid)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1ConnectionPolicyApi();
let sid = "sid_example"; // String | The unique string that we created to identify the Connection Policy resource to delete.
apiInstance.deleteConnectionPolicy(sid, (error, data, response) => {
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
 **sid** | **String**| The unique string that we created to identify the Connection Policy resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchConnectionPolicy

> VoiceV1ConnectionPolicy fetchConnectionPolicy(sid)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1ConnectionPolicyApi();
let sid = "sid_example"; // String | The unique string that we created to identify the Connection Policy resource to fetch.
apiInstance.fetchConnectionPolicy(sid, (error, data, response) => {
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
 **sid** | **String**| The unique string that we created to identify the Connection Policy resource to fetch. | 

### Return type

[**VoiceV1ConnectionPolicy**](VoiceV1ConnectionPolicy.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConnectionPolicy

> ListConnectionPolicyResponse listConnectionPolicy(opts)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1ConnectionPolicyApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listConnectionPolicy(opts, (error, data, response) => {
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

[**ListConnectionPolicyResponse**](ListConnectionPolicyResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateConnectionPolicy

> VoiceV1ConnectionPolicy updateConnectionPolicy(sid, opts)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1ConnectionPolicyApi();
let sid = "sid_example"; // String | The unique string that we created to identify the Connection Policy resource to update.
let opts = {
  'friendlyName': "friendlyName_example" // String | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
};
apiInstance.updateConnectionPolicy(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The unique string that we created to identify the Connection Policy resource to update. | 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long. | [optional] 

### Return type

[**VoiceV1ConnectionPolicy**](VoiceV1ConnectionPolicy.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

