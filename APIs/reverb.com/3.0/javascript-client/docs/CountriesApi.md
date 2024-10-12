# Reverb.CountriesApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**countriesGet**](CountriesApi.md#countriesGet) | **GET** /countries | Retrieve a list of country codes with corresponding subregions



## countriesGet

> countriesGet()

Retrieve a list of country codes with corresponding subregions

Retrieve a list of country codes with corresponding subregions

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.CountriesApi();
apiInstance.countriesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

