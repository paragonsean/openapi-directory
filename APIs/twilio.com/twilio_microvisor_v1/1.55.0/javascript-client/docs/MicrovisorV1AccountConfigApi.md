# TwilioMicrovisor.MicrovisorV1AccountConfigApi

All URIs are relative to *https://microvisor.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAccountConfig**](MicrovisorV1AccountConfigApi.md#createAccountConfig) | **POST** /v1/Configs | 
[**deleteAccountConfig**](MicrovisorV1AccountConfigApi.md#deleteAccountConfig) | **DELETE** /v1/Configs/{Key} | 
[**fetchAccountConfig**](MicrovisorV1AccountConfigApi.md#fetchAccountConfig) | **GET** /v1/Configs/{Key} | 
[**listAccountConfig**](MicrovisorV1AccountConfigApi.md#listAccountConfig) | **GET** /v1/Configs | 
[**updateAccountConfig**](MicrovisorV1AccountConfigApi.md#updateAccountConfig) | **POST** /v1/Configs/{Key} | 



## createAccountConfig

> MicrovisorV1AccountConfig createAccountConfig(key, value)



Create a config for an Account.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1AccountConfigApi();
let key = "key_example"; // String | The config key; up to 100 characters.
let value = "value_example"; // String | The config value; up to 4096 characters.
apiInstance.createAccountConfig(key, value, (error, data, response) => {
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
 **key** | **String**| The config key; up to 100 characters. | 
 **value** | **String**| The config value; up to 4096 characters. | 

### Return type

[**MicrovisorV1AccountConfig**](MicrovisorV1AccountConfig.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteAccountConfig

> deleteAccountConfig(key)



Delete a config for an Account.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1AccountConfigApi();
let key = "key_example"; // String | The config key; up to 100 characters.
apiInstance.deleteAccountConfig(key, (error, data, response) => {
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
 **key** | **String**| The config key; up to 100 characters. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchAccountConfig

> MicrovisorV1AccountConfig fetchAccountConfig(key)



Retrieve a Config for an Account.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1AccountConfigApi();
let key = "key_example"; // String | The config key; up to 100 characters.
apiInstance.fetchAccountConfig(key, (error, data, response) => {
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
 **key** | **String**| The config key; up to 100 characters. | 

### Return type

[**MicrovisorV1AccountConfig**](MicrovisorV1AccountConfig.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAccountConfig

> ListAccountConfigResponse listAccountConfig(opts)



Retrieve a list of all Configs for an Account.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1AccountConfigApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listAccountConfig(opts, (error, data, response) => {
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

[**ListAccountConfigResponse**](ListAccountConfigResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAccountConfig

> MicrovisorV1AccountConfig updateAccountConfig(key, value)



Update a config for an Account.

### Example

```javascript
import TwilioMicrovisor from 'twilio_microvisor';
let defaultClient = TwilioMicrovisor.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMicrovisor.MicrovisorV1AccountConfigApi();
let key = "key_example"; // String | The config key; up to 100 characters.
let value = "value_example"; // String | The config value; up to 4096 characters.
apiInstance.updateAccountConfig(key, value, (error, data, response) => {
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
 **key** | **String**| The config key; up to 100 characters. | 
 **value** | **String**| The config value; up to 4096 characters. | 

### Return type

[**MicrovisorV1AccountConfig**](MicrovisorV1AccountConfig.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

