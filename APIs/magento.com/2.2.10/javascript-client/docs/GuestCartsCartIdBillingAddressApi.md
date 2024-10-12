# MagentoB2B.GuestCartsCartIdBillingAddressApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteGuestBillingAddressManagementV1AssignPost**](GuestCartsCartIdBillingAddressApi.md#quoteGuestBillingAddressManagementV1AssignPost) | **POST** /V1/guest-carts/{cartId}/billing-address | guest-carts/{cartId}/billing-address
[**quoteGuestBillingAddressManagementV1GetGet**](GuestCartsCartIdBillingAddressApi.md#quoteGuestBillingAddressManagementV1GetGet) | **GET** /V1/guest-carts/{cartId}/billing-address | guest-carts/{cartId}/billing-address



## quoteGuestBillingAddressManagementV1AssignPost

> Number quoteGuestBillingAddressManagementV1AssignPost(cartId, opts)

guest-carts/{cartId}/billing-address

Assign a specified billing address to a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdBillingAddressApi();
let cartId = "cartId_example"; // String | The cart ID.
let opts = {
  'quoteBillingAddressManagementV1AssignPostRequest': new MagentoB2B.QuoteBillingAddressManagementV1AssignPostRequest() // QuoteBillingAddressManagementV1AssignPostRequest | 
};
apiInstance.quoteGuestBillingAddressManagementV1AssignPost(cartId, opts, (error, data, response) => {
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
 **cartId** | **String**| The cart ID. | 
 **quoteBillingAddressManagementV1AssignPostRequest** | [**QuoteBillingAddressManagementV1AssignPostRequest**](QuoteBillingAddressManagementV1AssignPostRequest.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## quoteGuestBillingAddressManagementV1GetGet

> QuoteDataAddressInterface quoteGuestBillingAddressManagementV1GetGet(cartId)

guest-carts/{cartId}/billing-address

Return the billing address for a specified quote.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdBillingAddressApi();
let cartId = "cartId_example"; // String | The cart ID.
apiInstance.quoteGuestBillingAddressManagementV1GetGet(cartId, (error, data, response) => {
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
 **cartId** | **String**| The cart ID. | 

### Return type

[**QuoteDataAddressInterface**](QuoteDataAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

