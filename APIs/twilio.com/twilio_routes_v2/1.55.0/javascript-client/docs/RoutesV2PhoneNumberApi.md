# TwilioRoutes.RoutesV2PhoneNumberApi

All URIs are relative to *https://routes.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchPhoneNumber**](RoutesV2PhoneNumberApi.md#fetchPhoneNumber) | **GET** /v2/PhoneNumbers/{PhoneNumber} | 
[**updatePhoneNumber**](RoutesV2PhoneNumberApi.md#updatePhoneNumber) | **POST** /v2/PhoneNumbers/{PhoneNumber} | 



## fetchPhoneNumber

> RoutesV2PhoneNumber fetchPhoneNumber(phoneNumber)



Fetch the Inbound Processing Region assigned to a phone number.

### Example

```javascript
import TwilioRoutes from 'twilio_routes';
let defaultClient = TwilioRoutes.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioRoutes.RoutesV2PhoneNumberApi();
let phoneNumber = "phoneNumber_example"; // String | The phone number in E.164 format
apiInstance.fetchPhoneNumber(phoneNumber, (error, data, response) => {
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
 **phoneNumber** | **String**| The phone number in E.164 format | 

### Return type

[**RoutesV2PhoneNumber**](RoutesV2PhoneNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatePhoneNumber

> RoutesV2PhoneNumber updatePhoneNumber(phoneNumber, opts)



Assign an Inbound Processing Region to a phone number.

### Example

```javascript
import TwilioRoutes from 'twilio_routes';
let defaultClient = TwilioRoutes.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioRoutes.RoutesV2PhoneNumberApi();
let phoneNumber = "phoneNumber_example"; // String | The phone number in E.164 format
let opts = {
  'friendlyName': "friendlyName_example", // String | A human readable description of this resource, up to 64 characters.
  'voiceRegion': "voiceRegion_example" // String | The Inbound Processing Region used for this phone number for voice
};
apiInstance.updatePhoneNumber(phoneNumber, opts, (error, data, response) => {
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
 **phoneNumber** | **String**| The phone number in E.164 format | 
 **friendlyName** | **String**| A human readable description of this resource, up to 64 characters. | [optional] 
 **voiceRegion** | **String**| The Inbound Processing Region used for this phone number for voice | [optional] 

### Return type

[**RoutesV2PhoneNumber**](RoutesV2PhoneNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

