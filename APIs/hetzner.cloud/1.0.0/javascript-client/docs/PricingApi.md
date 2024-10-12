# HetznerCloudApi.PricingApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pricingGet**](PricingApi.md#pricingGet) | **GET** /pricing | Get all prices



## pricingGet

> PricingGet200Response pricingGet()

Get all prices

Returns prices for all resources available on the platform. VAT and currency of the Project owner are used for calculations.  Both net and gross prices are included in the response. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.PricingApi();
apiInstance.pricingGet((error, data, response) => {
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

[**PricingGet200Response**](PricingGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

