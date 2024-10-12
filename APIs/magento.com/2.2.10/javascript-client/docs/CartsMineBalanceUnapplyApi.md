# MagentoB2B.CartsMineBalanceUnapplyApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerBalanceBalanceManagementFromQuoteV1UnapplyPost**](CartsMineBalanceUnapplyApi.md#customerBalanceBalanceManagementFromQuoteV1UnapplyPost) | **POST** /V1/carts/mine/balance/unapply | carts/mine/balance/unapply



## customerBalanceBalanceManagementFromQuoteV1UnapplyPost

> Boolean customerBalanceBalanceManagementFromQuoteV1UnapplyPost()

carts/mine/balance/unapply

Unapply store credit.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineBalanceUnapplyApi();
apiInstance.customerBalanceBalanceManagementFromQuoteV1UnapplyPost((error, data, response) => {
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

