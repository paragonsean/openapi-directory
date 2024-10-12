# SetlistFmApi.Class10SearchCountriesApi

All URIs are relative to */rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**resource10SearchCountriesGetCountriesGET**](Class10SearchCountriesApi.md#resource10SearchCountriesGetCountriesGET) | **GET** /1.0/search/countries | Get a complete list of all supported countries.



## resource10SearchCountriesGetCountriesGET

> JsonCountries resource10SearchCountriesGetCountriesGET()

Get a complete list of all supported countries.

Get a complete list of all supported countries.

### Example

```javascript
import SetlistFmApi from 'setlist_fm_api';

let apiInstance = new SetlistFmApi.Class10SearchCountriesApi();
apiInstance.resource10SearchCountriesGetCountriesGET((error, data, response) => {
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

[**JsonCountries**](JsonCountries.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json

