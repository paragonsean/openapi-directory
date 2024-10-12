# InterzoidGetGlobalPhoneNumberInformationApi.GlobalPhoneNumberInformationApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getglobalnumberinfo**](GlobalPhoneNumberInformationApi.md#getglobalnumberinfo) | **GET** /getglobalnumberinfo | Get demographic information for a global telephone number



## getglobalnumberinfo

> Getglobalnumberinfo200Response getglobalnumberinfo(license, intlnumber)

Get demographic information for a global telephone number

Get demographic information for a global telephone number, including city and country information, primary languages spoken, and mobile device identification.

### Example

```javascript
import InterzoidGetGlobalPhoneNumberInformationApi from 'interzoid_get_global_phone_number_information_api';

let apiInstance = new InterzoidGetGlobalPhoneNumberInformationApi.GlobalPhoneNumberInformationApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let intlnumber = "intlnumber_example"; // String | International number (with country code) to retrieve information for
apiInstance.getglobalnumberinfo(license, intlnumber, (error, data, response) => {
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
 **license** | **String**| Your Interzoid license API key. Register at www.interzoid.com/register | 
 **intlnumber** | **String**| International number (with country code) to retrieve information for | 

### Return type

[**Getglobalnumberinfo200Response**](Getglobalnumberinfo200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

