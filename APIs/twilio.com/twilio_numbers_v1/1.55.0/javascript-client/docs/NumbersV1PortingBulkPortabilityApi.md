# TwilioNumbers.NumbersV1PortingBulkPortabilityApi

All URIs are relative to *https://numbers.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPortingBulkPortability**](NumbersV1PortingBulkPortabilityApi.md#createPortingBulkPortability) | **POST** /v1/Porting/Portability | 
[**fetchPortingBulkPortability**](NumbersV1PortingBulkPortabilityApi.md#fetchPortingBulkPortability) | **GET** /v1/Porting/Portability/{Sid} | 



## createPortingBulkPortability

> NumbersV1PortingBulkPortability createPortingBulkPortability(phoneNumbers)



Allows to check if a list of phone numbers can be ported to Twilio or not. This is done asynchronous for each phone number.

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV1PortingBulkPortabilityApi();
let phoneNumbers = ["null"]; // [String] | The phone numbers which portability is to be checked. This should be a list of strings. Phone numbers are in E.164 format (e.g. +16175551212). .
apiInstance.createPortingBulkPortability(phoneNumbers, (error, data, response) => {
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
 **phoneNumbers** | [**[String]**](String.md)| The phone numbers which portability is to be checked. This should be a list of strings. Phone numbers are in E.164 format (e.g. +16175551212). . | 

### Return type

[**NumbersV1PortingBulkPortability**](NumbersV1PortingBulkPortability.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchPortingBulkPortability

> NumbersV1PortingBulkPortability fetchPortingBulkPortability(sid)



Fetch a previous portability check. This should return the current status of the validation and the result for all the numbers provided, given that they have been validated (as this process is performed asynchronously).

### Example

```javascript
import TwilioNumbers from 'twilio_numbers';
let defaultClient = TwilioNumbers.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioNumbers.NumbersV1PortingBulkPortabilityApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies the Portability check.
apiInstance.fetchPortingBulkPortability(sid, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies the Portability check. | 

### Return type

[**NumbersV1PortingBulkPortability**](NumbersV1PortingBulkPortability.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

