# InterzoidGetAreaCodeApi.AreaCodeInformationApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getareacode**](AreaCodeInformationApi.md#getareacode) | **GET** /getareacode | Gets telephone area code information



## getareacode

> Getareacode200Response getareacode(license, areacode)

Gets telephone area code information

Gets telephone area code information for a given area code.

### Example

```javascript
import InterzoidGetAreaCodeApi from 'interzoid_get_area_code_api';

let apiInstance = new InterzoidGetAreaCodeApi.AreaCodeInformationApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let areacode = "areacode_example"; // String | Telephone area code to retrieve area code information
apiInstance.getareacode(license, areacode, (error, data, response) => {
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
 **areacode** | **String**| Telephone area code to retrieve area code information | 

### Return type

[**Getareacode200Response**](Getareacode200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

