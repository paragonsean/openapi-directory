# TwilioVerify.VerifyV2SafelistApi

All URIs are relative to *https://verify.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSafelist**](VerifyV2SafelistApi.md#createSafelist) | **POST** /v2/SafeList/Numbers | 
[**deleteSafelist**](VerifyV2SafelistApi.md#deleteSafelist) | **DELETE** /v2/SafeList/Numbers/{PhoneNumber} | 
[**fetchSafelist**](VerifyV2SafelistApi.md#fetchSafelist) | **GET** /v2/SafeList/Numbers/{PhoneNumber} | 



## createSafelist

> VerifyV2Safelist createSafelist(phoneNumber)



Add a new phone number to SafeList.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2SafelistApi();
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

[**VerifyV2Safelist**](VerifyV2Safelist.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSafelist

> deleteSafelist(phoneNumber)



Remove a phone number from SafeList.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2SafelistApi();
let phoneNumber = "phoneNumber_example"; // String | The phone number to be removed from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
apiInstance.deleteSafelist(phoneNumber, (error, data, response) => {
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
 **phoneNumber** | **String**| The phone number to be removed from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164). | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSafelist

> VerifyV2Safelist fetchSafelist(phoneNumber)



Check if a phone number exists in SafeList.

### Example

```javascript
import TwilioVerify from 'twilio_verify';
let defaultClient = TwilioVerify.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVerify.VerifyV2SafelistApi();
let phoneNumber = "phoneNumber_example"; // String | The phone number to be fetched from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
apiInstance.fetchSafelist(phoneNumber, (error, data, response) => {
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
 **phoneNumber** | **String**| The phone number to be fetched from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164). | 

### Return type

[**VerifyV2Safelist**](VerifyV2Safelist.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

