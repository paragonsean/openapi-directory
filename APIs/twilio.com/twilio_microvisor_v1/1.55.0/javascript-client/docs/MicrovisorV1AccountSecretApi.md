# TwilioMicrovisor.MicrovisorV1AccountSecretApi

All URIs are relative to *https://microvisor.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAccountSecret**](MicrovisorV1AccountSecretApi.md#createAccountSecret) | **POST** /v1/Secrets | 
[**deleteAccountSecret**](MicrovisorV1AccountSecretApi.md#deleteAccountSecret) | **DELETE** /v1/Secrets/{Key} | 
[**fetchAccountSecret**](MicrovisorV1AccountSecretApi.md#fetchAccountSecret) | **GET** /v1/Secrets/{Key} | 
[**listAccountSecret**](MicrovisorV1AccountSecretApi.md#listAccountSecret) | **GET** /v1/Secrets | 
[**updateAccountSecret**](MicrovisorV1AccountSecretApi.md#updateAccountSecret) | **POST** /v1/Secrets/{Key} | 



## createAccountSecret

> MicrovisorV1AccountSecret createAccountSecret(key, value)



Create a secret for an Account.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1AccountSecretApi();
let key = "key_example"; // String | The secret key; up to 100 characters.
let value = "value_example"; // String | The secret value; up to 4096 characters.
apiInstance.createAccountSecret(key, value, (error, data, response) => {
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
 **key** | **String**| The secret key; up to 100 characters. | 
 **value** | **String**| The secret value; up to 4096 characters. | 

### Return type

[**MicrovisorV1AccountSecret**](MicrovisorV1AccountSecret.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteAccountSecret

> deleteAccountSecret(key)



Delete a secret for an Account.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1AccountSecretApi();
let key = "key_example"; // String | The secret key; up to 100 characters.
apiInstance.deleteAccountSecret(key, (error, data, response) => {
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
 **key** | **String**| The secret key; up to 100 characters. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchAccountSecret

> MicrovisorV1AccountSecret fetchAccountSecret(key)



Retrieve a Secret for an Account.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1AccountSecretApi();
let key = "key_example"; // String | The secret key; up to 100 characters.
apiInstance.fetchAccountSecret(key, (error, data, response) => {
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
 **key** | **String**| The secret key; up to 100 characters. | 

### Return type

[**MicrovisorV1AccountSecret**](MicrovisorV1AccountSecret.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAccountSecret

> ListAccountSecretResponse listAccountSecret(opts)



Retrieve a list of all Secrets for an Account.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1AccountSecretApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listAccountSecret(opts, (error, data, response) => {
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

[**ListAccountSecretResponse**](ListAccountSecretResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAccountSecret

> MicrovisorV1AccountSecret updateAccountSecret(key, value)



Update a secret for an Account.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1AccountSecretApi();
let key = "key_example"; // String | The secret key; up to 100 characters.
let value = "value_example"; // String | The secret value; up to 4096 characters.
apiInstance.updateAccountSecret(key, value, (error, data, response) => {
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
 **key** | **String**| The secret key; up to 100 characters. | 
 **value** | **String**| The secret value; up to 4096 characters. | 

### Return type

[**MicrovisorV1AccountSecret**](MicrovisorV1AccountSecret.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

