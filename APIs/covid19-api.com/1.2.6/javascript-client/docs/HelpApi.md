# Covid19DataApi.HelpApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getListOfCountries**](HelpApi.md#getListOfCountries) | **GET** /help/countries | getListOfCountries



## getListOfCountries

> [GetListOfCountries200ResponseInner] getListOfCountries(opts)

getListOfCountries

Get name name, alpha-2, alpha-3 code, latitude and longitude for every country.

### Example

```javascript
import Covid19DataApi from 'covid_19_data_api';

let apiInstance = new Covid19DataApi.HelpApi();
let opts = {
  'format': "'json'" // String | Format of the response
};
apiInstance.getListOfCountries(opts, (error, data, response) => {
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
 **format** | **String**| Format of the response | [optional] [default to &#39;json&#39;]

### Return type

[**[GetListOfCountries200ResponseInner]**](GetListOfCountries200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

