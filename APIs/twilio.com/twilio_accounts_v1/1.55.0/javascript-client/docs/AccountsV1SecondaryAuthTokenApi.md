# TwilioAccounts.AccountsV1SecondaryAuthTokenApi

All URIs are relative to *https://accounts.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSecondaryAuthToken**](AccountsV1SecondaryAuthTokenApi.md#createSecondaryAuthToken) | **POST** /v1/AuthTokens/Secondary | 
[**deleteSecondaryAuthToken**](AccountsV1SecondaryAuthTokenApi.md#deleteSecondaryAuthToken) | **DELETE** /v1/AuthTokens/Secondary | 



## createSecondaryAuthToken

> AccountsV1SecondaryAuthToken createSecondaryAuthToken()



Create a new secondary Auth Token

### Example

```javascript
import TwilioAccounts from 'twilio_accounts';
let defaultClient = TwilioAccounts.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAccounts.AccountsV1SecondaryAuthTokenApi();
apiInstance.createSecondaryAuthToken((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**AccountsV1SecondaryAuthToken**](AccountsV1SecondaryAuthToken.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSecondaryAuthToken

> deleteSecondaryAuthToken()



Delete the secondary Auth Token from your account

### Example

```javascript
import TwilioAccounts from 'twilio_accounts';
let defaultClient = TwilioAccounts.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAccounts.AccountsV1SecondaryAuthTokenApi();
apiInstance.deleteSecondaryAuthToken((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

