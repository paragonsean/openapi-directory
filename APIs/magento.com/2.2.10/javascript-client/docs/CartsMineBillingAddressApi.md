# MagentoB2B.CartsMineBillingAddressApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteBillingAddressManagementV1AssignPost**](CartsMineBillingAddressApi.md#quoteBillingAddressManagementV1AssignPost) | **POST** /V1/carts/mine/billing-address | carts/mine/billing-address
[**quoteBillingAddressManagementV1GetGet**](CartsMineBillingAddressApi.md#quoteBillingAddressManagementV1GetGet) | **GET** /V1/carts/mine/billing-address | carts/mine/billing-address



## quoteBillingAddressManagementV1AssignPost

> Number quoteBillingAddressManagementV1AssignPost(opts)

carts/mine/billing-address

Assigns a specified billing address to a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineBillingAddressApi();
let opts = {
  'quoteBillingAddressManagementV1AssignPostRequest': new MagentoB2B.QuoteBillingAddressManagementV1AssignPostRequest() // QuoteBillingAddressManagementV1AssignPostRequest | 
};
apiInstance.quoteBillingAddressManagementV1AssignPost(opts, (error, data, response) => {
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
 **quoteBillingAddressManagementV1AssignPostRequest** | [**QuoteBillingAddressManagementV1AssignPostRequest**](QuoteBillingAddressManagementV1AssignPostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## quoteBillingAddressManagementV1GetGet

> QuoteDataAddressInterface quoteBillingAddressManagementV1GetGet()

carts/mine/billing-address

Returns the billing address for a specified quote.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineBillingAddressApi();
apiInstance.quoteBillingAddressManagementV1GetGet((error, data, response) => {
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

[**QuoteDataAddressInterface**](QuoteDataAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

