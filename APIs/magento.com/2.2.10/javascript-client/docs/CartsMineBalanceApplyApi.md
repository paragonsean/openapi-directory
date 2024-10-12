# MagentoB2B.CartsMineBalanceApplyApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerBalanceBalanceManagementFromQuoteV1ApplyPost**](CartsMineBalanceApplyApi.md#customerBalanceBalanceManagementFromQuoteV1ApplyPost) | **POST** /V1/carts/mine/balance/apply | carts/mine/balance/apply



## customerBalanceBalanceManagementFromQuoteV1ApplyPost

> Boolean customerBalanceBalanceManagementFromQuoteV1ApplyPost()

carts/mine/balance/apply

Apply store credit.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineBalanceApplyApi();
apiInstance.customerBalanceBalanceManagementFromQuoteV1ApplyPost((error, data, response) => {
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

