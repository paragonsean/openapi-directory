# HandwryttenApi.CountriesApi

All URIs are relative to *https://api.handwrytten.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**countriesListGet**](CountriesApi.md#countriesListGet) | **GET** /countries/list | 



## countriesListGet

> [Country] countriesListGet()



Lists the countries to which Handwritten can mail, their associated country ID and any costs

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.CountriesApi();
apiInstance.countriesListGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Country]**](Country.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

