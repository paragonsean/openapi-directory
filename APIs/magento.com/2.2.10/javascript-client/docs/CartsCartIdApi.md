# MagentoB2B.CartsCartIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteCartManagementV1AssignCustomerPut**](CartsCartIdApi.md#quoteCartManagementV1AssignCustomerPut) | **PUT** /V1/carts/{cartId} | carts/{cartId}
[**quoteCartRepositoryV1GetGet**](CartsCartIdApi.md#quoteCartRepositoryV1GetGet) | **GET** /V1/carts/{cartId} | carts/{cartId}



## quoteCartManagementV1AssignCustomerPut

> Boolean quoteCartManagementV1AssignCustomerPut(cartId, opts)

carts/{cartId}

Assigns a specified customer to a specified shopping cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdApi();
let cartId = 56; // Number | The cart ID.
let opts = {
  'quoteCartManagementV1AssignCustomerPutRequest': new MagentoB2B.QuoteCartManagementV1AssignCustomerPutRequest() // QuoteCartManagementV1AssignCustomerPutRequest | 
};
apiInstance.quoteCartManagementV1AssignCustomerPut(cartId, opts, (error, data, response) => {
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
 **quoteCartManagementV1AssignCustomerPutRequest** | [**QuoteCartManagementV1AssignCustomerPutRequest**](QuoteCartManagementV1AssignCustomerPutRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## quoteCartRepositoryV1GetGet

> QuoteDataCartInterface quoteCartRepositoryV1GetGet(cartId)

carts/{cartId}

Enables an administrative user to return information for a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdApi();
let cartId = 56; // Number | 
apiInstance.quoteCartRepositoryV1GetGet(cartId, (error, data, response) => {
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
 **cartId** | **Number**|  | 

### Return type

[**QuoteDataCartInterface**](QuoteDataCartInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

