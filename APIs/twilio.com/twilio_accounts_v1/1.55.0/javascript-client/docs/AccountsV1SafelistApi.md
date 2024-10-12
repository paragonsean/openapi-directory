# TwilioAccounts.AccountsV1SafelistApi

All URIs are relative to *https://accounts.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSafelist**](AccountsV1SafelistApi.md#createSafelist) | **POST** /v1/SafeList/Numbers | 
[**deleteSafelist**](AccountsV1SafelistApi.md#deleteSafelist) | **DELETE** /v1/SafeList/Numbers | 
[**fetchSafelist**](AccountsV1SafelistApi.md#fetchSafelist) | **GET** /v1/SafeList/Numbers | 



## createSafelist

> AccountsV1Safelist createSafelist(phoneNumber)



Add a new phone number to SafeList.

### Example

```javascript
import TwilioAccounts from 'twilio_accounts';
let defaultClient = TwilioAccounts.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAccounts.AccountsV1SafelistApi();
let phoneNumber = "phoneNumber_example"; // String | The phone number to be added in SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
apiInstance.createSafelist(phoneNumber, (error, data, response) => {
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
 **phoneNumber** | **String**| The phone number to be added in SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164). | 

### Return type

[**AccountsV1Safelist**](AccountsV1Safelist.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSafelist

> deleteSafelist(opts)



Remove a phone number from SafeList.

### Example

```javascript
import TwilioAccounts from 'twilio_accounts';
let defaultClient = TwilioAccounts.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAccounts.AccountsV1SafelistApi();
let opts = {
  'phoneNumber': "phoneNumber_example" // String | The phone number to be removed from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
};
apiInstance.deleteSafelist(opts, (error, data, response) => {
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
 **phoneNumber** | **String**| The phone number to be removed from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164). | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSafelist

> AccountsV1Safelist fetchSafelist(opts)



Check if a phone number exists in SafeList.

### Example

```javascript
import TwilioAccounts from 'twilio_accounts';
let defaultClient = TwilioAccounts.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioAccounts.AccountsV1SafelistApi();
let opts = {
  'phoneNumber': "phoneNumber_example" // String | The phone number to be fetched from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
};
apiInstance.fetchSafelist(opts, (error, data, response) => {
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
 **phoneNumber** | **String**| The phone number to be fetched from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164). | [optional] 

### Return type

[**AccountsV1Safelist**](AccountsV1Safelist.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

