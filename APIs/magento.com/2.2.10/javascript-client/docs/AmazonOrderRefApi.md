# MagentoB2B.AmazonOrderRefApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**amazonPaymentOrderInformationManagementV1RemoveOrderReferenceDelete**](AmazonOrderRefApi.md#amazonPaymentOrderInformationManagementV1RemoveOrderReferenceDelete) | **DELETE** /V1/amazon/order-ref | amazon/order-ref



## amazonPaymentOrderInformationManagementV1RemoveOrderReferenceDelete

> ErrorResponse amazonPaymentOrderInformationManagementV1RemoveOrderReferenceDelete()

amazon/order-ref



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.AmazonOrderRefApi();
apiInstance.amazonPaymentOrderInformationManagementV1RemoveOrderReferenceDelete((error, data, response) => {
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

[**ErrorResponse**](ErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

