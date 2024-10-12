# AvazaApiDocumentation.CurrencyApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currencyGet**](CurrencyApi.md#currencyGet) | **GET** /api/Currency | Gets list of Currencies



## currencyGet

> CurrencyList currencyGet()

Gets list of Currencies

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';

let apiInstance = new AvazaApiDocumentation.CurrencyApi();
apiInstance.currencyGet((error, data, response) => {
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

[**CurrencyList**](CurrencyList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

