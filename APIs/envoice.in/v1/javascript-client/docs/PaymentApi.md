# ApiV100.PaymentApi

All URIs are relative to *https://www.envoice.in*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentApiSupported**](PaymentApi.md#paymentApiSupported) | **GET** /api/payment/supported | Return all supported payment gateways (no currencies means all are supported)



## paymentApiSupported

> [PaymentGatewayDetailsApiModel] paymentApiSupported(xAuthKey, xAuthSecret)

Return all supported payment gateways (no currencies means all are supported)

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.PaymentApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.paymentApiSupported(xAuthKey, xAuthSecret, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

[**[PaymentGatewayDetailsApiModel]**](PaymentGatewayDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml

