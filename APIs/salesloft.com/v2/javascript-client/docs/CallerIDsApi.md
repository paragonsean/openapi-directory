# SalesLoftPlatform.CallerIDsApi

All URIs are relative to *https://api.salesloft.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2PhoneNumbersCallerIdsJsonGet**](CallerIDsApi.md#v2PhoneNumbersCallerIdsJsonGet) | **GET** /v2/phone_numbers/caller_ids.json | List caller ids



## v2PhoneNumbersCallerIdsJsonGet

> [CallerId] v2PhoneNumbersCallerIdsJsonGet(phoneNumber)

List caller ids

Each entry is a possible caller ID match for the number. Multiple entries may be returned if the phone number is present on more than one person in the system.  Phone number should be in E.164 format. 

### Example

```javascript
import SalesLoftPlatform from 'sales_loft_platform';

let apiInstance = new SalesLoftPlatform.CallerIDsApi();
let phoneNumber = "phoneNumber_example"; // String | E.164 Phone Number
apiInstance.v2PhoneNumbersCallerIdsJsonGet(phoneNumber, (error, data, response) => {
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
 **phoneNumber** | **String**| E.164 Phone Number | 

### Return type

[**[CallerId]**](CallerId.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

