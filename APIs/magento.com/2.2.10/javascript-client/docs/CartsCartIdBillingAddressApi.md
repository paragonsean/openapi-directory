# MagentoB2B.CartsCartIdBillingAddressApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CartsCartIdBillingAddressGet**](CartsCartIdBillingAddressApi.md#v1CartsCartIdBillingAddressGet) | **GET** /V1/carts/{cartId}/billing-address | carts/{cartId}/billing-address
[**v1CartsCartIdBillingAddressPost**](CartsCartIdBillingAddressApi.md#v1CartsCartIdBillingAddressPost) | **POST** /V1/carts/{cartId}/billing-address | carts/{cartId}/billing-address



## v1CartsCartIdBillingAddressGet

> QuoteDataAddressInterface v1CartsCartIdBillingAddressGet(cartId)

carts/{cartId}/billing-address

Returns the billing address for a specified quote.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdBillingAddressApi();
let cartId = 56; // Number | The cart ID.
apiInstance.v1CartsCartIdBillingAddressGet(cartId, (error, data, response) => {
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
 **cartId** | **Number**| The cart ID. | 

### Return type

[**QuoteDataAddressInterface**](QuoteDataAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## v1CartsCartIdBillingAddressPost

> Number v1CartsCartIdBillingAddressPost(cartId, opts)

carts/{cartId}/billing-address

Assigns a specified billing address to a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdBillingAddressApi();
let cartId = 56; // Number | The cart ID.
let opts = {
  'quoteBillingAddressManagementV1AssignPostRequest': new MagentoB2B.QuoteBillingAddressManagementV1AssignPostRequest() // QuoteBillingAddressManagementV1AssignPostRequest | 
};
apiInstance.v1CartsCartIdBillingAddressPost(cartId, opts, (error, data, response) => {
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
 **cartId** | **Number**| The cart ID. | 
 **quoteBillingAddressManagementV1AssignPostRequest** | [**QuoteBillingAddressManagementV1AssignPostRequest**](QuoteBillingAddressManagementV1AssignPostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

