# MagentoB2B.GuestCartsCartIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteGuestCartManagementV1AssignCustomerPut**](GuestCartsCartIdApi.md#quoteGuestCartManagementV1AssignCustomerPut) | **PUT** /V1/guest-carts/{cartId} | guest-carts/{cartId}
[**quoteGuestCartRepositoryV1GetGet**](GuestCartsCartIdApi.md#quoteGuestCartRepositoryV1GetGet) | **GET** /V1/guest-carts/{cartId} | guest-carts/{cartId}



## quoteGuestCartManagementV1AssignCustomerPut

> Boolean quoteGuestCartManagementV1AssignCustomerPut(cartId, opts)

guest-carts/{cartId}

Assign a specified customer to a specified shopping cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdApi();
let cartId = "cartId_example"; // String | The cart ID.
let opts = {
  'quoteCartManagementV1AssignCustomerPutRequest': new MagentoB2B.QuoteCartManagementV1AssignCustomerPutRequest() // QuoteCartManagementV1AssignCustomerPutRequest | 
};
apiInstance.quoteGuestCartManagementV1AssignCustomerPut(cartId, opts, (error, data, response) => {
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
 **quoteCartManagementV1AssignCustomerPutRequest** | [**QuoteCartManagementV1AssignCustomerPutRequest**](QuoteCartManagementV1AssignCustomerPutRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## quoteGuestCartRepositoryV1GetGet

> QuoteDataCartInterface quoteGuestCartRepositoryV1GetGet(cartId)

guest-carts/{cartId}

Enable a guest user to return information for a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdApi();
let cartId = "cartId_example"; // String | 
apiInstance.quoteGuestCartRepositoryV1GetGet(cartId, (error, data, response) => {
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
 **cartId** | **String**|  | 

### Return type

[**QuoteDataCartInterface**](QuoteDataCartInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

