# InterzoidGetAreaCodeFromNumberApi.AreaCodeInformationApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getareacodefromnumber**](AreaCodeInformationApi.md#getareacodefromnumber) | **GET** /getareacodefromnumber | Gets area code information from a telephone number



## getareacodefromnumber

> Getareacodefromnumber200Response getareacodefromnumber(license, number)

Gets area code information from a telephone number

The area code will be parsed out of a telephone number and used to retrieve information about the area code.

### Example

```javascript
import InterzoidGetAreaCodeFromNumberApi from 'interzoid_get_area_code_from_number_api';

let apiInstance = new InterzoidGetAreaCodeFromNumberApi.AreaCodeInformationApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let number = "number_example"; // String | Telephone number to retrieve area code information
apiInstance.getareacodefromnumber(license, number, (error, data, response) => {
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
 **number** | **String**| Telephone number to retrieve area code information | 

### Return type

[**Getareacodefromnumber200Response**](Getareacodefromnumber200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

