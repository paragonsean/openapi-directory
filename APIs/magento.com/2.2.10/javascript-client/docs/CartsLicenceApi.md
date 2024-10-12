# MagentoB2B.CartsLicenceApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkoutAgreementsCheckoutAgreementsRepositoryV1GetListGet**](CartsLicenceApi.md#checkoutAgreementsCheckoutAgreementsRepositoryV1GetListGet) | **GET** /V1/carts/licence | carts/licence



## checkoutAgreementsCheckoutAgreementsRepositoryV1GetListGet

> [CheckoutAgreementsDataAgreementInterface] checkoutAgreementsCheckoutAgreementsRepositoryV1GetListGet()

carts/licence

Lists active checkout agreements.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsLicenceApi();
apiInstance.checkoutAgreementsCheckoutAgreementsRepositoryV1GetListGet((error, data, response) => {
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

[**[CheckoutAgreementsDataAgreementInterface]**](CheckoutAgreementsDataAgreementInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

