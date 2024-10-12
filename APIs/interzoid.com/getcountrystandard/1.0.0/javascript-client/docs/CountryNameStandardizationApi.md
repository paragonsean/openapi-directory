# InterzoidCountryDataStandardizationApi.CountryNameStandardizationApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getcountrystandard**](CountryNameStandardizationApi.md#getcountrystandard) | **GET** /getcountrystandard | Gets country name standard



## getcountrystandard

> Getcountrystandard200Response getcountrystandard(license, country)

Gets country name standard

Gets a pre-selected country name standard for various permutations of a given country name.

### Example

```javascript
import InterzoidCountryDataStandardizationApi from 'interzoid_country_data_standardization_api';

let apiInstance = new InterzoidCountryDataStandardizationApi.CountryNameStandardizationApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let country = "country_example"; // String | Country name from which to retrieve the standardized version
apiInstance.getcountrystandard(license, country, (error, data, response) => {
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
 **country** | **String**| Country name from which to retrieve the standardized version | 

### Return type

[**Getcountrystandard200Response**](Getcountrystandard200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

