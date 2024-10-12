# Reverb.ShippingApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shippingProvidersGet**](ShippingApi.md#shippingProvidersGet) | **GET** /shipping/providers | List of supported shipping providers
[**shippingRegionsGet**](ShippingApi.md#shippingRegionsGet) | **GET** /shipping/regions | 



## shippingProvidersGet

> shippingProvidersGet()

List of supported shipping providers

List of supported shipping providers

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ShippingApi();
apiInstance.shippingProvidersGet((error, data, response) => {
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


## shippingRegionsGet

> shippingRegionsGet()



### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.ShippingApi();
apiInstance.shippingRegionsGet((error, data, response) => {
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

