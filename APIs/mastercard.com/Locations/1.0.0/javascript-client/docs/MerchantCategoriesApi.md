# LocationsApi.MerchantCategoriesApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merchantsV1CategoryGet**](MerchantCategoriesApi.md#merchantsV1CategoryGet) | **GET** /merchants/v1/category | Returns a list of all merchant categories for contactless and cash back merchants (example:  Airline, Retail, etc.). 



## merchantsV1CategoryGet

> CategoriesResponse merchantsV1CategoryGet()

Returns a list of all merchant categories for contactless and cash back merchants (example:  Airline, Retail, etc.). 

Returns a list of all merchant categories for contactless and cash back merchants (example:  Airline, Retail, etc.). 

### Example

```javascript
import LocationsApi from 'locations_api';

let apiInstance = new LocationsApi.MerchantCategoriesApi();
apiInstance.merchantsV1CategoryGet((error, data, response) => {
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

[**CategoriesResponse**](CategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

