# FlinksterApiNg.PricesApi

All URIs are relative to *https://api.deutschebahn.com/flinkster-api-ng/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPrices**](PricesApi.md#getPrices) | **GET** /providernetworks/{providernetworkUID}/prices | Get information about the prices.



## getPrices

> RentalObjectJO getPrices(providernetworkUID)

Get information about the prices.

Prices of a rental object by query params. The params depend on the price determination strategy of the provider network. 

### Example

```javascript
import FlinksterApiNg from 'flinkster_api_ng';

let apiInstance = new FlinksterApiNg.PricesApi();
let providernetworkUID = "providernetworkUID_example"; // String | 
apiInstance.getPrices(providernetworkUID, (error, data, response) => {
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
 **providernetworkUID** | **String**|  | 

### Return type

[**RentalObjectJO**](RentalObjectJO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

