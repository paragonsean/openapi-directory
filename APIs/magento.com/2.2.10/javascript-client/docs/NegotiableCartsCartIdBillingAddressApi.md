# MagentoB2B.NegotiableCartsCartIdBillingAddressApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**negotiableQuoteBillingAddressManagementV1AssignPost**](NegotiableCartsCartIdBillingAddressApi.md#negotiableQuoteBillingAddressManagementV1AssignPost) | **POST** /V1/negotiable-carts/{cartId}/billing-address | negotiable-carts/{cartId}/billing-address
[**negotiableQuoteBillingAddressManagementV1GetGet**](NegotiableCartsCartIdBillingAddressApi.md#negotiableQuoteBillingAddressManagementV1GetGet) | **GET** /V1/negotiable-carts/{cartId}/billing-address | negotiable-carts/{cartId}/billing-address



## negotiableQuoteBillingAddressManagementV1AssignPost

> Number negotiableQuoteBillingAddressManagementV1AssignPost(cartId, opts)

negotiable-carts/{cartId}/billing-address

Assigns a specified billing address to a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableCartsCartIdBillingAddressApi();
let cartId = 56; // Number | The cart ID.
let opts = {
  'quoteBillingAddressManagementV1AssignPostRequest': new MagentoB2B.QuoteBillingAddressManagementV1AssignPostRequest() // QuoteBillingAddressManagementV1AssignPostRequest | 
};
apiInstance.negotiableQuoteBillingAddressManagementV1AssignPost(cartId, opts, (error, data, response) => {
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


## negotiableQuoteBillingAddressManagementV1GetGet

> QuoteDataAddressInterface negotiableQuoteBillingAddressManagementV1GetGet(cartId)

negotiable-carts/{cartId}/billing-address

Returns the billing address for a specified quote.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableCartsCartIdBillingAddressApi();
let cartId = 56; // Number | The cart ID.
apiInstance.negotiableQuoteBillingAddressManagementV1GetGet(cartId, (error, data, response) => {
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

