# InterzoidZipCodeDetailedInfoApi.DetailedZipCodeInformationApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getzipcodeinfo**](DetailedZipCodeInformationApi.md#getzipcodeinfo) | **GET** /getzipcodeinfo | Gets detailed zip code information



## getzipcodeinfo

> Getzipcodeinfo200Response getzipcodeinfo(license, zip)

Gets detailed zip code information

For a given zip code, detailed information is returned, including city, state, latitude, longitude, area size, and various population demographics, including income, age, and presence of farming data.

### Example

```javascript
import InterzoidZipCodeDetailedInfoApi from 'interzoid_zip_code_detailed_info_api';

let apiInstance = new InterzoidZipCodeDetailedInfoApi.DetailedZipCodeInformationApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let zip = "zip_example"; // String | Zip code to retrieve detailed information
apiInstance.getzipcodeinfo(license, zip, (error, data, response) => {
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
 **zip** | **String**| Zip code to retrieve detailed information | 

### Return type

[**Getzipcodeinfo200Response**](Getzipcodeinfo200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

